# Clinical Trial Eligibility Agent

**ID:** `biomedical.clinical.trial_eligibility`
**Version:** 1.0.0
**Status:** Production
**Category:** Clinical AI / Trial Matching

---

## Overview

The **Clinical Trial Eligibility Agent** streamlines clinical trial recruitment by automatically matching patients to suitable trials. It analyzes patient medical records against structured inclusion/exclusion criteria, reducing the manual screening workload that currently bottlenecks enrollment.

Clinical trials fail primarily due to recruitment challenges: 80% of trials don't meet enrollment timelines, and 30% fail to enroll a single patient. This skill addresses that gap by enabling scalable, automated eligibility screening.

---

## Key Capabilities

### 1. Criteria Extraction

- Parses clinical trial protocols from ClinicalTrials.gov
- Structures complex inclusion/exclusion criteria into machine-readable format
- Handles compound criteria (AND/OR logic)
- Extracts numeric thresholds (age, lab values, tumor stage)

### 2. Patient Matching

Analyzes multiple data sources:

| Source | Data Type | Matching Approach |
|--------|-----------|-------------------|
| **EHR Data** | FHIR resources (Conditions, Observations, MedicationRequests) | Structured queries |
| **Clinical Notes** | Unstructured text | NLP extraction |
| **Lab Results** | Numeric values with units | Threshold comparison |
| **Imaging Reports** | Radiology findings | Entity extraction |

### 3. Eligibility Reporting

Generates detailed reports explaining:
- Which criteria are **MET**
- Which criteria are **NOT MET** (with explanation)
- Which criteria have **INSUFFICIENT DATA** (prompts for additional information)

### 4. Privacy-Preserving Processing

- Processes de-identified patient data (HIPAA Safe Harbor or Expert Determination)
- Supports federated queries without data centralization
- Audit trail for all matching decisions

---

## Usage

### Example Prompt

```text
I have a patient with the following characteristics:
- 58-year-old female
- Stage IIIA NSCLC (non-small cell lung cancer)
- EGFR mutation positive (exon 19 deletion)
- Prior treatment: carboplatin/pemetrexed (4 cycles), then osimertinib (progressed after 14 months)
- ECOG performance status: 1
- No brain metastases
- Creatinine clearance: 72 mL/min

Check eligibility for trial NCT04487080 (EGFR-targeted therapy).
List specific criteria met and any exclusion criteria that might be a concern.
```

### Expected Output

```
## Eligibility Assessment: NCT04487080

### INCLUSION CRITERIA

| Criterion | Status | Evidence |
|-----------|--------|----------|
| Age ≥18 years | MET | Patient is 58 years old |
| Histologically confirmed NSCLC | MET | Stage IIIA NSCLC documented |
| EGFR mutation positive | MET | Exon 19 deletion confirmed |
| Prior EGFR TKI treatment | MET | Prior osimertinib with progression |
| ECOG PS 0-1 | MET | ECOG 1 documented |
| Adequate renal function (CrCl ≥50) | MET | CrCl 72 mL/min |

### EXCLUSION CRITERIA

| Criterion | Status | Evidence |
|-----------|--------|----------|
| Active brain metastases | NOT APPLICABLE | No brain metastases |
| Prior treatment with [study drug] | NEEDS REVIEW | Verify specific agent history |

### RECOMMENDATION
**LIKELY ELIGIBLE** - Patient meets all major criteria. Recommend confirming
no prior exposure to study agent and obtaining recent imaging.
```

### LLM Agent Integration

```python
@tool
def check_trial_eligibility(
    patient_summary: str,
    trial_id: str,
    data_sources: list[str] = ["clinical_notes"]
) -> str:
    """
    Screens a patient for clinical trial eligibility.

    Args:
        patient_summary: Text summary of patient characteristics
        trial_id: ClinicalTrials.gov NCT number
        data_sources: Available data types for matching

    Returns:
        Structured eligibility report with criteria assessment
    """
    # Implementation fetches trial criteria and performs matching
    pass
```

---

## Prerequisites

### Required Data Access

| Resource | Purpose | Format |
|----------|---------|--------|
| **ClinicalTrials.gov API** | Trial criteria extraction | REST API |
| **Patient Records** | Matching data | FHIR R4 or free text |
| **Terminology Services** | Code normalization | SNOMED-CT, ICD-10, RxNorm |

### Dependencies

```
requests>=2.28
fhir.resources>=6.0
pandas>=1.5
```

---

## Methodology

### Criteria Parsing

1. **Fetch trial record** from ClinicalTrials.gov API
2. **Parse eligibility text** into structured criteria
3. **Normalize medical concepts** to standard terminologies
4. **Build logical query** representing I/E requirements

### Patient Matching

1. **Extract patient features** from available data sources
2. **Map to trial criteria** using semantic matching
3. **Evaluate each criterion** (MET / NOT MET / UNKNOWN)
4. **Generate explanation** with supporting evidence

### Confidence Scoring

- **HIGH:** Structured data directly confirms criterion
- **MEDIUM:** NLP extraction from notes
- **LOW:** Inferred from related data

---

## Integration Patterns

### FHIR-Based Matching

```python
from fhir.resources.patient import Patient
from fhir.resources.condition import Condition

def extract_patient_features(fhir_bundle: dict) -> dict:
    """Extract matching features from FHIR resources."""
    features = {}

    for entry in fhir_bundle.get("entry", []):
        resource = entry.get("resource", {})
        resource_type = resource.get("resourceType")

        if resource_type == "Patient":
            patient = Patient.parse_obj(resource)
            features["age"] = calculate_age(patient.birthDate)

        elif resource_type == "Condition":
            condition = Condition.parse_obj(resource)
            features.setdefault("conditions", []).append(
                condition.code.coding[0].display
            )

    return features
```

### ClinicalTrials.gov API

```python
import requests

def fetch_trial_criteria(nct_id: str) -> dict:
    """Fetch and parse trial eligibility criteria."""
    url = f"https://clinicaltrials.gov/api/v2/studies/{nct_id}"
    response = requests.get(url)
    study = response.json()

    return {
        "inclusion": study["protocolSection"]["eligibilityModule"]["eligibilityCriteria"],
        "gender": study["protocolSection"]["eligibilityModule"]["sex"],
        "min_age": study["protocolSection"]["eligibilityModule"]["minimumAge"],
        "max_age": study["protocolSection"]["eligibilityModule"]["maximumAge"]
    }
```

---

## Related Skills

- **Clinical Note Summarization:** Structure notes before eligibility screening
- **Diagnostic Decision Support:** Verify diagnosis accuracy
- **Medical Coding:** Standardize condition codes for matching

---

## References

- Based on **TrialGPT** (NIH) and **LLM Pharma** frameworks
- [bab-git/llm_pharma](https://github.com/bab-git/llm_pharma)
- Jin et al. "TrialGPT: Matching Patients to Clinical Trials with Large Language Models" (2023)

---

## Author

**MD BABU MIA**
*Artificial Intelligence Group*
*Icahn School of Medicine at Mount Sinai*
md.babu.mia@mssm.edu
