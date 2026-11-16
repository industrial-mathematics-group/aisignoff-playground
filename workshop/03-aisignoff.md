[← 2 Live demo](02-live-demo.md) · **3 AI signoff** · [4 Hands-on →](04-hands-on.md)

# 3 · AI signoff

## Why

We **welcome AI tools**: for writing, coding, analysing, making figures. What we ask is that everything that
goes into `main` says **honestly how it was made and how it was checked**. Funders, journals and readers
increasingly ask; the answer should be on record, not in someone's memory. And the record travels with the
files: into every copy, every release and the Zenodo archive.

## Three questions, one line

Every change answers three questions. The answer reads like **G2 · H1 · A0**.

| | Question | 0 | 1 | 2 | 3 |
|---|---|---|---|---|---|
| **G** | How much did **AI generate**? | I did it myself, no AI | AI **helped**: suggestions, polishing, a structure | AI **wrote big parts**, I steered and edited | An AI agent did it **mostly on its own** |
| **H** | How did a **human check** it? | Looked at it as a whole: does what was asked, plausible | **Tried it**: ran it or recomputed the key results, read the important parts | **Every line**: every sentence, number, formula, reference | **Independently confirmed**: another method, or a second person checked every line |
| **A** | Did an **independent AI** check it? | No (the chat that wrote it checking itself doesn't count) | A **fresh AI session**, without the original chat, checked it | A **different, capable model** checked it and wrote a report | A different model **produced new evidence** (new tests, a recomputation), with the report |

- **G:** tick the highest level of any substantial part. A spell checker doesn't count; ChatGPT rewriting a
  paragraph is G1; ChatGPT drafting the section is G2.
- **H and A build up:** H2 includes H0 and H1. Tick the highest one you actually did.
- **A2 and A3** need the report committed or linked, and one more line: `AI-Review-Findings:`, the worst
  problem the review found in the change (`none`, `trivial`, `minor`, `major`, `critical`). A `major` or
  `critical` finding has to be fixed and reviewed again before merging. For A0 and A1, leave the line empty.
- **This repository** requires at least **H1** for every file, and A1 for anything at G3.

### Examples from research

| What happened | Declaration |
|---|---|
| I wrote the notes myself and reread them | G0 · H2 · A0 |
| ChatGPT polished the English of my abstract; I read every sentence | G1 · H2 · A0 |
| Claude wrote the plotting script; I ran it and checked the figure against the data | G2 · H1 · A0 |
| Same, and then a fresh Claude session checked the script without our chat | G2 · H1 · A1 |
| An agent did the literature table on its own; I checked every reference; GPT reviewed it and wrote a report with one minor finding | G3 · H2 · A2, `AI-Review-Findings: minor` |

The [full definitions](https://github.com/industrial-mathematics-group/.github/blob/main/.github/CONTRIBUTING.md#ai-assisted-contributions)
have a column for code and one for research and writing.

## Who is responsible?

**The person who opens the pull request.** By ticking a human review level you take responsibility for the
change, however it was made. AI can't take responsibility. If a bot opens the pull request for you, it names
you (`Responsible person: @you`) and you tick.

## Where the declaration is kept

| How the files get in | Where the declaration goes | Who writes it |
|---|---|---|
| A pull request (the usual way) | The ticked boxes, which become the merge commit's message | You, by ticking |
| Files already in `main` that need a declaration or a better review | `SIGNOFF.toml`, a list of paths and their levels | The **signoff request**: a form or the @signoff assistant (below) |

You never have to edit `SIGNOFF.toml` by hand. You can open it to see what it looks like:
[SIGNOFF.toml](../SIGNOFF.toml).

## The easiest way in: @signoff

To declare files that are already in the repository, or to record that you reviewed them:

1. **Issues → New issue → Blank issue** (or comment in an open issue).
2. Write `@signoff` and say in your own words what to record, as you would to a colleague:

   > @signoff I checked `results/summary.md` line by line against `results/fit.csv` today. Please record a
   > human review of H2 with me, Jane Doe, as reviewer.

3. Within a minute the **signoff assistant** (an AI) answers with what it understood, or asks what's missing.
4. The **signoff bot** opens a pull request that changes `SIGNOFF.toml`. Check *Files changed*, tick your
   human review in its description, merge. Done.

Prefer a form to a chat? **Issues → New issue → Signoff: declare or attest files** asks the same questions
as drop-downs, and no AI is involved.

## What you get: the report

- **Labels** on each pull request (`ai:G2`, `human:H1`, `ai-review:A0`) to see at a glance.
- **Badges** on the front page: the share of files and of merged pull requests at each level.
- **The folder report**: *Actions → File-signoff →* the newest run on `main`. Its summary shows the level mix
  per folder, and under *Artifacts* there is `aisignoff-report`: download it, unzip it and open the page in your browser. It's an interactive page with a sunburst of the
  folders, coloured by level. Look for the parts with a high G and a low H: that's where a second look pays off.

---

[← 2 Live demo](02-live-demo.md) · [4 Hands-on →](04-hands-on.md)
