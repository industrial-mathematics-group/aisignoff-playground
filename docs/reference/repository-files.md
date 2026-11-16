# Repository file reference

This page lists the files of aisignoff-playground, what each one is, and how its AI declaration is set. The declarations come from `SIGNOFF.toml`, the inline tags in `scripts/make_results.py`, and the snapshot in `SIGNOFF.snapshot.json`.

## How declarations are resolved

`SIGNOFF.toml` has a default annotation for `**` (G0 · H2 · A0, reviewer Pascal Jung). The last annotation that matches a file wins, so the more specific annotations below override the default. See [where declarations live](../concepts/where-declarations-live.md) for the full rules.

| Path | Declared as | Source |
|---|---|---|
| `src/playground/fitting.py` | G2 · H1 · A0, Claude Opus 5.5 (Anthropic) | annotation in `SIGNOFF.toml` |
| `results/**` | G3 · H1 · A1, Claude Opus 5.5 (Anthropic) | annotation in `SIGNOFF.toml` |
| `scripts/make_results.py` | G1 · H2 · A0, Claude Opus 5.5 (Anthropic) | its former inline tags, kept in `SIGNOFF.snapshot.json` |
| `docs/notes.md` | H3, reviewer John Doe | attestation in `SIGNOFF.toml`, tied to one blob |
| everything else | G0 · H2 · A0 | default annotation (`**`) |

## Python package: `src/playground/`

A small dummy package for trying aisignoff. It has no dependencies of its own.

| File | Contents |
|---|---|
| `src/playground/__init__.py` | Re-exports `mean`, `variance` and `fit_line` (`__all__`). |
| `src/playground/stats.py` | `mean(values)`: arithmetic mean, raises `ValueError` for an empty sequence. `variance(values, ddof=0)`: variance with `ddof` delta degrees of freedom, raises `ValueError` if there are not more than `ddof` values. |
| `src/playground/fitting.py` | `fit_line(xs, ys)`: returns `(slope, intercept)` of the least-squares line. Raises `ValueError` for fewer than two points, unequal lengths, or all x values equal. |

Declaration: `stats.py`, `__init__.py` take the default (G0 · H2 · A0). `fitting.py` has its own annotation (G2 · H1 · A0), because its docstring pretends an AI wrote most of it.

## Tests: `tests/test_playground.py`

pytest tests for the package: `test_mean`, `test_variance` (with `ddof=1`) and `test_fit_line`. `pyproject.toml` sets `pythonpath = ["src"]`, so the tests import `playground` without installing it.

Declaration: the default (G0 · H2 · A0).

## Script: `scripts/make_results.py`

Writes `results/fit.csv`. It fits a line to three small datasets (`a`, `b`, `c`) with `fit_line` and writes the slope and intercept, rounded to four decimals, per dataset.

The file still has a header comment with inline tags (G1 · H2 · A1). From aisignoff 1.0.0rc7 on, that header comment no longer counts as a declaration. The levels the file had before are kept in `SIGNOFF.snapshot.json` (G1 · H2 · A0). See [inline tags and commit trailers](../usage/inline-tags-and-commit-trailers.md).

## Results: `results/`

| File | Contents |
|---|---|
| `results/fit.csv` | Columns `dataset`, `slope`, `intercept` for datasets `a`, `b` and `c`. Written by `scripts/make_results.py`. |
| `results/summary.md` | A short statement that all three datasets fit a straight line well, and that dataset b is the only one with a negative slope. |

Declaration: both files fall under the `results/**` annotation (G3 · H1 · A1), with an AI reviewer recorded as a fresh review session.

## Project and tooling files

| File | What it is | Declaration |
|---|---|---|
| `pyproject.toml` | Project metadata: name `playground`, version `0.1.0`, description "Dummy package for trying aisignoff", `requires-python = ">=3.11"`, and the pytest `pythonpath` setting. | default |
| `.gitignore` | Ignores `__pycache__/`, `*.pyc`, `.pytest_cache/` and `aisignoff-report.html`. | default |
| `CITATION.cff` | Citation metadata (CFF 1.2.0): title, abstract, author, repository URL, type `software` and keywords. GitHub shows it as *Cite this repository*, and Zenodo can use it. | default |
| `zensical.toml` | Configuration of this documentation site: `site_name = "aisignoff-playground"` and the `nav` setting. | default |

## Other files

These are described on their own pages:

- `SIGNOFF.toml` and `SIGNOFF.snapshot.json`: see the [SIGNOFF.toml reference](signoff-toml.md) and [snapshots and freezing](../concepts/snapshots-and-freeze.md).
- `.github/workflows/` and `extras/workflows/`: see [the GitHub workflows](../deploy-extend/workflows.md) and [optional workflows](../deploy-extend/optional-workflows.md).
- `workshop/`: see [running the workshop](../deploy-extend/workshop-material.md).
- `docs/notes.md`: a notes file used in the scenarios, with an H3 attestation by John Doe in `SIGNOFF.toml`.
