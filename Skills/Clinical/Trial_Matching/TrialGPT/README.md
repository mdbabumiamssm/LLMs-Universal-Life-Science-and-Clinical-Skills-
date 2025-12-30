# TrialGPT: Clinical Trial Matching

**Source:** [ncbi-nlp/TrialGPT](https://github.com/ncbi-nlp/TrialGPT)
**Local Repository:** `./repo`
**Status:** Integrated & Downloaded

## Overview
TrialGPT is an NIH-developed algorithm that uses Large Language Models to match patients with suitable clinical trials. It addresses the critical bottleneck of patient recruitment.

## Functionality
1.  **Criterion Extraction:** Parses unstructured eligibility criteria.
2.  **Patient Profiling:** Summarizes patient medical records.
3.  **Matching Engine:** Calculates a relevance score (0-100).
4.  **Explanation:** Provides justifications for matches.

## Quick Start
1.  **Installation:**
    ```bash
    cd repo
    pip install -r requirements.txt
    ```
2.  **Modules:**
    *   **Retrieval:** `repo/trialgpt_retrieval/` - Gets relevant trials.
    *   **Matching:** `repo/trialgpt_matching/` - detailed criteria check.
    *   **Ranking:** `repo/trialgpt_ranking/` - final ordering.
3.  **Running:**
    Refer to specific scripts in the subdirectories. Likely involves running a retrieval script followed by the matching script.

## Performance
- **Accuracy:** Rankings closely match expert clinician assessments.
- **Efficiency:** Reduces screening time significantly.