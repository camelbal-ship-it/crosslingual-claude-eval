# Prompt Battery — Design Documentation

## Overview

This directory contains the core prompt battery for the `crosslingual-claude-eval` project. The battery is designed to elicit Claude responses that can be compared for semantic consistency, structural variation, and pragmatic calibration across six languages.

**Languages:** English (EN) · French (FR) · Romanian (RO) · Spanish (ES) · Italian (IT) · German (DE)  
**Prompts:** 8 (one per cluster)  
**Format:** `prompt_battery.json`

---

## ILR Framework Application

The [Interagency Language Roundtable (ILR) Skill Level Descriptions](https://www.govtilr.org/Skills/ILRscale.htm) are used here in a non-standard but principled way: not to rate human speaker proficiency, but to annotate the *linguistic complexity level* at which each prompt operates and the *expected output complexity level* for a fully capable response.

### ILR Input Level
Reflects the linguistic and cognitive demands of the prompt itself — vocabulary abstractness, syntactic complexity, and pragmatic indirection.

### ILR Expected Output Level
Reflects the complexity a well-calibrated response would require to fully address the prompt — not a ceiling, but a benchmark for comparison.

| ILR Level | Descriptor | Application to Output Analysis |
|-----------|------------|-------------------------------|
| 1 | Elementary | Simple declarative responses, limited elaboration |
| 2 | Limited Working | Basic argumentation, common vocabulary |
| 2+ | Limited Working+ | Beginning of abstract/nuanced expression |
| 3 | Professional Working | Full argument structure, hedging, cultural awareness |
| 4 | Full Professional | Sophisticated reasoning, domain expertise, pragmatic precision |
| 5 | Distinguished | Near-native-equivalent complexity and cultural embedding |

---

## Cluster Design Rationale

The 8 clusters were selected to maximize coverage across ILR levels and to probe different *types* of variation:

| Prompt | Cluster | ILR Input | ILR Output | Primary Variation Target |
|--------|---------|-----------|------------|--------------------------|
| P001 | MORAL_REASONING | 2+ | 3 | Hedging, epistemic modality |
| P002 | LEADERSHIP_CULTURE | 2 | 3 | Cultural value framing |
| P003 | METALINGUISTIC | 2+ | 3 | Self-referential language awareness |
| P004 | EMOTIONAL_SUPPORT | 2 | 2+ | Affective register, T-V address forms |
| P005 | TECHNICAL_EXPLANATION | 3 | 3 | Anglicism density, explanatory structure |
| P006 | ABSTRACT_ETHICS_AI | 4 | 4–5 | Legal tradition invocation, philosophical framing |
| P007 | CREATIVE_NARRATIVE | 2 | 3 | Aesthetic choices, sentence rhythm |
| P008 | LIFE_DECISIONS | 2+ | 3 | Pragmatic values, risk framing |

---

## Translation Methodology

All prompts were translated for **semantic equivalence**, not word-for-word correspondence. Key decisions:

- **Formality register:** Formal address (`vous`, `Sie`, `dumneavoastră`) used consistently except in P004 and P008, where the scenario implies intimacy and informal register (`tu`, `tu`, `tu`) is linguistically appropriate.
- **Technical terminology:** Domain-specific terms (e.g., "neural network") rendered in the most common professional usage for each language rather than forced native calques — this itself is a measurable variable in P005.
- **Pragmatic equivalence:** Prompt-final question structure preserved where grammatically natural; restructured where syntax demands differ (e.g., German verb-final embedding).
- **Diacritics:** Full use of language-appropriate diacritics (French accents, Romanian ș/ț/ă/â/î, German Umlaut) to avoid artificially simplified input.

---

## Files

```
prompts/
├── prompt_battery.json     # Machine-readable full battery with metadata
└── README.md               # This file
```

---

## Usage

```python
import json

with open("prompts/prompt_battery.json", "r", encoding="utf-8") as f:
    battery = json.load(f)

languages = battery["metadata"]["languages"]  # ['en', 'fr', 'ro', 'es', 'it', 'de']

for prompt in battery["prompts"]:
    print(f"\n{prompt['prompt_id']} — {prompt['cluster']}")
    for lang, text in prompt["translations"].items():
        print(f"  [{lang}] {text}")
```

---

## Citation

If using this battery in derivative work, please cite:

```
Baluta, C. (2026). crosslingual-claude-eval: An ILR-informed prompt battery
for cross-lingual LLM response consistency evaluation.
GitHub. https://github.com/camelbal-ship-it/crosslingual-claude-eval
```

---

## Planned Extension

The full project targets 12 clusters × 6 languages. Additional clusters in development:

- FACTUAL_RECALL (ILR 1–2)
- IMPLICIT_CULTURAL_KNOWLEDGE (ILR 3)
- REGISTER_SWITCHING (ILR 3–4)
- AMBIGUOUS_REFERENT (ILR 4)

See `METHODOLOGY.md` (root) for full framework specification.
