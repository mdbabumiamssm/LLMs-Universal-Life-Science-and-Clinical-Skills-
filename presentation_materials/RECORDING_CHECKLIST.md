# Recording Checklist & Cue Cards
## Universal Biomedical Skills Video Tutorial Series

---

## PRE-RECORDING CHECKLIST

### Technical Setup (Complete Before Recording)

#### Hardware
- [ ] External microphone connected and tested
- [ ] Webcam positioned (if using picture-in-picture)
- [ ] Good lighting on face (no backlighting)
- [ ] Quiet environment (no background noise)
- [ ] Phone on silent/Do Not Disturb

#### Software
- [ ] OBS Studio installed and configured
- [ ] Screen resolution set to 1920x1080
- [ ] Recording at 30fps minimum
- [ ] Audio levels tested (-12dB to -6dB peak)
- [ ] Hotkeys configured (Start/Stop recording)

#### Screen Layout
```
┌────────────────────────────────────────┐
│                                        │
│     Terminal/Code Editor (60%)         │
│                                        │
├────────────────────────┬───────────────┤
│                        │   Browser/    │
│                        │   Claude      │
│                        │   (40%)       │
│                        │               │
│                        │  ┌─────────┐  │
│                        │  │ Webcam  │  │
│                        │  │ (opt)   │  │
│                        │  └─────────┘  │
└────────────────────────┴───────────────┘
```

#### Terminal Setup
- [ ] Font size: 16-18pt (readable on video)
- [ ] Dark theme with high contrast
- [ ] Shell prompt clean and short
- [ ] Working directory set correctly
- [ ] Command history cleared

#### Browser Setup
- [ ] GitHub signed in
- [ ] Claude/ChatGPT signed in
- [ ] Bookmarks bar hidden
- [ ] Extensions hidden
- [ ] Zoom level: 100-110%

---

## DEMO VERIFICATION (Run Before Each Recording)

### Verify Data Exists
```bash
# Check test demonstration folder
ls -la /home/drdx/ARTIFICIALINTELLIGENCEGROUP/skills/test_demonstration/

# Check scRNA data
ls -la /home/drdx/ARTIFICIALINTELLIGENCEGROUP/skills/test_demonstration/scRNAsedata/

# Check QC results exist
ls -la /home/drdx/ARTIFICIALINTELLIGENCEGROUP/skills/test_demonstration/qc_results/
```

### Verify Python Environment
```bash
# Activate virtual environment
cd /home/drdx/ARTIFICIALINTELLIGENCEGROUP/skills/test_demonstration
source venv/bin/activate

# Test imports
python3 -c "import scanpy; import anndata; print('Ready!')"
```

### Quick Demo Test
```bash
# Run QC analysis to verify everything works
python3 qc_analysis.py test_input.h5ad
```

---

## CUE CARDS BY VIDEO

---

### VIDEO 1: Introduction & Vision (8-10 min)

#### Opening Hook (30 sec)
```
"What if you could write a biomedical AI skill once...
and have it work on Claude, ChatGPT, Gemini, AND your local LLM?"
```

#### Key Points to Hit
1. The fragmentation problem (4-8 hours to rewrite skills)
2. Three innovations: USDL, Adapters, BioKernel
3. Demo teaser (show QC plots briefly)
4. Six skills across three domains
5. Call to action: GitHub URL

#### Closing Line
```
"If you're working in biomedical AI and tired of platform fragmentation,
this is for you. Let's get started."
```

---

### VIDEO 2: GitHub Repository Tour (6-8 min)

#### Commands to Run
```bash
# Navigate to repository
cd /home/drdx/ARTIFICIALINTELLIGENCEGROUP/skills/Universal-Life-Science-and-Clinical-Skills-

# Show structure
ls -la

# Show skills folder
ls Skills/

# Show a skill's contents
ls Skills/Genomics/single_cell_qc/

# Show test demonstration
ls test_demonstration/
ls test_demonstration/scRNAsedata/
```

#### Key Points to Hit
1. Four main areas: Skills/, test_demonstration/, platform_prototype/, docs
2. Each skill has: README.md, prompt.md, implementation code
3. Real data in scRNAsedata/ (not synthetic)
4. Quick start: clone, install, run

#### Closing Line
```
"You now know your way around the repository.
In the next video, I'll walk through a complete live demonstration."
```

---

### VIDEO 3: Live Demo (12-15 min)

#### Commands Sequence
```bash
# 1. Show data location
cd /home/drdx/ARTIFICIALINTELLIGENCEGROUP/skills/test_demonstration
ls -la scRNAsedata/

# 2. Show one sample's contents
ls -la scRNAsedata/GSM3901485_BM1/

# 3. Activate environment
source venv/bin/activate

# 4. Quick data check
python3 -c "
import scanpy as sc
adata = sc.read_10x_mtx('scRNAsedata/GSM3901485_BM1/')
print(f'Cells: {adata.n_obs}')
print(f'Genes: {adata.n_vars}')
"

# 5. Run QC analysis (or invoke through Claude)
python3 qc_analysis.py test_input.h5ad

# 6. Show results
ls qc_results/
```

#### Key Points to Hit
1. Real data from GSE136112 (bone marrow)
2. 10X Genomics format explained
3. QC metrics: total_counts, n_genes, pct_mt
4. MAD-based filtering
5. Before/after comparison
6. Same skill works on all platforms

#### Closing Line
```
"You've now seen the complete workflow. All through a single skill invocation.
In the next video, I'll show you how this skill is defined in USDL."
```

---

### VIDEO 4: USDL & Adapters (10-12 min)

#### Commands/Files to Show
```bash
# Show USDL example
cd /home/drdx/ARTIFICIALINTELLIGENCEGROUP/skills/platform_prototype
cat examples/single_cell_qc.yaml | head -50

# Show adapter
cat adapters/claude_adapter.py | head -30

# Build for Claude
python cli.py build --platform claude examples/single_cell_qc.yaml

# Build for OpenAI
python cli.py build --platform openai examples/single_cell_qc.yaml
```

#### Key Points to Hit
1. Problem: Same skill, three different formats
2. USDL structure: metadata, capabilities, prompts, platforms
3. Adapters: automatic conversion
4. Same input → different outputs → same results
5. Validation catches errors early

#### Closing Line
```
"Same skill. Same capabilities. Different platform packaging.
That's the power of platform-agnostic skills."
```

---

### VIDEO 5: Platform Prototype SDK (10-12 min)

#### Commands to Show
```bash
cd /home/drdx/ARTIFICIALINTELLIGENCEGROUP/skills/platform_prototype

# Show structure
ls -la

# Show CLI help
python cli.py --help

# Validate
python cli.py validate examples/single_cell_qc.yaml

# Build
python cli.py build --platform claude examples/single_cell_qc.yaml

# Show BioKernel
cat biokernel/server.py | head -40
```

#### Key Points to Hit
1. Six CLI commands: validate, build, optimize, test, serve, compare
2. BioKernel: intelligent routing, code execution, dual API
3. Optimizer: AI-powered prompt tuning
4. Evaluator: cross-platform testing
5. Creating a new skill from template

#### Closing Line
```
"The Platform Prototype SDK gives you everything you need
to build and deploy biomedical AI skills."
```

---

### VIDEO 6: All Six Skills (15-18 min)

#### Structure
- 2-3 minutes per skill
- Show README for each
- Highlight key capability
- Show example input/output

#### Skills Order
1. Clinical Note Summarization → SOAP format
2. Trial Eligibility Agent → patient matching
3. scRNA-seq QC → quality control (quick recap)
4. CRISPR Design Agent → guide RNA design
5. Chemical Property Lookup → RDKit calculations
6. AgentD Drug Discovery → multi-step pipeline

#### Closing Line
```
"Six skills. Three domains. All platform-agnostic.
And the collection is growing. Contributions welcome!"
```

---

### VIDEO 7: Research Paper (12-15 min)

#### Key Sections
1. Abstract (2 min)
2. Problem statement (2 min)
3. Methods: USDL, Adapters, BioKernel (3 min)
4. Results: cross-platform validation (3 min)
5. Discussion: implications, limitations (2 min)
6. Conclusion (1 min)

#### Key Stats to Mention
- Performance variance < 5% for 5/6 skills
- 94.2% outputs semantically equivalent
- scRNA-seq QC: ~10% filter rate (consistent with literature)

#### Closing Line
```
"The fragmentation problem is solvable.
The science shouldn't depend on which vendor you choose."
```

---

### VIDEO 8: Contributing & Community (6-8 min)

#### Contribution Workflow
1. Fork → Clone → Branch → Develop → Commit → PR

#### Adding a Skill
```bash
# Copy template
cp examples/template.yaml Skills/Domain/my_skill.yaml

# Edit with your skill definition
# Then validate
python cli.py validate Skills/Domain/my_skill.yaml
```

#### Call to Action
```
"Here's what I'd love you to do right now:
1. Star the repository on GitHub
2. Try the demo with your own data
3. Share with colleagues who might benefit
4. Consider contributing a skill from your domain"
```

#### Final Line
```
"The goal of this project is simple: make biomedical AI
accessible to everyone, regardless of which platform they use.
Together, we can build something that truly serves the research community.
See you on GitHub."
```

---

## RECORDING TIPS

### Speaking
- Speak clearly and at moderate pace
- Pause after key points (1-2 seconds)
- Don't rush through commands
- Explain what you're doing before doing it

### Screen Recording
- Move cursor slowly and deliberately
- Highlight important areas by hovering
- Give viewers time to read code/output
- Don't scroll too fast

### Mistakes
- If you make a minor mistake, keep going
- If major error, pause, fix, explain briefly
- Authenticity is okay - shows real-world usage

### Energy
- Start each video with energy
- Maintain enthusiasm throughout
- End with clear call to action

---

## POST-RECORDING CHECKLIST

### Immediately After
- [ ] Watch recording to verify quality
- [ ] Check audio levels throughout
- [ ] Note timestamps for any needed edits

### Editing
- [ ] Trim beginning/end silence
- [ ] Add intro/outro slides
- [ ] Add chapter markers
- [ ] Blur any sensitive information
- [ ] Add captions (recommended)

### Upload
- [ ] Write title (include "Universal Biomedical Skills")
- [ ] Write description with timestamps
- [ ] Add tags: bioinformatics, AI, LLM, scRNA-seq, etc.
- [ ] Create custom thumbnail
- [ ] Add to playlist
- [ ] Add end screen with subscribe/next video

---

## TIMESTAMPS TEMPLATE

```
0:00 - Introduction
0:30 - [First major section]
2:00 - [Second major section]
...
```

---

## EMERGENCY BACKUP

If live demo fails during recording:

1. Keep calm, acknowledge briefly
2. Switch to pre-generated results in qc_results/
3. Explain: "Let me show you what the output looks like"
4. Continue with interpretation

Pre-generated files are always available:
```
test_demonstration/qc_results/
├── qc_metrics_before_filtering.png
├── qc_metrics_after_filtering.png
├── qc_filtering_thresholds.png
└── test_input_filtered.h5ad
```

---

**Good luck with the recording!**
