# Cross-Lingual Response Consistency in Large Language Models: An ILR-Informed Evaluation of Claude Across Six Languages

**Camelia Baluta**
Independent Researcher | Former Faculty, Defense Language Institute Foreign Language Center
ILR/OPI Assessment Specialist

*April 2026*

---

## Abstract

Large language models (LLMs) trained on multilingual corpora do not treat all languages equally. Training data distributions, tokenization artifacts, and reinforcement learning from human feedback sourced predominantly from English-speaking annotators may produce outputs that vary in quality, length, pragmatic calibration, and cultural framing across languages — even when the semantic input is held constant. This paper introduces a systematic evaluation framework grounded in the Interagency Language Roundtable (ILR) Skill Level Descriptions and applies it to Claude (Sonnet 4.6) across six languages: English, French, Romanian, Spanish, Italian, and German. We administer a battery of 12 semantically equivalent prompt clusters spanning ILR complexity levels 1 through 4, collect 216 responses (12 prompts × 6 languages × 3 runs), and analyze outputs through a two-layer methodology combining automated quantitative metrics with expert ILR qualitative assessment. Quantitative analysis reveals that French responses are approximately 30% longer than German responses on identical prompts, and that creative and affective clusters show the highest cross-lingual surface divergence. Qualitative analysis — conducted by a six-language professional with 12 years of ILR/OPI assessment experience — identifies five cross-lingual variation patterns: systematic differences in pragmatic disambiguation strategies, aesthetic and literary tradition divergence in creative output, language-internal technical terminology norms, cultural calibration through discourse framing rather than explicit content, and institutional anchoring in affective support responses. We argue that ILR-informed expert judgment applied to LLM outputs constitutes a novel and underreported evaluation methodology that complements purely computational benchmarks, and that cross-lingual output variation in Claude is interpretable, systematic, and consequential for equitable multilingual AI deployment.

**Keywords:** cross-lingual evaluation, large language models, ILR framework, pragmatic calibration, multilingual NLP, Claude, response consistency

---

## 1. Introduction

### 1.1 The Problem of Cross-Lingual Consistency

When a user asks Claude a question in Romanian, do they receive a response of equivalent quality, cultural appropriateness, and pragmatic calibration to a user asking the same question in English? This question has significant implications for the equitable deployment of AI systems across language communities — yet it remains underexplored in the literature.

Existing cross-lingual LLM benchmarks typically measure factual accuracy, reasoning correctness, or task completion on structured tasks (Ahuja et al., 2023; Bang et al., 2023; Lai et al., 2023). These approaches capture important dimensions of model performance but are less equipped to measure the pragmatic, stylistic, and culturally embedded dimensions of language use that determine whether a response feels appropriate, complete, and well-calibrated to its linguistic context. A response can be factually correct and pragmatically inadequate simultaneously — a distinction that structured benchmarks are not designed to capture.

This gap is particularly significant for languages that are well-represented in training data but whose cultural and pragmatic conventions may be underrepresented relative to English. French, German, Spanish, Italian, and Romanian are all high-resource European languages with substantial training data presence — yet their speakers may still receive outputs that are calibrated to English-language discourse norms rather than the conventions of their own language communities.

### 1.2 The ILR Framework as an Evaluation Tool

The Interagency Language Roundtable (ILR) Skill Level Descriptions (2012) provide a principled, field-tested framework for describing linguistic and pragmatic competence across five skill areas at levels 0 through 5. Developed for human language assessment and widely used in U.S. government language training and certification, the ILR scale has not previously been applied systematically to LLM output evaluation.

This project proposes and operationalizes such an application. We introduce two constructs adapted from the ILR framework for LLM output analysis:

**Prompt Complexity Level (PCL):** The ILR level a human would need to fully comprehend and respond appropriately to a given prompt, annotated by an expert assessor for each prompt in the battery.

**Response Adequacy Level (RAL):** The ILR level a human would need to have produced the observed response — a measure of the linguistic and pragmatic sophistication of the model's output assessed against the demands of the prompt that generated it.

The central research question is: *Does RAL vary significantly across languages when PCL is held constant?*

### 1.3 Why This Project and Why Now

Several convergent factors motivate this study at this moment.

First, frontier LLMs are being deployed at scale across multilingual user populations with limited systematic evaluation of cross-lingual output consistency. The consequences of inconsistency are not merely academic — they include differential quality of AI-assisted services across language communities, potential cultural misrepresentation, and the reproduction of English-centric discourse norms in non-English contexts.

Second, the ILR framework provides a uniquely appropriate vocabulary for this evaluation. Unlike automated metrics that measure surface properties, ILR descriptors capture the functional and pragmatic dimensions of language use — precisely the dimensions most likely to vary meaningfully across languages in LLM outputs.

Third, this project is conducted by a researcher with direct expertise in ILR/OPI assessment across all six target languages, enabling a quality of qualitative judgment that purely computational approaches cannot replicate. The researcher's native Romanian competence is particularly relevant for identifying the absence of culture-specific content — a finding that requires insider knowledge to make credibly.

### 1.4 Scope and Contributions

This paper makes four primary contributions:

1. **A novel evaluation framework** adapting ILR Skill Level Descriptions to LLM output analysis through the constructs of Prompt Complexity Level (PCL) and Response Adequacy Level (RAL).

2. **A citable prompt battery** of 12 semantically equivalent prompt clusters across six languages, annotated with ILR complexity levels, linguistic feature targets, and researcher hypotheses, made publicly available at [github.com/camelbal-ship-it/crosslingual-claude-eval](https://github.com/camelbal-ship-it/crosslingual-claude-eval).

3. **Five cross-lingual variation findings** in Claude (Sonnet 4.6) that are systematic, interpretable, and theoretically coherent with known cross-cultural pragmatic differences.

4. **A methodological argument** for the value of expert ILR judgment in LLM evaluation — a contribution to the growing conversation about what human expertise can provide that automated metrics cannot.

### 1.5 Paper Organization

Section 2 reviews related work in cross-lingual LLM evaluation and identifies the gap this project addresses. Section 3 describes the methodology, including prompt battery design, data collection protocol, and the two-layer analysis framework. Section 4 presents quantitative and qualitative results. Section 5 discusses implications for multilingual AI deployment and evaluation methodology. Section 6 acknowledges limitations and outlines directions for future work.

---

## 2. Related Work

### 2.1 Cross-Lingual LLM Benchmarks

Several recent studies have evaluated LLM performance across multiple languages. Bang et al. (2023) evaluated ChatGPT on 37 tasks across 26 languages, finding significant performance degradation for low-resource languages. Ahuja et al. (2023) introduced MEGA, a multilingual evaluation benchmark covering 16 NLP datasets across 70 languages. Lai et al. (2023) assessed cross-lingual reasoning and generation tasks across multiple model families. These studies established that cross-lingual performance gaps exist and are substantial for many languages.

However, these benchmarks share a common design assumption: that cross-lingual quality can be measured through task accuracy on structured inputs with ground-truth answers. This assumption is appropriate for factual recall, mathematical reasoning, and classification tasks, but systematically underspecifies the evaluation of pragmatic, stylistic, and culturally embedded language use — precisely the dimensions most relevant to user experience in open-ended conversational contexts.

### 2.2 Pragmatic and Cultural Evaluation

A smaller body of work addresses cultural and pragmatic dimensions of LLM outputs. Hershcovich et al. (2022) examined cultural biases in NLP systems and argued for culturally-aware evaluation frameworks. Cao et al. (2023) probed cultural knowledge in LLMs across multiple languages, finding that models demonstrate uneven cultural knowledge with English-centric biases. Johnson et al. (2022) examined politeness and formality calibration across languages in neural machine translation outputs.

None of these studies apply a proficiency-based framework to evaluate the linguistic and pragmatic adequacy of LLM outputs against the functional demands of the prompts that generated them. The ILR framework fills this gap.

### 2.3 The ILR Framework in Language Assessment

The ILR Skill Level Descriptions (Interagency Language Roundtable, 2012) are the standard proficiency framework for U.S. government language assessment, used in hiring, training evaluation, and certification across military, intelligence, and diplomatic contexts. The Oral Proficiency Interview (OPI) and its written equivalent (WPT) are the primary instruments for ILR assessment, conducted by certified assessors.

The ILR scale has been applied to machine translation evaluation through the ARPA MT program, which used ILR proficiency levels to calibrate text difficulty and output quality assessment (White, O'Connell, & O'Mara, 1994), and to calibrate language learning materials. Related work exists on rubric-based LLM evaluation and on mapping model outputs to proficiency frameworks such as CEFR and ACTFL (common in language learning applications). However, ILR-level annotation is not a standard or widely adopted evaluation framework for LLM-generated outputs — it is rarely used as a primary annotation schema in LLM evaluation literature, and no published study has applied it systematically to cross-lingual output consistency analysis. This paper proposes and operationalizes that application, arguing that the ILR framework's functional and pragmatic descriptors are particularly well-suited to capturing the dimensions of language use most likely to vary meaningfully across languages in open-ended conversational AI outputs.

---
