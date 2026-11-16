# Try-out scenarios

Seven short exercises that show how declarations behave in this repository, each with the result you should see. Run them in order, or pick the ones you want to understand.

In pull requests, fill the template by ticking boxes: exactly one generation box, the models, human review and AI review. See [declaring a pull request](declaring-a-pull-request.md).

Concepts behind the results: [declaration levels](../concepts/declaration-levels.md), [line-level history](../concepts/line-level-history.md), [policy](../concepts/policy.md) and [snapshots and freezing](../concepts/snapshots-and-freeze.md).

## 1. Plain push to main

Edit `docs/notes.md`, commit with a plain message and push to `main`.

**Expect:** lint is green. The new lines declare nothing, so they take the file-level declaration (G0 · H2 · A0). `aisignoff report --files` is unchanged.

Variant: put "Key: value" lines in the commit message (`AI-Generation: G2`, `Assisted-by: …`, `Human-Review: H1`, `Reviewed-by: …`, `AI-Review: A1`, `AI-Reviewed-by: …`).

**Expect:** `aisignoff report --files` shows `docs/notes.md` partly at G2. See [inline tags and commit trailers](inline-tags-and-commit-trailers.md).

## 2. Pull request into main

Create a branch, change `src/playground/stats.py` and open a pull request into `main`.

| What you do | Expected result |
|---|---|
| Leave the template untouched | `aisignoff / lint` and `pr-signoff / check` fail (unfilled template, `TODO`) |
| Tick G2, Claude Opus, H1, A1 | Both checks turn green after the edit, without a new push (the description check reruns on `edited`) |
| Tick only H0 | Policy failure: H1 is required |
| Tick G1 and G2 together | Error: more than one generation box |

Merge it on GitHub with a merge commit.

**Expect:** on `main`, `aisignoff report --files` shows `stats.py` as mostly G0 · H2 · A0 plus a share at the ticked levels. `aisignoff diff HEAD^1 --files` shows the added lines at G2 · H1 · A1. Their reviewer is the merge commit's author, that is, whoever clicked *Merge*.

## 3. Stacked pull requests

Branch `a` from `main`, then branch `b` from `a`. Open PR A (`a` → `main`) and PR B (`b` → `a`).

**Expect:** PR B's description is not checked by aisignoff, because it does not go into the default branch, and PR-signoff only checks pull requests into `main`. Merge B into A, then A into `main`: A's description declares all the lines, B's included.

Variant: merge A first, let GitHub retarget B to `main`, then merge B.

**Expect:** B's description now counts, for the lines B's merge brings in.

## 4. Something undeclared

Change the `results/**` annotation to `AI-Review = "A0"`.

**Expect:** lint fails with a policy error, because G3 needs A1.

Alternatively, add an annotation for a path that does not exist.

**Expect:** lint passes but warns. `lint --strict` would fail.

## 5. Squash merge

Set `merge-method = "squash"` in `SIGNOFF.toml` and land that change first. Then open a pull request with a few commits, some of them with `AI-Generation: G3` in their messages, and squash-merge it.

**Expect:** the squash commit's description declares all its lines. The generation in the branch commits is ignored.

With `merge-method = "merge"` and a merge commit instead, a branch commit with `AI-Generation: G3` raises the generation of the lines it wrote.

## 6. Freeze

Once a few pull requests have landed, take a snapshot:

```bash
git switch --detach origin/main
aisignoff freeze --prune
git switch -c freeze
git add SIGNOFF.snapshot.json SIGNOFF.toml && git commit -m "Freeze the declarations"
git push -u origin freeze      # and open a PR (tick G0 / H2 / A0, or "Key: value" lines)
```

**Expect:** lint in the pull request checks the snapshot by working it out again, and is green. Then try:

- Edit a level in `SIGNOFF.snapshot.json` by hand and push. **Expect:** lint fails.
- After the freeze has landed, change the `**` annotation. **Expect:** frozen lines keep their levels, so `aisignoff report --files` is unchanged. Running `aisignoff freeze --reset docs/notes.md` on `main` applies the change to that file.
- Run `aisignoff freeze --check` to run the snapshot check on its own.

## 7. Merge queue (optional)

Turn on the merge queue in the ruleset.

**Expect:** the `merge_group` run says it checks `HEAD` as landed, and fails if the description was left unfilled.
