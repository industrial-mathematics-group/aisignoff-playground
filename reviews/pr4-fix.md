# AI review of pull requests #3 and #4: interpolation and its fix

> Staged for the playground: this report shows the format of an A2 review of a fix, recorded in a
> review-only pull request.

- **Reviewer:** Claude Fable 5.2 (Anthropic), new session without the generating conversation
- **Reviewed:** the lines that the merge commits of #3 (`99d425b`) and #4 (`cf5f2fe`) landed, on 2026-11-21
- **Level:** A2
- **Highest finding in this change:** none

## Summary

#4 fixes the major finding of `reviews/pr3-interp.md`: `interp` now returns `ys[-1]` for
`x >= xs[-1]`, so the last knot no longer reaches `xs[i]` with `i == len(xs)`. The rest of #3 holds up.

## What was checked

Both diffs together, the new test `test_at_last_knot`, and the boundaries again: below, at and above
the first and the last knot, and at every inner knot of the test data. All 11 tests pass.

## Findings in this change

None.

## Outside this change

None.
