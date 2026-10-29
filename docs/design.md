# CodeStitch — Final Design (AgentX Hackathon 2026, PS-05)

Team FORTEC (Ronit Shrimankar + Anshul Kamthe). Idea deck due Oct 30, 2026,
11:59 PM IST. Build round Nov 11, 10:00 AM – Nov 12, 10:00 AM IST (24h, online).

## One line

CodeStitch is a multi-agent bug fixer that understands WHY the code is like
this before it stitches a fix — several agents fixing several bugs in parallel,
with accuracy and speed as the two headline goals.

## The problem (researched, Oct 29 2026)

Developers spend roughly 20–30% of their time debugging; 95% now also spend
extra time fixing AI-generated code. Today's AI fixers add new problems of
their own: symptom fixes (hide the error, keep the cause), wrong-cause fixes
(pattern-match to the most common cause, not the actual one), patches that
pass the test suite but miss the true intent (overfitting), fixes that break
other features (75% of agents break working code across multi-commit cycles
without strict regression gates), wrong-file localization (worse on repos
over 200k lines, where every agent drops below 45%), infinite loops, context
drift, high token cost, prompt-injection risk, and low real-world PR
acceptance (~40–44% for open agents). The best agents still fail over 20% of
benchmark tasks.

## Why existing tools don't solve it

Every existing fixer is strong at one thing and weak at the rest: great
fix loops with weak localization, great sandboxes that are heavy and
costly, great human control with a single-task mindset, reviewers that
never fix, localizers that never ship a patch. None of them uses the
code's own history.

## Architecture: 8 stages + 1 coordinator

1. **Triager** (small, fast model) — Is the issue real, complete, and
   reproducible? Rejects vague, duplicate, and hopeless issues early with a
   question back to the reporter. Kills wasted compute before it starts.
2. **Localizer** (graph-guided, staged) — Understand the
   failure → narrow to suspicious classes → confirm the exact method, using
   the WhyCode history graph: commits, PRs, and issues linked to code
   entities, so the fixer sees which change introduced the bug and what was
   discussed about it. This is the root-cause edge.
3. **Reproducer** (sandbox) — Builds a failing test/repro in an isolated
   isolated sandbox before any fix is attempted. No repro, no fix.
4. **Fixers in parallel** (coordinator-proposer style) — Several candidate
   fixes generated concurrently in isolated sandboxes, with different
   strategies. Speed comes from parallelism, not from rushing one attempt.
5. **Adversarial Tester** — Writes NEW tests from the inferred program
   intent, not just the existing suite. Catches fixes
   that pass old tests but miss the intent.
6. **Regression Gate** — Targeted test selection during the loop (affected
   code + neighbours only, for speed); full suite once, at the end, for the
   chosen patch. The new tests must go green AND all old tests must stay
   green.
7. **Reviewer** — Structured review of the final diff:
   summary, risk, test evidence, scope check.
8. **Human Gate** — A human approves before any PR is opened or merged.
   Nothing auto-merges. (Also a PS-05 must-have.)

**Coordinator (multi-bug):** orders repairs by dependency (shared files
first), keeps each bug in its own sandbox so fixes can't contaminate each
other, and runs one joint regression check before anything merges.

## Problem → mechanism map

| Problem | CodeStitch mechanism |
|---|---|
| Symptom / wrong-cause fixes | Graph-guided root-cause localization + repro-first |
| Patch overfitting / self-graded tests | Adversarial intent tests + independent verifier |
| Regressions | New tests pass + old tests stay green, targeted then full tests |
| Can't reproduce | Sandbox repro stage; packaged reproducible environments |
| Multi-file / multi-bug | Coordinator scheduling, isolated sandboxes |
| Loops / drift / overflow | Lean loop, step budgets, compact action-state messages between agents |
| Speed / cost | Parallel fixers, targeted tests, tiered models (small for triage, strong for fix), cached repo map + incremental graph |
| Security / injection | isolated sandbox, no network for fixers by default, injection scanning on issue text, least-privilege tokens |
| Low trust | Evidence chain on every fix + structured review + human gate |

## Tech stack (planned)

Python. isolated sandboxes. version-control API. Model-agnostic, bring-your-own-key
(any major model provider or local models). SQLite history graph from the
WhyCode engine. standard test runners. No paid APIs required for the core
loop; the model key is the only external dependency.

## 24-hour build plan (Nov 11–12)

- Hours 0–4: scaffolding, isolated sandbox, issue intake.
- Hours 4–10: pipeline stages 1–4 (triage → localize → repro → fix).
- Hours 10–16: stages 5–8 + multi-bug coordinator + demo repos.
- Hours 16–20: hardening, regression gates, safety checks, tests.
- Hours 20–24: demo video + final deck.

## Demo plan

Three real issues on a public Python repo, fixed live: issue in → repro
fails → fix lands → new + old tests green → PR opened with evidence chain
and human approval. Success is measured, not claimed: resolve rate,
time-to-PR, regression rate, and token cost per fix.

## Risks and mitigations

- Huge repos → staged localization + repo map, never full-repo context.
- Flaky tests → retry, then quarantine with a flag, never silently pass.
- Vague issues → triager asks clarifying questions instead of guessing.
- Multi-bug conflicts → dependency ordering + joint regression check.
- Model cost → tiered models + early abort + parallel-but-bounded fixers.

## Honest limits (idea stage)

CodeStitch is an idea deck, not a built product yet: no resolve-rate claim
is made until the 24-hour build runs it against real issues. The WhyCode
graph engine is real and already built and proven on a large real-world repo (200 commits, 100 PRs, 100
issue tickets, 630 edges); the fixer pipeline around it is the Nov 11–12
build.
