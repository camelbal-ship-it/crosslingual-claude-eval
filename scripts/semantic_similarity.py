"""
semantic_similarity.py
----------------------
Computes semantic similarity between non-English responses and the
English baseline using TF-IDF cosine similarity.

NO external model download required — works on any network.

This is a practical approximation suitable for cross-lingual comparison
at the response level. For publication, results should be validated
against a multilingual embedding model (paraphrase-multilingual-mpnet-base-v2)
in a network environment without SSL restrictions.

Usage:
    python scripts/semantic_similarity.py

Requires: pandas, scikit-learn (both already installed)
"""

import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity as sk_cosine

INPUT_CSV   = Path("data/processed/responses_flat.csv")
RESULTS_DIR = Path("results")


def compute_tfidf_similarities(df: pd.DataFrame) -> pd.DataFrame:
    """
    For each (prompt_id, run), compute TF-IDF cosine similarity of each
    language response against the English response.

    Note: TF-IDF similarity across languages is a surface-level proxy.
    It captures shared proper nouns, numbers, and borrowed vocabulary.
    Lower scores here indicate surface divergence; higher scores indicate
    lexical overlap (common in technical prompts with shared terminology).
    """
    results = []
    groups = df.groupby(["prompt_id", "run"])

    print(f"Computing TF-IDF similarities for {len(groups)} prompt×run groups...")

    for (prompt_id, run), group in groups:
        en_rows = group[group["language"] == "en"]
        if en_rows.empty:
            continue

        en_text = en_rows.iloc[0]["response_text"]

        for _, row in group.iterrows():
            lang = row["language"]
            text = row["response_text"]

            if lang == "en":
                similarity = 1.0
            else:
                # Fit TF-IDF on just this pair
                try:
                    vec = TfidfVectorizer(analyzer="char_wb", ngram_range=(3, 5))
                    tfidf = vec.fit_transform([en_text, text])
                    similarity = float(sk_cosine(tfidf[0], tfidf[1])[0][0])
                except Exception:
                    similarity = 0.0

            results.append({
                "prompt_id":        prompt_id,
                "cluster":          row["cluster"],
                "language":         lang,
                "run":              run,
                "similarity_to_en": round(similarity, 4),
                "word_count":       row["word_count"],
                "method":           "tfidf_char_ngram",
            })

    print(f"✓ Computed {len(results)} similarity scores")
    return pd.DataFrame(results)


def summarize(sim_df: pd.DataFrame):
    non_en = sim_df[sim_df["language"] != "en"]

    lang_summary = (non_en.groupby("language")["similarity_to_en"]
                          .agg(["mean", "std", "min", "max"])
                          .round(4).reset_index())
    lang_summary.columns = ["language", "mean_similarity", "std", "min", "max"]

    cluster_summary = (non_en.groupby(["cluster", "language"])["similarity_to_en"]
                             .mean().round(4).unstack(level="language"))

    print("\n" + "="*70)
    print("  SURFACE SIMILARITY TO ENGLISH BASELINE (TF-IDF char n-gram)")
    print("="*70)
    print("\n  Note: Cross-lingual TF-IDF captures shared vocabulary,")
    print("  proper nouns, numbers, and borrowed terms.")
    print("  Lower scores = more lexically divergent from English.\n")

    print("--- Mean similarity by language ---")
    for _, row in lang_summary.iterrows():
        bar = "█" * int(row["mean_similarity"] * 40)
        print(f"  {row['language']:4s}  {row['mean_similarity']:.4f}  {bar}")

    print("\n--- Most divergent responses ---")
    bottom = non_en.nsmallest(8, "similarity_to_en")[
        ["prompt_id", "cluster", "language", "run", "similarity_to_en"]
    ]
    for _, row in bottom.iterrows():
        print(f"  {row['prompt_id']} [{row['language']}] run {row['run']}: "
              f"{row['similarity_to_en']:.4f}  ({row['cluster']})")

    print("\n--- Similarity by cluster (mean across languages) ---")
    cluster_mean = non_en.groupby("cluster")["similarity_to_en"].mean().sort_values()
    for cluster, val in cluster_mean.items():
        bar = "█" * int(val * 40)
        print(f"  {cluster:35s}  {val:.4f}  {bar}")

    return lang_summary, cluster_summary


def main():
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Loading {INPUT_CSV}...")
    df = pd.read_csv(INPUT_CSV, encoding="utf-8")
    print(f"✓ Loaded {len(df)} rows")

    sim_df = compute_tfidf_similarities(df)

    out1 = RESULTS_DIR / "semantic_similarity.csv"
    sim_df.to_csv(out1, index=False)
    print(f"✓ Saved {out1}")

    lang_summary, cluster_summary = summarize(sim_df)

    out2 = RESULTS_DIR / "similarity_by_language.csv"
    lang_summary.to_csv(out2, index=False)
    print(f"✓ Saved {out2}")

    out3 = RESULTS_DIR / "similarity_by_cluster.csv"
    cluster_summary.to_csv(out3)
    print(f"✓ Saved {out3}")

    print(f"\n✓ All results saved to {RESULTS_DIR}/")
    print("\nNote: For publication, validate with multilingual sentence")
    print("embeddings (paraphrase-multilingual-mpnet-base-v2) on an")
    print("unrestricted network connection.")


if __name__ == "__main__":
    main()
