# aisignoff playground

aisignoff playground is a throwaway repository for trying [aisignoff](https://github.com/industrial-mathematics-group/aisignoff) on GitHub. It holds a small dummy Python package, some results and a script, and the material of a workshop, all declared with the setup the aisignoff docs recommend.

## Why it exists

aisignoff records how each file or line was made and reviewed: how much an AI generated, how a human checked it, and whether an independent AI checked it. The playground gives you a repository where you can change files, open pull requests and see the checks, labels and badges react. Nothing in it matters, so you can try things out.

The repository's citation metadata says the same: it is "a playground for trying aisignoff", and if you cite it anyway, the `CITATION.cff` file gives the form to use.

## What is in the repository

| Path | What it is |
|---|---|
| `src/playground/` | A tiny Python package named `playground` (version 0.1.0, Python 3.11 or newer) with `mean`, `variance` and `fit_line` |
| `tests/` | Tests for the package, run with pytest |
| `scripts/make_results.py` | A script that writes `results/fit.csv` |
| `results/` | Fitted slopes and intercepts for three datasets, and a short summary |
| `docs/notes.md` | A notes file to edit when trying the scenarios |
| `SIGNOFF.toml` | The declarations, the line-level history setting and the policy |
| `SIGNOFF.snapshot.json` | A frozen snapshot of the declarations |
| `.github/workflows/` | The checks, labels, badges and release reports |
| `extras/workflows/` | Optional workflows to copy into `.github/workflows/` |
| `workshop/` | The material of the workshop of 19 November 2026 |
| `CITATION.cff` | Citation metadata |

## How the files are declared

Everything is declared G0 · H2 · A0 by default. The fitting module, the results and the script then override that default with their own levels. `SIGNOFF.toml` also turns on line-level declarations and sets a policy: every file needs at least H1, and G3 needs A1.

The [declaration levels](concepts/declaration-levels.md) page explains what G, H and A mean. [Where declarations are kept](concepts/where-declarations-live.md) shows what this repository declares for each path.

## Where to go next

- [Getting started](getting-started/index.md): set up the repository on GitHub, open a first pull request and run aisignoff locally.
- [Concepts](concepts/index.md): the G · H · A scheme, where declarations live, line-level history, policy, snapshots, and the labels, badges and reports.
- [Usage](usage/index.md): declaring pull requests and existing files, commit trailers, the try-out scenarios and release reports.
- [Install and extend](deploy-extend/index.md): the workflows, the optional workflows, version pinning and the workshop material.
- [Reference](reference/index.md): `SIGNOFF.toml`, workflow options and the repository files.
- [Troubleshooting](troubleshooting.md): red checks and other common problems.
