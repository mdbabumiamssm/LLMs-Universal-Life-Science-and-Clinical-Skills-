# Video Scripts: Part 1 (Videos 1-3)
## Universal Biomedical Skills Platform Tutorial Series

---

# VIDEO 1: Introduction & Vision
## "Universal Biomedical Skills: One Skill, Every LLM"
### Duration: 8-10 minutes

---

### SCENE 1: HOOK (0:00 - 0:30)
**[VISUAL: Black screen fading to title card]**

**SCRIPT:**
> "What if you could write a biomedical AI skill once... and have it work on Claude, ChatGPT, Gemini, and even your local LLM?

> No more rewriting prompts. No more platform lock-in. No more duplicated effort.

> Welcome to the Universal Biomedical Skills Platform."

**[VISUAL: Animated logo reveal]**

---

### SCENE 2: THE PROBLEM (0:30 - 2:00)
**[VISUAL: Split screen showing different LLM interfaces]**

**SCRIPT:**
> "If you work in bioinformatics, clinical informatics, or drug discovery, you've probably experienced this frustration:

> You spend hours crafting the perfect prompt for single-cell RNA sequencing analysis on ChatGPT. It works beautifully. Then your institution adopts Claude. Now you need to rewrite everything.

> Or maybe you've built a clinical note summarization tool for one platform, only to discover your collaborators use a different one.

**[VISUAL: Show fragmented ecosystem diagram]**

> "The biomedical AI ecosystem is fragmented. Every platform has its own format, its own conventions, its own limitations.

> This fragmentation creates three major problems:

**[VISUAL: Bullet points appearing]**

> "First: **Duplicated effort**. Teams rewrite the same skills for each platform.

> Second: **Platform lock-in**. Your work becomes tied to one vendor's ecosystem.

> Third: **Limited collaboration**. Sharing skills across institutions becomes nearly impossible when everyone uses different tools."

---

### SCENE 3: THE SOLUTION (2:00 - 4:00)
**[VISUAL: Architecture diagram animation]**

**SCRIPT:**
> "Today, I'm introducing our solution: the Universal Biomedical Skills Platform.

> The core idea is simple but powerful: **Write your skill once in a universal format, and our platform automatically converts it for any LLM.**

**[VISUAL: USDL to multiple platforms animation]**

> "We created something called USDL - the Universal Skill Definition Language. It's a standardized YAML schema specifically designed for biomedical AI skills.

> You define your skill in USDL once. Our adapters then convert it to:
> - Claude's MCP format
> - OpenAI's function calling schema
> - Google's Gemini format
> - Or any local model through our unified API

**[VISUAL: Show conversion flow]**

> "But we didn't stop there. We also built:

> **BioKernel** - a runtime that intelligently routes requests to the optimal LLM. Simple tasks go to fast, cheap models. Complex reasoning goes to powerful models. You don't have to manage this manually.

> **An Optimizer** - that uses AI to tune your prompts for each platform automatically.

> **An Evaluator** - that tests your skills across all platforms and generates performance scorecards.

> This isn't just a concept. It's a working system with production-ready skills."

---

### SCENE 4: DEMO TEASER (4:00 - 5:30)
**[VISUAL: Screen recording preview of scRNA-seq demo]**

**SCRIPT:**
> "Let me show you what this looks like in practice.

> Here I have real single-cell RNA sequencing data from bone marrow samples. Three samples from the GSE136112 dataset.

**[VISUAL: Show folder structure briefly]**

> "I'm going to invoke our scRNA-seq Quality Control skill through Claude.

**[VISUAL: Quick demo - show command and immediate results]**

> "In seconds, the skill analyzes over 10,000 cells, calculates quality metrics, identifies outliers using MAD-based statistical methods, and generates publication-ready visualizations.

**[VISUAL: Show before/after QC plots]**

> "Look at this before-and-after comparison. The skill automatically identified dying cells with high mitochondrial content, empty droplets with too few genes, and potential doublets.

> And here's the key point: this exact same skill can run on GPT-4, Gemini, or a local model - with zero modifications to the core logic.

> In Video 3, I'll walk through this demo step by step."

---

### SCENE 5: WHAT'S INCLUDED (5:30 - 7:30)
**[VISUAL: Skills grid/table]**

**SCRIPT:**
> "The platform currently includes six production-ready skills across three biomedical domains:

**[VISUAL: Clinical section]**

> "In **Clinical Informatics**:
> - Clinical Note Summarization - converts unstructured medical notes to standardized SOAP format
> - Trial Eligibility Agent - matches patients to clinical trials based on inclusion and exclusion criteria

**[VISUAL: Genomics section]**

> "In **Genomics**:
> - Single-Cell RNA-seq QC - what you just saw, automated quality control following scverse best practices
> - CRISPR Design Agent - automates guide RNA design with off-target analysis

**[VISUAL: Drug Discovery section]**

> "In **Drug Discovery**:
> - Chemical Property Lookup - calculates molecular properties using RDKit
> - AgentD - a multi-step drug discovery pipeline integrating ChEMBL, PubChem, and molecular docking

> Each skill is documented, tested, and ready to use. And the collection is growing."

---

### SCENE 6: CALL TO ACTION (7:30 - 8:30)
**[VISUAL: GitHub page]**

**SCRIPT:**
> "Everything I've shown you is open source and available on GitHub right now.

**[VISUAL: Show URL]**

> "You can find it at github.com/mdbabumiamssm/Universal-Life-Science-and-Clinical-Skills-

> Clone it, try the demo, adapt it for your research.

**[VISUAL: Video series preview]**

> "In this video series, I'll cover:
> - A complete tour of the GitHub repository
> - A live demonstration with real scRNA-seq data
> - Deep dives into the USDL architecture and platform adapters
> - Walkthroughs of each skill
> - And how you can contribute to the project

> If you're working in biomedical AI and tired of platform fragmentation, this is for you.

> Let's get started."

**[VISUAL: End card with subscribe/like prompt and GitHub URL]**

---

### VIDEO 1 NOTES FOR RECORDING:
- Maintain energetic but professional tone
- Pause briefly after key points for emphasis
- Demo teaser should be fast-paced to build excitement
- End with clear call to action

---
---

# VIDEO 2: GitHub Repository Tour
## "Exploring the Skills Repository: Structure & Organization"
### Duration: 6-8 minutes

---

### SCENE 1: OPENING (0:00 - 0:30)
**[VISUAL: GitHub homepage]**

**SCRIPT:**
> "Welcome back. In this video, I'll give you a complete tour of our GitHub repository.

> By the end, you'll understand the structure, know where everything is located, and be ready to clone and start using the skills.

> Let's dive in."

---

### SCENE 2: REPOSITORY OVERVIEW (0:30 - 1:30)
**[VISUAL: GitHub repository main page]**

**SCRIPT:**
> "Here's the main repository page. Let me orient you.

**[VISUAL: Highlight README]**

> "The README gives you a quick start guide. It tells you what the project is, how to install it, and links to detailed documentation.

**[VISUAL: Scroll through README sections]**

> "You'll see the project description, installation instructions, a table of all available skills, and contribution guidelines.

**[VISUAL: Show stars/forks/license]**

> "The repository is MIT licensed, meaning you can use it freely in your own projects, including commercial applications.

> Now let's look at the folder structure."

---

### SCENE 3: MAIN FOLDER STRUCTURE (1:30 - 3:30)
**[VISUAL: Terminal or VS Code file explorer]**

**SCRIPT:**
> "I'm going to navigate through the key directories.

```bash
cd Universal-Life-Science-and-Clinical-Skills-
ls -la
```

**[VISUAL: Show directory listing]**

> "There are four main areas you need to know:

**[VISUAL: Highlight Skills folder]**

> "First, the **Skills** folder. This is where all the biomedical AI skills live. It's organized by domain.

```bash
ls Skills/
```

> "You can see three subdirectories: Clinical, Genomics, and Drug_Discovery.

**[VISUAL: Navigate into Skills]**

> "Let's look inside Clinical:

```bash
ls Skills/Clinical/
```

> "Each skill has its own folder with a README, prompt templates, and implementation code.

**[VISUAL: Highlight test_demonstration]**

> "Second, the **test_demonstration** folder. This contains working examples with real data. We'll use this extensively in the live demo.

```bash
ls test_demonstration/
```

> "You'll find the scRNAsedata folder with our bone marrow samples, pre-generated results in qc_results, and scripts to run everything.

**[VISUAL: Highlight platform_prototype]**

> "Third, the **platform_prototype** folder. This is the SDK - the tooling that makes platform-agnostic skills possible.

```bash
ls platform_prototype/
```

> "Adapters for different platforms, the BioKernel runtime, the USDL schema, and more. We'll cover this in detail in Video 5.

**[VISUAL: Highlight documentation files]**

> "Finally, at the root level, you have documentation files like the strategy document and this video tutorial plan."

---

### SCENE 4: INSIDE A SKILL (3:30 - 5:00)
**[VISUAL: Navigate to scRNA-seq QC skill]**

**SCRIPT:**
> "Let's look at what's inside an actual skill. I'll use the single-cell RNA-seq QC skill as our example.

```bash
cd Skills/Genomics/single_cell_qc/
ls -la
```

**[VISUAL: Show files]**

> "Every skill follows a consistent structure:

> **README.md** - Documentation explaining what the skill does, its capabilities, and usage examples.

**[VISUAL: Open README briefly]**

> **prompt.md** - The system prompt that defines the skill's behavior. This is where the AI instructions live.

> **Implementation files** - Python modules with the actual functionality. For this skill, we have:
> - qc_core.py - core metric calculations
> - qc_plotting.py - visualization functions
> - qc_analysis.py - the main analysis script

**[VISUAL: Show code briefly]**

> "The key point is: the prompt defines what the skill knows and how it responds. The Python code provides the actual computational capabilities.

> When you convert this to different platforms, the prompt adapts but the core logic stays the same."

---

### SCENE 5: TEST DATA LOCATION (5:00 - 6:00)
**[VISUAL: Navigate to scRNAsedata]**

**SCRIPT:**
> "For the live demo, you'll need data. Let's look at the test dataset.

```bash
cd test_demonstration/scRNAsedata/
ls -la
```

> "We have three bone marrow samples from the GSE136112 dataset:
> - GSM3901485
> - GSM3901486
> - GSM3901487

```bash
ls GSM3901485/
```

> "Each sample contains the standard 10X Genomics output:
> - matrix.mtx - the sparse gene expression matrix
> - genes.tsv - gene identifiers
> - barcodes.tsv - cell barcodes

> This is real, publicly available data. Not synthetic. Not toy examples. Production-quality validation."

---

### SCENE 6: CLONING & SETUP (6:00 - 7:00)
**[VISUAL: Fresh terminal]**

**SCRIPT:**
> "Ready to try it yourself? Here's how to get started.

> Step one - clone the repository:

```bash
git clone https://github.com/mdbabumiamssm/Universal-Life-Science-and-Clinical-Skills-.git
```

> Step two - navigate to the directory:

```bash
cd Universal-Life-Science-and-Clinical-Skills-
```

> Step three - install dependencies:

```bash
pip install -r test_demonstration/requirements.txt
```

> "This installs scanpy, anndata, matplotlib, and other required packages.

> Step four - verify the demo works:

```bash
cd test_demonstration
bash run_test.sh
```

> "That's it. You're ready to run the skills."

---

### SCENE 7: CLOSING (7:00 - 7:30)
**[VISUAL: GitHub page with star button highlighted]**

**SCRIPT:**
> "You now know your way around the repository.

> In the next video, I'll walk through a complete live demonstration using Claude and the scRNA-seq QC skill with our bone marrow dataset.

> If you find this useful, consider starring the repository on GitHub. It helps others discover the project.

> See you in Video 3."

**[VISUAL: End card]**

---
---

# VIDEO 3: Live Demo - scRNA-seq QC
## "Live Demo: Single Cell RNA-seq Quality Control"
### Duration: 12-15 minutes

---

### SCENE 1: OPENING (0:00 - 0:45)
**[VISUAL: Terminal ready, Claude interface visible]**

**SCRIPT:**
> "Welcome to the live demonstration. This is where theory meets practice.

> In this video, I'm going to run our Single Cell RNA-seq Quality Control skill using real bone marrow data. No simulated results. No pre-recorded outputs. Everything you see happens in real time.

> By the end, you'll understand exactly how this skill works and what it produces.

> Let's begin."

---

### SCENE 2: DATASET INTRODUCTION (0:45 - 2:30)
**[VISUAL: Terminal showing file structure]**

**SCRIPT:**
> "First, let me introduce the data we're working with.

```bash
cd /home/drdx/ARTIFICIALINTELLIGENCEGROUP/skills/test_demonstration
ls -la scRNAsedata/
```

**[VISUAL: Show three sample folders]**

> "We have three bone marrow samples from GEO dataset GSE136112. These are publicly available samples from a published study.

> Let me show you what's inside one sample:

```bash
ls -la scRNAsedata/GSM3901485/
```

**[VISUAL: Show files]**

> "This is standard 10X Genomics output format:

> **matrix.mtx** - A sparse matrix containing gene expression counts. Rows are genes, columns are cells, values are UMI counts.

> **genes.tsv** - Maps row indices to gene names. Contains Ensembl IDs and gene symbols.

> **barcodes.tsv** - Maps column indices to cell barcodes. Each barcode represents one cell.

**[VISUAL: Show file sizes]**

> "These aren't toy files. The matrix file alone contains millions of data points. This is production-scale data.

> Let me quickly verify the dimensions:

```python
python3 -c "
import scanpy as sc
adata = sc.read_10x_mtx('scRNAsedata/GSM3901485/')
print(f'Cells: {adata.n_obs}')
print(f'Genes: {adata.n_vars}')
"
```

**[VISUAL: Show output]**

> "We're looking at thousands of cells and over 30,000 genes per sample. Real experimental data."

---

### SCENE 3: SKILL OVERVIEW (2:30 - 4:00)
**[VISUAL: Show skill README or prompt]**

**SCRIPT:**
> "Before running the analysis, let me explain what this QC skill actually does.

> Single-cell RNA sequencing generates data from individual cells, but not every detected 'cell' is actually a healthy, intact cell. Some are:

**[VISUAL: Diagram or bullet points]**

> - **Empty droplets** - beads that captured very few transcripts
> - **Dying cells** - cells with damaged membranes leaking cytoplasmic RNA
> - **Doublets** - two cells captured in one droplet
> - **Low-quality cells** - cells with too few genes detected

> Our QC skill identifies and removes these problematic observations. It calculates key metrics:

> **Total counts** - How many UMIs were detected per cell
> **Genes by counts** - How many unique genes were detected
> **Mitochondrial percentage** - What fraction of reads map to mitochondrial genes (high values indicate dying cells)

> It then uses MAD-based filtering - Median Absolute Deviation - a robust statistical method that identifies outliers without being skewed by extreme values.

> Let's see it in action."

---

### SCENE 4: INVOKING THE SKILL (4:00 - 7:00)
**[VISUAL: Claude interface]**

**SCRIPT:**
> "Now I'll invoke the skill through Claude. Watch what happens.

**[VISUAL: Type or paste prompt into Claude]**

> "I'm asking Claude to perform single-cell RNA-seq quality control analysis on our bone marrow sample.

**[Read/paraphrase the prompt you're using]**

**[VISUAL: Claude responding in real-time]**

> "Claude is now executing the skill. Let me narrate what's happening:

> First, it's loading the data using scanpy's read_10x_mtx function.

> Now it's calculating QC metrics - total counts, genes detected, mitochondrial percentage for each cell.

> It's computing summary statistics and determining filtering thresholds using the MAD approach.

**[VISUAL: Show progress/output]**

> "The filtering step is removing cells that fall outside acceptable ranges.

> And now it's generating visualizations...

**[VISUAL: Claude completing the response]**

> "The analysis is complete. Let me show you the results."

---

### SCENE 5: RESULTS WALKTHROUGH (7:00 - 10:30)
**[VISUAL: Open qc_results folder]**

**SCRIPT:**
> "Let's examine what the skill produced.

```bash
ls -la qc_results/
```

**[VISUAL: List output files]**

> "We have several outputs:

**[VISUAL: Open qc_metrics_before_filtering.png]**

> "First, the **before filtering** visualization. This shows the distribution of our QC metrics across all cells in the raw data.

> Look at this histogram of mitochondrial percentage. See that tail extending to the right? Those are dying cells with 30, 40, even 50 percent mitochondrial content. Healthy cells typically have under 10-15 percent.

> This scatter plot shows total counts versus genes detected. That cloud in the lower left? Empty droplets and low-quality cells.

**[VISUAL: Open qc_metrics_after_filtering.png]**

> "Now the **after filtering** visualization.

> Notice the difference. The distributions are much tighter. We've removed:
> - Cells with very low gene counts (empty droplets)
> - Cells with very high mitochondrial percentage (dying cells)
> - Outliers in total count distribution (potential doublets)

**[VISUAL: Open qc_filtering_thresholds.png]**

> "This plot shows exactly where the thresholds were set. The red lines indicate our cutoffs.

> The skill used MAD-based detection, which adapts to the data distribution. It's not arbitrary. It's statistically grounded.

**[VISUAL: Show filtered h5ad file]**

> "Finally, we have the filtered dataset saved as an h5ad file - the standard format for the scverse ecosystem. This is ready for downstream analysis - clustering, trajectory inference, differential expression."

---

### SCENE 6: INTERPRETING THE OUTPUT (10:30 - 12:30)
**[VISUAL: Show summary statistics or Claude's report]**

**SCRIPT:**
> "Let me put these results in biological context.

**[VISUAL: Before/after comparison side by side]**

> "We started with [X] cells. After filtering, we retained [Y] cells. That's [Z] percent passing quality control.

> Is that good? For bone marrow samples, yes. Bone marrow has high cellular diversity and some fragile cell populations. Losing 10-20 percent to QC is typical.

> What would concern me:
> - Losing more than 30 percent - suggests sample handling issues
> - Very high mitochondrial percentages across the board - suggests delayed processing
> - Bimodal distributions - suggests batch effects or mixed samples

**[VISUAL: Point to clean distributions in after plot]**

> "What we see here is a clean dataset. Unimodal distributions. Reasonable filtering rates. No red flags.

> This data is ready for biological analysis."

---

### SCENE 7: PLATFORM PORTABILITY (12:30 - 13:30)
**[VISUAL: Show USDL file or adapter code briefly]**

**SCRIPT:**
> "Here's the crucial point I want you to remember:

> Everything you just saw - the analysis, the visualizations, the statistical filtering - works identically on other platforms.

> I demonstrated with Claude, but the same USDL skill definition can be converted to:
> - OpenAI's GPT-4
> - Google's Gemini
> - A local LLM through our BioKernel

> The prompts adapt. The output format adjusts. But the science stays the same.

> That's the power of platform-agnostic skills."

---

### SCENE 8: CLOSING (13:30 - 14:30)
**[VISUAL: Return to terminal/GitHub]**

**SCRIPT:**
> "You've now seen the complete workflow:
> - Real 10X Genomics data loaded
> - QC metrics calculated
> - Outliers detected with MAD-based methods
> - Publication-ready visualizations generated
> - Filtered dataset saved for downstream analysis

> All through a single skill invocation.

> In the next video, I'll show you how this skill is defined in USDL and how our adapters convert it for different platforms.

> If you want to try this yourself, the data and scripts are in the test_demonstration folder on GitHub.

> See you in Video 4."

**[VISUAL: End card with GitHub URL]**

---

### VIDEO 3 RECORDING NOTES:

**Before Recording:**
- Verify all commands work
- Pre-generate outputs as backup (but run live)
- Have Claude ready with the skill loaded
- Test screen recording captures both terminal and Claude

**During Recording:**
- Pause briefly when showing visualizations
- Point cursor to relevant areas of plots
- Read numbers from actual output, don't guess
- If something fails, explain and troubleshoot (authenticity)

**Backup Plan:**
- If live demo fails, have pre-recorded segment ready
- Keep qc_results/ outputs for showing even if generation fails
