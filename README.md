# aisignoff playground

[![AI generation](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/industrial-mathematics-group/aisignoff-playground/badges/aisignoff-generation.json)](#what-the-report-shows)
[![Human review](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/industrial-mathematics-group/aisignoff-playground/badges/aisignoff-human-review.json)](#what-the-report-shows)
[![AI review](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/industrial-mathematics-group/aisignoff-playground/badges/aisignoff-ai-review.json)](#what-the-report-shows)
[![AI review findings](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/industrial-mathematics-group/aisignoff-playground/badges/aisignoff-findings.json)](#what-the-report-shows)

A testground for [aisignoff](https://github.com/industrial-mathematics-group/aisignoff) **0.24.0**. The content is a tiny numerical package (`src/playground/`: statistics, interpolation, unit conversions). The point is its history: each merged pull request shows one feature of aisignoff, and together they give the report something to show for every level.

> **Everything here is staged.** All code, reports and declarations were written by Claude (Anthropic) to demonstrate aisignoff. "Jane Doe" is a fictional maintainer, and the reviews credited to Claude Fable and to a new Claude Opus session are example reports written to show the format, not reviews those models ran. The bugs the reviews find were planted on purpose. Don't read the levels as a statement about this code.

## Setup

- `SIGNOFF.toml` comes from `aisignoff init --history`, with `merge-method = "merge"` and a small `[policy]`: H0 for everything, H1 for G3.
- The workflows call the group's reusable workflows in `industrial-mathematics-group/.github`, with aisignoff at the organisation's version: [`file-signoff.yml`](.github/workflows/file-signoff.yml) (lint and file badges), [`pr-signoff.yml`](.github/workflows/pr-signoff.yml) (the pull request's declaration), [`zensical-docs.yml`](.github/workflows/zensical-docs.yml) (the docs site with the folder report at `signoff/`), [`reuse.yml`](.github/workflows/reuse.yml) and [`citation.yml`](.github/workflows/citation.yml). [`tests.yml`](.github/workflows/tests.yml) runs pytest. `REUSE.toml`, `CITATION.cff` and `zensical.toml` were set up by IMGAgent (#13 to #15).
- Pull requests land as merge commits whose message is the pull request description, so each description declares the lines its pull request landed.
- `AGENTS.md` points coding agents to `aisignoff guide`.

## The pull requests, step by step

| # | Pull request | What it shows | Result |
|---|---|---|---|
| — | `c20c8d2` Set up aisignoff 0.18.0 (direct commit) | a commit on `main` declares itself with trailers | G3 H1 A0 |
| [#1](../../pull/1) | Add descriptive statistics | G3 with an **A1** check by a new session of the same model; `AI-Review-Findings: minor` | `stats.py` at **F1**. The check missed the planted variance bug |
| [#2](../../pull/2) | Add a CSV column reader | G2 with **no AI review** (A0) | `io.py` at **F-** |
| [#3](../../pull/3) | Add piecewise linear interpolation | **A2** by a different model, with its report [`reviews/pr3-interp.md`](reviews/pr3-interp.md) added in the same pull request; finds a **major** bug (a crash at the last knot) | `interp.py` at **F2**: a finding is recorded, not a threshold |
| [#4](../../pull/4) | Fix interpolation at the last knot | a hand-written fix (G0 H2 A0) | the touched lines go back to **F-**, the rest stays F2 |
| [#5](../../pull/5) | Review #3 and its fix #4 | **review-only** pull request: [`reviews/pr4-fix.toml`](reviews/pr4-fix.toml) attests both merge commits (**commit-scoped**), no findings | all lines of #3 and #4 at **F0**; no declaration needed |
| [#6](../../pull/6) | Review stats.py and io.py | review-only, **blob-scoped**: an **A3** review of `stats.py` with new evidence ([`reviews/stats-a3/`](reviews/stats-a3/)) that finds the **major** variance bug, and an A1 check of `io.py` (trivial typo) | `stats.py` from F1 to **F2** (the newest review counts), `io.py` at **F0** |
| [#7](../../pull/7) | Add temperature conversions | declared **G0**, hand-written | `units.py` G0 H2 A0 |
| [#8](../../pull/8) | Correct the generation of #7 | a person's **`[[commits]]` correction** in `SIGNOFF.toml` (`aisignoff correct`): code completions wrote parts | `units.py` from G0 to **G1**, reviews unchanged |
| [#9](../../pull/9) | Remove the unused CSV column reader | deleting a file leaves `reviews/io-a1.toml` covering **no line** | no error; `lint` notes one dead record |
| [#10](../../pull/10) | Remove the review record of the deleted io.py | **`aisignoff gc`** deletes the dead record file, the one deletion the add-only review folder allows | levels unchanged; git history keeps the record |
| [#11](../../pull/11) | Explain the playground in the README | this page | G3 H1 A0 |

The variance bug of `stats.py` (it divides by n instead of n − 1) is left open on purpose, so that the report has an open major finding to show. Fixing it, and then reviewing the fix with a new record file, is a good first exercise.

## What the report shows

On `main` with this README (#11), by lines (`aisignoff report`):

| Axis | |
|---|---|
| Generation | G0 1.0% · G1 7.5% · G2 8.6% · G3 82.9% |
| Human review | H1 82.9% · H2 17.1% |
| AI review | A0 80.6% · A1 4.1% · A2 9.6% · A3 5.7% |
| Findings | F0 9.6% · F1 4.1% · F2 5.7% · F- 80.6% |

The G3, A0 and F- shares are mostly the workflow files of the setup commit and this README. Per file (`aisignoff report --files`):

| File | Levels | Findings |
|---|---|---|
| `src/playground/stats.py` | G3 H1 A3 (#1, raised by the A3 attestation of #6) | F2: the open variance bug |
| `tests/test_stats.py` | G3 H1 A1 (#1) | F1: the A1 check of #1 |
| `src/playground/interp.py`, `tests/test_interp.py` | G2 H2 A2, the fix's lines G0 H2 A2 | F0: reviewed with the fix in #5 |
| `src/playground/units.py`, `tests/test_units.py` | G1 H2 A0 (#7 corrected by #8) | F- |

## Try it

```bash
pipx install aisignoff==0.24.0
git clone https://github.com/industrial-mathematics-group/aisignoff-playground && cd aisignoff-playground
aisignoff lint
aisignoff report --files
aisignoff report --html report.html --with-source   # the interactive folder report
git checkout ed8ae70 && aisignoff report --files    # main after #8: io.py and its A1 record are back
```

Every CI run of `signoff.yml` also uploads the interactive report as the artifact `aisignoff-report`, and each pull request's run of `signoff-pr-diff.yml` shows the levels of just its lines in the job summary.
