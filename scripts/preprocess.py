"""
preprocess.py
-------------
Reads all raw response JSON files from data/raw/ and flattens them into
a single CSV file at data/processed/responses_flat.csv.

Each row = one response (prompt × language × run).

Usage:
    python scripts/preprocess.py

Output columns:
    prompt_id, cluster, language, run, prompt_text, response_text,
    input_tokens, output_tokens, stop_reason, model, collected_at,
    word_count, sentence_count, char_count, has_list
"""

import json
import csv
import re
from pathlib import Path

RAW_DIR       = Path("data/raw")
PROCESSED_DIR = Path("data/processed")
OUTPUT_CSV    = PROCESSED_DIR / "responses_flat.csv"

FIELDNAMES = [
    "prompt_id", "cluster", "language", "run",
    "prompt_text", "response_text",
    "input_tokens", "output_tokens", "stop_reason", "model",
    "collected_at",
    "word_count", "sentence_count", "char_count", "has_list"
]


def count_words(text: str) -> int:
    return len(text.split())


def count_sentences(text: str) -> int:
    """
    Rough sentence count using punctuation boundaries.
    Works across languages — splits on . ! ? followed by space or end.
    """
    sentences = re.split(r'[.!?]+(?:\s|$)', text.strip())
    return len([s for s in sentences if s.strip()])


def has_list_structure(text: str) -> bool:
    """
    Detects whether the response uses bullet points or numbered lists.
    Covers markdown bullets (- *) and numbered lists (1. 2.).
    """
    return bool(re.search(r'(^\s*[-*•]\s)|(^\s*\d+[.)]\s)', text, re.MULTILINE))


def load_and_flatten():
    records = []
    json_files = sorted(RAW_DIR.glob("*/*/run_*.json"))

    print(f"Found {len(json_files)} response files in {RAW_DIR}")

    for path in json_files:
        # Skip sample/placeholder files
        if "sample" in path.name:
            continue

        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        response = data.get("response", {})
        text = response.get("text", "")
        usage = response.get("usage", {})

        # Skip placeholder responses
        if "PLACEHOLDER" in text:
            continue

        record = {
            "prompt_id":     data.get("prompt_id", ""),
            "cluster":       data.get("cluster", ""),
            "language":      data.get("language", ""),
            "run":           data.get("run", ""),
            "prompt_text":   data.get("prompt_text", ""),
            "response_text": text,
            "input_tokens":  usage.get("input_tokens", ""),
            "output_tokens": usage.get("output_tokens", ""),
            "stop_reason":   response.get("stop_reason", ""),
            "model":         response.get("model", ""),
            "collected_at":  data.get("collected_at", ""),
            "word_count":    count_words(text),
            "sentence_count": count_sentences(text),
            "char_count":    len(text),
            "has_list":      has_list_structure(text),
        }
        records.append(record)

    return records


def main():
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    records = load_and_flatten()
    records.sort(key=lambda r: (r["prompt_id"], r["language"], r["run"]))

    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(records)

    print(f"\n✓ Wrote {len(records)} rows to {OUTPUT_CSV}")
    print(f"  Prompts:   {len(set(r['prompt_id'] for r in records))}")
    print(f"  Languages: {sorted(set(r['language'] for r in records))}")
    print(f"  Runs:      {sorted(set(str(r['run']) for r in records))}")
    print(f"  Clusters:  {sorted(set(r['cluster'] for r in records))}")


if __name__ == "__main__":
    main()
