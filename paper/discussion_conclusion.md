# Discussion, Limitations, Conclusion, and References

---

## 5. Discussion

### 5.1 Implications for Multilingual AI Deployment

The findings of this study have direct implications for how AI systems like Claude are deployed across multilingual user populations. Cross-lingual output variation is not merely an academic curiosity — it has practical consequences for the equity and reliability of AI-assisted services when those services are accessed in different languages.

The most consequential finding for deployment is the cultural calibration pattern identified in P010 (IMPLICIT_CULTURAL_KNOWLEDGE): Claude's responses in Romanian did not invoke Romanian-specific mourning traditions, reading instead as structurally consistent with a culturally neutralized English-language template. A Romanian user seeking culturally grounded guidance on honoring a deceased family member receives advice that is technically correct but culturally generic — advice that would be equally appropriate for any Western European context. This is not a failure of factual accuracy; it is a failure of cultural adequacy, and it is the kind of failure that purely accuracy-based benchmarks cannot detect.

The pragmatic disambiguation findings (P012) raise a related concern. A German-speaking user asking an ambiguous question receives a minimal, precise clarification request — consistent with German discourse norms favoring informational economy. A Spanish-speaking user asking the identical question receives a full interpretive scaffold: mapped interpretations, response options, and a clarification request embedded within an elaborated decision framework. Both users are asked for more context before receiving a direct answer, but the Spanish-speaking user receives substantially more analytical support in the interim. The model is not producing errors in either case; it is producing culturally calibrated responses. But the calibration is asymmetric in elaboration depth: some users receive richer decision support than others on identical inputs. Whether this asymmetry is appropriate or constitutes differential service quality is a question that deployment decisions should engage explicitly.

The response length differential — French responses approximately 30% longer than German on identical prompts — suggests that users of different languages may be receiving substantively different amounts of information. If response length correlates with informational completeness (a relationship that merits further investigation), then French-speaking users are systematically receiving more elaborated responses than German-speaking users. This is a systemic effect that aggregates across millions of interactions.

### 5.2 Implications for LLM Evaluation Methodology

The two-layer methodology introduced in this paper — combining automated quantitative metrics with expert ILR qualitative assessment — demonstrates that different analytical layers answer fundamentally different questions and are not substitutable for each other.

Quantitative analysis (Layer 1) established *that* variation exists and identified *where* it was largest. Surface similarity scores correctly flagged Romanian CREATIVE_NARRATIVE responses as the most divergent from English. Response length metrics revealed the French-German differential. These are reproducible, scalable findings that can be computed for any dataset without domain expertise.

But Layer 1 could not determine *what the variation means*. The low surface similarity of Romanian creative responses could have indicated semantic drift, translation failure, or — as qualitative analysis revealed — genuine aesthetic distinctiveness reflecting a different literary tradition. The difference between these interpretations is consequential: one implies a model deficiency, the other implies appropriate cross-lingual calibration. Only ILR-informed expert judgment, applied by a researcher with native competence in Romanian and professional assessment training, could make that distinction reliably.

This is the core methodological contribution of this paper: demonstrating that the interpretive gap between detecting variation and understanding its meaning requires domain expertise that automated metrics cannot provide. We argue that this gap is systematic and not merely a feature of the specific clusters analyzed here. Any cross-lingual evaluation that stops at quantitative metrics risks mischaracterizing culturally appropriate variation as model error, or — equally — mischaracterizing genuine model failures as cultural appropriateness.

The ILR framework provides a particularly well-suited vocabulary for navigating this interpretive gap. Its functional and pragmatic descriptors — register appropriateness, pragmatic completeness, cultural calibration, illocutionary adequacy — map directly onto the dimensions of language use that vary meaningfully across languages in LLM outputs. We encourage the NLP evaluation community to consider ILR-level annotation as a complement to existing rubric-based and automated evaluation approaches, particularly for open-ended multilingual evaluation tasks.

### 5.3 On Cultural Calibration vs. Cultural Reproduction

A finding that merits careful theoretical framing is the analogy selection pattern in P005 (TECHNICAL_EXPLANATION). Claude chose culturally resonant analogies for each language — dart throwing for German, wine tasting for Romanian, apartment price estimation for French — without being instructed to do so. This is, on one reading, an impressive demonstration of cross-lingual cultural calibration. On another reading, it raises questions about whose cultural stereotypes are being reproduced.

The German-dart-throwing association, the Romanian-wine-tasting association, and the French-apartment-economics association are recognizable cultural touchstones, but they are also simplifications. Not all German speakers would find dart throwing a natural reference; not all Romanian speakers are familiar with wine connoisseurship. The model is drawing on statistical regularities in its training data — cultural associations that are common enough to be reproduced but not universal enough to be assumed.

We flag this not as a finding requiring correction but as a dimension of cross-lingual calibration that deserves ongoing scrutiny. The question of whether a model's cultural calibration reflects the diversity within a language community, or only its most statistically common associations, is one that this study's methodology is not equipped to answer definitively — but that future work should address.

---

## 6. Limitations

### 6.1 Single Model

All data in this study was collected from a single model — Claude Sonnet 4.6, collected during a single week in April 2026. The findings are specific to this model version and cannot be generalized to other LLMs (GPT-4, Gemini, Mistral, etc.) or to future versions of Claude. Cross-lingual variation patterns are likely to differ substantially across model families, training data compositions, and RLHF feedback sources. Replication across model families is a necessary next step before any findings can be treated as characterizing LLM behavior generally rather than Claude specifically.

### 6.2 Six High-Resource European Languages

The six languages in this study — English, French, Romanian, Spanish, Italian, and German — are all high-resource European languages with substantial representation in Claude's training data. The variation patterns identified here may differ substantially for lower-resource languages, non-European languages, or languages with non-Latin scripts. The finding that cross-lingual variation is "interpretable and systematic" may not hold for languages where training data is sparse and model behavior is less predictable. This is a significant scope limitation that the paper acknowledges explicitly.

Additionally, all six languages belong to the Indo-European family and share considerable typological similarity. Cross-lingual variation patterns for typologically distant language pairs (e.g., English-Japanese, English-Arabic, English-Swahili) are likely to be more pronounced and may reveal qualitatively different failure modes than those identified here.

### 6.3 TF-IDF Similarity Proxy

The semantic similarity analysis in this study uses TF-IDF character n-gram cosine similarity — a surface-level proxy that captures shared vocabulary, proper nouns, numbers, and borrowed technical terms, but does not measure semantic equivalence at the meaning level. This choice was necessitated by network restrictions preventing access to multilingual sentence embedding models during data collection.

TF-IDF similarity is appropriate for identifying *relative* divergence patterns across clusters and languages, and the cluster-level ordering produced by this method is consistent with theoretical expectations. However, it should not be treated as a measure of semantic equivalence. Two responses can have very low TF-IDF similarity while conveying equivalent meaning (as in the Romanian CREATIVE_NARRATIVE case), and two responses can have high TF-IDF similarity while differing substantially in pragmatic framing.

For publication validation, similarity results should be confirmed using a multilingual sentence embedding model (recommended: `paraphrase-multilingual-mpnet-base-v2`) in an unrestricted network environment. This validation step is planned as part of the camera-ready revision process.

### 6.4 Single Rater — Inter-Rater Reliability

The qualitative Layer 2 analysis was conducted by a single researcher. While the researcher's ILR/OPI assessor certification and six-language proficiency provide strong grounds for the judgments made, the absence of a second rater means inter-rater reliability cannot be formally reported. ILR assessment practice typically requires two certified assessors for official ratings; this study diverges from that standard in the interest of feasibility for an independent research project.

This limitation is most consequential for the findings that rely most heavily on researcher judgment: the characterization of the Romanian P010 response as "culturally neutralized," the attribution of German P004 responses to "institutional trust," and the literary tradition claims in P007. These interpretations are grounded in the researcher's professional expertise but have not been validated by an independent assessor.

Future work should recruit at least one additional certified ILR assessor for each language pair to establish inter-rater reliability estimates, ideally using Cohen's kappa on the RAL ratings assigned to each response.

### 6.5 Prompt Battery Coverage

The 12-cluster prompt battery covers a broad range of ILR complexity levels and communicative functions but does not exhaust the space of cross-lingual variation. Several potentially diagnostic prompt types are absent from this study, including: requests for humor or irony (which vary substantially across cultures), requests involving sensitive social topics (where cultural norms of directness vary most sharply), and highly technical domain-specific prompts (legal, medical, scientific) where register calibration differences may be most consequential.

---

## 7. Conclusion

This paper introduced an ILR-informed framework for evaluating cross-lingual response consistency in large language models and applied it to Claude Sonnet 4.6 across six languages. The central finding is that Claude's outputs vary in linguistically and pragmatically meaningful ways across languages even when semantic input is held constant — and that these variations are interpretable, systematic, and theoretically coherent with known cross-cultural pragmatic differences.

The five qualitative findings — pragmatic disambiguation strategies, aesthetic and literary divergence, technical terminology norms, cultural calibration through framing, and institutional anchoring in emotional support — collectively demonstrate that cross-lingual variation in LLM outputs is not random noise but structured behavior that reflects both the cultural embedding of language and the differential representation of language communities in model training and feedback processes.

The methodological contribution of this paper extends beyond its specific findings. By demonstrating that ILR-informed expert judgment can identify meaningful variation that automated metrics correctly detect but cannot interpret, we argue for a two-layer evaluation approach as a standard practice in multilingual LLM assessment. The interpretive gap between detecting variation and understanding its meaning is not a gap that can be closed by scaling computational resources — it requires human expertise, cultural knowledge, and professional assessment training. Making that expertise visible and methodologically explicit, as this paper attempts to do, is a step toward more rigorous and equitable evaluation of AI systems deployed across language communities.

The prompt battery, data, and analysis code for this study are publicly available at [github.com/camelbal-ship-it/crosslingual-claude-eval](https://github.com/camelbal-ship-it/crosslingual-claude-eval) to support replication, extension, and cross-model comparison.

---

## References

Ahuja, K., Diddee, H., Hada, R., Ochieng, M., Ramesh, K., Jain, A., ... & Sitaram, S. (2023). MEGA: Multilingual Evaluation of Generative AI. *Proceedings of EMNLP 2023*.

Bang, Y., Cahyawijaya, S., Lee, N., Dai, W., Su, D., Wilie, B., ... & Fung, P. (2023). A Multitask, Multilingual, Multimodal Evaluation of ChatGPT on Reasoning, Hallucination, and Interactivity. *arXiv:2302.04023*.

Cao, Y., Zhou, L., Lee, S., Cabello, L., Chen, M., & Hershcovich, D. (2023). Assessing Cross-Cultural Alignment between ChatGPT and Human Societies: An Empirical Study. *Proceedings of the C3NLP Workshop at EACL 2023*.

Conneau, A., Khandelwal, K., Goyal, N., Chaudhary, V., Wenzek, G., Guzmán, F., ... & Stoyanov, V. (2020). Unsupervised Cross-lingual Representation Learning at Scale. *Proceedings of ACL 2020*.

Hershcovich, D., Frank, S., Lent, H., de Lhoneux, M., Abdou, M., Brandl, S., ... & Søgaard, A. (2022). Challenges and Strategies in Cross-Cultural NLP. *Proceedings of ACL 2022*.

Interagency Language Roundtable. (2012). *ILR Skill Level Descriptions for Listening, Speaking, Reading, Writing, and Translation*. https://www.govtilr.org

Lai, V. D., Ngo, N. T., Veyseh, A. P. B., Man, H., Dernoncourt, F., Bui, T., & Nguyen, T. H. (2023). ChatGPT Beyond English: Towards a Comprehensive Evaluation of Large Language Models in Multilingual Learning. *arXiv:2304.05613*.

Malik, A., Mayhew, S., Piech, C., & Bicknell, K. (2024). From Tarzan to Tolkien: Controlling the Language Proficiency Level of LLMs for Content Generation. *Findings of the Association for Computational Linguistics: ACL 2024*, pages 15670–15693. https://aclanthology.org/2024.findings-acl.926/

White, J. S., O'Connell, T. A., & O'Mara, F. E. (1994). The ARPA MT Evaluation Methodologies: Evolution, Lessons, and Future Approaches. *Proceedings of the First Conference of the Association for Machine Translation in the Americas*, Columbia, Maryland. https://aclanthology.org/1994.amta-1.25/

**Note on references:** Bang et al. (2023), Ahuja et al. (2023), Lai et al. (2023), Conneau et al. (2020), and Hershcovich et al. (2022) are verified published works. Cao et al. (2023) should be verified against current databases before final submission. The ILR reference is verified at govtilr.org. CEFR/ACTFL mapping work on LLM evaluation should be searched in ACL Anthology and arXiv for 2023–2026 citations to add to Section 2.3.
