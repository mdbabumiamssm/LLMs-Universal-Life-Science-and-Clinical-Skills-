<!--
# COPYRIGHT NOTICE
# This file is part of the "Universal AI Agentic Skills" project.
# Copyright (c) 2026 MD BABU MIA, PhD <md.babu.mia@mssm.edu>
# All Rights Reserved.
#
# This code is proprietary and confidential.
# Unauthorized copying of this file, via any medium is strictly prohibited.
#
# Provenance: Authenticated by MD BABU MIA
-->



<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->

---
name: 'clinical-llm-evaluation-benchmarking'
description: 'Design and run clinical LLM evaluation benchmarks grounded in systematic review evidence on AI-generated clinical note evaluation methods.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# Clinical LLM Evaluation Benchmarking

## Overview

Use this skill to design, run, and interpret evaluations for clinical LLM outputs, especially AI-generated clinical notes and related clinical text. It turns a broad evaluation request into a structured benchmark plan with explicit metrics, safety labels, clinician adjudication, provenance controls, and deployment regression gates.

The workflow is grounded in the finding that evaluation methods for AI-generated clinical notes need systematic selection and benchmarking rather than relying on a single similarity, preference, or fluency score.

## When to Use This Skill

- Evaluating AI-generated clinical notes, summaries, handoffs, discharge instructions, referrals, or chart messages.
- Comparing clinical LLM outputs across prompts, model versions, vendors, retrieval settings, or fine-tunes.
- Designing benchmarks for clinical Q&A, guideline support, imaging-report text, patient education, or documentation assistance.
- Creating clinician review rubrics for omissions, hallucinations, contradictions, inappropriate certainty, bias, or unsafe recommendations.
- Establishing regression gates before deploying a clinical LLM workflow into pilot or production use.
- Auditing dataset provenance, de-identification, consent, license constraints, and train-test leakage risk.

## Core Capabilities

1. **Evaluation scope definition**  
   Identify the clinical task, intended users, care setting, input source, output format, decision impact, and unacceptable failure modes before choosing metrics.

2. **Dataset provenance and split design**  
   Document source systems, inclusion criteria, time ranges, de-identification process, annotation history, license or use restrictions, and leakage controls. Prefer held-out temporal or site-level splits when assessing deployment readiness.

3. **Metric selection matrix**  
   Match metrics to the output type: factual consistency, information completeness, omission severity, contradiction detection, clinical usefulness, readability, guideline concordance, calibration, citation support, and patient-safety risk.

4. **Safety and harm labeling**  
   Label outputs for hallucinated facts, missing critical findings, wrong medications or doses, contraindicated advice, delayed-care risk, inappropriate reassurance, privacy exposure, and misleading uncertainty.

5. **Omission and commission scoring**  
   Separate missing necessary information from added incorrect information. Score omissions by clinical severity, recoverability, and whether the missing item changes triage, diagnosis, treatment, follow-up, or patient behavior.

6. **Clinician adjudication workflow**  
   Use at least two qualified reviewers for high-impact tasks when feasible. Define reviewer specialty, blinding, disagreement resolution, escalation criteria, and inter-rater agreement reporting without treating agreement as proof of clinical safety.

7. **Automated evaluator use with controls**  
   Use automated metrics or LLM-as-judge methods only as screening or regression aids unless validated against clinician adjudication for the specific task. Calibrate prompts, anchors, and score thresholds against labeled examples.

8. **Error taxonomy and root-cause analysis**  
   Categorize errors by source: input ambiguity, retrieval failure, prompt instruction conflict, model medical reasoning failure, formatting failure, unsupported extrapolation, or evaluation artifact.

9. **Regression gates for deployment**  
   Define minimum pass criteria before clinical release, including no critical safety failures in the reviewed sample, bounded severe-error rate, stable performance across key subgroups, and documented rollback criteria.

10. **Reporting and interpretation**  
   Produce a benchmark report that distinguishes statistical performance, clinical acceptability, residual risk, subgroup behavior, and operational readiness. Avoid claiming safety or superiority from narrow or nonclinical metrics alone.

11. **On-prem open-source diagnosis deployment evaluation**  
   Evaluate distilled DeepSeek-R1 or other open-source reasoning models for diagnosis workflows by matching diagnostic task benchmarks to the intended clinical setting, then checking local hosting constraints, data governance, model provenance, diagnosis-specific failure-mode logging, human oversight requirements, and comparison against closed frontier models before clinical use.

12. **Fine-grained domain-specific medical Q&A dataset evaluation**  
   For domain-specific clinical Q&A benchmarks, define domain, specialty, topic, and subtopic tags plus an item-level error taxonomy, evaluate items individually by annotating omission categories, ambiguity, correctness, answer grounding, hallucination or commission, risk-of-harm labels, trustworthiness labels, and confidence calibration rather than relying only on aggregate accuracy, use stratified reporting by specialty, topic, subtopic, and harm label, run dataset quality and benchmark provenance checks on source, scope, construction, answer keys, annotation or review process, limitations, and intended use, report inter-rater reliability plus calibration and prompt sensitivity checks, maintain reporting templates that expose item ID, source provenance, domain stratum, error labels, omission labels, harm labels, trustworthiness labels, reviewer disposition, and model or prompt version, monitor benchmark drift over time, and use trustworthy medical model benchmarking rubrics that make item-level errors, omissions, and harm labels auditable.

13. **Domain-specific medical Q&A dataset trustworthiness audit**  
   For fine-grained medical Q&A dataset evaluation, audit question quality, answer validity, clinical risk, domain coverage, and train-test or source leakage checks at item level, then use trustworthy reporting templates that expose provenance, domain stratum, quality labels, validity labels, risk labels, leakage disposition, reviewer disposition, and model or prompt version.

14. **Systematic clinical-note evaluation method benchmarking**  
   For AI-generated clinical notes, design experimental benchmarks that compare evaluation methods rather than relying on one score: factual correctness, omissions, harm potential, note completeness, clinician preference, inter-rater reliability, benchmark dataset construction, and automated scoring compared with clinician scoring.

15. **Clinical-note quality method triangulation**  
   For AI-generated clinical notes, evaluate correctness, content omissions, risk of harm, and hallucination detection with clinician adjudication; report inter-rater reliability, and treat automated similarity metrics as limited proxies that require validation against clinician judgments.

16. **Ophthalmology CME-style response adjudication**  
   For ophthalmology continuing medical education-style questions, evaluate LLM responses for correctness, content omission, and risk of harm with clinician adjudication, explicitly reporting unsafe omissions rather than aggregate accuracy alone.

17. **Test-time knowledge acquisition evaluation**  
   For medical decision support systems that retrieve or acquire external clinical knowledge at inference time, use a controlled evaluation and mitigation pattern that measures whether acquired evidence improves correctness, omissions, and harm risk; log sources for acquired facts, evaluate retrieval timing, source trust, benchmark contamination risk, closed-book or no-retrieval baselines, and require evidence-grounded answer grading with safeguards that prevent over-trusting newly retrieved context without clinician-adjudicated support.

18. **Clinical-note benchmark selection and reviewer calibration**  
   When evaluating AI-generated clinical notes, choose benchmark methods that explicitly test factual correctness, clinically important omissions, and potential harm rather than fluency alone; calibrate automated or human review against clinician-adjudicated examples before using scores for deployment decisions.

19. **Distilled reasoning model deployment risk gates**  
   For on-premises DeepSeek-R1 derivatives or similar distilled open-source reasoning models, require diagnostic benchmark design, calibration against closed model baselines, privacy and governance review, latency and hardware tradeoff analysis, diagnosis-specific failure-mode review, and validation gates before clinical use.

20. **On-prem clinical LLM deployment checklist**  
   For open-source and distilled reasoning models such as DeepSeek-R1 derivatives, benchmark against diagnosis tasks, validate domain drift and calibration, document privacy and security tradeoffs, and require local governance approval before production use.

21. **Open-source distilled reasoning model safety gates**  
   For on-prem clinical diagnosis workflows using DeepSeek-R1 derivatives or similar open-source distilled reasoning models, evaluate deployment constraints, calibration, privacy controls, hardware limits, refusal or abstention behavior, and clinical safety gates beyond raw benchmark accuracy before operational use.

22. **On-prem diagnostic reasoning oversight gates**  
   For open-source or distilled reasoning models used in local clinical diagnosis, evaluate diagnostic benchmark fit, deployment constraints, local privacy and security tradeoffs, calibration and abstention behavior, and human-oversight gates that keep diagnostic suggestions under clinician review before operational use.

23. **Systematic-review-backed clinical-note quality dimensions**  
   For AI-generated clinical-note evaluations, explicitly assess correctness, omissions, harmfulness, factual consistency, completeness, and structure; document reviewer design, gold-standard creation, and experimental benchmark reporting when comparing evaluation methods.

24. **Comparative on-prem diagnosis performance validation**  
   For distilled DeepSeek-R1 and other open-source LLMs considered for on-premises medical diagnosis, evaluate comparative diagnostic performance against closed-model baselines on the same cases and rubrics, document local hosting and privacy constraints, and require clinician oversight plus governance approval before clinical use.

25. **Systematic-review-derived clinical-note evaluation templates**  
   For AI-generated clinical-note benchmarks, include method-specific templates for correctness, completeness, hallucination, harm-risk, and note-quality assessment, and report experimental benchmark setup, evaluation method comparisons, reviewer roles, score definitions, and limitations when comparing automated, clinician, or hybrid evaluation methods.

26. **Distilled DeepSeek-R1 on-prem diagnosis comparison**  
   For on-premises clinical diagnosis evaluation of distilled DeepSeek-R1 or other open-source models, compare diagnostic task performance under the intended local deployment constraints, document privacy and hardware limits, test calibration and abstention behavior, and complete clinician-reviewed failure-mode analysis before clinical use.

27. **Paired clinical-note quality evaluation benchmarks**  
   For AI-generated clinical notes, use paired experimental benchmark designs to compare evaluation methods across factuality, clinically important omissions, hallucination or unsupported additions, completeness, harmfulness, and rubric-based human review; document limitations of automated metrics and avoid treating them as standalone quality evidence without task-specific validation.

28. **On-prem DeepSeek-R1 distill deployment comparison**  
   For open-source DeepSeek-R1 distilled models considered for on-premises clinical diagnosis, compare diagnostic performance, latency, privacy posture, local hardware constraints, calibration, and failure modes against hosted frontier models on the same cases and rubrics before clinical use.

29. **Open-source reasoning distillation production review**  
   For open-source reasoning model distillations such as DeepSeek-R1 derivatives, evaluate diagnostic performance alongside local deployment constraints, privacy controls, latency, calibration, and clinician safety review before production use.

30. **Source-grounded on-prem open-source diagnostic benchmarking**  
   For distilled DeepSeek-R1 style open-source models considered for local clinical diagnosis, benchmark the exact local model, prompt, and serving configuration on diagnostic tasks before use; document deployment constraints, privacy tradeoffs, and required clinician oversight for any diagnostic suggestion.

31. **Systematic-review-derived clinical-note quality benchmarking**  
   For AI-generated clinical notes, structure benchmark protocols around correctness, clinically important omissions, harm risk, factual consistency, and usability; compare evaluation methods using inter-rater adjudication and documented disagreement resolution, and report the experimental benchmark design, reviewer roles, score definitions, and limitations.

32. **Test-time acquired-knowledge provenance and freshness checks**  
   When evaluating medical decision-making LLMs that acquire knowledge at test time, record retrieval provenance for acquired facts, check acquired-knowledge freshness using source publication or access dates when available, run ablations against no-retrieval baselines, and flag unsupported updates to diagnoses, treatments, medication details, guidelines, or local policies for safety review before they affect recommendations.

33. **Systematic-review-informed AI clinical-note quality dimensions**  
   For AI-generated clinical-note benchmarks, explicitly evaluate correctness, omissions, hallucinations or unsupported additions, formatting quality, risk of harm, inter-rater agreement, and benchmark dataset construction when selecting or comparing evaluation methods.

34. **Distilled DeepSeek-R1 on-prem diagnostic deployment evaluation**  
   For distilled DeepSeek-R1 style open-source models proposed for on-premises clinical diagnosis, compare diagnostic performance under the exact local inference configuration, document hardware, latency, and serving constraints, validate protected health information handling, test calibration and hallucination behavior, and require human-review gates before clinical use.

35. **Fine-grained medical Q&A error-mode reporting**  
   For domain-specific medical Q&A dataset evaluations, classify item-level omissions, unsafe reasoning, unsupported claims, ambiguity handling, source grounding, and per-domain error modes rather than reporting only aggregate accuracy.

36. **DeepSeek-R1-derived clinical workflow selection**  
   For on-premises diagnosis workflows using open-source or distilled reasoning models such as DeepSeek-R1 derivatives, select models only after comparative evaluation against closed models on the same diagnostic cases and rubrics, review local deployment constraints, calibration, data-governance controls, and clinician safety requirements, and document why the selected local model is appropriate for the intended clinical workflow.

37. **Trustworthy domain-specific Q&A adjudication templates**  
   For fine-grained domain-specific medical Q&A dataset evaluation, require item-level taxonomy fields for domain, specialty, topic, subtopic, ambiguity flags, omission labels, hallucination or unsupported-claim labels, answer grounding, and trustworthiness risk; use expert adjudication to resolve ambiguous, omitted, or hallucinated content; and report benchmarks with templates that expose item IDs, taxonomy strata, error labels, adjudicator disposition, and model or prompt version.

38. **AI-generated clinical-note quality benchmark design**  
   For AI-generated clinical-note quality evaluation, include rubric fields for correctness, clinically important omissions, hallucinations or unsupported additions, harm-risk severity, and note style or structure; use inter-rater adjudication with documented disagreement resolution, and design experimental benchmark comparisons that evaluate alternative methods on the same cases, reviewer roles, score definitions, and limitations.

39. **Test-time knowledge acquisition decision-change audit**  
   For medical decision-making evaluations where the model acquires knowledge at inference time, assess retrieval and source selection, verify citations against cited evidence, track answer changes before and after knowledge acquisition, and flag unsupported late-context shifts in diagnoses, treatments, medications, guidelines, or escalation advice for safety review.

40. **On-prem distilled diagnosis comparative reporting**  
   For comparative evaluations of distilled DeepSeek-R1 or other open-source diagnosis models, report performance using the same diagnostic cases, rubrics, model versions, prompts, and serving constraints intended for local use; treat local inference as requiring stronger governance, calibration, protected health information handling, and clinician-review checks when deployment constraints or model provenance uncertainty affect clinical use.

41. **Domain-specific medical Q&A dataset quality audits**  
   For fine-grained evaluation of domain-specific medical Q&A datasets, audit item source provenance, clinical scope, answer-key support, annotation process, ambiguity, and intended use; assign trustworthiness labels plus omission and harm scores at item level; and report model performance by clinical topic, subtopic, evidence type, and safety label rather than aggregate accuracy alone.

42. **Clinician-validated test-time knowledge acquisition pattern**  
   For medical decision-support evaluations where an LLM acquires knowledge at test time, treat acquisition as an evaluated intervention: record retrieval provenance for every acquired fact or cited source, compare pre-acquisition and post-acquisition answers on the same case, check whether acquired context introduces hallucinated, unsupported, or contradicted claims, and limit use of acquired knowledge as clinical guidance unless the source and answer change have clinician validation.

43. **On-prem distilled DeepSeek-R1 diagnostic deployment checklist**  
   For distilled DeepSeek-R1 style open models proposed for on-premises clinical diagnosis, evaluate diagnostic benchmark fit, local inference constraints, hallucination and clinical-safety failure modes, privacy controls for protected health information, and comparative performance against proprietary model baselines on the same cases and rubrics before clinical use.

44. **Fine-grained Q&A difficulty and prompt-stability checks**  
   For domain-specific medical Q&A dataset benchmarks, label item-level difficulty alongside specialty, topic, subtopic, omission category, and risk-of-harm score; stratify results by specialty and difficulty; rerun representative items across prompt variants to check answer stability; and document dataset scope, construction, answer-key support, annotation process, limitations, and intended use so trustworthy medical model benchmark results remain auditable.

45. **AI-generated clinical-note evaluation method benchmark design**  
   For AI-generated clinical-note quality evaluations, compare methods across factuality, omissions, harmfulness, style, completeness, clinician preference, and inter-rater reliability within a documented experimental benchmark design rather than relying on a single evaluation score.

46. **Test-time knowledge acquisition deployment comparison**  
   For medical decision support evaluations that acquire knowledge at inference time, separate retrieval-enabled benchmark runs from static zero-shot prompting runs, record retrieval timing and source-vetting criteria, keep benchmark items and retrieved knowledge sources separated where possible, document contamination controls for any acquired evidence, and compare decision changes against the same cases without test-time acquisition before deployment use.

47. **Hosted-frontier comparison for local diagnosis models**  
   For open-source distilled reasoning models considered for on-premises clinical diagnosis, including DeepSeek-R1 distillations, require local validation before clinical use that compares the exact local model, prompt, and serving configuration against hosted frontier models on the same diagnostic cases and rubrics, while documenting deployment constraints, calibration, refusal and harm patterns, security posture, and clinician-review gates.

48. **Fine-grained medical QA dataset audit before reliability claims**  
   Before using domain-specific medical QA benchmarks to claim model reliability, produce a dataset audit report that reviews item difficulty, ambiguity checks, answer-key quality, subdomain stratification, item-level error taxonomy, trustworthiness scoring, and benchmark limitations.

49. **Source-whitelisted test-time acquisition audit**  
   For clinical LLM decision evaluations that use test-time knowledge acquisition or retrieval, define an allowed source whitelist, verify citation provenance against retrieved evidence, check publication or access-date freshness, document conflict resolution when retrieved sources disagree, and compare pre-acquisition versus post-acquisition answer deltas before accepting changes to diagnoses, treatments, medications, guidelines, or escalation advice.

50. **Open-source diagnostic model performance-risk reporting**  
   For on-premises clinical diagnosis evaluations of open-source or distilled DeepSeek-R1 style models, report performance-risk tradeoffs under the intended local serving configuration, including local governance approval, privacy and protected health information constraints, model provenance, calibration and failure modes, and benchmark results against closed frontier models on the same cases and rubrics before deployment decisions.

51. **Fine-grained trustworthy medical Q&A assessment**  
   For domain-specific medical Q&A dataset evaluation, score each item with an explicit error taxonomy, omission tags, potential-harm tags, uncertainty or confidence calibration checks, answer-grounding review, and dataset provenance checks covering source, construction, answer-key support, annotation process, limitations, and intended use before using the benchmark to assess trustworthy medical language model behavior.

52. **On-prem open-source diagnosis readiness gates**  
   For open-source or distilled reasoning LLMs evaluated for on-premises clinical diagnosis, require benchmark design tied to the intended diagnostic cases and local serving constraints, document privacy and operational tradeoffs, run clinician safety review of diagnosis-specific failure modes, and enforce performance or regression gates before clinical use.

53. **ICU nursing Q&A blinded comparative evaluation**  
   For intensive care nursing Q&A evaluations, construct specialty-specific questions that reflect the intended ICU nursing scope; compare providers such as ChatGPT, DeepSeek, and Google Gemini on the same items with model identities blinded during review; score factual accuracy and clinical relevance; weight omissions, incorrect additions, and other errors by potential clinical consequence; require models to report uncertainty or abstain when appropriate; and use qualified ICU nurse experts to adjudicate ambiguous, unsafe, or potentially consequential answers before drawing comparative conclusions.

54. **Fine-grained domain Q&A reliability evaluation**
   For domain-specific medical Q&A datasets, apply an item-level error taxonomy; check question ambiguity, answerability, and alignment of reference answers and model responses with supporting evidence; report clinically relevant subgroup slices; define and document reliability thresholds before drawing trustworthiness conclusions; and publish dataset documentation covering scope, construction, provenance, annotation, limitations, and intended use.

55. **Ophthalmology response safety dimension reporting**  
   For ophthalmology continuing medical education-style responses, score correctness, clinically important omission, and risk of harm as separate clinician-adjudicated dimensions; use severity-weighted scoring, report confidence intervals, and include explicit examples of unsafe answers rather than relying on aggregate accuracy.

56. **Fine-grained clinically meaningful Q&A evaluation**  
   Evaluate domain-specific medical Q&A at item level using clinically meaningful error taxonomies, omission and potential-harm labels, subgroup analysis, evidence-grounding checks, confidence calibration, and expert adjudication rather than aggregate accuracy alone.

57. **Clinical-note quality rubric and preference separation**  
   For AI-generated clinical notes, design explicit rubric items and scoring anchors for correctness, clinically important omissions, and harmfulness; report inter-rater reliability for human judgments, and evaluate note quality separately from model-preference scoring so preference is not treated as evidence of clinical-note quality.

58. **On-premises distilled reasoning model go/no-go evaluation**  
   For distilled reasoning models proposed for on-premises clinical diagnosis, evaluate the exact model, quantization, hardware, and serving configuration for diagnostic accuracy, calibration, latency, privacy controls, and clinician-reviewed failure modes, then apply predeclared deployment go/no-go thresholds rather than inferring readiness from model family or aggregate performance alone.

59. **Fine-grained domain-specific Q&A dataset auditing**  
   Audit each domain-specific medical Q&A item for ambiguity, evidence sufficiency, clinically important omissions, potential harmfulness, subgroup-specific difficulty, and benchmark contamination, then report these dimensions transparently in trustworthy benchmark documentation rather than relying on aggregate performance alone.

60. **Clinical-note quality measure taxonomy and benchmark validity**  
   For AI-generated clinical-note benchmarks, separate factuality, completeness, structure, readability, harmfulness, and clinician preference into distinct quality dimensions; report automated metrics separately from blinded human review, compare methods on the same notes and reference conditions, and document whether each measure is valid for the intended quality dimension rather than treating agreement with another metric as general benchmark validity.

61. **Fine-grained medical Q&A dataset audit and stratification**  
   Audit medical Q&A items for ambiguity, answerability, evidence sufficiency, label quality, specialty coverage, and harmful errors, then stratify model performance by relevant question characteristics rather than relying only on aggregate results.

62. **Blinded specialist response safety adjudication**  
   For ophthalmology continuing medical education-style responses, score correctness, clinically important omission, and risk of harm as separate dimensions; use specialist adjudicators blinded to model identity, and report severity-weighted results rather than accuracy alone.

63. **Specialty-specific intensive-care nursing model benchmarking**  
   For comparative benchmarking on intensive-care nursing questions, capture the exact model and version for each ChatGPT, DeepSeek, or Google Gemini run; use qualified experts blinded to model identity for scoring; report error patterns across clinically relevant question subgroups; and score factual accuracy separately from clinically harmful omissions so aggregate correctness does not conceal missing safety-critical content.

64. **Fine-grained domain Q&A trustworthiness reporting**  
   For domain-specific medical Q&A evaluation, apply an item-level taxonomy with ambiguity and omission labels, resolve disputed labels through expert adjudication, evaluate confidence calibration, check for dataset leakage, and report item-level and stratified trustworthiness findings beyond aggregate accuracy.

65. **Model-family and version comparison for board-style medical questions**  
   Compare exact model families and versions on the same board-style medical question set, prompt, answer format, scoring rubric, and inference settings; document item provenance and release dates, use private or newly authored held-out items where feasible, flag suspected training exposure, and avoid claiming contamination is absent without evidence. Record evaluation dates, model identifiers, prompts, and settings for temporal reproducibility; report confidence intervals and question-level paired significance tests appropriate to the endpoint, and state explicitly that exam performance does not establish clinical competence, patient safety, or deployment readiness.

66. **Clinical-note quality framework reliability and validity**  
   For AI-generated clinical-note evaluation, score factuality, completeness, clinical usefulness, readability, hallucination, safety, and human-edit burden as distinct quality dimensions; document evaluator reliability and the validity of each benchmark method for its intended dimension when comparing human, automated, or hybrid evaluators.

67. **Severity-weighted ophthalmology response endpoints**  
   For ophthalmology continuing medical education-style responses, define correctness, clinically important omission, and risk of harm as explicit endpoints; apply severity-weighted adjudication, and report confidently wrong, incomplete, and unsafe answers as separate outcome categories rather than combining them into aggregate accuracy.

68. **On-premises distilled reasoning model adequacy benchmark**  
   For distilled reasoning models considered for on-premises clinical diagnosis, compare model sizes and quantization configurations on diagnostic tasks stratified by specialty, difficulty, and clinical consequence; measure diagnostic performance, calibration, latency, and hardware requirements under the exact local serving configuration; conduct clinician-reviewed failure analysis and verify privacy constraints; and predeclare explicit task-specific thresholds for performance, calibration, critical failures, latency, and privacy that identify when local deployment is not clinically adequate.

69. **Clinical-note quality taxonomy and benchmark protocol**  
   For AI-generated clinical notes, score factual correctness, clinically important omission, hallucination or unsupported content, clinical usefulness, structure, readability, temporal consistency, and potential harm as separate dimensions. Use a documented human-review protocol specifying reviewer qualifications, blinding, independent scoring, rubric anchors, disagreement adjudication, and inter-rater reliability; state each automated metric's intended dimension and limitations; do not let a composite score hide dimension-level failures or unreported weighting; and use experimental benchmark templates that keep the note set, reference context, reviewer instructions, and comparison conditions constant while reporting per-dimension results, human-versus-automated comparisons, reliability, and limitations.

## On-Prem Clinical LLM Deployment Risk Evaluation

When an evaluation includes open-source reasoning model distillations, including distilled DeepSeek-R1 derivatives, for on-premises diagnosis tasks, treat comparative findings such as the 2026 J Med Syst study as a prompt for pre-deployment evaluation rather than as evidence of local clinical readiness, and document risk controls for:

- Benchmark selection: choose diagnostic cases, rubrics, and comparison baselines that reflect the intended specialty, care setting, case mix, and clinical decision impact rather than relying on a generic medical score alone.
- Diagnostic accuracy: measure correctness on the intended diagnostic cases, report clinically consequential errors separately from aggregate performance, and avoid generalizing results beyond the evaluated case mix and configuration.
- Comparative performance reporting: report the exact open-source or distilled model, checkpoint, prompt, local serving configuration, comparator models, diagnostic task set, rubric, and deployment constraints used for each comparison.
- Hardware and latency tradeoffs: available CPU/GPU memory, latency, quantization or runtime choices, concurrency limits, local network boundaries, capacity constraints, and whether the deployment can meet clinical workflow needs.
- Hosted frontier comparison: compare diagnostic performance, latency, privacy posture, local hardware constraints, calibration, and failure modes for local DeepSeek-R1 distilled models against hosted frontier models on the same diagnosis cases and rubrics before clinical use.
- Model-selection guidance: choose a DeepSeek-R1-derived local workflow only when the exact model, checkpoint, prompt, and serving configuration satisfy the intended diagnostic rubric, calibration expectations, safety-review requirements, data-governance checks, and local deployment constraints; otherwise document the rationale for choosing a closed model, another open-source model, or no model deployment.
- Privacy and data-governance checks: local inference may reduce external data sharing, but protected health information (PHI) handling, access control, logging, retention, de-identification, and approval scope still need validation.
- Model provenance: record model source, distillation lineage when known, version or checkpoint, license constraints, local modifications, and serving configuration used for each benchmark run.
- Benchmark drift: repeat diagnosis benchmarks after model, prompt, retrieval, guideline, local population, or case-mix changes.
- Calibration: test confidence expression, abstention behavior, uncertainty communication, and threshold stability against clinician-adjudicated cases.
- Refusal behavior: test when the model refuses, abstains, over-answers, or gives unsupported diagnostic suggestions, and route unsafe or ambiguous outputs to clinician review.
- Failure-mode logging: track missed diagnoses, hallucinated or unsupported diagnoses, inappropriate certainty, delayed escalation, contraindicated advice, privacy leakage, model version, prompt version, and reviewer disposition when comparing DeepSeek-R1 distills or other local open-source models.
- Closed model calibration: benchmark and calibrate on-prem open-source distilled reasoning models against closed model baselines on the same diagnostic task set and rubrics before clinical use.
- Clinician safety review: require human-review gates and clinician review of diagnostic outputs, unsafe failure modes, privacy handling, latency impact, calibration behavior, and residual risk before pilot or production use.
- Validation gates: require documented validation scope, clinician review responsibility, audit logs, incident escalation, rollback criteria, and institutional approval before clinical use.
- Deployment go/no-go thresholds: predeclare acceptable diagnostic performance, calibration, latency, privacy, and critical-failure criteria for the intended workflow; do not proceed when any required threshold is unmet, and document the decision and required remediation.

## Inputs / Outputs

### Inputs

- Clinical task description and target setting.
- Representative input cases, source documents, prompts, model outputs, and expected use constraints.
- Reference standards when available, such as clinician-authored notes, guideline passages, structured chart facts, or adjudicated answer keys.
- Candidate metrics, reviewer rubrics, acceptable-risk thresholds, and deployment criteria.
- Dataset provenance details, de-identification status, license constraints, and protected health information handling plan.

### Outputs

- Benchmark protocol with task scope, dataset design, evaluation axes, reviewer workflow, and analysis plan.
- Metric matrix mapping each clinical risk to human, automated, or hybrid evaluation methods.
- Safety rubric covering omissions, hallucinations, contradictions, bias, privacy exposure, and patient-harm severity.
- Adjudication template for clinician reviewers, including score anchors and disagreement handling.
- Regression gate checklist for prompt, model, retrieval, and workflow changes before pilot or deployment.
- Final evaluation summary with limitations, residual risks, and recommended next actions.

## References

- PubMed: Dahlberg A, Käenniemi T, Winther-Jensen T, Tapiola O, Luisto R. "Measuring the quality of AI-generated clinical notes: A systematic review and experimental benchmark of evaluation methods." Artif Intell Med. 2026 Jul. https://pubmed.ncbi.nlm.nih.gov/41955894/
- PubMed: Zhong W, Fu Y, Peng D, Liu Y, Liu Y. "Open-Source Large Language Models Distilled DeepSeek-R1 Pose Challenges for On-Premises Clinical Deployment in Medical Diagnosis: A Comparative Study of Performance." J Med Syst. 2026 May 1. https://pubmed.ncbi.nlm.nih.gov/42062641/
- PubMed: Fonseca RDC, Rios RA, Castaldoni R, Carvalho AA, Lopes TJS. "Fine-grained evaluation of a domain-specific Q&A dataset to support trustworthy medical language models." Health Inf Sci Syst. 2026 Dec. https://pubmed.ncbi.nlm.nih.gov/42039929/
- PubMed: Chen JL, Lu AJ, Verma R, Wang L, Koch DD. "Assessment of Correctness, Content Omission, and Risk of Harm in Large Language Model Responses to Ophthalmology Continuing Medical Education Questions." Ophthalmol Sci. 2026 May. https://pubmed.ncbi.nlm.nih.gov/41908501/
- PubMed: Li S, Bao L, Li S, Wan B. "Enhancing LLM-based medical decision-making by test-time knowledge acquisition." Health Inf Sci Syst. 2026 Dec. https://pubmed.ncbi.nlm.nih.gov/41953846/
- PubMed: Gülhan Güner S, Tan Z, Gülpınar S. "Comparative performance of artificial intelligence models in intensive care nursing questions: an evaluation of ChatGPT, DeepSeek, and Google Gemini." BMC Nurs. 2026 May 2. https://pubmed.ncbi.nlm.nih.gov/42069581/
- PubMed: Shean RS, Mallapu JK, Shah T, Rasheed HA, Younessi DN. "Comparative Performance of Gemini 3 Pro and GPT-5 Family Models on Ophthalmology Board-Style Questions." Ophthalmol Sci. 2026 May. https://pubmed.ncbi.nlm.nih.gov/41970036/
