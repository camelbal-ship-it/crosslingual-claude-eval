"""
collect_responses.py
--------------------
Loads the prompt battery and collects Claude responses for each prompt × language
combination. Saves raw responses to /data/raw/ as JSON.

Usage:
    export ANTHROPIC_API_KEY=your_key_here
    python scripts/collect_responses.py [--prompts P001,P002] [--languages en,fr,ro]

Requirements:
    pip install anthropic tqdm
"""

import json
import os
import time
import argparse
from pathlib import Path
from datetime import datetime

try:
    import anthropic
    from tqdm import tqdm
except ImportError:
    raise SystemExit("Run: pip install anthropic tqdm")


# ─── Configuration ───────────────────────────────────────────────────────────

MODEL          = "claude-sonnet-4-6"
MAX_TOKENS     = 1024
TEMPERATURE    = 1.0    # default; set to 0 for reproducibility studies
SYSTEM_PROMPT  = None   # null = model default; change to "" for truly blank
DELAY_SECONDS  = 1.0    # rate-limit buffer between API calls
RUNS_PER_CELL  = 3      # collect N responses per prompt×language for variance analysis

BATTERY_PATH   = Path("prompts/prompt_battery.json")
OUTPUT_DIR     = Path("data/raw")

# ─── Helpers ─────────────────────────────────────────────────────────────────

def load_battery(path: Path) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def build_messages(prompt_text: str) -> list:
    return [{"role": "user", "content": prompt_text}]


def call_claude(client: anthropic.Anthropic, prompt_text: str) -> dict:
    """Single API call. Returns the full response object as a dict."""
    kwargs = dict(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        temperature=TEMPERATURE,
        messages=build_messages(prompt_text),
    )
    if SYSTEM_PROMPT is not None:
        kwargs["system"] = SYSTEM_PROMPT

    response = client.messages.create(**kwargs)

    return {
        "model":        response.model,
        "stop_reason":  response.stop_reason,
        "usage": {
            "input_tokens":  response.usage.input_tokens,
            "output_tokens": response.usage.output_tokens,
        },
        "text": response.content[0].text,
    }


def output_path(prompt_id: str, lang: str, run: int) -> Path:
    p = OUTPUT_DIR / prompt_id / lang
    p.mkdir(parents=True, exist_ok=True)
    return p / f"run_{run:02d}.json"


def save_response(path: Path, data: dict):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


# ─── Main ────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Collect Claude responses for prompt battery.")
    parser.add_argument("--prompts",   type=str, default=None,
                        help="Comma-separated prompt IDs to run (e.g. P001,P003). Default: all.")
    parser.add_argument("--languages", type=str, default=None,
                        help="Comma-separated language codes (e.g. en,fr,ro). Default: all.")
    parser.add_argument("--runs",      type=int, default=RUNS_PER_CELL,
                        help=f"Responses per prompt×language cell. Default: {RUNS_PER_CELL}")
    parser.add_argument("--dry-run",   action="store_true",
                        help="Print prompts without calling the API.")
    args = parser.parse_args()

    # Load battery
    battery  = load_battery(BATTERY_PATH)
    prompts  = battery["prompts"]
    all_langs = battery["metadata"]["languages"]

    # Filter if requested
    if args.prompts:
        ids_requested = set(args.prompts.upper().split(","))
        prompts = [p for p in prompts if p["prompt_id"] in ids_requested]
    if args.languages:
        langs = args.languages.lower().split(",")
        for lang in langs:
            assert lang in all_langs, f"Unknown language code: {lang}"
    else:
        langs = all_langs

    print(f"\n{'='*60}")
    print(f"  crosslingual-claude-eval · Response Collection")
    print(f"  Model:   {MODEL}")
    print(f"  Prompts: {[p['prompt_id'] for p in prompts]}")
    print(f"  Langs:   {langs}")
    print(f"  Runs:    {args.runs}")
    print(f"  Total:   {len(prompts) * len(langs) * args.runs} API calls")
    print(f"{'='*60}\n")

    if args.dry_run:
        for p in prompts:
            for lang in langs:
                print(f"[{p['prompt_id']}][{lang}] {p['translations'][lang]}")
        return

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise SystemExit("Set ANTHROPIC_API_KEY environment variable.")

    client = anthropic.Anthropic(api_key=api_key)

    total = len(prompts) * len(langs) * args.runs
    with tqdm(total=total, desc="Collecting") as bar:
        for p in prompts:
            for lang in langs:
                prompt_text = p["translations"][lang]
                for run in range(1, args.runs + 1):
                    out_path = output_path(p["prompt_id"], lang, run)
                    if out_path.exists():
                        bar.set_postfix_str(f"{p['prompt_id']}/{lang}/r{run} SKIPPED")
                        bar.update(1)
                        continue

                    try:
                        result = call_claude(client, prompt_text)
                        record = {
                            "prompt_id":    p["prompt_id"],
                            "cluster":      p["cluster"],
                            "language":     lang,
                            "run":          run,
                            "prompt_text":  prompt_text,
                            "collected_at": datetime.utcnow().isoformat() + "Z",
                            "response":     result,
                        }
                        save_response(out_path, record)
                        bar.set_postfix_str(f"{p['prompt_id']}/{lang}/r{run} ✓ ({result['usage']['output_tokens']} tok)")
                    except Exception as e:
                        print(f"\n  ERROR [{p['prompt_id']}][{lang}] run {run}: {e}")

                    bar.update(1)
                    time.sleep(DELAY_SECONDS)

    print(f"\nDone. Responses saved to: {OUTPUT_DIR.resolve()}")


if __name__ == "__main__":
    main()
