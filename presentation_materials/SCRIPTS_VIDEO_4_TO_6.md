# Video Scripts: Part 2 (Videos 4-6)
## Universal Biomedical Skills Platform Tutorial Series

---

# VIDEO 4: USDL & Platform Adapters
## "Write Once, Deploy Everywhere: The USDL Architecture"
### Duration: 10-12 minutes

---

### SCENE 1: OPENING (0:00 - 0:45)
**[VISUAL: Split screen - Claude on left, ChatGPT on right]**

**SCRIPT:**
> "In the last video, you saw our scRNA-seq QC skill running on Claude. But what if your lab uses ChatGPT? What if your collaborators prefer Gemini?

> Do you rewrite everything from scratch?

> No. You use USDL - the Universal Skill Definition Language.

> In this video, I'll show you how one skill definition becomes multiple platform-specific implementations - automatically."

---

### SCENE 2: THE REWRITING PROBLEM (0:45 - 2:15)
**[VISUAL: Side-by-side code comparison]**

**SCRIPT:**
> "Let me show you the problem we're solving.

**[VISUAL: Show Claude-style prompt]**

> "Here's how you might define a skill for Claude. Notice the XML-style tags, the specific formatting conventions, the way tools are declared.

**[VISUAL: Show OpenAI-style function]**

> "And here's the same skill for OpenAI. Completely different structure. JSON schemas. Function definitions. Different system message patterns.

**[VISUAL: Show Gemini format]**

> "Gemini has yet another format. Different conventions for grounding, different handling of long context.

**[VISUAL: Frustrated developer illustration]**

> "If you're a researcher, you don't want to learn three different prompt engineering paradigms. You want to focus on the science.

> That's why we created USDL. Write your skill once in a neutral format. Let the adapters handle the platform-specific translations."

---

### SCENE 3: USDL INTRODUCTION (2:15 - 4:30)
**[VISUAL: Open single_cell_qc.yaml in editor]**

**SCRIPT:**
> "Let me show you what USDL looks like in practice.

```bash
cd platform_prototype/examples/
cat single_cell_qc.yaml
```

**[VISUAL: Show YAML structure]**

> "This is our scRNA-seq QC skill defined in USDL. Let's walk through the key sections.

**[VISUAL: Highlight metadata section]**

```yaml
skill:
  id: single-cell-qc
  name: "Single Cell RNA-seq Quality Control"
  version: "1.0.0"
  author: "Universal Skills Team"
  domain: genomics
  tags:
    - scRNA-seq
    - quality-control
    - bioinformatics
```

> "Metadata section. Standard information about the skill - ID, version, author, domain classification.

**[VISUAL: Highlight capabilities section]**

```yaml
capabilities:
  - name: calculate_qc_metrics
    description: "Calculate QC metrics for scRNA-seq data"
    inputs:
      - name: data_path
        type: file_path
        description: "Path to 10X or h5ad data"
    outputs:
      - name: metrics
        type: dataframe
```

> "Capabilities define what the skill can do. Each capability has inputs, outputs, and descriptions. This is platform-agnostic - we're describing what, not how.

**[VISUAL: Highlight prompts section]**

```yaml
prompts:
  system: |
    You are a bioinformatics expert specializing in single-cell
    RNA sequencing analysis. You help researchers perform quality
    control on their scRNA-seq data following scverse best practices.
  user_template: |
    Analyze the following scRNA-seq data: {data_path}
    Calculate QC metrics and identify low-quality cells.
```

> "Prompts section. The core instructions that define skill behavior. Notice these are written in plain language - no platform-specific markup yet.

**[VISUAL: Highlight platform configs]**

```yaml
platforms:
  claude:
    prompt_style: xml_tags
    max_tokens: 4096
    use_prefill: true
  openai:
    prompt_style: json_schema
    function_calling: true
  gemini:
    prompt_style: markdown
    grounding: true
```

> "Platform configurations. Hints for the adapters about how to optimize for each platform. But notice - you don't write platform-specific code here. Just configuration."

---

### SCENE 4: THE ADAPTER SYSTEM (4:30 - 7:00)
**[VISUAL: Architecture diagram showing USDL -> Adapters -> Platforms]**

**SCRIPT:**
> "Now let's see how adapters transform USDL into platform-specific formats.

```bash
cd platform_prototype/adapters/
ls -la
```

**[VISUAL: Show adapter files]**

> "We have adapters for Claude, OpenAI, and more. Let me show you the Claude adapter in action.

**[VISUAL: Open claude_adapter.py]**

```python
# Show key conversion function
def convert_to_mcp(usdl_skill):
    # Transform capabilities to MCP tools
    # Add XML formatting
    # Configure Claude-specific features
```

> "The adapter reads the USDL definition and produces Claude-native output. Let's run it:

```bash
python cli.py build --platform claude ../examples/single_cell_qc.yaml
```

**[VISUAL: Show output]**

> "It generates:
> - An MCP server package
> - A SKILL.md file for Claude Code
> - Tool use schemas for the API

**[VISUAL: Show generated Claude format]**

> "Look at the generated prompt. See how it added XML tags? How it structured the tool definitions? The adapter did this automatically.

> Now let's do the same for OpenAI:

```bash
python cli.py build --platform openai ../examples/single_cell_qc.yaml
```

**[VISUAL: Show OpenAI output]**

> "Completely different output format. JSON function definitions. OpenAPI schema. Assistants API configuration.

> Same skill. Same capabilities. Different platform packaging."

---

### SCENE 5: SIDE-BY-SIDE DEMONSTRATION (7:00 - 9:00)
**[VISUAL: Split screen - Claude and ChatGPT both visible]**

**SCRIPT:**
> "Let me prove this works. I'm going to run the same analysis on both platforms.

**[VISUAL: Show same input on both]**

> "Same data. Same request. Let's see what happens.

**[VISUAL: Run on Claude]**

> "Claude is processing... generating the QC analysis...

**[VISUAL: Run on ChatGPT]**

> "And ChatGPT is doing the same thing...

**[VISUAL: Show both results]**

> "Look at the outputs. The formatting is different - that's expected, each platform has its style. But the analysis? The metrics? The filtering thresholds?

> Identical. Because the underlying skill logic is the same.

> This is what platform-agnostic means. The science doesn't change when you switch vendors."

---

### SCENE 6: VALIDATION & TESTING (9:00 - 10:30)
**[VISUAL: Show validation output]**

**SCRIPT:**
> "USDL isn't just a format - it's a validated schema. Let me show you the built-in quality checks.

```bash
python cli.py validate ../examples/single_cell_qc.yaml
```

**[VISUAL: Show validation output]**

> "The validator checks:
> - Required fields are present
> - Data types are correct
> - Capability definitions are complete
> - Platform configurations are valid

> If something's wrong, you find out before deployment, not in production.

**[VISUAL: Show test section of YAML]**

```yaml
tests:
  - name: "basic_qc_test"
    input:
      data_path: "test_data/sample.h5ad"
    expected:
      contains: "total_counts"
      contains: "pct_counts_mt"
```

> "You can also define tests directly in the skill. The evaluator runs these across all platforms and generates comparison reports.

> We'll cover the full testing system in Video 5."

---

### SCENE 7: CLOSING (10:30 - 11:30)
**[VISUAL: USDL logo and key points]**

**SCRIPT:**
> "To summarize what we covered:

> **USDL** - A standardized YAML schema for defining biomedical AI skills. Platform-neutral, human-readable.

> **Adapters** - Automatic conversion to Claude, OpenAI, Gemini, and more. No manual rewriting.

> **Validation** - Built-in schema checking catches errors early.

> **Portability** - Same skill, same results, any platform.

> In the next video, I'll show you the complete platform prototype SDK - including the BioKernel runtime and the AI-powered optimizer.

> The USDL specification is in the platform_prototype/schema folder if you want to explore it further.

> See you in Video 5."

**[VISUAL: End card]**

---
---

# VIDEO 5: Platform Prototype SDK
## "Building Skills with the Platform Prototype SDK"
### Duration: 10-12 minutes

---

### SCENE 1: OPENING (0:00 - 0:30)
**[VISUAL: platform_prototype folder open in VS Code]**

**SCRIPT:**
> "You've seen what USDL is and how adapters work. Now let's explore the complete toolkit.

> The Platform Prototype SDK gives you everything you need to build, test, optimize, and deploy biomedical AI skills.

> Let's take a tour."

---

### SCENE 2: SDK OVERVIEW (0:30 - 2:00)
**[VISUAL: Folder structure diagram]**

**SCRIPT:**
```bash
cd platform_prototype/
ls -la
```

**[VISUAL: Show directory listing]**

> "The SDK has six main components:

```
platform_prototype/
├── adapters/      # Platform converters
├── biokernel/     # Unified runtime
├── schema/        # USDL specification
├── optimizer/     # AI prompt tuning
├── evaluator/     # Cross-platform testing
├── examples/      # Sample skills
└── cli.py         # Command-line interface
```

> "Let me explain what each does and then demonstrate them."

---

### SCENE 3: THE CLI TOOL (2:00 - 4:00)
**[VISUAL: Terminal with CLI help]**

**SCRIPT:**
> "Everything is accessible through the CLI. Let's see the available commands:

```bash
python cli.py --help
```

**[VISUAL: Show command list]**

> "Six main commands:

> **validate** - Check your skill definition against the USDL schema

```bash
python cli.py validate examples/single_cell_qc.yaml
```

**[VISUAL: Show successful validation]**

> **build** - Generate platform-specific artifacts

```bash
python cli.py build --platform claude examples/single_cell_qc.yaml
python cli.py build --platform openai examples/single_cell_qc.yaml
```

**[VISUAL: Show build output]**

> **optimize** - AI-tune prompts for specific platforms

```bash
python cli.py optimize examples/single_cell_qc.yaml --platform gemini
```

> **test** - Run the evaluation suite

```bash
python cli.py test examples/single_cell_qc.yaml
```

> **serve** - Start the BioKernel runtime

```bash
python cli.py serve
```

> **compare** - Run skill across all platforms and compare results

```bash
python cli.py compare examples/single_cell_qc.yaml
```

> "Let's dive deeper into each component."

---

### SCENE 4: BIOKERNEL RUNTIME (4:00 - 6:30)
**[VISUAL: Open biokernel/server.py]**

**SCRIPT:**
> "BioKernel is the unified runtime that powers everything. Let me show you what makes it special.

```bash
cat biokernel/server.py
```

**[VISUAL: Show key sections of code]**

> "BioKernel does three things:

**[VISUAL: Diagram - Intelligent Routing]**

> "First: **Intelligent Routing**. Not all tasks need the most powerful model. BioKernel analyzes each request and routes it optimally.

```python
# Routing logic (simplified)
if task.complexity == 'simple':
    route_to('gemini-flash')  # Fast and cheap
elif task.requires_reasoning:
    route_to('claude-opus')   # Best reasoning
elif task.is_creative:
    route_to('gpt-4o')        # Creative tasks
else:
    route_to('claude-sonnet') # Default
```

> "Simple queries go to fast, cheap models. Complex reasoning goes to powerful models. You get optimal cost-performance automatically.

**[VISUAL: Show code execution capability]**

> "Second: **Code Execution**. BioKernel can execute Python, R, and shell commands in a sandboxed environment.

```python
# Execute skill code
result = biokernel.execute(
    code=skill.implementation,
    data=user_data,
    sandbox=True
)
```

> "This is how skills like scRNA-seq QC actually run the analysis - not just generate text, but execute real bioinformatics pipelines.

**[VISUAL: Show API endpoints]**

> "Third: **Dual API Support**. BioKernel exposes both MCP-compatible and OpenAI-compatible endpoints.

```
POST /mcp/tools        # MCP format
POST /v1/completions   # OpenAI format
```

> "Any client that speaks either protocol can connect. Maximum compatibility.

> Let's start the server:

```bash
python biokernel/server.py
```

**[VISUAL: Show server starting]**

> "BioKernel is now running on localhost:8080, ready to handle skill requests."

---

### SCENE 5: THE OPTIMIZER (6:30 - 8:30)
**[VISUAL: Open optimizer/meta_prompter.py]**

**SCRIPT:**
> "Writing good prompts for one platform doesn't mean they'll work well on another. Each LLM has quirks and preferences.

> The Optimizer solves this by using AI to tune prompts for specific platforms.

```bash
python cli.py optimize examples/single_cell_qc.yaml --platform gemini
```

**[VISUAL: Show optimization process]**

> "Here's what happens:

> 1. It takes your base USDL prompt
> 2. Applies platform-specific best practices
> 3. Generates variations
> 4. Tests them against evaluation cases
> 5. Selects the best-performing version

**[VISUAL: Show before/after prompts]**

> "For example, Claude prefers XML-style tags and benefits from 'prefilling' - starting the response for the model. OpenAI prefers concise system messages and specific function schemas. Gemini works best with long-context optimization and grounding.

> The optimizer knows these patterns and applies them automatically.

**[VISUAL: Show optimization hints from YAML]**

```yaml
optimization_hints:
  claude:
    - "Use XML tags for structure"
    - "Leverage prefilling"
  openai:
    - "Keep system messages concise"
    - "Use precise function definitions"
  gemini:
    - "Optimize for long context"
    - "Enable Google Search grounding"
```

> "You can also provide hints in your USDL file to guide the optimization."

---

### SCENE 6: THE EVALUATOR (8:30 - 10:00)
**[VISUAL: Open evaluator/eval_engine.py]**

**SCRIPT:**
> "How do you know your skill works correctly across platforms? You test it systematically.

> The Evaluator runs your skill against test cases on every supported platform and generates comparison reports.

```bash
python cli.py test examples/single_cell_qc.yaml --all-platforms
```

**[VISUAL: Show test execution]**

> "It's running the skill on Claude, GPT-4, and Gemini simultaneously...

**[VISUAL: Show results table]**

```
Platform    | Accuracy | Latency  | Cost
------------|----------|----------|-------
Claude 3.5  | 98.2%    | 2.3s     | $0.02
GPT-4o      | 96.8%    | 3.1s     | $0.03
Gemini Pro  | 94.5%    | 1.8s     | $0.01
```

> "Now you can see exactly how your skill performs on each platform. Maybe Gemini is fastest but less accurate. Maybe Claude is most expensive but most reliable.

> This data helps you make informed deployment decisions.

**[VISUAL: Show test case definition]**

```yaml
evaluation_tests:
  - name: "detect_dying_cells"
    input:
      data: "test_high_mito.h5ad"
    assertions:
      - type: contains
        value: "high mitochondrial"
      - type: greater_than
        field: cells_filtered
        value: 100
```

> "Tests are defined in your USDL file. The evaluator runs them automatically on every build."

---

### SCENE 7: CREATING A NEW SKILL (10:00 - 11:00)
**[VISUAL: Blank YAML file]**

**SCRIPT:**
> "Let me quickly show you how to create a new skill from scratch.

> Step 1: Copy the template

```bash
cp examples/template.yaml my_new_skill.yaml
```

> Step 2: Fill in your skill details

```yaml
skill:
  id: my-new-skill
  name: "My New Biomedical Skill"
  # ... define capabilities, prompts, tests
```

> Step 3: Validate

```bash
python cli.py validate my_new_skill.yaml
```

> Step 4: Build for your target platforms

```bash
python cli.py build --platform claude my_new_skill.yaml
```

> Step 5: Test

```bash
python cli.py test my_new_skill.yaml
```

> That's it. You've created a platform-agnostic biomedical skill."

---

### SCENE 8: CLOSING (11:00 - 11:30)
**[VISUAL: SDK component summary]**

**SCRIPT:**
> "The Platform Prototype SDK gives you:

> - **CLI** for all operations
> - **BioKernel** for intelligent routing and execution
> - **Optimizer** for AI-powered prompt tuning
> - **Evaluator** for cross-platform testing

> Together, these tools make building and deploying biomedical AI skills dramatically easier.

> In the next video, I'll walk through all six skills in our library - Clinical, Genomics, and Drug Discovery.

> The full SDK is in the platform_prototype folder on GitHub.

> See you in Video 6."

**[VISUAL: End card]**

---
---

# VIDEO 6: All Six Skills Overview
## "Complete Skills Library: Clinical, Genomics, Drug Discovery"
### Duration: 15-18 minutes

---

### SCENE 1: OPENING (0:00 - 0:45)
**[VISUAL: Skills grid showing all 6 skills]**

**SCRIPT:**
> "We've covered the platform and the architecture. Now let's look at what you can actually do with it.

> The Universal Biomedical Skills Platform includes six production-ready skills across three domains:

> - Clinical Informatics
> - Genomics
> - Drug Discovery

> I'll walk through each one, showing you what it does, how it works, and where you might use it."

---

### SCENE 2: CLINICAL - NOTE SUMMARIZATION (0:45 - 3:30)
**[VISUAL: Clinical domain header, then skill folder]**

**SCRIPT:**
> "Let's start with Clinical Informatics. First up: Clinical Note Summarization.

```bash
cd Skills/Clinical/clinical_note_summarization/
cat README.md
```

**[VISUAL: Show README content]**

> "**What it does:** Converts unstructured clinical notes into standardized SOAP format.

> SOAP stands for:
> - **S**ubjective - What the patient reports
> - **O**bjective - What the clinician observes and measures
> - **A**ssessment - The diagnosis or clinical impression
> - **P**lan - The treatment plan

**[VISUAL: Show example input/output]**

> "Here's an example. Input - a messy, narrative clinical note:

```
Patient is a 58yo male presenting with chest pain x 3 days.
States the pain is worse with exertion. Denies SOB. BP 142/88,
HR 78, afebrile. ECG shows NSR, no ST changes. Will order
stress test and start ASA 81mg daily.
```

> "Output - structured SOAP format:

```
SUBJECTIVE:
- 58-year-old male
- Chief complaint: chest pain for 3 days
- Worse with exertion
- Denies shortness of breath

OBJECTIVE:
- BP: 142/88
- HR: 78
- Afebrile
- ECG: Normal sinus rhythm, no ST changes

ASSESSMENT:
- Chest pain, possible angina

PLAN:
- Order stress test
- Start aspirin 81mg daily
```

**[VISUAL: Show the prompt.md file]**

> "**How it works:** The skill uses a carefully crafted prompt that understands clinical terminology, knows the SOAP structure, and extracts relevant information while maintaining accuracy.

> **Use cases:**
> - Automated medical scribing
> - EHR data standardization
> - Clinical documentation improvement
> - Quality assurance audits"

---

### SCENE 3: CLINICAL - TRIAL ELIGIBILITY (3:30 - 6:00)
**[VISUAL: Second clinical skill folder]**

**SCRIPT:**
> "The second clinical skill: Trial Eligibility Agent.

```bash
cd Skills/Clinical/trial_eligibility_agent/
cat README.md
```

**[VISUAL: Show README]**

> "**What it does:** Matches patients to clinical trials based on inclusion and exclusion criteria.

> Finding eligible patients for clinical trials is a major bottleneck in medical research. This skill automates the matching process.

**[VISUAL: Show workflow diagram]**

> "The workflow:
> 1. **Input** - Patient data and trial criteria
> 2. **Extract** - Parse inclusion/exclusion requirements
> 3. **Match** - Compare patient attributes against criteria
> 4. **Report** - Generate eligibility assessment with explanations

**[VISUAL: Show example]**

> "Example - Trial requires:
> - Age 18-65
> - Confirmed Type 2 diabetes
> - HbA1c between 7.0-10.0%
> - No history of DKA

> Patient profile:
> - Age 54
> - Type 2 diabetes since 2018
> - HbA1c 8.2%
> - No DKA history

> Output:

```
ELIGIBILITY: LIKELY ELIGIBLE

Criteria Analysis:
 Age (18-65): MEETS - Patient is 54
 Type 2 diabetes: MEETS - Confirmed diagnosis 2018
 HbA1c (7.0-10.0%): MEETS - Current value 8.2%
 No DKA history: MEETS - No documented episodes

Recommendation: Patient appears to meet all stated criteria.
Suggest formal screening.
```

**[VISUAL: Show HIPAA note]**

> "**Important note:** This skill is designed with privacy in mind. It processes de-identified data and includes guidance on HIPAA compliance. Always follow your institution's data governance policies."

---

### SCENE 4: GENOMICS - scRNA-seq QC (6:00 - 8:30)
**[VISUAL: Genomics domain header]**

**SCRIPT:**
> "Moving to Genomics. You've already seen our flagship skill in action - Single Cell RNA-seq Quality Control.

```bash
cd Skills/Genomics/single_cell_qc/
```

**[VISUAL: Show skill structure]**

> "Let me highlight some aspects we didn't cover in the live demo.

**[VISUAL: Show qc_core.py]**

> "The implementation uses scanpy, the standard Python library for single-cell analysis. We follow scverse best practices - the community-driven ecosystem that includes scanpy, anndata, and related tools.

**[VISUAL: Show metrics calculated]**

> "Metrics we calculate:
> - **total_counts** - Total UMIs per cell
> - **n_genes_by_counts** - Unique genes detected
> - **pct_counts_mt** - Mitochondrial percentage (quality indicator)
> - **pct_counts_ribo** - Ribosomal percentage
> - **pct_counts_hb** - Hemoglobin percentage (contamination indicator)

**[VISUAL: Show filtering approach]**

> "Filtering uses MAD - Median Absolute Deviation. Unlike mean-based approaches, MAD is robust to outliers. A cell is flagged if it's more than N MADs from the median.

> Default: 5 MADs for total counts and genes, 3 MADs for mitochondrial percentage.

**[VISUAL: Show output formats]**

> "Outputs:
> - Annotated AnnData object with QC metrics
> - Filtered AnnData object
> - Before/after visualization plots
> - Detailed QC report

> This skill integrates directly into any scverse workflow."

---

### SCENE 5: GENOMICS - CRISPR DESIGN (8:30 - 11:00)
**[VISUAL: CRISPR skill folder]**

**SCRIPT:**
> "The second genomics skill: CRISPR Design Agent.

```bash
cd Skills/Genomics/crispr_design_agent/
cat README.md
```

**[VISUAL: Show README]**

> "**What it does:** Automates CRISPR guide RNA design with off-target analysis.

> CRISPR-Cas9 gene editing requires designing short guide RNAs that target specific genomic locations. Good guides have high on-target efficiency and minimal off-target effects.

**[VISUAL: Show workflow]**

> "The workflow:
> 1. **Input** - Target gene or sequence
> 2. **Identify** - Find PAM sites (NGG for SpCas9)
> 3. **Design** - Generate candidate sgRNAs
> 4. **Score** - Predict on-target efficiency
> 5. **Analyze** - Check for off-target matches
> 6. **Output** - Ranked list with recommendations

**[VISUAL: Show example output]**

> "Example - Designing guides for BRCA1:

```
Top 3 Guide Candidates:

1. GCAGTGAAGAGATGCCGCTT
   Position: Exon 11
   On-target score: 0.87
   Off-targets: 0 in exons, 2 in intergenic regions
   Recommendation: EXCELLENT

2. AGTGCTACCATGGTGCCAAG
   Position: Exon 11
   On-target score: 0.82
   Off-targets: 1 in intron
   Recommendation: GOOD

3. TTGATCAGGACTTGCGCTTT
   Position: Exon 10
   On-target score: 0.79
   Off-targets: 3 in coding regions
   Recommendation: USE WITH CAUTION
```

**[VISUAL: Show PAM handling]**

> "The skill handles multiple Cas variants:
> - SpCas9 (NGG PAM)
> - SaCas9 (NNGRRT PAM)
> - Cas12a (TTTV PAM)

> And generates complete protocols including oligo sequences for cloning."

---

### SCENE 6: DRUG DISCOVERY - CHEMICAL PROPERTY (11:00 - 13:00)
**[VISUAL: Drug Discovery domain header]**

**SCRIPT:**
> "Now Drug Discovery. First: Chemical Property Lookup.

```bash
cd Skills/Drug_Discovery/chemical_property_lookup/
cat README.md
```

**[VISUAL: Show README]**

> "**What it does:** Calculates molecular properties using RDKit, the open-source cheminformatics toolkit.

> This is an agent tool skill - designed to be called by other agents that need chemical information.

**[VISUAL: Show capabilities]**

> "Capabilities:
> - **Molecular weight** calculation
> - **SMILES to structure** conversion
> - **Structure to SMILES** conversion
> - **Lipinski's Rule of Five** assessment
> - **LogP** (lipophilicity) calculation
> - **TPSA** (topological polar surface area)
> - **Rotatable bonds** count

**[VISUAL: Show example]**

> "Example - Query about aspirin:

> Input: 'What are the drug-like properties of aspirin?'

> Output:
```
Compound: Aspirin (acetylsalicylic acid)
SMILES: CC(=O)OC1=CC=CC=C1C(=O)O

Properties:
- Molecular Weight: 180.16 g/mol
- LogP: 1.19
- H-Bond Donors: 1
- H-Bond Acceptors: 4
- Rotatable Bonds: 3
- TPSA: 63.6

Lipinski Rule of Five: PASSES
- MW < 500: Yes (180.16)
- LogP < 5: Yes (1.19)
- HBD <= 5: Yes (1)
- HBA <= 10: Yes (4)

Drug-likeness: Favorable oral bioavailability expected.
```

> "This skill is especially useful when integrated into larger drug discovery workflows."

---

### SCENE 7: DRUG DISCOVERY - AgentD (13:00 - 15:30)
**[VISUAL: AgentD skill folder]**

**SCRIPT:**
> "The most ambitious skill in our library: AgentD - the Drug Discovery Agent.

```bash
cd Skills/Drug_Discovery/agentd_drug_discovery/
cat README.md
```

**[VISUAL: Show README]**

> "**What it does:** Orchestrates a multi-step drug discovery pipeline from target to candidate molecules.

> This is a full agentic workflow - it coordinates multiple tools and databases to accelerate early-stage drug discovery.

**[VISUAL: Show pipeline diagram]**

> "The pipeline:

> **Step 1: Literature Mining**
> - Searches PubMed for target-disease associations
> - Extracts known modulators and binding sites
> - Summarizes mechanism of action

> **Step 2: Known Compound Retrieval**
> - Queries ChEMBL for existing bioactive compounds
> - Retrieves IC50, Ki, EC50 data
> - Identifies chemical scaffolds

> **Step 3: Molecule Generation**
> - Proposes novel molecules based on known scaffolds
> - Uses molecular generation algorithms
> - Ensures drug-likeness constraints

> **Step 4: ADMET Prediction**
> - Predicts Absorption, Distribution, Metabolism, Excretion, Toxicity
> - Flags potential liabilities
> - Ranks candidates

> **Step 5: Docking Preparation**
> - Generates 3D structures
> - Prepares files for molecular docking
> - Suggests binding poses

**[VISUAL: Show example output summary]**

> "Example - Finding inhibitors for a kinase target:

```
TARGET: JAK2 (Janus Kinase 2)
INDICATION: Myeloproliferative disorders

Literature Summary:
- 847 publications found
- Key binding site: ATP pocket
- Known inhibitors: ruxolitinib, fedratinib

ChEMBL Compounds Retrieved: 1,247 bioactive molecules
Top Scaffold: Pyrimidine core

Novel Candidates Generated: 50 molecules
Top 5 by ADMET Score:
1. CANDIDATE-001: Score 0.89, Novel pyrrolopyrimidine
2. CANDIDATE-002: Score 0.85, Modified ruxolitinib analog
...

Recommendation: CANDIDATE-001 suggested for docking studies.
```

**[VISUAL: Show integrations]**

> "AgentD integrates with:
> - PubMed API
> - ChEMBL database
> - PubChem
> - RDKit
> - Open-source docking tools

> This is drug discovery acceleration in action."

---

### SCENE 8: CLOSING (15:30 - 16:30)
**[VISUAL: All 6 skills summary grid]**

**SCRIPT:**
> "Let's recap the complete skills library:

**[VISUAL: Table appearing]**

| Domain | Skill | Key Capability |
|--------|-------|----------------|
| Clinical | Note Summarization | Unstructured to SOAP |
| Clinical | Trial Eligibility | Patient-trial matching |
| Genomics | scRNA-seq QC | Single-cell quality control |
| Genomics | CRISPR Design | Guide RNA design |
| Drug Discovery | Chemical Properties | Molecular calculations |
| Drug Discovery | AgentD | Full discovery pipeline |

> "Six skills. Three domains. All platform-agnostic.

> And this is just the beginning. The library is designed to grow. In Video 8, I'll show you how to contribute your own skills.

> In the next video, I'll present the research paper that formalizes this work - the science behind Universal Biomedical Skills.

> All skills are in the Skills folder on GitHub.

> See you in Video 7."

**[VISUAL: End card]**

---

### VIDEO 6 RECORDING NOTES:

**Pacing:**
- Spend roughly equal time on each skill (2-3 min)
- Use visuals to break up narration
- Show actual code/files briefly for credibility

**Visuals Needed:**
- Domain header graphics
- Workflow diagrams for each skill
- Example input/output displays
- Integration logos (PubMed, ChEMBL, etc.)

**Emphasis:**
- These are real, working skills, not concepts
- Each solves a genuine biomedical problem
- All work across platforms
