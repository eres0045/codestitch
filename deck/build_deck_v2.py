"""Build the CodeStitch idea deck PPTX (v2): same revised content as the
impress deck, no external names, dark + green python-pptx template."""
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

BG = RGBColor(0x0F, 0x1A, 0x14)
GREEN = RGBColor(0x2E, 0xCC, 0x71)
LIGHT = RGBColor(0xE8, 0xF5, 0xEC)
MUTED = RGBColor(0x9A, 0xB3, 0xA0)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
FONT = "DejaVu Sans"

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
BLANK = prs.slide_layouts[6]


def add_slide(title, subtitle, bullets):
    slide = prs.slides.add_slide(BLANK)
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = BG
    bar = slide.shapes.add_shape(1, Inches(0.55), Inches(0.55), Inches(1.1), Pt(6))
    bar.fill.solid()
    bar.fill.fore_color.rgb = GREEN
    bar.line.fill.background()
    tb = slide.shapes.add_textbox(Inches(0.55), Inches(0.85), Inches(12.2), Inches(1.3))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(34)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p.font.name = FONT
    if subtitle:
        tb2 = slide.shapes.add_textbox(Inches(0.55), Inches(1.95), Inches(12.2), Inches(0.6))
        tf2 = tb2.text_frame
        tf2.word_wrap = True
        p2 = tf2.paragraphs[0]
        p2.text = subtitle
        p2.font.size = Pt(18)
        p2.font.color.rgb = GREEN
        p2.font.name = FONT
    tb3 = slide.shapes.add_textbox(Inches(0.55), Inches(2.75), Inches(12.2), Inches(4.1))
    tf3 = tb3.text_frame
    tf3.word_wrap = True
    for i, b in enumerate(bullets):
        p = tf3.paragraphs[0] if i == 0 else tf3.add_paragraph()
        p.text = "▸  " + b
        p.font.size = Pt(17)
        p.font.color.rgb = LIGHT
        p.font.name = FONT
        p.space_after = Pt(14)
        p.space_before = Pt(2)
    tb4 = slide.shapes.add_textbox(Inches(0.55), Inches(7.0), Inches(12.2), Inches(0.4))
    tf4 = tb4.text_frame
    tf4.word_wrap = True
    p4 = tf4.paragraphs[0]
    p4.text = "CodeStitch  ·  Team FORTEC  ·  AgentX Hackathon 2026  ·  PS-05"
    p4.font.size = Pt(11)
    p4.font.color.rgb = MUTED
    p4.font.name = FONT
    return slide


add_slide(
    "CodeStitch",
    "The multi-bug fixer that understands WHY before it stitches.",
    [
        "Team FORTEC  —  Ronit Shrimankar (lead) · Anshul Kamthe",
        "AgentX Hackathon 2026  ·  Problem Statement PS-05: Bug-fix agent",
        "Several agents fixing several bugs in parallel — accuracy and speed as the headline goals.",
        "Powered by the WhyCode history graph.",
    ],
)

add_slide(
    "Bugs eat time — and answers are missing",
    "01 · The problems developers face",
    [
        "20–30% of developer time goes to debugging — and 95% now also fix AI-written code.",
        "Reports say “it doesn't work” — no steps, no environment, no failing test to start from.",
        "The cause is forgotten — reasons scatter across old commits, tickets, and developers who left.",
        "So most of debugging is not fixing. It is searching: for the repro, for the cause, for the why.",
    ],
)

add_slide(
    "Confident fixes that are wrong",
    "02 · What today's fixers get wrong",
    [
        "Symptom fixes — the error is hidden with a null check; the log goes quiet, the bug stays.",
        "Fake-green fixes — the patch passes old tests but misses what the code was supposed to do.",
        "Regressions — a fix in one place silently breaks features somewhere else.",
        "Slow, costly, untrusted — endless loops, burnt tokens, unsafe code, and a human must re-check all of it.",
    ],
)

add_slide(
    "8 agents, one pipeline, one coordinator",
    "03 · The solution",
    [
        "1. Triager — real and reproducible? Rejects vague ones early.",
        "2. Localizer — graph-guided to the exact method.",
        "3. Reproducer — sandboxed failing test first. No repro, no fix.",
        "4. Parallel Fixers — several candidates, isolated sandboxes.",
        "5. Adversarial Tester — NEW intent tests, catch overfitting.",
        "6. Regression Gate — targeted tests in loop, full suite at end.",
        "7. Reviewer + Human Gate — human approves before merge.",
        "Coordinator on top: orders multi-bug repairs by dependency.",
    ],
)

add_slide(
    "How CodeStitch solves each one",
    "04 · Every problem, answered",
    [
        "Vague reports → Triager asks clarifying questions, rejects early.",
        "Unknown cause → History graph finds origin commit + discussion.",
        "Symptom fixes → Repro-first: prove it, then fix the cause.",
        "Fake-green fixes → New intent tests + independent verification.",
        "Regressions → Targeted tests in loop, full suite at merge.",
        "Slow & untrusted → Parallel fixers, tiered models, sandbox, human gate.",
    ],
)

add_slide(
    "Stitch the fix, not the symptom.",
    "Build round: Nov 11–12 · Proof: resolve rate · time-to-PR · regression rate · cost per fix.",
    [
        "Hours 0–4: scaffolding, isolated sandbox, issue intake.",
        "Hours 4–10: pipeline stages 1–4 (triage → localize → repro → fix).",
        "Hours 10–16: stages 5–8 + multi-bug coordinator + demo repos.",
        "Hours 16–20: hardening, regression gates, safety checks, tests.",
        "Hours 20–24: demo video + final deck.",
        "Powered by the WhyCode history graph — our own engine, already proven on a large real-world repo.",
    ],
)

out = "/home/hatch/workspace/goals/hackathon-registration-drive/projects/agentx-codestitch/deck/codestitch-idea-deck.pptx"
prs.save(out)
print(f"saved {out} with {len(prs.slides._sldIdLst)} slides")
