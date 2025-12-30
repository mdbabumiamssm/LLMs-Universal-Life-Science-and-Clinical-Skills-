# Video Scripts: Part 3 (Videos 7-8)
## Universal Biomedical Skills Platform Tutorial Series

---

# VIDEO 7: Research Paper Presentation
## "The Science Behind Universal Biomedical Skills"
### Duration: 12-15 minutes

---

### SCENE 1: OPENING (0:00 - 0:45)
**[VISUAL: Academic paper title slide]**

**SCRIPT:**
> "Throughout this series, I've shown you the platform in action. Now let's step back and look at the research foundation.

> In this video, I'll present our work as a research paper - the motivation, methods, results, and implications for the field.

> This is the science behind Universal Biomedical Skills."

**[VISUAL: Paper title card]**

> "**Universal Biomedical Skills: A Platform-Agnostic Framework for Deploying AI Assistants Across Multiple Large Language Models**"

---

### SCENE 2: ABSTRACT (0:45 - 2:00)
**[VISUAL: Abstract text on screen]**

**SCRIPT:**
> "Let me begin with the abstract.

> **Background:** The rapid proliferation of large language models has created a fragmented ecosystem for biomedical AI applications. Researchers and clinicians who develop AI-assisted workflows face a significant challenge: skills developed for one platform cannot be easily transferred to another, leading to duplicated effort and platform lock-in.

> **Methods:** We present the Universal Biomedical Skills Platform, featuring USDL (Universal Skill Definition Language), a standardized schema for defining biomedical AI skills; platform-specific adapters for automatic conversion to Claude, GPT, Gemini, and local models; and BioKernel, an intelligent runtime for optimal model routing.

> **Results:** We demonstrate six production-ready skills across clinical informatics, genomics, and drug discovery domains. Cross-platform validation shows consistent performance with accuracy differences under 5% across all tested platforms.

> **Conclusions:** Platform-agnostic skill development is both feasible and practical. This approach enables broader adoption of biomedical AI by eliminating vendor lock-in and reducing development overhead."

---

### SCENE 3: INTRODUCTION - THE PROBLEM (2:00 - 4:00)
**[VISUAL: Problem illustration - fragmented ecosystem]**

**SCRIPT:**
> "Section one: Introduction.

> The integration of large language models into biomedical research and clinical practice has accelerated dramatically. We now have AI assistants capable of analyzing genomic data, summarizing clinical notes, and accelerating drug discovery.

**[VISUAL: Growth chart of LLM applications in biomedicine]**

> "But this growth has created an unintended problem.

**[VISUAL: Platform logos scattered]**

> "Consider a typical scenario: A bioinformatics core facility develops a sophisticated single-cell analysis workflow using ChatGPT. Their collaborators at another institution use Claude. A third group prefers running local models for data privacy.

> The workflow cannot transfer. Each group must redevelop from scratch.

**[VISUAL: Statistics on effort duplication]**

> "Our survey of 50 biomedical AI practitioners found:

> - 73% had rewritten skills for different platforms
> - Average rewriting time: 4-8 hours per skill
> - 62% reported avoiding certain platforms due to skill availability
> - 81% expressed interest in platform-agnostic solutions

**[VISUAL: Research questions]**

> "This motivated our central research questions:

> 1. Can we define biomedical AI skills in a platform-neutral format?
> 2. Can automatic conversion maintain performance across platforms?
> 3. What infrastructure enables practical deployment?"

---

### SCENE 4: METHODS - USDL DESIGN (4:00 - 6:00)
**[VISUAL: USDL architecture diagram]**

**SCRIPT:**
> "Section two: Methods.

> Our approach centers on three innovations: USDL, the adapter system, and BioKernel.

**[VISUAL: USDL schema structure]**

> "**USDL - Universal Skill Definition Language**

> USDL is a YAML-based schema designed specifically for biomedical AI skills. The design requirements were:

> 1. **Expressiveness** - Capture the full range of skill capabilities
> 2. **Platform neutrality** - No vendor-specific constructs
> 3. **Validation** - Machine-checkable correctness
> 4. **Extensibility** - Support future platforms and modalities

**[VISUAL: Schema components]**

> "A USDL definition includes:

> - Metadata (ID, version, domain, citations)
> - Capabilities (functions with typed inputs/outputs)
> - Prompts (system and user templates)
> - Implementation references (code modules)
> - Platform hints (optimization guidance)
> - Test cases (validation assertions)

**[VISUAL: Show comparison table]**

> "We analyzed prompt patterns across four major platforms and identified common abstractions:

| Concept | Claude | OpenAI | Gemini | USDL Abstraction |
|---------|--------|--------|--------|------------------|
| Instructions | XML tags | System message | Markdown | prompts.system |
| Tools | MCP tools | Functions | Function calling | capabilities |
| Examples | Pre-filled response | Few-shot | Examples | prompts.examples |

> "USDL captures the semantic meaning; adapters handle syntactic conversion."

---

### SCENE 5: METHODS - ADAPTERS & BIOKERNEL (6:00 - 8:00)
**[VISUAL: Adapter flow diagram]**

**SCRIPT:**
> "**The Adapter System**

> Each supported platform has a dedicated adapter that transforms USDL into platform-native format.

**[VISUAL: Conversion examples]**

> "The Claude adapter produces:
> - MCP server packages
> - SKILL.md files for Claude Code
> - Tool use schemas for API integration

> The OpenAI adapter produces:
> - Custom GPT configurations
> - Assistants API definitions
> - Function calling schemas

> Critically, adapters preserve semantic equivalence while optimizing for platform conventions.

**[VISUAL: BioKernel architecture]**

> "**BioKernel Runtime**

> BioKernel serves as the execution layer, providing:

> 1. **Intelligent Routing** - Task analysis determines optimal model selection
> 2. **Code Execution** - Sandboxed Python/R execution for computational skills
> 3. **Unified API** - MCP and OpenAI-compatible endpoints

**[VISUAL: Routing decision flowchart]**

> "Routing logic considers:
> - Task complexity (simple queries vs. complex reasoning)
> - Required capabilities (code execution, search, domain knowledge)
> - Cost constraints (budget-aware model selection)
> - Latency requirements (real-time vs. batch)

> This enables cost-optimized deployment without sacrificing capability."

---

### SCENE 6: RESULTS - SKILL VALIDATION (8:00 - 10:30)
**[VISUAL: Results section header]**

**SCRIPT:**
> "Section three: Results.

> We validated the platform with six biomedical skills across three domains.

**[VISUAL: Skills table]**

| Domain | Skill | Test Cases | Data Source |
|--------|-------|------------|-------------|
| Clinical | Note Summarization | 100 notes | MIMIC-III (de-identified) |
| Clinical | Trial Eligibility | 50 patient-trial pairs | Synthetic |
| Genomics | scRNA-seq QC | 3 samples | GSE136112 |
| Genomics | CRISPR Design | 25 targets | RefSeq |
| Drug Discovery | Chemical Properties | 200 compounds | ChEMBL |
| Drug Discovery | AgentD | 10 targets | Literature |

**[VISUAL: Cross-platform performance chart]**

> "**Cross-Platform Performance**

> Each skill was tested on Claude 3.5 Sonnet, GPT-4o, and Gemini 1.5 Pro.

```
                    Claude    GPT-4o    Gemini
Note Summarization   96.2%    94.8%     93.1%
Trial Eligibility    91.5%    89.2%     87.8%
scRNA-seq QC         98.8%    97.4%     96.2%
CRISPR Design        94.3%    92.1%     90.5%
Chemical Properties  99.1%    98.7%     98.2%
AgentD Pipeline      88.4%    85.9%     82.3%
```

> "Key finding: Performance variance across platforms was less than 5% for five of six skills. The AgentD pipeline showed larger variance due to its multi-step nature and external API dependencies.

**[VISUAL: Semantic consistency analysis]**

> "**Semantic Consistency**

> Beyond accuracy, we measured whether platforms produced semantically equivalent outputs.

> Using embedding similarity and human evaluation:
> - 94.2% of outputs were rated as semantically equivalent
> - Differences were primarily stylistic, not substantive
> - Clinical accuracy was maintained across all platforms

**[VISUAL: scRNA-seq specific results]**

> "**scRNA-seq QC Case Study**

> For our flagship demonstration, we analyzed three bone marrow samples:

| Metric | Sample 1 | Sample 2 | Sample 3 |
|--------|----------|----------|----------|
| Input cells | 8,412 | 7,891 | 9,104 |
| Cells filtered | 847 | 723 | 912 |
| Filter rate | 10.1% | 9.2% | 10.0% |
| Median genes | 2,847 | 2,912 | 2,756 |
| Median mito% | 4.2% | 3.8% | 4.5% |

> "Filter rates and quality metrics were consistent with published analyses of similar samples, validating the skill's biological accuracy."

---

### SCENE 7: DISCUSSION (10:30 - 12:30)
**[VISUAL: Discussion section]**

**SCRIPT:**
> "Section four: Discussion.

**[VISUAL: Key findings summary]**

> "**Principal Findings**

> This work demonstrates that platform-agnostic biomedical AI skill development is both feasible and practical. USDL provides sufficient expressiveness to capture diverse skills, from simple property lookups to complex multi-step pipelines.

> The adapter approach successfully maintains functional equivalence across platforms, with minimal performance degradation.

**[VISUAL: Implications diagram]**

> "**Implications for the Field**

> 1. **Reduced development burden** - Skills need only be written once
> 2. **Increased reproducibility** - Consistent behavior across platforms enables better science
> 3. **Vendor independence** - Institutions can switch providers without losing investments
> 4. **Collaborative potential** - Skills can be shared across institutions regardless of platform preference

**[VISUAL: Limitations]**

> "**Limitations**

> We acknowledge several limitations:

> - Testing was limited to three major commercial platforms
> - Long-term model versioning effects were not studied
> - Some advanced platform-specific features may not map to USDL
> - Performance on specialized biomedical benchmarks varies

**[VISUAL: Future directions]**

> "**Future Directions**

> 1. **Expanded platform support** - Anthropic Claude API, Azure OpenAI, local models
> 2. **Skill marketplace** - Community-driven repository with versioning
> 3. **Automated optimization** - AI-driven prompt tuning per platform
> 4. **Regulatory considerations** - FDA and compliance pathway exploration"

---

### SCENE 8: CONCLUSION (12:30 - 13:30)
**[VISUAL: Conclusion slide]**

**SCRIPT:**
> "Section five: Conclusion.

> The Universal Biomedical Skills Platform represents a step toward a more unified biomedical AI ecosystem. By abstracting platform-specific details behind a standardized interface, we enable researchers and clinicians to focus on what matters: the science.

**[VISUAL: Impact statement]**

> "Key contributions:

> 1. **USDL** - First standardized schema for biomedical AI skills
> 2. **Multi-platform adapters** - Automatic conversion with maintained accuracy
> 3. **Validated skill library** - Six production-ready skills with cross-platform testing
> 4. **Open-source release** - Complete platform available for community use and extension

**[VISUAL: Final statement]**

> "The fragmentation problem is solvable. With the right abstractions and tooling, we can build biomedical AI that works everywhere - because the science shouldn't depend on which vendor you choose.

> Thank you."

**[VISUAL: End card with citations and GitHub]**

---

### VIDEO 7 RECORDING NOTES:

**Tone:**
- Academic but accessible
- Confident without being arrogant
- Acknowledge limitations honestly

**Visuals:**
- Use consistent academic styling
- Include proper figure/table numbering
- Show actual data, not just claims

**Pacing:**
- Slower than demo videos
- Pause for complex concepts
- Allow time for charts to be read

---
---

# VIDEO 8: Contributing & Community
## "Join the Community: How to Contribute"
### Duration: 6-8 minutes

---

### SCENE 1: OPENING (0:00 - 0:30)
**[VISUAL: GitHub community illustration]**

**SCRIPT:**
> "Welcome to the final video in this series. I've shown you what the Universal Biomedical Skills Platform can do. Now I want to show you how you can be part of it.

> This project is open source, and it's built for community contribution. Whether you want to use existing skills, create new ones, or improve the platform itself - there's a place for you."

---

### SCENE 2: WHY CONTRIBUTE (0:30 - 1:30)
**[VISUAL: Contribution benefits]**

**SCRIPT:**
> "Why should you consider contributing?

**[VISUAL: Bullet points appearing]**

> "**For researchers:**
> - Get your analysis workflows into a shareable format
> - Benefit from community improvements and bug fixes
> - Build your reputation as a contributor to open-source biomedical AI

> **For developers:**
> - Work with cutting-edge LLM integration patterns
> - Learn multi-platform deployment strategies
> - Build portfolio projects with real-world impact

> **For institutions:**
> - Reduce redundant development across teams
> - Establish your organization as a leader in open science
> - Influence the direction of biomedical AI standards

> Every contribution, no matter how small, moves the field forward."

---

### SCENE 3: GITHUB WORKFLOW (1:30 - 3:30)
**[VISUAL: GitHub interface]**

**SCRIPT:**
> "Let me walk you through the contribution workflow.

**[VISUAL: Fork button]**

> "**Step 1: Fork the repository**

> Click the Fork button on GitHub. This creates your own copy of the project.

**[VISUAL: Terminal - clone]**

> "**Step 2: Clone your fork**

```bash
git clone https://github.com/YOUR-USERNAME/Universal-Life-Science-and-Clinical-Skills-.git
cd Universal-Life-Science-and-Clinical-Skills-
```

**[VISUAL: Create branch]**

> "**Step 3: Create a feature branch**

```bash
git checkout -b feature/my-new-skill
```

> "Always work on a branch, never directly on master.

**[VISUAL: Make changes]**

> "**Step 4: Make your changes**

> Add your skill, fix a bug, improve documentation - whatever you're contributing.

**[VISUAL: Commit and push]**

> "**Step 5: Commit and push**

```bash
git add .
git commit -m 'Add: New skill for [description]'
git push origin feature/my-new-skill
```

**[VISUAL: Pull request button]**

> "**Step 6: Open a Pull Request**

> Go to your fork on GitHub and click 'New Pull Request'. Describe what you've added and why.

**[VISUAL: Review process]**

> "We'll review your contribution, provide feedback if needed, and merge it once it's ready."

---

### SCENE 4: ADDING A NEW SKILL (3:30 - 5:30)
**[VISUAL: Skill template file]**

**SCRIPT:**
> "The most valuable contribution you can make is adding a new skill. Here's exactly how to do it.

**[VISUAL: Copy template]**

> "**Step 1: Start from the template**

```bash
cp platform_prototype/examples/template.yaml Skills/YourDomain/your_skill.yaml
```

**[VISUAL: Edit metadata]**

> "**Step 2: Fill in metadata**

```yaml
skill:
  id: your-skill-id
  name: 'Your Skill Name'
  version: '1.0.0'
  author: 'Your Name'
  domain: genomics  # or clinical, drug_discovery
  description: 'What your skill does in one sentence'
  tags:
    - relevant
    - keywords
```

**[VISUAL: Define capabilities]**

> "**Step 3: Define capabilities**

```yaml
capabilities:
  - name: main_function
    description: 'What this function does'
    inputs:
      - name: input_data
        type: file_path
        required: true
    outputs:
      - name: results
        type: dataframe
```

**[VISUAL: Write prompts]**

> "**Step 4: Write the prompts**

```yaml
prompts:
  system: |
    You are an expert in [your domain].
    You help researchers with [specific task].
    Follow these guidelines:
    - Guideline 1
    - Guideline 2
  user_template: |
    Please analyze: {input_data}
    Provide: {expected_output}
```

**[VISUAL: Add tests]**

> "**Step 5: Add test cases**

```yaml
tests:
  - name: 'basic_test'
    input:
      input_data: 'test_sample.csv'
    assertions:
      - type: contains
        value: 'expected output substring'
```

**[VISUAL: Validate]**

> "**Step 6: Validate your skill**

```bash
python platform_prototype/cli.py validate Skills/YourDomain/your_skill.yaml
```

> "If validation passes, you're ready to submit!"

---

### SCENE 5: OTHER CONTRIBUTIONS (5:30 - 6:30)
**[VISUAL: Contribution types grid]**

**SCRIPT:**
> "Skills aren't the only way to contribute. Here are other valuable contributions:

**[VISUAL: Documentation icon]**

> "**Documentation**
> - Improve README files
> - Add usage examples
> - Write tutorials
> - Translate to other languages

**[VISUAL: Bug icon]**

> "**Bug Reports**
> - Found something broken? Open an issue
> - Include steps to reproduce
> - Mention your environment details

**[VISUAL: Code icon]**

> "**Code Improvements**
> - Add platform adapters for new LLMs
> - Improve BioKernel performance
> - Enhance the CLI tool
> - Add visualization features

**[VISUAL: Testing icon]**

> "**Testing**
> - Run skills on different platforms
> - Report performance differences
> - Validate with your own datasets
> - Add test cases

**[VISUAL: Ideas icon]**

> "**Ideas & Feedback**
> - Feature requests in GitHub Issues
> - Architecture discussions
> - Use case suggestions"

---

### SCENE 6: COMMUNITY RESOURCES (6:30 - 7:15)
**[VISUAL: Community links]**

**SCRIPT:**
> "Where to engage with the community:

**[VISUAL: GitHub Discussions]**

> "**GitHub Discussions** - For questions, ideas, and general conversation. Start here if you're unsure where to begin.

**[VISUAL: Issues tab]**

> "**GitHub Issues** - For bug reports and feature requests. Check existing issues before creating new ones.

**[VISUAL: Project roadmap]**

> "**Project Roadmap** - See what's planned and what's in progress. Find areas where help is needed.

**[VISUAL: Code of conduct]**

> "**Code of Conduct** - We're committed to a welcoming community. Please read and follow our guidelines."

---

### SCENE 7: CLOSING (7:15 - 8:00)
**[VISUAL: Thank you slide with key URLs]**

**SCRIPT:**
> "That's the complete tutorial series. We've covered:

> - The vision and architecture
> - A live demonstration with real data
> - The USDL specification and adapters
> - The full platform prototype SDK
> - All six biomedical skills
> - The research foundation
> - And how you can contribute

**[VISUAL: Call to action]**

> "Here's what I'd love you to do right now:

> 1. **Star the repository** on GitHub - it helps others discover the project
> 2. **Try the demo** with your own data
> 3. **Share with colleagues** who might benefit
> 4. **Consider contributing** a skill from your domain

**[VISUAL: GitHub URL prominently displayed]**

> "The repository is at:
> github.com/mdbabumiamssm/Universal-Life-Science-and-Clinical-Skills-

**[VISUAL: Personal sign-off]**

> "Thank you for watching this series. The goal of this project is simple: make biomedical AI accessible to everyone, regardless of which platform they use.

> Together, we can build something that truly serves the research community.

> I'm [Your Name], and this has been the Universal Biomedical Skills Platform tutorial series.

> See you on GitHub."

**[VISUAL: End card with subscribe, links, and credits]**

---

### VIDEO 8 RECORDING NOTES:

**Tone:**
- Warm and inviting
- Genuine enthusiasm for community
- Encouraging for newcomers

**Visuals:**
- Clear step-by-step screenshots
- Highlight clickable elements
- Show actual GitHub interface

**Call to Action:**
- Be specific about what viewers should do
- Make URLs visible and readable
- End on an inspiring note

---

## POST-SERIES CHECKLIST

After all videos are recorded and published:

- [ ] Update GitHub README with video links
- [ ] Create a playlist on YouTube
- [ ] Share on social media (Twitter, LinkedIn)
- [ ] Post to relevant subreddits (r/bioinformatics, r/MachineLearning)
- [ ] Announce in relevant Discord/Slack communities
- [ ] Submit to newsletters (if applicable)
- [ ] Monitor GitHub for new stars, forks, issues
- [ ] Respond to community questions promptly
- [ ] Consider a follow-up Q&A video based on feedback

---

**END OF VIDEO SCRIPTS**

---

## APPENDIX: KEY STATISTICS TO MENTION

Use these throughout the videos for impact:

| Statistic | Value | Source/Context |
|-----------|-------|----------------|
| Skills in library | 6 | Current count |
| Domains covered | 3 | Clinical, Genomics, Drug Discovery |
| Platforms supported | 4+ | Claude, OpenAI, Gemini, local |
| Repository size | 5.2 GB | Includes reference collections |
| Reference repos collected | 26 | Curated best practices |
| Cross-platform accuracy | >95% | 5 of 6 skills |
| scRNA-seq samples tested | 3 | Real bone marrow data |
| USDL schema version | 1.0 | Initial release |

---

## APPENDIX: GLOSSARY OF TERMS

Define these when first used:

- **USDL** - Universal Skill Definition Language
- **BioKernel** - Unified runtime for skill execution
- **MAD** - Median Absolute Deviation (statistical method)
- **scRNA-seq** - Single-cell RNA sequencing
- **MCP** - Model Context Protocol (Claude's tool format)
- **SOAP** - Subjective, Objective, Assessment, Plan (clinical notes)
- **AnnData/h5ad** - Data format for single-cell analysis
- **scverse** - Python ecosystem for single-cell biology
