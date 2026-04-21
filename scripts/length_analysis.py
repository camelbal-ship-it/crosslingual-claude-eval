"""
length_analysis.py
------------------
Reads data/processed/responses_flat.csv and computes length and structural
statistics per language and per prompt cluster.

Outputs:
    results/length_by_language.csv     — mean/std metrics per language
    results/length_by_cluster.csv      — mean/std metrics per cluster × language
    results/list_structure_rates.csv   — % responses using list formatting

Usage:
    python scripts/length_analysis.py

Requires:
    pip install pandas tabulate
"""

import pandas as pd
from pathlib import Path

INPUT_CSV   = Path("data/processed/responses_flat.csv")
RESULTS_DIR = Path("results")

METRICS = ["word_count", "sentence_count", "output_tokens", "char_count"]


def load_data() -> pd.DataFrame:
    df = pd.read_csv(INPUT_CSV, encoding="utf-8")
    df["has_list"] = df["has_list"].astype(str).str.upper() == "TRUE"
    df["output_tokens"] = pd.to_numeric(df["output_tokens"], errors="coerce")
    return df


def language_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Mean and std of key metrics per language, across all prompts and runs."""
    rows = []
    for lang, group in df.groupby("language"):
        row = {"language": lang}
        for m in METRICS:
            row[f"{m}_mean"] = round(group[m].mean(), 1)
            row[f"{m}_std"]  = round(group[m].std(), 1)
        row["list_rate_pct"] = round(group["has_list"].mean() * 100, 1)
        rows.append(row)
    return pd.DataFrame(rows).sort_values("language")


def cluster_language_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Mean word count per cluster × language — the core comparison table."""
    pivot = df.groupby(["cluster", "language"])["word_count"].mean().round(1)
    return pivot.unstack(level="language")


def list_structure_rates(df: pd.DataFrame) -> pd.DataFrame:
    """Percentage of responses using list formatting per cluster × language."""
    pivot = (df.groupby(["cluster", "language"])["has_list"]
               .mean()
               .mul(100)
               .round(1)
               .unstack(level="language"))
    return pivot


def print_summary(df: pd.DataFrame):
    """Print a readable summary to the terminal."""
    lang_df = language_summary(df)
    print("\n" + "="*70)
    print("  CROSS-LINGUAL LENGTH ANALYSIS — SUMMARY")
    print("="*70)
    print(f"\n  Total responses analyzed: {len(df)}")
    print(f"  Prompts: {df['prompt_id'].nunique()}")
    print(f"  Languages: {sorted(df['language'].unique())}")
    print(f"  Runs per cell: {df['run'].nunique()}")

    print("\n--- Mean word count by language (all prompts) ---")
    for _, row in lang_df.iterrows():
        bar = "█" * int(row["word_count_mean"] / 10)
        print(f"  {row['language']:4s}  {row['word_count_mean']:6.1f} words  {bar}")

    print("\n--- List structure usage by language ---")
    for _, row in lang_df.iterrows():
        print(f"  {row['language']:4s}  {row['list_rate_pct']:5.1f}% responses use lists")

    print("\n--- Output tokens by language ---")
    for _, row in lang_df.iterrows():
        print(f"  {row['language']:4s}  {row['output_tokens_mean']:6.1f} tokens (±{row['output_tokens_std']:.1f})")


def main():
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Loading {INPUT_CSV}...")
    df = load_data()
    print(f"✓ Loaded {len(df)} rows")

    # Language summary
    lang_df = language_summary(df)
    out1 = RESULTS_DIR / "length_by_language.csv"
    lang_df.to_csv(out1, index=False)
    print(f"✓ Saved {out1}")

    # Cluster × language pivot
    cluster_df = cluster_language_summary(df)
    out2 = RESULTS_DIR / "length_by_cluster.csv"
    cluster_df.to_csv(out2)
    print(f"✓ Saved {out2}")

    # List structure rates
    list_df = list_structure_rates(df)
    out3 = RESULTS_DIR / "list_structure_rates.csv"
    list_df.to_csv(out3)
    print(f"✓ Saved {out3}")

    # Print readable summary
    print_summary(df)

    print(f"\n✓ All results saved to {RESULTS_DIR}/")


if __name__ == "__main__":
    main()
