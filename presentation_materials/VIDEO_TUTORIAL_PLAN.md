# Universal Biomedical Skills - Video Tutorial Production Plan

## 1. Executive Summary
This document outlines the production strategy for a comprehensive video tutorial series (or single long-form walkthrough) showcasing the **Universal Biomedical Skills Platform**. The goal is to demonstrate novelty, technical robustness (live demo), and community value (GitHub sharing).

**Target Audience:** Researchers, Bioinformaticians, and LLM Developers.
**Key Message:** "Write once, deploy everywhere" - a unified standard for biomedical AI.

## 2. Production Strategy

### Format Options
*   **Option A: The Series (Recommended)** - 8 distinct, short videos (3-5 mins each) as outlined in the slides. Easier to consume and share specific parts.
*   **Option B: The Masterclass** - One continuous 20-30 minute video with chapter markers.
    *   *Recommendation:* Record as distinct modules (Option A). You can stitch them together later if desired.

### Core Narrative Arc
1.  **The Hook:** The problem of platform fragmentation.
2.  **The Solution:** USDL & BioKernel.
3.  **The Proof:** Live demo on real data (scRNA-seq).
4.  **The Depth:** Research paper & validation.
5.  **The Ask:** Contribute on GitHub.

## 3. Preparation Checklist

### Environment Setup
- [ ] **Clean Desktop:** Hide unrelated icons. Use a neutral wallpaper.
- [ ] **Terminal:** Set font size to 14-16pt (e.g., JetBrains Mono). Use a clean prompt (e.g., `user@biokernel:~$`).
- [ ] **VS Code:** Open the project root. Close all tabs except relevant ones (`README.md`, `qc_analysis.py`).
- [ ] **Browser:** Open tabs for:
    -   GitHub Repository (Draft/Private or Public URL)
    -   Claude/ChatGPT/Gemini interfaces (if showing comparison)
    -   Presentation Slides (Preview mode)

### Data Prep
- [ ] **Real Data Check:** Ensure `scRNAsedata/GSM3901485_BM1` is accessible.
- [ ] **Code Update:** Ensure `qc_analysis.py` supports reading standard 10X directories (MTX format) or convert data to `.h5ad` beforehand.
- [ ] **Pre-run:** Run the demo once off-camera to ensure no library errors occur.

## 4. Recording Sequence (Optimized)

Record in this order to build confidence:

1.  **Video 3: Live Demo** (Most technical, get it right first).
2.  **Video 2: Repo Tour** (Screen sharing, low stress).
3.  **Video 6: Skills Overview** (Slides/Static content).
4.  **Video 7: Research Paper** (Academic presentation).
5.  **Video 1: Intro & Vision** (High energy, requires "freshness").
6.  **Videos 4, 5, 8** (Remaining technical/community details).

## 5. Post-Production Notes
-   **Zooming:** Zoom in on code blocks during editing (200% scale).
-   **Callouts:** Add arrows/boxes when mentioning specific file names.
-   **Audio:** Remove keyboard typing sounds if distracting.
-   **Chapters:** If combining, add timestamps in the YouTube description.
