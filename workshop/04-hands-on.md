[← 3 AI signoff](03-aisignoff.md) · **4 Hands-on** · [5 Releases and DOIs →](05-zenodo.md)

# 4 · Hands-on

Your turn. Keep the [cheat sheet](cheat-sheet.md) open next to this page. Raise your hand when a check stays
red: reading what it says is part of the exercise.

Everyone works on **their own file** in [`workshop/hands-on/`](hands-on/), so nobody gets in anybody's way.
Use your name in the file name, lower case with hyphens: `jane-doe.md`.

## Exercise 1 · Your first pull request (10 min)

1. Open the folder [`workshop/hands-on/`](hands-on/) and click **Add file → Create new file**.
2. Name it `your-name.md` and paste this, filled in (keep it to things you're happy to have on the internet):

   ```markdown
   # Jane Doe

   - What I work on: …
   - The kind of file I deal with most: …
   - Where I've used AI in my work so far: …
   ```

3. **Commit changes…** → **Create a new branch for this commit and start a pull request** → **Propose changes**
   → **Create pull request**.
4. Wait for the checks to go red, then **tick the AI declaration** in the description, honestly:
   - If you typed it yourself: **G0**, no models.
   - If you asked an AI to write or polish it: **G1** or **G2**, and tick the model (or **Other:** and write it).
   - Human review: at least **H1**. You wrote three lines and read them all: **H2** is fair.
   - AI review: **A0**, unless a fresh AI session checked it.
5. When both checks are green: **Merge pull request → Confirm merge → Delete branch**.
6. Check that your file is in [`workshop/hands-on/`](hands-on/) on `main`, and find your merge in the
   [history](https://github.com/industrial-mathematics-group/aisignoff-playground/commits/main).

## Exercise 2 · Break it on purpose (3 min)

Open a second small pull request (add a line to your file) and, before you tick properly, try:

- **two** generation boxes (G0 and G1),
- G1 without a model,
- only **H0**.

Each time, open the check's **Details** and read why it's red. Then tick it properly and merge, or close the
pull request without merging (**Close pull request**): also fine.

## Exercise 3 · Review your neighbour, with @signoff (7 min)

Pair up. Read your neighbour's file on `main` carefully, as if it were a paper draft. Then record your review:

1. **Issues → New issue → Blank issue**, title: `Review of jane-doe.md`.
2. In the text, write `@signoff` and what you did, in your own words, for example:

   > @signoff I, Omar Khan, read workshop/hands-on/jane-doe.md line by line as it is now and checked it with
   > Jane. Please record this as an independent review, H3, with me as reviewer.

3. Wait for the assistant's comment. If it asks something, answer in a new comment that starts with `@signoff`.
4. The bot opens a pull request. Look at **Files changed**: one entry added to `SIGNOFF.toml`, with your name.
5. In that pull request's description, **tick your human review** of the bot's change (did it write down what
   you said?). It's your responsibility now, even though a bot made the change. Merge it.

Why H3? H3 means "independently validated", and a **second person's line-by-line review** is one way to get
there. The author can't give themselves H3 by rereading.

## Optional · Upload a figure or a table (5 min)

**Add file → Upload files** in `workshop/hands-on/`, drag in a small picture or CSV that is already public or
made up (a plot of `y = x²` is perfect), then the same steps as exercise 1. If you made it with an AI tool, say
so: that's what the boxes are for.

---

[← 3 AI signoff](03-aisignoff.md) · [5 Releases and DOIs →](05-zenodo.md)
