# aisignoff playground

> **Workshop on 19 November 2026?** Start here: **[workshop/](workshop/README.md)**, and keep the
> [cheat sheet](workshop/cheat-sheet.md) ([PDF](workshop/cheat-sheet.pdf)) at hand.

Files and lines (folder report: *Actions → File-signoff →* newest run on `main` → artifact `aisignoff-report`):
[![AI generation (files)](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/industrial-mathematics-group/aisignoff-playground/badges/aisignoff-generation.json)](https://github.com/industrial-mathematics-group/aisignoff-playground/actions/workflows/file-signoff.yml)
[![Human review (files)](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/industrial-mathematics-group/aisignoff-playground/badges/aisignoff-human-review.json)](https://github.com/industrial-mathematics-group/aisignoff-playground/actions/workflows/file-signoff.yml)
[![AI review (files)](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/industrial-mathematics-group/aisignoff-playground/badges/aisignoff-ai-review.json)](https://github.com/industrial-mathematics-group/aisignoff-playground/actions/workflows/file-signoff.yml)
<!-- The findings badge needs the organisation's File-signoff to publish aisignoff-findings.json (aisignoff >= 1.0.0rc9):
[![AI review findings (files)](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/industrial-mathematics-group/aisignoff-playground/badges/aisignoff-findings.json)](https://github.com/industrial-mathematics-group/aisignoff-playground/actions/workflows/file-signoff.yml) -->

Merged pull requests:
[![AI generation](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/industrial-mathematics-group/aisignoff-playground/badges/ai-generation.json)](https://github.com/industrial-mathematics-group/.github/blob/main/.github/CONTRIBUTING.md#g-generation)
[![Human review](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/industrial-mathematics-group/aisignoff-playground/badges/ai-human-review.json)](https://github.com/industrial-mathematics-group/.github/blob/main/.github/CONTRIBUTING.md#h-human-review)
[![AI review](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/industrial-mathematics-group/aisignoff-playground/badges/ai-review.json)](https://github.com/industrial-mathematics-group/.github/blob/main/.github/CONTRIBUTING.md#a-ai-review)

A throwaway repository for trying [aisignoff](https://github.com/industrial-mathematics-group/aisignoff) on GitHub: a small dummy Python package, results, a script and workshop material, declared with the setup the aisignoff docs recommend.

## What's in it

| Path | Declared as | How |
|---|---|---|
| everything (`**`) | G0 · H2 · A0, by Pascal Jung | default annotation in `SIGNOFF.toml` |
| `src/playground/fitting.py` | G2 · H1 · A0, Claude Opus | annotation |
| `results/**` | G3 · H1 · A1, Claude Opus | annotation (folder) |
| `scripts/make_results.py` | G1 · H2 · A0, Claude Opus | its former inline tags, kept in `SIGNOFF.snapshot.json`; the header comment itself no longer counts (from aisignoff 1.0.0rc7 on) |

`SIGNOFF.toml` also turns on line-level declarations (`[history]`, `merge-method = "merge"`) and a policy: every file needs at least H1, G3 needs A1.

| File | What it does |
|---|---|
| `.github/workflows/file-signoff.yml` | The organisation's File-signoff check (pinned to aisignoff 1.0.0rc9): every line declared, policy met; folder tree in the job summary, folder report as an artifact; on `main` also the file badges (top row above) on the `badges` branch |
| `.github/workflows/pr-signoff.yml` | The organisation's PR-signoff check: validates the ticked template, sets `ai:G*` / `human:H*` / `ai-review:A*` labels |
| `.github/workflows/signoff-badges.yml` | The organisation's Signoff-Badges workflow: badges of the declarations of merged pull requests (second row) |
| `.github/workflows/signoff-request.yml`, `signoff-assistant.yml` | The issue form *Signoff: declare or attest files* and the @signoff assistant, which open pull requests that change `SIGNOFF.toml` |
| `.github/workflows/signoff-release.yml` | Attaches the AI signoff report to every published release |
| `CITATION.cff` | Citation metadata, for *Cite this repository* and Zenodo |
| `workshop/` | The material of the workshop of 19 November 2026 |
| `extras/workflows/` | Optional workflows to copy into `.github/workflows/`: the PR diff and PR files summaries |

The pull request template is the organisation's default (`.github/PULL_REQUEST_TEMPLATE.md` in `industrial-mathematics-group/.github`), with the generation, model, human review and AI review boxes and the `AI-Review-Findings:` line.

## Setup on GitHub

1. Create an empty repository and push: `git remote add origin <url> && git push -u origin main`.
2. *Settings → General → Pull Requests*: allow merge commits (and squash, for scenario 5), and set the default commit message of both to **Pull request title and description**. Without this the declaration never reaches git.
3. *Settings → Rules → Rulesets* (or *Branches*), for `main`: require a pull request, and require the checks **File-signoff** and **PR-signoff**. Leave direct pushes allowed for yourself if you want to try scenario 1 after this.
4. Check the first run under *Actions*: File-signoff should be green, and its summary should show the folder tree.
5. The badges branch is created by the first push to main after this. The pull request badges show "no declarations yet" until a declared pull request is merged. Don't protect `badges` against pushes by github-actions[bot].

Locally: `pipx install aisignoff==1.0.0rc9`, then `aisignoff lint`, `aisignoff report --files` (with `[history]`, files with mixed lines show the share of each declaration), `aisignoff diff HEAD^1 --files` (the levels of the lines a commit added) and `aisignoff report --json` (every line run with its source).

## Scenarios

Each one says what should happen. In pull requests, fill the template by ticking boxes: generation (exactly one), models, human review, AI review.

### 1. Plain push to main

Edit `docs/notes.md`, commit with a plain message, push to `main`.
**Expect:** lint green. The new lines declare nothing, so they take the file-level declaration (G0 · H2 · A0). `aisignoff report --files` is unchanged.

Variant: commit with "Key: value" lines in the message (`AI-Generation: G2`, `Assisted-by: …`, `Human-Review: H1`, `Reviewed-by: …`, `AI-Review: A1`, `AI-Reviewed-by: …`). **Expect:** `aisignoff report --files` shows `docs/notes.md` partly at G2.

### 2. Pull request into main

Branch, change `src/playground/stats.py`, open a pull request into `main`.

- With the template untouched: **expect** `aisignoff / lint` and `pr-signoff / check` to fail (unfilled template, `TODO`).
- Tick G2, Claude Opus, H1, A1: both turn green after the edit, without a new push (the description check reruns on `edited`).
- Tick only H0: **expect** a policy failure (H1 is required).
- Tick G1 and G2 together: **expect** an error (more than one generation box).

Merge it on GitHub with a merge commit. **Expect:** on `main`, `aisignoff report --files` shows `stats.py` as mostly G0 · H2 · A0 plus a share at the ticked levels, and `aisignoff diff HEAD^1 --files` shows the added lines at G2 · H1 · A1. Their reviewer is the merge commit's author, i.e. whoever clicked *Merge*.

### 3. Stacked pull requests

Branch `a` from `main`, branch `b` from `a`. Open PR A (`a` → `main`) and PR B (`b` → `a`).
**Expect:** PR B's description isn't checked by aisignoff (it doesn't go into the default branch), and PR-signoff only checks PRs into `main`. Merge B into A, then A into `main`: A's description declares all the lines, B's included.

Variant: merge A first, let GitHub retarget B to `main`, then merge B. **Expect:** B's description now counts, for the lines B's merge brings in.

### 4. Something undeclared

Change the `results/**` annotation to `AI-Review = "A0"`. **Expect:** lint fails with a policy error (G3 needs A1). Or add an annotation for a path that doesn't exist: lint passes but warns (`lint --strict` would fail).

### 5. Squash merge

Set `merge-method = "squash"` in `SIGNOFF.toml` (land that first), then open a PR with a few commits, some of them with `AI-Generation: G3` in their messages, and squash-merge it.
**Expect:** the squash commit's description declares all its lines; the branch commits' generation is ignored. With `merge-method = "merge"` and a merge commit instead, a branch commit with `AI-Generation: G3` raises the generation of the lines it wrote.

### 6. Freeze

Once a few PRs have landed, take a snapshot:

```bash
git switch --detach origin/main
aisignoff freeze --prune
git switch -c freeze
git add SIGNOFF.snapshot.json SIGNOFF.toml && git commit -m "Freeze the declarations"
git push -u origin freeze      # and open a PR (tick G0 / H2 / A0, or "Key: value" lines)
```

**Expect:** lint in the PR checks the snapshot by working it out again (green). Then try:

- Edit a level in `SIGNOFF.snapshot.json` by hand and push: **expect** lint to fail.
- After the freeze has landed, change the `**` annotation: frozen lines keep their levels (`aisignoff report --files` unchanged). `aisignoff freeze --reset docs/notes.md` on `main` applies it to that file.
- `aisignoff freeze --check` runs the snapshot check on its own.

### 7. Findings (aisignoff 1.0.0rc9)

Reports show a fourth axis: what the last independent AI review of a line found. **F-** no such review since the line last changed, **F0** reviewed and nothing open (or only trivial findings), **F1**/**F2**/**F3** an open minor/major/critical finding. A line gets F0 to F3 only from an A2 or A3 review with its findings: the merge commit of a pull request that ticks A2 or A3 and fills `AI-Review-Findings:`, an attestation with `AI-Review-Findings` (`aisignoff attest FILE -a A2 --ai-reviewed-by "…, <report>" --findings none`), or a `[[commits]]` entry or annotation with that key. Lines that a later change touches go back to F-, so a fix is unreviewed until the next review. Findings of any severity pass the checks; a missing or invalid `AI-Review-Findings:` line next to A2 or A3 fails them.

The playground has test findings at every level, from pull requests of 20 November 2026. Each pull request has the review report of Claude Fable in its description:

| File | Findings | From |
|---|---|---|
| `src/playground/__init__.py`, `pyproject.toml`, `.gitignore`, `CITATION.cff` | F0 | attestations of an A2 review that found nothing (#26) |
| `src/playground/stats.py` | F1 | an attestation of an A2 review with a minor finding (#26) |
| `tests/test_playground.py` | F1 on the added tests | #21, minor: a test that passes for the wrong reason |
| README and docs lines of #20 | F1, F- where #26 (declared A1) fixed them | #20, minor: docs that still named the old pins |
| `src/playground/robust.py`, `tests/test_robust.py` | F2 | #22, major: the median of an even number of values |
| `src/playground/fitting.py`, `tests/test_weighted.py` | F3 on the weighted fit, F- on the lines of the fix | #23, critical: unweighted sums of squares; fixed in #25, declared A1 (no review findings) |
| `scripts/make_results.py` | F3 on the changed lines | #24, critical: slope and intercept swapped in the output |
| everything else | F- | no A2 or A3 review |

**Expect:** the folder report (artifact `aisignoff-report` of File-signoff on `main`) has a *Findings* button and shows the share of F- and of F2/F3 at the top; `aisignoff report` ends with a *Findings* block. Then try: open a pull request that changes one line of `src/playground/__init__.py` with A1 ticked. **Expect** that line to go back to F- after the merge, the rest of the file to stay at F0.

### 8. Merge queue (optional)

Turn on the merge queue in the ruleset. **Expect:** the `merge_group` run says it checks `HEAD` as landed, and fails if the description was left unfilled.

## Updating aisignoff

File-signoff and PR-signoff pin aisignoff 1.0.0rc9 with `aisignoff-version:` in `.github/workflows/file-signoff.yml` and `pr-signoff.yml` (the organisation's default is 1.0.0rc8 at the time of writing); change it there, and the one in `signoff-release.yml` and `extras/workflows/`. Keep your local install at the same version: a snapshot written by another version than CI's can fail the check.
