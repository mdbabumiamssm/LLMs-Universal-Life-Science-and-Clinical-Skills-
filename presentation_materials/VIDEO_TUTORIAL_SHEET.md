# Video Tutorial Run Sheet & Script

**Project:** Universal Biomedical Skills Platform
**Total Estimated Duration:** 15-20 Minutes (Combined)

---

## MODULE 1: INTRODUCTION (Slides 1.1 - 1.9)
**Goal:** Hook the viewer and explain the "Why".

| Time | Visual | Action | Key Speaking Points |
|------|--------|--------|---------------------|
| 0:00 | Face/Camera | Talking Head | "Hi, I'm [Name]. Today I'm sharing a solution to a huge problem in Biomedical AI: Fragmentation." |
| 0:30 | Slide 1.3 | Screen | "We have Claude, Gemini, GPT-4. Rewriting skills for each is a waste of time." |
| 1:00 | Slide 1.5 | Screen | **"Introducing the Universal Biomedical Skills Platform."** Explain the diagram: One Skill, Every LLM. |
| 1:30 | Slide 1.9 | Screen | "Everything I'm showing today is Open Source. Let's dive in." |

---

## MODULE 2: REPOSITORY TOUR (Slides 2.1 - 2.5)
**Goal:** Orient the user in the codebase.

| Time | Visual | Action | Key Speaking Points |
|------|--------|--------|---------------------|
| 0:00 | Browser | Show GitHub | "Here is the repository. Structure is key." |
| 0:30 | VS Code | Open Explorer | "Three main folders: `Skills` (the core logic), `platform_prototype` (the SDK), and `test_demonstration`." |
| 1:00 | VS Code | Open `Skills/Genomics/single_cell_qc` | "Look at this. A standard structure: README, prompt, and code. Clean and modular." |

---

## MODULE 3: LIVE DEMO - scRNA-seq QC (Slides 3.1 - 3.9)
**Goal:** Prove it works with real data. **CRITICAL SECTION**

| Time | Visual | Action | Key Speaking Points |
|------|--------|--------|---------------------|
| 0:00 | Slide 3.2 | Screen | "We're using real bone marrow data (GSE136112), not synthetic noise. 10X Genomics format." |
| 0:30 | Terminal | `ls -F test_demonstration/scRNAsedata/` | "Here are our samples: GSM3901485_BM1, etc." |
| 0:45 | Terminal | `cd test_demonstration` | "Let's run the Quality Control skill." |
| 1:00 | Terminal | **RUN COMMAND:**<br>`python3 qc_analysis.py scRNAsedata/GSM3901485_BM1` | "I'm pointing the tool at the raw data directory. It handles loading, metric calc, and filtering automatically." |
| 1:15 | Terminal | Watch Output | "Watch the logs. [Read logs: 'Loading data...', 'Calculating metrics...']. It's using MAD-based outlier detection." |
| 1:45 | VS Code | Open `qc_results` folder | "Done. Let's look at the results." |
| 2:00 | Image Viewer | Open `qc_metrics_before.png` | "Here's the data *before* filtering. See those high mitochondrial spikes? Dying cells." |
| 2:15 | Image Viewer | Open `qc_metrics_after.png` | "And *after*. Clean, tight distributions. Ready for analysis." |
| 2:30 | Slide 3.9 | Screen | "The best part? This same logic runs on Claude or Gemini via our adapters." |

*Note: Ensure `qc_analysis.py` is updated to read the directory input before recording.*

---

## MODULE 4: THE PAPER & SCIENCE (Slides 7.1 - 7.10)
**Goal:** Establish academic credibility.

| Time | Visual | Action | Key Speaking Points |
|------|--------|--------|---------------------|
| 0:00 | Slide 7.1 | Screen | "We've documented the methodology in our paper: 'A Platform-Agnostic Framework...'" |
| 0:45 | Slide 7.5 | Screen | "Validation is crucial. We tested 6 skills across 3 platforms." |
| 1:15 | Slide 7.6 | Screen | "We found 94% semantic consistency. The science holds up regardless of the LLM." |

---

## MODULE 5: CONCLUSION & COMMUNITY (Slides 8.1 - 8.9)
**Goal:** Drive engagement.

| Time | Visual | Action | Key Speaking Points |
|------|--------|--------|---------------------|
| 0:00 | Slide 8.4 | Screen | "Want to add a skill? It's easy. Copy the template, define capabilities, validate." |
| 0:45 | Browser | GitHub Issues | "Join us. Fork the repo, submit a PR. Let's build the standard for Biomedical AI together." |
| 1:00 | Camera | Wave/Smile | "Check the link in the description. Thanks for watching." |

---
**End of Sheet**
