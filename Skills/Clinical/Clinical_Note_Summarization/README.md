# Clinical Note Summarization

**ID:** `biomedical.clinical.note_summarization`
**Version:** 1.0.0
**Status:** Production
**Category:** Clinical AI / Documentation

---

## Overview

The **Clinical Note Summarization Skill** transforms unstructured clinical text (dictations, progress notes, discharge summaries) into structured **SOAP (Subjective, Objective, Assessment, Plan)** format. It standardizes documentation for EHR systems and clinical workflows.

This skill addresses a critical bottleneck in healthcare: physicians spend 2+ hours daily on documentation. By automating structuring tasks, clinicians can focus on patient care.

---

## Key Capabilities

### 1. SOAP Format Structuring

Converts free-text clinical notes into standardized sections:

| Section | Content | Example |
|---------|---------|---------|
| **Subjective** | Patient's reported symptoms, history, concerns | "Patient reports 3 days of worsening chest pain" |
| **Objective** | Measurable findings (vitals, exam, labs) | "BP 145/92, HR 88, lungs CTA bilaterally" |
| **Assessment** | Clinical interpretation and diagnoses | "Hypertensive urgency, r/o ACS" |
| **Plan** | Treatment decisions and follow-up | "Start amlodipine 5mg, ECG, troponins x2" |

### 2. Medical Entity Extraction

- **Conditions:** ICD-10 mappable diagnoses
- **Medications:** Drug names, doses, frequencies
- **Procedures:** CPT-relevant interventions
- **Vitals:** Structured numeric values

### 3. Multi-Format Support

- Dictation transcripts
- Handwritten note OCR output
- Free-text progress notes
- Discharge summary narratives

---

## Usage

### Prompt Template

The `prompt.md` file contains the system prompt for SOAP structuring:

```markdown
You are a clinical documentation specialist...
[See prompt.md for full template]
```

### Integration Examples

#### LangChain

```python
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI

with open("prompt.md") as f:
    system_prompt = f.read()

template = PromptTemplate.from_template(
    system_prompt + "\n\nClinical Note:\n{note}\n\nStructured SOAP:"
)

chain = template | ChatOpenAI(model="gpt-4")
result = chain.invoke({"note": clinical_note_text})
```

#### Direct API (OpenAI)

```python
import openai

with open("prompt.md") as f:
    system_prompt = f.read()

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Structure this note:\n{note}"}
    ]
)
```

#### Anthropic Claude

```python
import anthropic

client = anthropic.Anthropic()

with open("prompt.md") as f:
    system_prompt = f.read()

message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1024,
    system=system_prompt,
    messages=[
        {"role": "user", "content": f"Structure this note:\n{note}"}
    ]
)
```

---

## Example

### Input (Unstructured Dictation)

```
45-year-old male here for hypertension follow-up. He says his blood pressure
has been running high at home, around 150s over 90s. He's been compliant with
his lisinopril 10mg daily. No chest pain, shortness of breath, or headaches.
Exam today shows BP 148/94, pulse 76, weight stable at 210 pounds. Heart
regular rate and rhythm, no murmurs. Plan to increase lisinopril to 20mg daily,
recheck in 4 weeks, continue low sodium diet.
```

### Output (Structured SOAP)

```
## Subjective
- Chief Complaint: Hypertension follow-up
- HPI: 45-year-old male with elevated home BP readings (150s/90s)
- Medications: Lisinopril 10mg daily (compliant)
- Review of Systems: Denies chest pain, SOB, headaches

## Objective
- Vitals: BP 148/94, HR 76, Weight 210 lbs
- Cardiovascular: RRR, no murmurs

## Assessment
1. Essential hypertension (I10) - suboptimally controlled

## Plan
1. Increase lisinopril to 20mg daily
2. Continue low sodium diet
3. Follow-up in 4 weeks for BP recheck
```

---

## Compliance Considerations

### HIPAA

- This skill processes PHI and must be deployed in HIPAA-compliant environments
- Use BAA-covered LLM providers (Azure OpenAI, Google Cloud Healthcare API)
- Never log or store raw clinical notes in non-compliant systems

### Clinical Validation

- Output should be reviewed by licensed clinicians before EHR entry
- This tool assists documentation; it does not replace clinical judgment
- Validate against institutional documentation standards

---

## Files

| File | Description |
|------|-------------|
| `prompt.md` | System prompt template for SOAP structuring |
| `usage.py` | Python integration examples |

---

## Supported Models

| Provider | Model | Performance |
|----------|-------|-------------|
| OpenAI | gpt-4, gpt-4-turbo | Excellent |
| Anthropic | claude-3-opus, claude-3-sonnet | Excellent |
| Google | gemini-1.5-pro | Good |
| Open Source | Llama 3 70B, Mixtral 8x22B | Good (fine-tuning recommended) |

---

## Related Skills

- **Trial Eligibility Screening:** Extract criteria from structured notes
- **Medical Coding:** ICD-10/CPT assignment from structured documentation
- **Diagnostic Decision Support:** Differential diagnosis from assessment section

---

## Author

**MD BABU MIA**
*Artificial Intelligence Group*
*Icahn School of Medicine at Mount Sinai*
md.babu.mia@mssm.edu
