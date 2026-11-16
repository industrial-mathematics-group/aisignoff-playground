[← 1 The mental model](01-mental-model.md) · **2 Live demo** · [3 AI signoff →](03-aisignoff.md)

# 2 · Live demo

Follow along on the projector; you'll do the same yourself in part 4. Every step is a click in the browser.

## A. Look around (3 min)

1. The [front page](https://github.com/industrial-mathematics-group/aisignoff-playground): the files, the
   README underneath, and badges that summarise how the files were made and reviewed.
2. **Commits** (the clock icon above the file list): the history, newest first. Click one to see what changed.
3. **Pull requests → Closed**: open [#13](https://github.com/industrial-mathematics-group/aisignoff-playground/pull/13).
   Its description has ticked boxes (the AI declaration), its labels say `ai:G1`, `human:H2`, …, and the
   checks at the bottom were green when it was merged.

## B. Change a file and open a pull request (7 min)

1. Open [`docs/notes.md`](../docs/notes.md) and click the **pencil** (Edit this file).
2. Add a line, for example `Workshop on 19 November: hello from the demo.`
3. Click **Commit changes…**. In the dialog:
   - write a short message, e.g. `Add a hello from the workshop`;
   - choose **Create a new branch for this commit and start a pull request** and give it a name such as
     `demo/hello`;
   - click **Propose changes**.
4. You're on the "Open a pull request" page. The description is already filled with a template that ends in
   the **AI declaration**. Leave it as it is for now and click **Create pull request**.

## C. Red, then green (7 min)

1. Scroll down to the checks. After a few seconds **PR-signoff** and **File-signoff** turn **red**. Click
   **Details** on one: the summary says that no generation or human review level is ticked.
2. Scroll back up to the description. You can **tick the boxes right there**, no need to edit anything:
   - Generation: **G0** (I typed it myself);
   - AI models: none (it's G0);
   - Human review: **H2** (I read every line I changed);
   - AI review: **A0**, or nothing (nothing ticked means A0);
   - leave the `AI-Review-Findings:` line empty: it only matters for A2 and A3.
3. Ticking edits the description, and the checks run again by themselves. After half a minute both are
   **green**, and the labels `ai:G0`, `human:H2`, `ai-review:A0` appear on the right.
4. **Make it fail on purpose:** untick H2 and tick **H0** instead. The checks go red again: this repository
   requires at least **H1** for every file (its "policy"). Put H2 back.

## D. Merge (3 min)

1. Click **Merge pull request**, then **Confirm merge**. GitHub offers to **Delete branch**: do it, the
   branch has done its job.
2. Go to **Commits** on `main`: the newest one is the merge, and its message contains the ticked declaration.
   That's how the declaration travels with the files, for good.

## Variant: upload a file instead of typing

**Add file → Upload files**, drag a picture or a CSV in, then the same: **Create a new branch** →
**Propose changes** → **Create pull request** → tick → merge. That's the everyday way to add figures,
data or a PDF.

---

What we just ticked was the AI declaration. Part 3 explains what the boxes mean.

[← 1 The mental model](01-mental-model.md) · [3 AI signoff →](03-aisignoff.md)
