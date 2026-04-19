# METHODOLOGY.md
## ILR-Informed Cross-Lingual LLM Response Consistency Evaluation

**Project:** crosslingual-claude-eval  
**Author:** Camelia Baluta  
**Affiliation at time of study:** Independent researcher; former DLIFLC faculty (12 years), ILR/OPI specialist  
**Version:** 1.0 — April 2026

---

## 1. Background and Motivation

Large language models (LLMs) trained on multilingual corpora do not treat all languages equally. Training data distributions, tokenization artifacts, and RLHF feedback sourced predominantly from English-speaking annotators may produce outputs that vary in quality, length, hedging behavior, and cultural framing across languages — even when the semantic input is held constant.

This project introduces a systematic evaluation framework grounded in the **Interagency Language Roundtable (ILR) Skill Level Descriptions** — a proficiency framework developed for human language assessment — and adapts it for the analysis of LLM-generated outputs. The ILR framework provides a principled vocabulary for describing linguistic complexity, register, and pragmatic adequacy that is well-suited to the cross-lingual comparison task.

---

## 2. The ILR Framework: Standard Application

The ILR scale (Levels 0–5, with "+" subdivisions) describes human language proficiency across five skill areas: Speaking, Listening, Reading, Writing, and Translation. Level 3 ("Professional Working Proficiency") is the operational threshold for professional communication; Level 5 ("Functionally Native") represents near-native performance.

**ILR Skill Level Descriptors (abbreviated):**

| Level | Label | Core Descriptor |
|-------|-------|----------------|
| 0 | No Proficiency | No functional ability |
| 1 | Elementary | Basic survival-level communication |
| 2 | Limited Working | Routine social and simple professional communication |
| 2+ | Limited Working+ | Beginning of abstract discussion |
| 3 | Professional Working | Full range of professional topics, some nuance |
| 3+ | Professional Working+ | Sophisticated argumentation, precision |
| 4 | Full Professional | Near-complete command; subtle register control |
| 4+ | Full Professional+ | Highly specialized or technical discourse |
| 5 | Distinguished | Equivalent to a highly educated and versed native speaker |

---

## 3. Novel Application: LLM Output Analysis

### 3.1 Reframing the Framework

This project applies ILR descriptors to **model outputs**, not human speakers. Specifically, we use ILR-level language to operationalize two constructs:

**Prompt Complexity Level (PCL):** The ILR level a human would need to *produce* the prompt text and fully comprehend its pragmatic demands. This is annotated per prompt in `prompt_battery.json`.

**Response Adequacy Level (RAL):** The ILR level a human would need to have *produced* the observed response — a measure of the linguistic and pragmatic sophistication of the model's output in a given language.

The central research question is: **Does RAL vary significantly across languages when PCL is held constant?**

### 3.2 Operationalizing RAL

RAL is not a single metric. It is a composite assessment along five dimensions, each drawn from ILR descriptor language:

| Dimension | Operationalization | Measurement Method |
|-----------|-------------------|-------------------|
| **Lexical Range** | Breadth and precision of vocabulary used | Type-Token Ratio (TTR); low-frequency word density |
| **Syntactic Complexity** | Clause-embedding depth, coordination patterns | Mean Dependency Distance (MDD); clause count per sentence |
| **Pragmatic Appropriateness** | Register consistency, illocutionary force calibration | Manual annotation + classifier-based proxy |
| **Epistemic Marking** | Hedging density, modal verb frequency, evidential markers | Automated lexicon-based extraction per language |
| **Discourse Coherence** | Topic continuity, cohesion device use | Coreference chain analysis; discourse connector density |

### 3.3 Semantic Similarity as Baseline Consistency Measure

Before RAL analysis, semantic equivalence across language responses is confirmed using multilingual sentence embeddings:

- **Model:** `paraphrase-multilingual-mpnet-base-v2` (sentence-transformers)
- **Metric:** Cosine similarity between each non-English response and the English baseline
- **Interpretation:** Similarity < 0.70 flags potential semantic divergence warranting qualitative review

---

## 4. Prompt Battery Design

### 4.1 Equivalence Standards

Each prompt was developed in English and translated by a six-language professional with ILR 3+ proficiency in all target languages. Translation criteria:

1. **Semantic equivalence** over literal correspondence
2. **Pragmatic naturalness** — prompts sound like native speaker questions, not machine translations
3. **Register consistency** — formality level held constant within each prompt (with principled exceptions in P004 and P008 where informal register is contextually appropriate)
4. **Lexical density parity** — approximate match in content word count across versions

### 4.2 Cluster Selection Logic

Eight clusters were selected to provide:
- Coverage across ILR levels 2 through 4+
- Variation in the *type* of language produced (affective, technical, creative, argumentative)
- Maximal expected variation in cross-lingual output patterns (high diagnostic value)
- Replicability in future studies (no time-sensitive or model-version-specific content)

See `prompts/README.md` for full cluster documentation.

### 4.3 Design Controls

| Control | Implementation |
|---------|---------------|
| Model version | Fixed: `claude-sonnet-4-20250514` |
| System prompt | Null (model default) across all cells |
| Temperature | 1.0 (default); separate reproducibility run at T=0 |
| Runs per cell | 3 (variance estimation); primary analysis on run 1 |
| Collection window | Single calendar week (minimize model drift) |
| Interface | API only (no chat UI variables) |

---

## 5. Analysis Pipeline

```
prompts/prompt_battery.json
        │
        ▼
scripts/collect_responses.py   →   data/raw/{prompt_id}/{lang}/run_{n}.json
        │
        ▼
scripts/preprocess.py          →   data/processed/responses_flat.csv
        │
        ├──► scripts/semantic_similarity.py   →   results/semantic_similarity.csv
        ├──► scripts/length_analysis.py       →   results/length_stats.csv
        ├──► scripts/ilr_proxy_scoring.py     →   results/ral_scores.csv
        └──► scripts/visualize.py             →   figures/
```

---

## 6. Researcher Positionality and Expertise Contribution

The interpretive validity of this project rests significantly on the researcher's professional background. Camelia Baluta holds ILR/OPI assessor certifications and brings 12 years of language testing experience at DLIFLC, the U.S. government's primary language training institution. This background enables:

1. **Principled PCL annotation** — not algorithmic, but expert-judgment-based, mirroring ILR testing practice
2. **Qualitative response review** — direct identification of naturalness failures, register breaks, and culturally inappropriate framings in all six languages
3. **ILR-grounded interpretation** — connecting quantitative results to the proficiency constructs that give them meaning

This is the methodological contribution that differentiates this project from purely computational cross-lingual benchmarks.

---

## 7. Limitations

1. **Single model:** Results are specific to Claude (Sonnet 4). Generalization to other LLMs requires replication.
2. **Six languages:** All six are high-resource European languages with strong representation in training data. Results may not generalize to lower-resource languages.
3. **Researcher subjectivity in ILR annotation:** Partially mitigated by published ILR descriptor anchors, but inter-rater reliability data is not available for this project.
4. **Temporal validity:** LLM behavior changes with model updates. All collection timestamps are recorded for reproducibility documentation.
5. **Prompt battery coverage:** 8 clusters do not exhaust the space of communicative functions. Planned extension to 12 clusters in v2.

---

## 8. Ethical Considerations

- No personal data collected
- No human subjects involved
- All API usage complies with Anthropic's usage policies
- Data and code released under MIT license

---

## 9. References

- Interagency Language Roundtable. (2012). *ILR Skill Level Descriptions for Listening, Speaking, Reading, Writing, and Translation.* https://www.govtilr.org
- Conneau, A., et al. (2020). Unsupervised Cross-lingual Representation Learning at Scale. *ACL 2020.*
- Ahuja, K., et al. (2023). MEGA: Multilingual Evaluation of Generative AI. *EMNLP 2023.*
- Bang, Y., et al. (2023). A Multitask, Multilingual, Multimodal Evaluation of ChatGPT. *arXiv:2302.04023.*
- Lai, V.D., et al. (2023). ChatGPT Beyond English: Towards a Comprehensive Evaluation of Large Language Models in Multilingual Learning. *arXiv:2304.05613.*

---

*This document should be cited as part of the project methodology. For questions about ILR framework application, contact the author via the project repository.*
