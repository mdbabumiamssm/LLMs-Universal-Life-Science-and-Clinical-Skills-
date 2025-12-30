# Presentation Slides
## Universal Biomedical Skills Platform
### Slide-by-Slide Content for All Videos

---

# MASTER SLIDE DECK

## Design Guidelines

**Color Scheme:**
- Primary: #1E3A5F (Deep Blue) - Headers, emphasis
- Secondary: #2E86AB (Teal) - Accents, icons
- Accent: #F18F01 (Orange) - Call to action, highlights
- Background: #FFFFFF (White) or #F5F5F5 (Light Gray)
- Text: #333333 (Dark Gray)

**Fonts:**
- Titles: Inter Bold or Helvetica Bold, 44-60pt
- Body: Inter Regular or Helvetica, 24-32pt
- Code: JetBrains Mono or Fira Code, 18-24pt

**Layout:**
- Left-aligned text preferred
- Maximum 6 bullet points per slide
- One key idea per slide
- Generous white space

---

# VIDEO 1 SLIDES: Introduction & Vision

---

## SLIDE 1.1 - Title Slide

```
[CENTERED]

UNIVERSAL BIOMEDICAL SKILLS

One Skill. Every LLM.

━━━━━━━━━━━━━━━━━━━━━━━━

[Your Name]
[Institution/Affiliation]
[Date]

github.com/mdbabumiamssm/Universal-Life-Science-and-Clinical-Skills-
```

---

## SLIDE 1.2 - The Hook

```
[LARGE TEXT, CENTERED]

"What if you could write a biomedical
AI skill once...

and have it work on Claude, ChatGPT,
Gemini, AND your local LLM?"

[ICON: Multiple platform logos connected]
```

---

## SLIDE 1.2a - The Importance of Skills

```
WHY SKILLS MATTER IN BIOMEDICINE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

In healthcare and life sciences, an AI "prompt" isn't enough.
We need **Robust Skills**.

[FOUR PILLARS OF IMPORTANCE]

1. REPRODUCIBILITY
   Scientific results must be consistent, regardless of the AI model used.

2. SAFETY & VALIDATION
   Prevent hallucinations in critical tasks (e.g., dosage, gene targets).

3. STANDARDIZATION
   A "Clinical Summary" should follow SOAP format every time.

4. ACCESSIBILITY
   Democratizing advanced bioinformatics for non-coders.

[QUOTE] "A skill is a validated, reliable unit of work."
```

---

## SLIDE 1.3 - The Problem

```
THE FRAGMENTATION PROBLEM
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[VISUAL: Scattered platform logos - Claude, ChatGPT, Gemini, Llama]

Current Reality:
• Each platform has different formats
• Skills must be rewritten for each
• Collaboration across platforms is difficult
• Vendor lock-in limits flexibility

[STAT BOX]
73% of practitioners have rewritten skills for different platforms
```

---

## SLIDE 1.4 - The Cost

```
THE REAL COST OF FRAGMENTATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[THREE ICONS WITH STATS]

     [Clock Icon]              [Chain Icon]           [Wall Icon]
   WASTED TIME              PLATFORM LOCK-IN       BROKEN COLLABORATION

   4-8 hours to            Once built, hard         Can't share skills
   rewrite each skill      to switch vendors        across institutions
```

---

## SLIDE 1.5 - The Solution

```
OUR SOLUTION: UNIVERSAL BIOMEDICAL SKILLS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[ARCHITECTURE DIAGRAM]

                    ┌─────────────┐
                    │    USDL     │
                    │ (One Skill) │
                    └──────┬──────┘
                           │
           ┌───────────────┼───────────────┐
           ▼               ▼               ▼
    ┌──────────┐    ┌──────────┐    ┌──────────┐
    │  Claude  │    │  OpenAI  │    │  Gemini  │
    │ Adapter  │    │ Adapter  │    │ Adapter  │
    └──────────┘    └──────────┘    └──────────┘
           │               │               │
           ▼               ▼               ▼
    [Claude Logo]   [GPT Logo]     [Gemini Logo]

Write Once. Deploy Everywhere.
```

---

## SLIDE 1.6 - Key Innovations

```
THREE KEY INNOVATIONS
━━━━━━━━━━━━━━━━━━━━━━

[1] USDL - Universal Skill Definition Language
    Standardized YAML schema for biomedical AI skills

[2] PLATFORM ADAPTERS
    Automatic conversion to Claude, OpenAI, Gemini, local

[3] BIOKERNEL RUNTIME
    Intelligent routing to optimal LLM per task

[BADGE: Open Source | MIT License]
```

---

## SLIDE 1.7 - Demo Preview

```
LIVE DEMO PREVIEW
━━━━━━━━━━━━━━━━━

[SCREENSHOT: Before/After QC Plots side by side]

Single-Cell RNA-seq Quality Control
• Real bone marrow data (GSE136112)
• 10,000+ cells analyzed
• MAD-based outlier detection
• Publication-ready visualizations

[ARROW] Same skill runs on Claude, GPT, Gemini
```

---

## SLIDE 1.8 - Skills Library Overview

```
SIX PRODUCTION-READY SKILLS
━━━━━━━━━━━━━━━━━━━━━━━━━━━

[THREE COLUMNS]

CLINICAL               GENOMICS              DRUG DISCOVERY
─────────             ────────              ──────────────
• Note                • scRNA-seq           • Chemical
  Summarization         QC                    Properties

• Trial               • CRISPR              • AgentD
  Eligibility           Design                Pipeline

[FOOTER: All skills validated across 3+ platforms]
```

---

## SLIDE 1.9 - Call to Action

```
GET STARTED TODAY
━━━━━━━━━━━━━━━━━

[GITHUB ICON]
github.com/mdbabumiamssm/Universal-Life-Science-and-Clinical-Skills-

[THREE STEPS]
1. Clone the repository
2. Run the demo with your data
3. Try skills on your preferred platform

[QR CODE: Repository URL]

Coming up: Repository Tour →
```

---

# VIDEO 2 SLIDES: GitHub Repository Tour

---

## SLIDE 2.1 - Title

```
GITHUB REPOSITORY TOUR
━━━━━━━━━━━━━━━━━━━━━━

Navigating the Universal Biomedical Skills Platform

[GITHUB ICON + FOLDER ICON]

Video 2 of 8
```

---

## SLIDE 2.2 - Repository Structure

```
REPOSITORY STRUCTURE
━━━━━━━━━━━━━━━━━━━━

Universal-Life-Science-and-Clinical-Skills-/
│
├── Skills/                    ← All biomedical skills
│   ├── Clinical/
│   ├── Genomics/
│   └── Drug_Discovery/
│
├── test_demonstration/        ← Working demo with data
│   ├── scRNAsedata/
│   └── qc_results/
│
├── platform_prototype/        ← SDK & tooling
│   ├── adapters/
│   ├── biokernel/
│   └── schema/
│
└── README.md                  ← Start here
```

---

## SLIDE 2.3 - Skills Folder Deep Dive

```
THE SKILLS FOLDER
━━━━━━━━━━━━━━━━━

Skills/
├── Clinical/
│   ├── clinical_note_summarization/
│   └── trial_eligibility_agent/
│
├── Genomics/
│   ├── single_cell_qc/          ← Featured demo
│   └── crispr_design_agent/
│
└── Drug_Discovery/
    ├── chemical_property_lookup/
    └── agentd_drug_discovery/

Each skill contains:
• README.md - Documentation
• prompt.md - AI instructions
• *.py - Implementation code
```

---

## SLIDE 2.4 - Test Demonstration

```
TEST DEMONSTRATION FOLDER
━━━━━━━━━━━━━━━━━━━━━━━━━

test_demonstration/
│
├── scRNAsedata/              ← Real bone marrow samples
│   ├── GSM3901485/
│   ├── GSM3901486/
│   └── GSM3901487/
│
├── qc_results/               ← Pre-generated outputs
│   ├── qc_metrics_before_filtering.png
│   ├── qc_metrics_after_filtering.png
│   └── test_input_filtered.h5ad
│
├── run_test.sh               ← Run the demo
└── requirements.txt          ← Dependencies

[NOTE: Everything you need to try it yourself]
```

---

## SLIDE 2.5 - Quick Start Commands

```
QUICK START
━━━━━━━━━━━

# 1. Clone the repository
git clone https://github.com/mdbabumiamssm/
    Universal-Life-Science-and-Clinical-Skills-.git

# 2. Navigate to the folder
cd Universal-Life-Science-and-Clinical-Skills-

# 3. Install dependencies
pip install -r test_demonstration/requirements.txt

# 4. Run the demo
cd test_demonstration
bash run_test.sh

[CHECKMARK] Ready in under 5 minutes
```

---

# VIDEO 3 SLIDES: Live Demo

---

## SLIDE 3.1 - Title

```
LIVE DEMO
━━━━━━━━━

Single-Cell RNA-seq Quality Control
with Real Bone Marrow Data

[DNA HELIX ICON + MICROSCOPE ICON]

Video 3 of 8
```

---

## SLIDE 3.2 - Dataset Introduction

```
THE DATASET
━━━━━━━━━━━

Source: GEO Dataset GSE136112
Tissue: Human Bone Marrow
Samples: 3 biological replicates

[TABLE]
Sample      | Cells  | Format
------------|--------|--------
GSM3901485  | ~8,400 | 10X Genomics
GSM3901486  | ~7,900 | 10X Genomics
GSM3901487  | ~9,100 | 10X Genomics

[NOTE: Real published data, not synthetic]
```

---

## SLIDE 3.3 - 10X Genomics Format

```
10X GENOMICS FILE FORMAT
━━━━━━━━━━━━━━━━━━━━━━━━

Each sample folder contains:

GSM3901485/
├── matrix.mtx      Sparse expression matrix
│                   (genes × cells × counts)
│
├── genes.tsv       Gene identifiers
│                   (Ensembl ID + Symbol)
│
└── barcodes.tsv    Cell barcodes
                    (unique cell IDs)

[ICON: Matrix visualization]
```

---

## SLIDE 3.4 - What is QC?

```
WHY QUALITY CONTROL?
━━━━━━━━━━━━━━━━━━━━

Not every "cell" is a healthy, intact cell:

[FOUR ICONS WITH LABELS]

[Empty Drop]          [Dying Cell]
Empty droplets       Damaged cells with
with few reads       high mitochondrial %

[Two Cells]          [Low Genes]
Doublets - two       Low-quality with
cells in one drop    few genes detected

[ARROW] QC identifies and removes these
```

---

## SLIDE 3.5 - QC Metrics

```
QC METRICS CALCULATED
━━━━━━━━━━━━━━━━━━━━━

[TABLE WITH ICONS]

Metric              | Meaning                | Threshold
--------------------|------------------------|-------------
total_counts        | Total UMIs per cell    | MAD-based
n_genes_by_counts   | Unique genes detected  | MAD-based
pct_counts_mt       | Mitochondrial %        | < 20%
pct_counts_ribo     | Ribosomal %            | Informational
pct_counts_hb       | Hemoglobin %           | < 1%

[NOTE: MAD = Median Absolute Deviation (robust outlier detection)]
```

---

## SLIDE 3.6 - Before Filtering (Placeholder for Screenshot)

```
BEFORE FILTERING
━━━━━━━━━━━━━━━━

[PLACEHOLDER: Insert qc_metrics_before_filtering.png]

Key Observations:
• Wide distribution of total counts
• Cells with >30% mitochondrial (dying cells)
• Low-gene-count outliers (empty droplets)
• Potential doublets (very high counts)
```

---

## SLIDE 3.7 - After Filtering (Placeholder for Screenshot)

```
AFTER FILTERING
━━━━━━━━━━━━━━━

[PLACEHOLDER: Insert qc_metrics_after_filtering.png]

Results:
• Tighter distributions
• Mitochondrial outliers removed
• Empty droplets excluded
• Clean dataset ready for analysis
```

---

## SLIDE 3.8 - Results Summary

```
QC RESULTS SUMMARY
━━━━━━━━━━━━━━━━━━

[RESULTS TABLE]

Metric              | Before    | After     | Change
--------------------|-----------|-----------|--------
Total Cells         | 25,407    | 22,925    | -9.8%
Median Genes/Cell   | 2,838     | 2,912     | +2.6%
Median Mito %       | 4.2%      | 3.8%      | -0.4%
Doublet Score       | Variable  | Low       | Cleaned

[CHECKMARK] Dataset ready for downstream analysis
• Clustering
• Trajectory inference
• Differential expression
```

---

## SLIDE 3.9 - Platform Portability

```
SAME SKILL, ANY PLATFORM
━━━━━━━━━━━━━━━━━━━━━━━━

[THREE LOGOS SIDE BY SIDE]

Claude              OpenAI              Gemini
──────              ──────              ──────
MCP Format          Function Calling    API Format

        ↑               ↑                  ↑
        └───────────────┼──────────────────┘
                        │
                   ┌────────────┐
                   │    USDL    │
                   │  (Source)  │
                   └────────────┘

The science doesn't change when you switch vendors.
```

---

# VIDEO 4 SLIDES: USDL & Adapters

---

## SLIDE 4.1 - Title

```
WRITE ONCE, DEPLOY EVERYWHERE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

The USDL Architecture

[CODE ICON + TRANSFORM ICON]

Video 4 of 8
```

---

## SLIDE 4.2 - The Rewriting Problem

```
THE REWRITING PROBLEM
━━━━━━━━━━━━━━━━━━━━━

Same skill, three different formats:

[THREE CODE BLOCKS SIDE BY SIDE]

CLAUDE                  OPENAI                 GEMINI
──────                  ──────                 ──────
<system>                {"role":               You are...
You are...              "system",
</system>               "content":             [markdown
<human>                 "You are..."}          format]
...
</human>                functions: [           generateContent
<assistant>             {name: ...}            ({...})
                        ]

[FRUSTRATED FACE] Different syntax. Same meaning. Wasted effort.
```

---

## SLIDE 4.3 - USDL Introduction

```
USDL: UNIVERSAL SKILL DEFINITION LANGUAGE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

A standardized YAML schema for biomedical AI skills

[USDL ICON]

Design Principles:
• Platform-neutral - No vendor-specific syntax
• Human-readable - Easy to write and review
• Machine-validatable - Schema-checked correctness
• Extensible - Add new platforms without changing core

[FILE ICON] single_cell_qc.yaml → Source of truth
```

---

## SLIDE 4.4 - USDL Structure

```
USDL STRUCTURE
━━━━━━━━━━━━━━

skill:
  id: single-cell-qc              ← Unique identifier
  name: "scRNA-seq QC"            ← Human name
  version: "1.0.0"                ← Semantic versioning
  domain: genomics                ← Classification

capabilities:                      ← What it can do
  - name: calculate_qc_metrics
    inputs: [...]
    outputs: [...]

prompts:                          ← AI instructions
  system: "You are an expert..."
  user_template: "Analyze {data}"

platforms:                        ← Platform hints
  claude: {prompt_style: xml_tags}
  openai: {function_calling: true}
```

---

## SLIDE 4.5 - Adapter Flow

```
THE ADAPTER SYSTEM
━━━━━━━━━━━━━━━━━━

[FLOW DIAGRAM]

┌──────────────────┐
│   USDL Source    │
│  (YAML file)     │
└────────┬─────────┘
         │
         │ parse & validate
         ▼
┌──────────────────┐
│  Adapter Engine  │
└────────┬─────────┘
         │
    ┌────┴────┬────────────┐
    ▼         ▼            ▼
┌───────┐ ┌───────┐ ┌───────────┐
│Claude │ │OpenAI │ │  Gemini   │
│Adapter│ │Adapter│ │  Adapter  │
└───┬───┘ └───┬───┘ └─────┬─────┘
    │         │           │
    ▼         ▼           ▼
 MCP pkg   Functions   API config
```

---

## SLIDE 4.6 - Claude Adapter Output

```
CLAUDE ADAPTER OUTPUT
━━━━━━━━━━━━━━━━━━━━━

Input: single_cell_qc.yaml

Output:
├── mcp_server/
│   ├── server.py
│   ├── tools.json
│   └── manifest.json
│
├── SKILL.md              ← Claude Code integration
│
└── api_schema.json       ← Tool use schema

[COMMAND]
python cli.py build --platform claude examples/single_cell_qc.yaml
```

---

## SLIDE 4.7 - OpenAI Adapter Output

```
OPENAI ADAPTER OUTPUT
━━━━━━━━━━━━━━━━━━━━━

Input: single_cell_qc.yaml

Output:
├── custom_gpt/
│   ├── instructions.md
│   └── actions.json
│
├── assistants_api.json   ← Assistants API config
│
└── functions.json        ← Function calling schema

[COMMAND]
python cli.py build --platform openai examples/single_cell_qc.yaml
```

---

## SLIDE 4.8 - Side-by-Side Comparison

```
SAME INPUT, SAME OUTPUT
━━━━━━━━━━━━━━━━━━━━━━━

[TWO COLUMNS]

CLAUDE OUTPUT              OPENAI OUTPUT
─────────────              ─────────────
<analysis>                 {
  Cells analyzed: 8,412      "cells_analyzed": 8412,
  Cells filtered: 847        "cells_filtered": 847,
  Filter rate: 10.1%         "filter_rate": 0.101,
  ...                        ...
</analysis>                }

[CHECKMARK] Different format. Identical analysis.
```

---

## SLIDE 4.9 - Validation

```
BUILT-IN VALIDATION
━━━━━━━━━━━━━━━━━━━

[TERMINAL OUTPUT]

$ python cli.py validate examples/single_cell_qc.yaml

✓ Schema validation passed
✓ Required fields present
✓ Capability definitions complete
✓ Platform configurations valid
✓ Test cases defined

Skill 'single-cell-qc' is valid and ready for deployment.

[SHIELD ICON] Catch errors before they reach production
```

---

# VIDEO 5 SLIDES: Platform Prototype SDK

---

## SLIDE 5.1 - Title

```
PLATFORM PROTOTYPE SDK
━━━━━━━━━━━━━━━━━━━━━━

Building & Deploying Biomedical Skills

[TOOLBOX ICON]

Video 5 of 8
```

---

## SLIDE 5.2 - SDK Components

```
SDK COMPONENTS
━━━━━━━━━━━━━━

platform_prototype/
│
├── cli.py              [TERMINAL] Command-line interface
│
├── adapters/           [TRANSFORM] Platform converters
│
├── biokernel/          [BRAIN] Intelligent runtime
│
├── schema/             [SCHEMA] USDL specification
│
├── optimizer/          [SPARKLE] AI prompt tuning
│
└── evaluator/          [CHECK] Cross-platform testing
```

---

## SLIDE 5.3 - CLI Commands

```
CLI COMMANDS
━━━━━━━━━━━━

[COMMAND LIST WITH ICONS]

validate    ✓  Check skill against USDL schema
build       →  Generate platform-specific artifacts
optimize    ★  AI-tune prompts for platforms
test        ◉  Run evaluation suite
serve       ▶  Start BioKernel runtime
compare     ≡  Cross-platform performance comparison

[EXAMPLE]
python cli.py build --platform claude examples/skill.yaml
```

---

## SLIDE 5.4 - BioKernel Architecture

```
BIOKERNEL: INTELLIGENT RUNTIME
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[ARCHITECTURE DIAGRAM]

                 ┌───────────────┐
                 │   Request     │
                 └───────┬───────┘
                         │
                         ▼
                 ┌───────────────┐
                 │  Task Router  │ ← Analyzes complexity
                 └───────┬───────┘
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
   ┌─────────┐     ┌──────────┐    ┌──────────┐
   │ Simple  │     │ Complex  │    │  Local   │
   │ (Flash) │     │ (Opus)   │    │ (Llama)  │
   └─────────┘     └──────────┘    └──────────┘

Fast & Cheap     Most Capable      Privacy First
```

---

## SLIDE 5.5 - Routing Logic

```
INTELLIGENT ROUTING
━━━━━━━━━━━━━━━━━━━

[ROUTING TABLE]

Task Type            | Routed To      | Why
---------------------|----------------|-------------------
Simple lookup        | Gemini Flash   | Fast, low cost
Complex reasoning    | Claude Opus    | Best reasoning
Code execution       | BioKernel      | Sandboxed runtime
Multi-step pipeline  | Claude Sonnet  | Good balance
Privacy-sensitive    | Local model    | No data leaves

[LIGHTBULB] Optimal performance without manual configuration
```

---

## SLIDE 5.6 - The Optimizer

```
AI-POWERED OPTIMIZATION
━━━━━━━━━━━━━━━━━━━━━━━

[OPTIMIZATION FLOW]

     USDL Prompt
          │
          ▼
┌─────────────────────┐
│  Meta-Prompter AI   │
│  (Optimization)     │
└─────────┬───────────┘
          │
    ┌─────┴─────┐
    ▼           ▼
┌───────┐   ┌───────┐
│Claude │   │OpenAI │   ← Platform-specific
│Version│   │Version│      best practices
└───────┘   └───────┘

[EXAMPLES]
Claude: Add XML tags, use prefilling
OpenAI: Concise system messages, JSON outputs
Gemini: Long-context optimization, grounding
```

---

## SLIDE 5.7 - The Evaluator

```
CROSS-PLATFORM EVALUATION
━━━━━━━━━━━━━━━━━━━━━━━━━

[RESULTS TABLE]

$ python cli.py test examples/skill.yaml --all-platforms

Platform     | Accuracy | Latency | Cost/1K
-------------|----------|---------|--------
Claude 3.5   | 98.2%    | 2.3s    | $0.018
GPT-4o       | 96.8%    | 3.1s    | $0.025
Gemini Pro   | 94.5%    | 1.8s    | $0.007

[CHART ICON] Make informed deployment decisions
```

---

## SLIDE 5.8 - Creating a New Skill

```
CREATE YOUR OWN SKILL
━━━━━━━━━━━━━━━━━━━━━

[5 STEPS]

1. COPY TEMPLATE
   cp examples/template.yaml my_skill.yaml

2. DEFINE METADATA
   id, name, version, domain

3. WRITE CAPABILITIES
   inputs, outputs, descriptions

4. CREATE PROMPTS
   system instructions, user templates

5. VALIDATE & BUILD
   python cli.py validate my_skill.yaml
   python cli.py build --platform claude my_skill.yaml

[ROCKET] Your skill is ready for deployment!
```

---

# VIDEO 6 SLIDES: Skills Overview

---

## SLIDE 6.1 - Title

```
COMPLETE SKILLS LIBRARY
━━━━━━━━━━━━━━━━━━━━━━━

Six Production-Ready Biomedical AI Skills

[GRID OF 6 ICONS]

Video 6 of 8
```

---

## SLIDE 6.2 - Skills Grid

```
THE SKILLS LIBRARY
━━━━━━━━━━━━━━━━━━

[3x2 GRID]

┌─────────────────┬─────────────────┐
│    CLINICAL     │    CLINICAL     │
│  Note Summary   │ Trial Matching  │
│   [Document]    │    [People]     │
├─────────────────┼─────────────────┤
│    GENOMICS     │    GENOMICS     │
│   scRNA-seq     │  CRISPR Design  │
│   [Cell Icon]   │   [Scissors]    │
├─────────────────┼─────────────────┤
│ DRUG DISCOVERY  │ DRUG DISCOVERY  │
│   Mol Props     │    AgentD       │
│  [Molecule]     │   [Pipeline]    │
└─────────────────┴─────────────────┘
```

---

## SLIDE 6.3 - Clinical Note Summarization

```
CLINICAL NOTE SUMMARIZATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━

[SKILL ICON: Document with checkmark]

Purpose: Convert unstructured notes → SOAP format

[BEFORE/AFTER COMPARISON]

BEFORE (Raw Note)           AFTER (SOAP)
─────────────────           ────────────
"58yo male c/o             SUBJECTIVE:
chest pain x3d,            • 58-year-old male
worse w/ exertion,         • Chest pain 3 days
denies SOB..."             • Worse with exertion

Use Cases:
• Automated medical scribing
• EHR standardization
• Quality audits
```

---

## SLIDE 6.4 - Trial Eligibility Agent

```
TRIAL ELIGIBILITY AGENT
━━━━━━━━━━━━━━━━━━━━━━━

[SKILL ICON: People matching]

Purpose: Match patients to clinical trials

[WORKFLOW]

Patient Data  →  Criteria   →  Eligibility
                 Matching      Report

┌──────────┐    ┌──────────┐    ┌──────────┐
│ Age: 54  │    │ Age 18-65│    │✓ ELIGIBLE│
│ T2D      │ →  │ Has T2D  │ →  │          │
│ HbA1c 8.2│    │ HbA1c 7-10    │ Meets all│
└──────────┘    └──────────┘    │ criteria │
                                └──────────┘

[BADGE: HIPAA-aware design]
```

---

## SLIDE 6.5 - scRNA-seq QC

```
SINGLE-CELL RNA-seq QC
━━━━━━━━━━━━━━━━━━━━━━

[SKILL ICON: Cell with checkmark]

Purpose: Quality control for single-cell data

[METRICS TABLE]

Metric          | Meaning              | Threshold
----------------|----------------------|------------
total_counts    | UMIs per cell        | MAD-based
n_genes         | Genes detected       | MAD-based
pct_mt          | Mitochondrial %      | < 20%

Removes:
• Empty droplets
• Dying cells
• Doublets

[OUTPUT: Clean dataset + QC visualizations]
```

---

## SLIDE 6.6 - CRISPR Design Agent

```
CRISPR DESIGN AGENT
━━━━━━━━━━━━━━━━━━━

[SKILL ICON: Scissors + DNA]

Purpose: Automate guide RNA design

[WORKFLOW]

Target Gene → PAM Sites → sgRNA Design → Off-target
   (BRCA1)    (Find NGG)   (20nt guides)   Analysis

[EXAMPLE OUTPUT]

Top Guide: GCAGTGAAGAGATGCCGCTT
├── Position: Exon 11
├── On-target score: 0.87
├── Off-targets: 0 in exons
└── Recommendation: EXCELLENT

Supports: SpCas9, SaCas9, Cas12a
```

---

## SLIDE 6.7 - Chemical Property Lookup

```
CHEMICAL PROPERTY LOOKUP
━━━━━━━━━━━━━━━━━━━━━━━━

[SKILL ICON: Molecule structure]

Purpose: Calculate molecular properties (RDKit)

[CAPABILITIES]

• Molecular weight
• LogP (lipophilicity)
• H-bond donors/acceptors
• Rotatable bonds
• TPSA
• Lipinski Rule of 5

[EXAMPLE: Aspirin]

MW: 180.16 g/mol
LogP: 1.19
Lipinski: PASSES ✓

[USE: Agent tool for chemistry queries]
```

---

## SLIDE 6.8 - AgentD Drug Discovery

```
AGENTD: DRUG DISCOVERY PIPELINE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[SKILL ICON: Multi-step pipeline]

Purpose: End-to-end drug discovery workflow

[PIPELINE STEPS]

1. Literature    2. Compound     3. Molecule
   Mining           Retrieval       Generation
   [PubMed]        [ChEMBL]        [AI Design]
      │               │                │
      └───────────────┼────────────────┘
                      ▼
   4. ADMET         5. Docking
   Prediction       Preparation
   [Properties]     [3D Structure]

[INTEGRATIONS: PubMed, ChEMBL, PubChem, RDKit]
```

---

## SLIDE 6.9 - Skills Summary

```
SKILLS SUMMARY
━━━━━━━━━━━━━━

[SUMMARY TABLE]

Skill               | Domain    | Status     | Platforms
--------------------|-----------|------------|------------
Note Summarization  | Clinical  | Production | All
Trial Eligibility   | Clinical  | Beta       | All
scRNA-seq QC        | Genomics  | Production | All
CRISPR Design       | Genomics  | Beta       | All
Chemical Props      | Drug Disc | Production | All
AgentD Pipeline     | Drug Disc | Beta       | All

[6 skills | 3 domains | 4+ platforms]

Library is growing. Contributions welcome!
```

---

# VIDEO 7 SLIDES: Research Paper

---

## SLIDE 7.1 - Title

```
THE SCIENCE BEHIND
UNIVERSAL BIOMEDICAL SKILLS
━━━━━━━━━━━━━━━━━━━━━━━━━━━

A Platform-Agnostic Framework for Deploying
AI Assistants Across Multiple LLMs

[ACADEMIC PAPER ICON]

Video 7 of 8
```

---

## SLIDE 7.2 - Research Motivation

```
RESEARCH MOTIVATION
━━━━━━━━━━━━━━━━━━━

[PROBLEM STATEMENT]

Current State:
• LLM adoption in biomedicine is accelerating
• Each platform requires different implementation
• Skills cannot be shared across institutions
• Significant duplicated effort

Research Questions:
1. Can we define skills in a platform-neutral format?
2. Can automatic conversion maintain performance?
3. What infrastructure enables practical deployment?
```

---

## SLIDE 7.3 - Methods Overview

```
METHODS OVERVIEW
━━━━━━━━━━━━━━━━

[THREE PILLARS]

        USDL                 ADAPTERS             BIOKERNEL
   ─────────────         ─────────────         ─────────────
   Standardized          Automatic             Intelligent
   schema for            conversion to         runtime with
   skill definition      each platform         optimal routing

   [YAML Icon]           [Transform Icon]      [Brain Icon]

Cross-Platform Validation:
• 6 skills tested on Claude, GPT-4o, Gemini
• Accuracy, latency, cost metrics collected
• Semantic equivalence evaluated
```

---

## SLIDE 7.4 - USDL Design

```
USDL DESIGN PRINCIPLES
━━━━━━━━━━━━━━━━━━━━━━

[FOUR PRINCIPLES]

1. EXPRESSIVENESS
   Capture full range of biomedical AI capabilities

2. PLATFORM NEUTRALITY
   No vendor-specific constructs in core schema

3. VALIDATION
   Machine-checkable correctness via JSON Schema

4. EXTENSIBILITY
   Support new platforms without schema changes

[SCHEMA ANALYSIS]
Analyzed 4 major platforms
Identified common abstractions
Unified in single representation
```

---

## SLIDE 7.5 - Validation Results

```
VALIDATION RESULTS
━━━━━━━━━━━━━━━━━━

[RESULTS TABLE]

                    Claude    GPT-4o    Gemini
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Note Summarization   96.2%    94.8%     93.1%
Trial Eligibility    91.5%    89.2%     87.8%
scRNA-seq QC         98.8%    97.4%     96.2%
CRISPR Design        94.3%    92.1%     90.5%
Chemical Properties  99.1%    98.7%     98.2%
AgentD Pipeline      88.4%    85.9%     82.3%
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[KEY FINDING]
Performance variance < 5% for 5 of 6 skills
```

---

## SLIDE 7.6 - Semantic Consistency

```
SEMANTIC CONSISTENCY
━━━━━━━━━━━━━━━━━━━━

[ANALYSIS]

Method:
• Embedding similarity analysis
• Human evaluation (n=3 reviewers)
• Cross-platform output comparison

Results:
• 94.2% of outputs rated semantically equivalent
• Differences primarily stylistic, not substantive
• Clinical accuracy maintained across all platforms

[CHART: Embedding similarity distribution]

Conclusion: Platform choice doesn't affect scientific validity
```

---

## SLIDE 7.7 - scRNA-seq Case Study

```
CASE STUDY: scRNA-seq QC
━━━━━━━━━━━━━━━━━━━━━━━━

[DETAILED RESULTS]

Dataset: GSE136112 (Bone Marrow)
Samples: 3 biological replicates

           | Sample 1 | Sample 2 | Sample 3
-----------|----------|----------|----------
Input      | 8,412    | 7,891    | 9,104
Filtered   | 847      | 723      | 912
Rate       | 10.1%    | 9.2%     | 10.0%
Med. Genes | 2,847    | 2,912    | 2,756
Med. Mito  | 4.2%     | 3.8%     | 4.5%

[VALIDATION]
Filter rates consistent with published analyses
Biological conclusions unchanged across platforms
```

---

## SLIDE 7.8 - Implications

```
IMPLICATIONS FOR THE FIELD
━━━━━━━━━━━━━━━━━━━━━━━━━━

[FOUR IMPLICATIONS]

1. REDUCED DEVELOPMENT BURDEN
   Write skills once, deploy everywhere

2. INCREASED REPRODUCIBILITY
   Consistent behavior enables better science

3. VENDOR INDEPENDENCE
   Switch providers without losing investments

4. COLLABORATIVE POTENTIAL
   Share skills across institutions

[QUOTE]
"Platform-agnostic development is both feasible and practical."
```

---

## SLIDE 7.9 - Limitations & Future Work

```
LIMITATIONS & FUTURE WORK
━━━━━━━━━━━━━━━━━━━━━━━━━

LIMITATIONS:
• Testing limited to 3 commercial platforms
• Long-term model versioning not studied
• Some advanced features may not map to USDL

FUTURE DIRECTIONS:

1. Expanded platform support
   → Azure OpenAI, Anthropic API, local models

2. Skill marketplace
   → Community repository with versioning

3. Automated optimization
   → AI-driven prompt tuning per platform

4. Regulatory pathway
   → FDA and compliance exploration
```

---

## SLIDE 7.10 - Conclusion

```
CONCLUSION
━━━━━━━━━━

KEY CONTRIBUTIONS:

[1] USDL
    First standardized schema for biomedical AI skills

[2] MULTI-PLATFORM ADAPTERS
    Automatic conversion with maintained accuracy

[3] VALIDATED LIBRARY
    6 production skills with cross-platform testing

[4] OPEN-SOURCE RELEASE
    Complete platform available for community use

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"The fragmentation problem is solvable.
 The science shouldn't depend on which vendor you choose."
```

---

# VIDEO 8 SLIDES: Contributing & Community

---

## SLIDE 8.1 - Title

```
JOIN THE COMMUNITY
━━━━━━━━━━━━━━━━━━

Contributing to Universal Biomedical Skills

[COMMUNITY ICON: Multiple people]

Video 8 of 8
```

---

## SLIDE 8.2 - Why Contribute

```
WHY CONTRIBUTE?
━━━━━━━━━━━━━━━

[THREE COLUMNS]

FOR RESEARCHERS          FOR DEVELOPERS         FOR INSTITUTIONS
─────────────────        ──────────────         ─────────────────
• Share your             • Work with            • Reduce redundant
  analysis workflows       cutting-edge LLM       development
                          integration
• Benefit from                                  • Establish open
  community fixes        • Build portfolio        science leadership
                          projects
• Build reputation                              • Influence
                        • Learn multi-           standards
                          platform skills

[HEART ICON] Every contribution moves the field forward
```

---

## SLIDE 8.3 - Contribution Workflow

```
CONTRIBUTION WORKFLOW
━━━━━━━━━━━━━━━━━━━━━

[6-STEP PROCESS]

1. FORK          → Create your copy on GitHub
        ↓
2. CLONE         → git clone [your-fork-url]
        ↓
3. BRANCH        → git checkout -b feature/my-skill
        ↓
4. DEVELOP       → Make your changes
        ↓
5. COMMIT        → git commit -m "Add: description"
        ↓
6. PULL REQUEST  → Open PR on GitHub

[TIMELINE ARROW SHOWING FLOW]
```

---

## SLIDE 8.4 - Adding a New Skill

```
ADDING A NEW SKILL
━━━━━━━━━━━━━━━━━━

[STEP-BY-STEP]

STEP 1: Copy Template
cp examples/template.yaml Skills/Domain/my_skill.yaml

STEP 2: Define Metadata
skill:
  id: my-skill-id
  name: "My Skill Name"
  domain: genomics

STEP 3: Write Capabilities
capabilities:
  - name: main_function
    inputs: [...]
    outputs: [...]

STEP 4: Create Prompts
prompts:
  system: "You are an expert in..."

STEP 5: Validate
python cli.py validate my_skill.yaml

[ROCKET] Ready to submit!
```

---

## SLIDE 8.5 - Other Contributions

```
OTHER WAYS TO CONTRIBUTE
━━━━━━━━━━━━━━━━━━━━━━━━

[GRID OF CONTRIBUTION TYPES]

┌────────────────┬────────────────┐
│ DOCUMENTATION  │   BUG REPORTS  │
│  [Book Icon]   │   [Bug Icon]   │
│ Improve READMEs│ Report issues  │
│ Add tutorials  │ with details   │
├────────────────┼────────────────┤
│     CODE       │    TESTING     │
│ [Code Icon]    │ [Test Icon]    │
│ New adapters   │ Validate skills│
│ BioKernel perf │ on platforms   │
├────────────────┼────────────────┤
│    IDEAS       │    OUTREACH    │
│ [Bulb Icon]    │ [Share Icon]   │
│ Feature reqs   │ Share project  │
│ Use cases      │ Write blogs    │
└────────────────┴────────────────┘
```

---

## SLIDE 8.6 - Community Resources

```
COMMUNITY RESOURCES
━━━━━━━━━━━━━━━━━━━

[LINKS WITH ICONS]

GitHub Discussions        → Questions & Ideas
github.com/.../discussions

GitHub Issues             → Bugs & Features
github.com/.../issues

Project Roadmap           → What's Coming
github.com/.../projects

Code of Conduct          → Community Guidelines
CONTRIBUTING.md

[QR CODE: Repository URL]
```

---

## SLIDE 8.7 - Call to Action

```
YOUR NEXT STEPS
━━━━━━━━━━━━━━━

[CHECKLIST WITH STARS]

★ STAR the repository
  Helps others discover the project

★ TRY the demo
  With your own data

★ SHARE with colleagues
  Who might benefit

★ CONTRIBUTE a skill
  From your domain

[GITHUB URL LARGE]
github.com/mdbabumiamssm/Universal-Life-Science-and-Clinical-Skills-
```

---

## SLIDE 8.8 - Thank You

```
THANK YOU
━━━━━━━━━

[CENTERED]

Universal Biomedical Skills Platform

Making biomedical AI accessible to everyone,
regardless of platform choice.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Your Name]
[Institution]
[Contact Info]

[GITHUB LOGO]  [LINKEDIN LOGO]  [EMAIL ICON]

See you on GitHub!
```

---

## SLIDE 8.9 - Series Recap

```
SERIES RECAP
━━━━━━━━━━━━

[8 VIDEO THUMBNAILS IN GRID]

1. Introduction & Vision
2. GitHub Repository Tour
3. Live Demo: scRNA-seq QC
4. USDL & Platform Adapters
5. Platform Prototype SDK
6. Complete Skills Library
7. Research Paper
8. Contributing & Community

[PLAYLIST LINK]
Watch all videos: [YouTube Playlist URL]

[SUBSCRIBE BUTTON]
```

---

# APPENDIX: VISUAL ASSETS NEEDED

## Icons to Create/Source
- Platform logos (Claude, OpenAI, Gemini, Llama)
- Domain icons (Clinical, Genomics, Drug Discovery)
- Skill icons (6 unique icons)
- Action icons (fork, clone, commit, etc.)
- Contribution type icons

## Diagrams to Create
- USDL architecture flow
- Adapter conversion diagram
- BioKernel routing flowchart
- Skill pipeline visualizations

## Screenshots to Capture
- GitHub repository main page
- Terminal running demos
- Claude/GPT interfaces
- QC result plots
- VS Code with YAML files

## Charts to Generate
- Cross-platform accuracy comparison
- Performance benchmarks
- Skills coverage by domain

---

**END OF PRESENTATION SLIDES**
