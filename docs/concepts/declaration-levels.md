# Generation, human review and AI review levels

Every change in this repository is described by three levels: how much an AI generated (G), how a human checked it (H), and whether an independent AI checked it (A). Together they read like one line, for example **G2 · H1 · A0**.

## Why declare

AI tools are welcome here for writing, coding, analysing and making figures. What is asked is that everything that goes into `main` says honestly how it was made and how it was checked. The declaration is stored with the files, so it travels with every copy and every release. See [where declarations are kept](where-declarations-live.md).

## The three axes

Each axis has four levels, numbered 0 to 3.

| | Question | 0 | 1 | 2 | 3 |
|---|---|---|---|---|---|
| **G** | How much did AI generate? | No AI, done by hand | AI **helped**: suggestions, polishing, a structure | AI **wrote big parts**; a human steered and edited | An AI agent did it **mostly on its own** |
| **H** | How did a human check it? | Looked at the whole: does what was asked, plausible | **Tried it**: ran it or recomputed the key results, read the important parts | **Every line**: every sentence, number, formula, reference | **Independently confirmed**: another method, or a second person checked every line |
| **A** | Did an independent AI check it? | No. The chat that wrote it checking itself does not count | A **fresh AI session**, without the original chat, checked it | A **different, capable model** checked it and wrote a report | A different model **produced new evidence** (new tests, a recomputation), with the report |

### G: generation

Choose the highest level of any substantial part of the change. A spell checker does not count. An AI rewriting a paragraph is G1. An AI drafting the section is G2. For G1 to G3, also name the AI model or models used.

Exactly one generation level applies to a change. Ticking two generation boxes in a pull request is an error.

### H and A: review

The review levels build up. H2 includes what H0 and H1 describe, and A2 includes A1. State the highest level you actually did.

If no AI review box is ticked, the change has A0.

## The findings line for A2 and A3

A2 and A3 need two more things:

- the review report, committed to the repository or linked, and
- an `AI-Review-Findings:` line stating the worst problem the review found in the change.

The accepted values are `none`, `trivial`, `minor`, `major` and `critical`. A `major` or `critical` finding has to be fixed and reviewed again before merging.

For A0 and A1, leave the line empty.

## Who is responsible

The person who opens the pull request. Ticking a human review level means taking responsibility for the change, however it was made. An AI cannot take responsibility. If a bot opens the pull request on someone's behalf, it names that person as the responsible one, and that person ticks the boxes.

## Minimum levels in this repository

This repository requires at least H1 for every file, and G3 additionally requires at least A1. See [policy](policy.md).

## Examples from research

| What happened | Declaration |
|---|---|
| I wrote the notes myself and reread them | G0 · H2 · A0 |
| ChatGPT polished the English of my abstract; I read every sentence | G1 · H2 · A0 |
| Claude wrote the plotting script; I ran it and checked the figure against the data | G2 · H1 · A0 |
| Same, and then a fresh Claude session checked the script without our chat | G2 · H1 · A1 |
| An agent did the literature table on its own; I checked every reference; GPT reviewed it and wrote a report with one minor finding | G3 · H2 · A2, `AI-Review-Findings: minor` |

## Next

- [Where declarations are kept](where-declarations-live.md)
- [Declaring a pull request](../usage/declaring-a-pull-request.md)
