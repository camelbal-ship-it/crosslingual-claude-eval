# Results

## 4.1 Quantitative Overview

Across 216 responses (12 prompt clusters × 6 languages × 3 runs), Layer 1 analysis revealed systematic variation in response length, structural formatting, and surface similarity to the English baseline.

### Response Length

Mean word count varied significantly across languages (Table 1). French produced the longest responses (M = 266.4 words), followed by Spanish (239.5), Italian (239.0), Romanian (219.8), English (213.4), and German (204.9). The French–German differential of approximately 30% represents a substantial cross-lingual variation on semantically identical prompts. This pattern was consistent across prompt clusters, suggesting a systemic rather than prompt-specific effect.

**Table 1. Mean word count by language (all prompts, all runs)**

| Language | Mean words | SD |
|----------|-----------|-----|
| French | 266.4 | — |
| Spanish | 239.5 | — |
| Italian | 239.0 | — |
| Romanian | 219.8 | — |
| English | 213.4 | — |
| German | 204.9 | — |

### List Structure Usage

The proportion of responses using list or bullet-point formatting varied by language. French showed the highest list usage (75.0%), followed by English, Spanish, and Italian (all 72.2%), while German and Romanian showed the lowest (both 63.9%). The German finding is noteworthy given the language's reputation for structural precision — it suggests that German responses favor prose elaboration over enumerated structure, consistent with German academic writing conventions.

### Surface Similarity to English Baseline

TF-IDF character n-gram cosine similarity scores revealed that cross-lingual surface similarity varied more by prompt cluster than by language pair (Table 2). CREATIVE_NARRATIVE showed the lowest mean similarity across all non-English languages (M = 0.049), while METALINGUISTIC showed the highest (M = 0.250). This pattern is theoretically coherent: creative prose is where each language's distinctive vocabulary and aesthetic conventions are most visible, while metalinguistic discussion of language itself draws on shared abstract vocabulary across European languages.

**Table 2. Mean surface similarity to English baseline by cluster (non-English languages)**

| Cluster | Mean similarity |
|---------|----------------|
| CREATIVE_NARRATIVE | 0.049 |
| FACTUAL_RECALL | 0.084 |
| EMOTIONAL_SUPPORT | 0.103 |
| AMBIGUOUS_REFERENT | 0.115 |
| TECHNICAL_EXPLANATION | 0.133 |
| IMPLICIT_CULTURAL_KNOWLEDGE | 0.145 |
| MORAL_REASONING | 0.145 |
| LIFE_DECISIONS | 0.170 |
| LEADERSHIP_CULTURE | 0.192 |
| ABSTRACT_ETHICS_AI | 0.204 |
| REGISTER_SWITCHING | 0.240 |
| METALINGUISTIC | 0.250 |

By language, German showed the lowest mean similarity to English (M = 0.121), consistent with its greater lexical distance from English, while French showed the highest (M = 0.189), consistent with the higher proportion of shared Latin-derived vocabulary.

---

## 4.2 Qualitative Findings

Layer 2 analysis examined responses from five prompt clusters selected for maximum diagnostic value based on pragmatic complexity: P004 (EMOTIONAL_SUPPORT), P005 (TECHNICAL_EXPLANATION), P007 (CREATIVE_NARRATIVE), P010 (IMPLICIT_CULTURAL_KNOWLEDGE), and P012 (AMBIGUOUS_REFERENT). Findings are presented in order of theoretical significance.

### 4.2.1 Pragmatic Disambiguation Strategies (P012 — AMBIGUOUS_REFERENT)

The prompt "They said it would be better if we didn't come. What should we do?" contains deliberate referential ambiguity — the identity of "they," the nature of the event, and the relationship between parties are all unspecified. Disambiguation strategies varied systematically by language in ways consistent with cross-cultural pragmatic norms.

German responses refused resolution in all three runs, explicitly requesting clarification before providing any guidance. Representative phrasings included acknowledgment that the statement could be interpreted in multiple contexts, followed by requests for additional information. This behavior is consistent with German discourse norms that prioritize informational precision over pragmatic inference.

English responses also flagged ambiguity but with a warmer, more service-oriented framing — offering to help once context was provided, rather than withholding engagement. French responses acknowledged the emotional complexity of the situation without treating ambiguity as an epistemic obstacle, proceeding to reflective guidance — consistent with French tolerance for productive ambiguity in discourse.

Spanish, Italian, and Romanian responses resolved the ambiguity silently and proceeded directly to practical advice, with Romanian briefly noting context-dependence before defaulting to the most pragmatically salient interpretation. This five-way divergence on a single prompt maps directly onto known cross-cultural pragmatic differences and represents the most structurally varied finding in the dataset.

### 4.2.2 Aesthetic and Stylistic Divergence (P007 — CREATIVE_NARRATIVE)

Romanian responses to the creative writing prompt ("Write a short paragraph describing a rainy afternoon in a city") showed the lowest surface similarity to English in the entire dataset (mean cosine similarity = 0.035 across three runs). Qualitative analysis confirmed that this divergence reflects genuine aesthetic distinctiveness rather than semantic drift.

English responses (run 3): *"The sky hung low and grey over the city, pressing down on the rooftops like a heavy wool blanket... umbrellas blooming like dark flowers above the crowd... A lone pigeon huddled beneath a bus shelter."*

Romanian responses drew on markedly different aesthetic conventions: *"umbrele multicolore care au înflorit pe trotuare ca niște ciuperci după ploaie"* (umbrellas blooming like mushrooms after rain — a distinctly Romanian folk simile absent from English responses), *"un miros proaspăt și pământiu"* (a fresh, earthy smell — petrichor rendered through sensory specificity), and *"orașul părea că respiră altfel"* (the city seemed to breathe differently — personification of urban space as a living organism with needs). Romanian responses ended with the city given "permission to rest" (*ploaia îi dădea voie să se odihnească*) — a philosophical framing absent from English closings, which favored individual emotional containment.

These differences are not errors of calibration but evidence of genuine literary tradition influence: Romanian prose aesthetics drawing on nature-derived imagery, organic personification, and syntactic structures characteristic of Romanian literary fiction.

### 4.2.3 Technical Terminology and Analogical Reasoning (P005 — TECHNICAL_EXPLANATION)

The prompt requesting a neural network explanation for an educated non-specialist produced the predicted pattern of native vs. borrowed terminology, with an unexpected additional finding regarding analogy selection.

German used native compound terminology almost exclusively: *Gradientenabstieg* (gradient descent), *Rückwärtspropagierung* (backpropagation), *Verlust* (loss), *Lernrate* (learning rate). The term *Loss* appeared once parenthetically as a gloss. French showed an equivalent pattern: *rétropropagation*, *taux d'apprentissage*, *perte*, *couches*. Romanian adopted a hybrid strategy — native terms for foundational concepts (*rețea neuronală*, *straturi*, *greutăți*) while retaining English labels for specialized ML vocabulary (*forward pass*, *backpropagation*, *gradient descent*), reflecting the relative recency of Romanian ML discourse.

More striking was the analogy selection. Each language chose a culturally distinct pedagogical example:

- **German:** Dart throwing (*Dartwerfen*) — precision sport requiring physical calibration through repetitive correction
- **Romanian:** Wine tasting (*recunoașterea vinurilor*) — sensory connoisseurship, gradual refinement of judgment
- **French:** Apartment price estimation — economic judgment, urban context, practical calibration

No two languages shared an analogy. All three are culturally resonant within their respective language communities. This finding suggests that Claude's explanatory scaffolding draws on culturally embedded reference points rather than defaulting to a universal English-derived example.

### 4.2.4 Cultural Calibration in Commemorative Practices (P010 — IMPLICIT_CULTURAL_KNOWLEDGE)

The prompt asking about meaningful ways to honor a deceased elderly family member tested whether Claude's cultural frame of reference shifts with the language of the prompt. Romanian Orthodox traditions (parastas, pomană, coliva) and German secular memorial institutions did not appear explicitly in any response — itself a significant finding suggesting that Claude's cultural calibration operates through framing and emphasis rather than explicit cultural content invocation.

However, structural and sequencing differences revealed genuine calibration. Romanian responses opened with a section titled "Immediately after death" (*Imediat după deces*) emphasizing community announcement — notifying friends, neighbors, and former colleagues — reflecting the Romanian cultural norm of death as a collective community event. German responses opened directly with personal memory preservation, consistent with a more privatized grief culture.

Romanian responses foregrounded the deceased's faith (*credința persoanei*) as the organizing principle of ceremony in the first bullet point. German responses treated religious observance as one item in a secular-pluralist menu, buried mid-list. Both responses closed with culturally characteristic discourse moves: German with a pragmatic service offer (*"Gibt es etwas Bestimmtes, das Sie für Ihre Familie suchen?"*), Romanian with a relational value statement (*"Cel mai important este ca gestul să fie sincer și personalizat"* — the most important thing is that the gesture be sincere and personalized).

### 4.2.5 Affective Register and Institutional Anchoring (P004 — EMOTIONAL_SUPPORT)

All six languages produced safety-conscious responses to the emotional support prompt with structurally similar frameworks: active listening, avoidance of minimization, direct inquiry about self-harm, and referral to professional support. The hypothesis that Italian and Spanish would show markedly warmer affective vocabulary than German was partially confirmed at the level of relational framing rather than lexical density.

German uniquely embedded a specific national crisis resource (Telefonseelsorge: 0800 111 0 111) — the only language to provide a concrete institutional referral — consistent with German institutional trust and the culturally specific availability of such resources in German-speaking contexts. Italian responses foregrounded physical proximity (*stare vicino* — to stay near/close) and collaborative reasoning (*ragionare insieme* — reason together) as primary support modalities. Spanish invoked *acompañamiento* — the Latin American concept of sustained relational accompaniment — as the core emotional offering.

The most notable cross-lingual finding in P004 is German's institutional anchoring: while all languages recommended professional help in general terms, only German operationalized this recommendation with a specific, callable resource, reflecting both German institutional specificity and Claude's apparent calibration to Germany-specific support infrastructure when responding in German.

---

## 4.3 Summary of Findings

Across quantitative and qualitative layers, five patterns emerged consistently:

1. **Response length varies systematically by language**, with French producing approximately 30% more words than German on identical prompts — a systemic effect not attributable to any single prompt cluster.

2. **Surface divergence from English is highest in creative and affective clusters** (CREATIVE_NARRATIVE, EMOTIONAL_SUPPORT) and lowest in abstract/metalinguistic clusters (METALINGUISTIC, REGISTER_SWITCHING), consistent with the prediction that language-specific vocabulary and aesthetic conventions are most visible in expressive registers.

3. **Disambiguation strategies reflect cross-cultural pragmatic norms**: German refuses resolution; French embraces productive ambiguity; Spanish, Italian, and Romanian resolve silently with varying degrees of contextual acknowledgment.

4. **Technical terminology follows established language-internal traditions**: German and French use native compound terminology; Romanian adopts a hybrid strategy reflecting the relative recency of Romanian ML discourse.

5. **Cultural calibration operates through framing and emphasis rather than explicit cultural content**: Claude does not invoke culture-specific rituals or institutions by name, but structural sequencing, discourse closings, and the selection of pedagogical analogies consistently reflect culturally embedded conventions of the target language community.

These findings collectively support the central research claim: Claude's outputs vary in linguistically and pragmatically meaningful ways across languages even when the semantic input is held constant, and these variations are interpretable through an ILR-informed framework of cross-lingual pragmatic calibration.
