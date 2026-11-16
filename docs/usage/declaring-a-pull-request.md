# Declaring a pull request

Every pull request into `main` carries an AI declaration: how the change was made and how it was checked. You write it by ticking boxes in the pull request description. PR-signoff checks it, and when the pull request is merged, the declaration becomes part of the merge commit message.

## What the template contains

The pull request template is the organisation's default. It has four groups of boxes and one line:

| Part | What you tick or write | How many |
|---|---|---|
| Generation | G0, G1, G2 or G3 | Exactly one |
| Models | The AI models that were used | One or more for G1 to G3; none for G0 |
| Human review | H0, H1, H2 or H3 | The highest level you actually did |
| AI review | A0, A1, A2 or A3 | The highest level that was done; nothing ticked means A0 |
| `AI-Review-Findings:` | The worst problem the AI review found | Only for A2 and A3 |

The levels are defined in [Generation, human review and AI review levels](../concepts/declaration-levels.md).

## Fill it in

1. Open the pull request. Right after you create it, the template is unfilled and the checks fail.
2. Tick **one** generation box. Pick the highest level of any substantial part of the change.
3. If you ticked G1, G2 or G3, tick the model you used. If it is not listed, use the **Other:** box and write its name.
4. Tick your human review level. Tick the highest one you did: H2 includes H0 and H1.
5. Tick your AI review level, or leave the group empty for A0. A chat that wrote the change and then checked it itself does not count as an AI review.
6. For A2 and A3, name the reviewing model and link or commit the report. Then fill the `AI-Review-Findings:` line with one of `none`, `trivial`, `minor`, `major` or `critical`. A `major` or `critical` finding has to be fixed and reviewed again before merging.
7. For G0, G1, A0 and A1, leave the `AI-Review-Findings:` line empty.

You can tick the boxes directly on the pull request page. You do not need to open the edit form.

## The check reruns when you edit

The description check runs again whenever the description is edited, so you do not need to push a new commit. After a short time the checks turn green and the labels `ai:G*`, `human:H*` and `ai-review:A*` appear on the pull request. If a check does not change after you tick, reload the page.

## What a failing check means

Open **Details** on the failing check to read the reason. These are the usual ones:

| What you did | Result |
|---|---|
| Left the template untouched | Both **File-signoff** and **PR-signoff** fail because the template is unfilled (`TODO`). |
| Ticked more than one generation box, for example G1 and G2 | An error: more than one generation box. Untick all but one. |
| Ticked G1, G2 or G3 without a model | An error: a model is required. Tick one, or use **Other:**. |
| Ticked only H0 as the human review | A policy failure. This repository requires at least H1 for every file. |
| Ticked G3 with AI review below A1 | A policy failure. G3 needs at least A1. |

The minimum levels are explained in [Policy](../concepts/policy.md).

## Who is responsible

The person who opens the pull request. By ticking a human review level you take responsibility for the change, however it was made. If a bot opens the pull request for you, it names you as the responsible person, and you tick the boxes.

## After the merge

Merge with a merge commit. This only works if the repository's default merge commit message is set to **Pull request title and description**, see [Setting up the repository on GitHub](../getting-started/setup-on-github.md). On `main`, the lines the pull request brought in take the ticked levels. The reviewer is the author of the merge commit, that is, whoever clicked **Merge**. See [Line-level declarations and merge methods](../concepts/line-level-history.md).

A pull request into a branch other than `main` is not checked. Its lines are declared by the pull request that lands them on `main`.
