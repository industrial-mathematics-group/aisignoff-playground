# AI review of src/playground/stats.py, with new evidence

> Staged for the playground: this report shows the format of an A3 review of a whole file. Finding 1
> is a bug planted on purpose, which the A1 check of #1 missed. It stays open in the playground, so
> that the report shows an open major finding.

- **Reviewer:** Claude Fable 5.2 (Anthropic), new session without the generating conversation
- **Reviewed:** `src/playground/stats.py` as it is on `main` after #5, on 2026-11-21
- **Level:** A3
- **Highest finding in this change:** major

## Summary

`mean`, `median` and `std` are straightforward, but `variance` computes the population variance
while its docstring promises the sample variance, so `variance` and `std` are wrong for every
sample. The reviewer compared both with Python's `statistics` module and committed that check.

## What was checked

The whole file against its docstrings; the existing tests in `tests/test_stats.py`; and new
evidence: `reviews/stats-a3/check_variance_reference.py` compares `variance` and `std` with
`statistics.variance` and `statistics.stdev` on three samples. It fails as described below.

## Findings in this change

| # | Severity | Where | Finding |
|---|---|---|---|
| 1 | major | `src/playground/stats.py:14` | `variance` divides by `len(xs)`, not `len(xs) - 1`: for `[1, 2, 4]` it gives 1.556 instead of 2.333. Every caller relying on the documented sample variance gets a value too small by the factor (n − 1)/n. The existing test only checks a constant sample, where both agree. |
| 2 | minor | `src/playground/stats.py:8` | `mean([])` raises `ZeroDivisionError` instead of a `ValueError` that says the sample is empty (also found by the A1 check of #1). `variance([x])` should say it needs two values. |

## Outside this change

None.

## New evidence (A3 only)

`reviews/stats-a3/check_variance_reference.py`: three checks against the reference implementation.
Run it with `python -m pytest reviews/stats-a3/check_variance_reference.py -q`; on the reviewed
content all three fail. It is named `check_*.py` so that the package's own test suite doesn't
collect it; the author can copy it into `tests/` with the fix.
