# CodeStitch

**The multi-bug fixer that understands WHY before it stitches.**

Team FORTEC — AgentX Hackathon 2026, Problem Statement PS-05 (bug-fix agent).

## What it is

CodeStitch is a multi-agent system that fixes reported bugs end to end:
several agents fixing several bugs in parallel, with accuracy and speed as
the headline goals. It takes a reported issue, reproduces it, finds the
root cause, writes a fix, proves the fix with tests, and opens a pull
request — with a human approving before anything merges.

## Why it exists

Developers spend roughly 20–30% of their time debugging, and most of that
time is not fixing — it is searching for a reproduction, for the cause,
for the why. Today's fixers get it wrong in predictable ways: they hide
symptoms instead of fixing causes, they produce patches that pass old
tests but miss what the code was supposed to do, they break other
features, and they are slow, costly, and untrusted.

## How it works

Eight stages, one pipeline, one coordinator:

1. **Triager** — is the issue real and reproducible? Rejects vague ones
   early.
2. **Localizer** — graph-guided to the exact method, using the WhyCode
   history graph: commits, pull requests, and tickets linked to code.
3. **Reproducer** — isolated sandboxed failing test first. No repro, no
   fix.
4. **Parallel Fixers** — several candidates at once, in isolated
   sandboxes.
5. **Adversarial Tester** — new tests written from intent, so overfitting
   gets caught.
6. **Regression Gate** — targeted tests during the loop, full suite at
   the end.
7. **Reviewer** — structured review of the final diff.
8. **Human Gate** — a human approves before any pull request merges.

A coordinator on top orders multi-bug repairs by dependency and runs one
joint regression check at merge.

## The edge

The WhyCode history graph — our own engine. It tells the fixer why the
code is like this before it stitches a fix, so it fixes causes, not
symptoms.

## Deck

- [Idea deck (PDF, 6 slides)](deck/codestitch-impress.pdf)
- [Idea deck (PPTX, 6 slides)](deck/codestitch-idea-deck.pptx)
- [Live animated deck](deck/impress-deck/index.html) (open in a browser,
  arrow keys / spacebar to navigate)

## Build plan

24-hour build round, Nov 11–12, 2026. Success is measured, not claimed:
resolve rate, time-to-PR, regression rate, and cost per fix.

## Team

Team FORTEC: Ronit Shrimankar (lead) · Anshul Kamthe.
