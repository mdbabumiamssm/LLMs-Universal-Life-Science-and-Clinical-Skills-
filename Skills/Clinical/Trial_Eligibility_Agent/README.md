# Clinical Trial Eligibility Agent

## Description
An intelligent agent designed to streamline the clinical trial recruitment process. It analyzes patient medical records against clinical trial inclusion/exclusion criteria to determine eligibility, reducing manual screening workload.

## Capabilities
- **Criteria Extraction**: Parses clinical trial protocols (from ClinicalTrials.gov) to extract structured inclusion and exclusion criteria.
- **Patient Matching**: Analyzes unstructured clinical notes and structured EHR data to match patients with suitable trials.
- **Eligibility Report**: Generates a detailed report explaining why a patient is eligible or ineligible for a specific trial.
- **Anonymization**: Ensures patient data is processed in a privacy-preserving manner (HIPAA compliant handling).

## Usage (Conceptual)

### Prerequisite
Access to de-identified patient records (FHIR format or text notes) and a trial registry database.

### Example Prompt
```text
I have a patient with Stage III NSCLC (Non-Small Cell Lung Cancer), EGFR mutation positive, prior progression on Osimertinib.
Check eligibility for the following trial: NCT01234567.
List specific inclusion criteria met and any exclusion criteria that might be a blocker.
```

## References
- Based on **LLM Pharma** ([bab-git/llm_pharma](https://github.com/bab-git/llm_pharma)).
- Related skills: Clinical Note Summarization.
