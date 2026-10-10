"""Build the LinkedIn article as a formatted Word (.docx) document."""
import docx
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

OUT = ("/media/drdx/mystorage/ARTIFICIALINTELLIGENCEGROUP/skills/tests/"
       "scRNAseqdata/analysis_results/AI_Computational_Biologist_LinkedIn_Article.docx")

doc = docx.Document()
style = doc.styles["Normal"]
style.font.name = "Calibri"
style.font.size = Pt(11)


def add_hyperlink(paragraph, url, text):
    part = paragraph.part
    r_id = part.relate_to(
        url, docx.opc.constants.RELATIONSHIP_TYPE.HYPERLINK, is_external=True)
    hyperlink = OxmlElement("w:hyperlink")
    hyperlink.set(qn("r:id"), r_id)
    new_run = OxmlElement("w:r")
    rPr = OxmlElement("w:rPr")
    color = OxmlElement("w:color"); color.set(qn("w:val"), "1155CC"); rPr.append(color)
    u = OxmlElement("w:u"); u.set(qn("w:val"), "single"); rPr.append(u)
    new_run.append(rPr)
    t = OxmlElement("w:t"); t.text = text; new_run.append(t)
    hyperlink.append(new_run)
    paragraph._p.append(hyperlink)


def para(text="", bold=False, italic=False, size=11, align=None, space_after=6):
    p = doc.add_paragraph()
    if align:
        p.alignment = align
    if text:
        r = p.add_run(text); r.bold = bold; r.italic = italic; r.font.size = Pt(size)
    p.paragraph_format.space_after = Pt(space_after)
    return p


def runs(p, parts):
    """parts = list of (text, bold, italic)"""
    for text, b, i in parts:
        r = p.add_run(text); r.bold = b; r.italic = i
    return p


def label_link(label, url, link_text):
    p = doc.add_paragraph()
    p.add_run(label + " ").bold = True
    add_hyperlink(p, url, link_text)
    p.paragraph_format.space_after = Pt(6)
    return p


# ----------------------------------------------------------------- Title
t = doc.add_heading("AI Is the Computational Biologist", level=0)
sub = doc.add_paragraph()
sr = sub.add_run("A Reproducible, Cross-Language, Live Demonstration")
sr.italic = True; sr.font.size = Pt(14); sr.font.color.rgb = RGBColor(0x40, 0x40, 0x40)
sub.alignment = WD_ALIGN_PARAGRAPH.LEFT

p = doc.add_paragraph()
runs(p, [("Can an AI system independently reproduce a peer-reviewed computational "
          "biology paper — from raw data, in a different programming language, with "
          "no human writing the analysis code?", True, False)])
para("I set out to answer that question on camera. This is what happened.", italic=True)

doc.add_paragraph().add_run("―" * 30)

# ----------------------------------------------------------------- Backstory
doc.add_heading("Where this story begins", level=1)
para("A little over a year ago, I gave Luciano Martelotto the first live "
     "demonstration of my Biomedical Operating System — an agentic framework built "
     "on Skills + MCP (Model Context Protocol) + Agentic AI that performs "
     "end-to-end computational biology tasks. Work that takes a trained specialist "
     "weeks to months was completed, in front of him, in minutes.")
para("Since then, the ground has shifted dramatically under all of us working at "
     "the intersection of AI and biology. In subsequent conversations with the "
     "Anthropic Claude Code team and the OpenAI Codex team, both indicated interest "
     "in integrating my open framework:")
label_link("\U0001F517 LLMs — Universal Life-Science and Clinical Skills:",
           "https://github.com/mdbabumiamssm/LLMs-Universal-Life-Science-and-Clinical-Skills-",
           "github.com/mdbabumiamssm/LLMs-Universal-Life-Science-and-Clinical-Skills-")
para("But excitement is cheap. The field is full of impressive demos that quietly "
     "collapse the moment you ask for rigor. So I held my own system to the hardest "
     "standard I know.")

# ----------------------------------------------------------------- Reproducibility
doc.add_heading("The reproducibility problem — and why it's the right test", level=1)
para("Recently, Marija Cvijovic raised an important conversation around a Nature "
     "Portfolio (npj Digital Medicine) article on reproducibility in computational "
     "science:")
label_link("\U0001F517 Nature npj Digital Medicine:",
           "https://www.nature.com/articles/s41746-026-02777-1",
           "nature.com/articles/s41746-026-02777-1")
para("I agree with the premise wholeheartedly. Reproducibility is the currency of "
     "science. If AI is going to claim a seat at the computational biology bench, it "
     "cannot simply generate plausible-looking analyses — it must produce results "
     "that another scientist can independently verify.")
para("So I asked a deliberately uncomfortable question:")
q = doc.add_paragraph(); q.style = doc.styles["Intense Quote"] if "Intense Quote" in [s.name for s in doc.styles] else doc.styles["Normal"]
qr = q.add_run("Can my software independently reproduce a published result — using a "
               "different programming language — and arrive at the same biological "
               "conclusions from the same raw data?")
qr.bold = True; qr.italic = True
para("This is not the easy version of reproducibility. Re-running an author's "
     "original code is computational reproducibility. Rebuilding the entire analysis "
     "with independent tools and a different language and still landing on the same "
     "conclusions is methodological reproducibility / robustness — a substantially "
     "higher bar, and the one that actually validates a scientific claim.")

# ----------------------------------------------------------------- Test case
doc.add_heading("The test case", level=1)
p = doc.add_paragraph(); p.add_run("Paper: ").bold = True
p.add_run("Hua P, Roy N, de la Fuente J, et al. “Single-cell analysis of bone "
          "marrow–derived CD34⁺ cells from children with sickle cell disease "
          "and thalassemia.” ").italic = False
p.add_run("Blood").italic = True
p.add_run(" 2019;134(23):2111–2115.")
label_link("\U0001F517 Article:",
           "https://www.sciencedirect.com/science/article/pii/S0006497120731691",
           "sciencedirect.com/science/article/pii/S0006497120731691")
p = doc.add_paragraph(); p.add_run("Data: ").bold = True
p.add_run("GEO accession GSE133181 — 13 × 10x Genomics scRNA-seq samples of "
          "CD34⁺ bone-marrow cells (4 healthy controls, 3 β-thalassemia, 5 "
          "sickle cell disease).")
label_link("\U0001F517 GEO:",
           "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE133181",
           "ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE133181")
para("The original authors used an R stack — Seurat for clustering, AUCell for "
     "signature scoring, and an in-house R trajectory package.")
para("My system reproduced the entire study in Python — scanpy for processing, "
     "Harmony for batch integration, Leiden for clustering, an independent AUCell "
     "implementation, and diffusion pseudotime (DPT) for trajectory inference. "
     "Different language. Different algorithms. Same data. Autonomous code generation.")

# ----------------------------------------------------------------- What it did
doc.add_heading("What the AI actually did", level=1)
para("I pointed Claude Code at the raw matrices and the manuscript and let the "
     "agentic skills run. It autonomously:")
steps = [
    "Standardized and loaded all 13 raw 10x matrices (33,694 genes) into a unified object",
    "Ran QC and filtering → 59,822 high-quality cells",
    "Normalized, selected variable genes, and reduced dimensions",
    "Integrated 13 batches with Harmony and clustered with Leiden (20 clusters)",
    "Annotated cell types from canonical markers (HSPC, B-lymphoid progenitors, "
    "erythroid/megakaryocyte, granulocyte/monocyte)",
    "Scored the exact lymphoid signature from the paper (CD79A, CD79B, VPREB1, "
    "VPREB3, EBF1; AUCell, AUC > 0.25)",
    "Tested differential abundance across conditions",
    "Inferred the B-progenitor maturation trajectory",
    "Wrote the figures, tables, and a claim-by-claim interpretation report — itself.",
]
for s in steps:
    doc.add_paragraph(s, style="List Number")
para("(I have used Google Gemini and OpenAI Codex on the same task — all three "
     "converge on the same biological conclusions.)", italic=True)

# ----------------------------------------------------------------- Results table
doc.add_heading("The results — every major finding, reproduced", level=1)
table = doc.add_table(rows=1, cols=4)
table.style = "Light Grid Accent 1"
hdr = table.rows[0].cells
for c, txt in zip(hdr, ["Finding in Blood (2019)", "Original conclusion",
                        "Independent Python reproduction", "Match"]):
    c.paragraphs[0].add_run(txt).bold = True
rows_data = [
    ("Expansion of CD34⁺ B-lymphoid progenitors in patients",
     "↑ in all 8 patients", "6.9% → ~44% of CD34⁺ cells; p = 0.004", "✅"),
    ("Lymphoid-gene signature (AUCell, AUC>0.25)",
     ">65% in some children", "BT2 = 73%, SCD1 = 80%", "✅"),
    ("No expansion of erythroid cells (transfusion-suppressed)",
     "Not significant", "11.7 / 8.8 / 9.8%; p = 0.81 (ns)", "✅"),
    ("Early → late B-progenitor trajectory",
     "IL7R/IGHM → CD24", "Same ordering recovered", "✅"),
    ("Relative reduction of multipotent HSPCs",
     "Reduced", "68.7% → 33.4%; p = 0.004", "✅"),
    ("CD133 (PROM1) spares B-progenitors (corrects HSC estimate)",
     "Very few B-progenitors are CD133⁺", "3.6% in B-prog vs 20.6% in HSPC", "✅"),
]
for r in rows_data:
    cells = table.add_row().cells
    for cell, txt in zip(cells, r):
        cell.paragraphs[0].add_run(txt)
doc.add_paragraph()
para("The system even reproduced a specific detail of the paper — that in certain "
     "children (the authors named BT2 and SCD2) more than 65% of CD34⁺ cells were "
     "B-progenitors. In my run, BT2 hit 73% and SCD1 hit 80%.")
para("And critically — the central message of the paper survived: the apparent loss "
     "of HSCs is not a true loss but a dilution by the expanded B-progenitor pool, "
     "which is why CD34 alone over-counts HSCs in these patients and why CD133 gating "
     "rescues the estimate. The AI reconstructed that logic from the data, not from "
     "being told the answer.")

# ----------------------------------------------------------------- Honesty
doc.add_heading("The intellectual honesty that makes this real", level=1)
para("I will not claim “byte-identical output,” because that is not what "
     "scientific reproduction means — and claiming it would be dishonest. Two "
     "different languages running two different clustering and integration algorithms "
     "will never produce identical floating-point percentages.")
para("What was reproduced is what matters: the direction, the statistical "
     "significance, the effect size, and the biological interpretation of every major "
     "finding. That is the definition of a result that holds. A low-depth sample "
     "(SCD5) behaved as the weakest patient signal — exactly as you'd expect — and "
     "changed no conclusion.")
para("That distinction — reproducing conclusions, not artifacts — is precisely the "
     "standard the reproducibility literature is calling for.")

# ----------------------------------------------------------------- Why it matters
doc.add_heading("Why this matters", level=1)
para("If an agentic AI can take raw GEO data + a PDF and independently regenerate a "
     "Blood paper's conclusions in a different language — with the QC, the statistics, "
     "the figures, and a written interpretation — then the role of the computational "
     "biologist is being redefined in real time. Not replaced: amplified. The "
     "scientist moves from writing pipelines to posing questions, auditing reasoning, "
     "and certifying conclusions.")
para("This is what a Biomedical Operating System is for: making rigorous, "
     "reproducible, multi-omics analysis a conversation rather than a multi-week "
     "engineering project — while keeping a human firmly in the loop as the scientific "
     "authority.")

# ----------------------------------------------------------------- Links
doc.add_heading("See it for yourself", level=1)
label_link("\U0001F3A5 Full live demonstration (uncut):",
           "https://youtu.be/JDZ6hx6z6Js", "youtu.be/JDZ6hx6z6Js")
p = doc.add_paragraph(); p.add_run("\U0001F4E6 All outputs — code, figures, tables, "
    "AnnData checkpoints, and the AI-generated interpretation report: ").bold = True
p.add_run("[add repository / folder link]").italic = True
label_link("\U0001F4BB The open framework:",
           "https://github.com/mdbabumiamssm/LLMs-Universal-Life-Science-and-Clinical-Skills-",
           "github.com/mdbabumiamssm/LLMs-Universal-Life-Science-and-Clinical-Skills-")

# ----------------------------------------------------------------- Discuss
doc.add_heading("Let's discuss", level=1)
para("I built this to be challenged. So I'll ask the community directly:")
p = doc.add_paragraph()
p.add_run("What paper should the system reproduce next — and what would you accept as "
          "proof that an AI has genuinely done the work of a computational "
          "biologist?").bold = True
para("Drop a GEO accession and a DOI in the comments. Let's keep raising the bar, in "
     "public, with the data open.")
tags = doc.add_paragraph()
tr = tags.add_run("#AIinBiology #ComputationalBiology #Reproducibility #SingleCell "
                  "#Bioinformatics #AgenticAI #MCP #ClaudeCode #Genomics #OpenScience")
tr.italic = True; tr.font.color.rgb = RGBColor(0x11, 0x55, 0xCC)

doc.save(OUT)
print("Saved:", OUT)
