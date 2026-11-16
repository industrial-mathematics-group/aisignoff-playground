# Snapshots and freezing declarations

A snapshot writes the declarations of every line into a file, `SIGNOFF.snapshot.json`, so they no longer depend on the git history or on later changes to `SIGNOFF.toml`. You create it with `aisignoff freeze`.

## Why freeze

With `[history]` enabled, aisignoff works out each line's declaration from the commit that landed it on `main`. That information lives in the git history, and the fallback annotations in `SIGNOFF.toml` can change over time. A snapshot fixes the result at one commit:

- The declarations of the pull requests are kept in a file in the repository, so they are archived with the files (for example in a release).
- **Frozen lines keep their levels.** If you change an annotation in `SIGNOFF.toml` after a freeze, lines that are in the snapshot keep the levels they had. `aisignoff report --files` stays unchanged for them.

## What the file holds

`SIGNOFF.snapshot.json` has these top-level keys:

| Key | Content |
|---|---|
| `format` | The version of the snapshot file format (`1` here). |
| `aisignoff` | The version of aisignoff that wrote the snapshot. |
| `rules` | A number recorded by the freeze; this repository's file has `2`. |
| `commit` | The full hash of the commit the snapshot was taken at. |
| `declarations` | A list of distinct declarations. Each entry has `AI-Generation`, `Human-Review`, `AI-Review`, the name lists `Assisted-by`, `AI-Reviewed-by` and `Reviewed-by`, and a `source` that says where the declaration came from. |
| `files` | One entry per file, with its `blob` (the git object hash of the content) and `runs`. |

A `source` is, for example, `SIGNOFF.toml [1]` (the first annotation), a commit with its subject and "pull request checkboxes", or `inline`.

### Line runs

Each file lists `runs` as `[first line, last line, declaration index]`. The index points into the `declarations` list, counting from 0. This entry from the snapshot of this repository:

```json
"README.md": {"blob": "62ca5aa3…", "runs": [[1, 2, 0], [3, 12, 3], [13, 27, 0], …]}
```

means that lines 1 to 2 of `README.md` use declaration 0, lines 3 to 12 use declaration 3, and so on. A file declared as a whole has one run, such as `[[1, 20, 0]]`.

The `blob` ties the runs to one exact version of the file. A file whose content has changed since the freeze no longer matches its blob, so the snapshot does not apply to the changed lines.

## Commands

=== "Take a snapshot"

    ```bash
    git switch --detach origin/main
    aisignoff freeze --prune
    ```

    Writes `SIGNOFF.snapshot.json`. With `--prune`, the command is run as in the README's freeze scenario, which then commits `SIGNOFF.snapshot.json` and `SIGNOFF.toml`.

=== "Check"

    ```bash
    aisignoff freeze --check
    ```

    Runs the snapshot check on its own.

=== "Reset a file"

    ```bash
    aisignoff freeze --reset docs/notes.md
    ```

    Run on `main` to apply the current annotations to that file, instead of its frozen levels.

## Freezing in a pull request

The README's scenario 6 takes a snapshot after a few pull requests have landed:

```bash
git switch --detach origin/main
aisignoff freeze --prune
git switch -c freeze
git add SIGNOFF.snapshot.json SIGNOFF.toml && git commit -m "Freeze the declarations"
git push -u origin freeze
```

Open a pull request for the `freeze` branch and declare it like any other (for example G0 · H2 · A0, or "Key: value" lines in the description).

**Expect:** lint in the pull request checks the snapshot by working it out again, and passes.

## The snapshot is checked

Lint does not trust the file. It works the declarations out again and compares them with the snapshot.

- If you edit a level in `SIGNOFF.snapshot.json` by hand, lint fails.
- A snapshot written by a different aisignoff version than the one CI runs can fail the check. Keep your local install at the same version as CI; see [Running aisignoff locally](../getting-started/local-commands.md).

## Scripts with inline tags

`scripts/make_results.py` has a header comment with tags. From aisignoff 1.0.0rc7 on, that comment no longer counts as a declaration. Its former levels (G1 · H2 · A0) are kept in the snapshot with the source `inline`, which is how the file still has them.
