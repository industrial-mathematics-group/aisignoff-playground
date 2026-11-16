# Policy: minimum review levels

The `[policy]` table in `SIGNOFF.toml` sets the lowest review levels a declaration may have. A file or line that falls below them fails the check, even if it is declared.

## What the policy says here

```toml
[policy]
"*" = { human = "H1" }
G3  = { human = "H1", ai = "A1" }
```

| Key | Applies to | Requires |
|---|---|---|
| `"*"` | every declaration | human review of at least H1 |
| `G3` | declarations with generation level G3 | human review of at least H1 and AI review of at least A1 |

In practice:

- Nothing in the repository may be declared with only H0. Every file needs at least H1.
- Anything generated at G3 (an AI agent did it mostly on its own) also needs at least A1, a review by a fresh AI session.

A comment in `SIGNOFF.toml` adds that G1 to G3 always need at least A1. That comment is the only place in the repository that states this rule, and the `[policy]` table itself only spells out the G3 entry. For the meaning of the levels, see [declaration levels](declaration-levels.md).

## Why a policy

A declaration says how a change was made and checked. It does not say whether that was enough. The policy turns "enough" into a rule that CI can enforce, so a change that was only glanced at (H0) cannot land unnoticed.

## Where the policy is checked

The policy applies to every declaration, whichever source it comes from:

- the annotations in `SIGNOFF.toml`,
- the ticked template of a pull request, which becomes the merge commit message and declares the lines that pull request lands (see [line-level history](line-level-history.md)).

So the policy is checked both in the **File-signoff** check and in pull requests. If you tick only H0 in a pull request, the check fails with a policy error because H1 is required.

## What a policy failure looks like

A policy failure is reported as an error by `aisignoff lint`, and the **File-signoff** check turns red. Two cases from the scenarios show it:

- **Pull request with only H0 ticked.** The declaration is complete, but the human level is below H1. The checks fail with a policy error. Tick a human review level of H1 or higher in the description; the check reruns when you edit it, without a new push.
- **G3 without A1.** If the `results/**` annotation is changed to `AI-Review = "A0"`, lint fails with a policy error, because that annotation is G3 and G3 needs A1. Restoring `AI-Review = "A1"` fixes it.

A policy failure differs from a missing declaration. A path in an annotation that matches no file only produces a warning, and only `lint --strict` would fail on it.

!!! note
    To see a policy failure yourself, run `aisignoff lint` after lowering the level in an annotation, or tick only H0 in a pull request. See the [try-out scenarios](../usage/scenarios.md).

## Changing the policy

Edit the `[policy]` table in `SIGNOFF.toml` and open a pull request. Raising a minimum can make existing declarations invalid, so run `aisignoff lint` locally before you push.
