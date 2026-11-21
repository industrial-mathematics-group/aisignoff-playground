# AI review of pull request #3: piecewise linear interpolation

> Staged for the playground: this report shows the format of an A2 review. The finding is a bug
> planted on purpose, so that later pull requests can show a fix and the review of the fix.

- **Reviewer:** Claude Fable 5.2 (Anthropic), new session without the generating conversation
- **Reviewed:** pull request #3 (`src/playground/interp.py`, `tests/test_interp.py`), on 2026-11-21
- **Level:** A2
- **Highest finding in this change:** major

## Summary

The change adds `interp(x, xs, ys)`, linear interpolation that holds the end values outside the
knots. Between the knots and at inner knots it is right; at the last knot it crashes.

## What was checked

The diff against the task ("linear interpolation with constant extrapolation"), the four new tests,
and the boundaries by hand: `x` below, at and above the first and the last knot.

## Findings in this change

| # | Severity | Where | Finding |
|---|---|---|---|
| 1 | major | `src/playground/interp.py:16` | At `x == xs[-1]`, `bisect_right` returns `len(xs)`, and `xs[i]` raises `IndexError`. The last knot is a supported input (the docstring includes it in `[xs[0], xs[-1]]`), and no test covers it. Use `bisect_left` with a clamp, or return `ys[-1]` for `x >= xs[-1]`. |

## Outside this change

None.
