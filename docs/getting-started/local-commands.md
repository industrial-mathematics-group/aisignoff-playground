# Running aisignoff locally

The same `aisignoff` tool that CI runs can be installed on your machine, so you can check declarations and see the reports before you push.

## Install

Install it with pipx, at the version CI uses:

```bash
pipx install aisignoff==1.0.0rc9
```

The playground pins `1.0.0rc9` in `file-signoff.yml` and `pr-signoff.yml`, and `signoff-release.yml` pins the same version in `AISIGNOFF_VERSION`. If you pin another version in `file-signoff.yml` (with `aisignoff-version:`), install that one locally. See [Updating and pinning aisignoff](../deploy-extend/updating-aisignoff.md).

!!! warning
    Keep your local install at the same version as CI. A snapshot written by another version than CI's can fail the check. See [snapshots and freezing](../concepts/snapshots-and-freeze.md).

## Commands

Run these from the root of the repository.

| Command | What it shows |
|---|---|
| `aisignoff lint` | Checks that every file is declared and that the policy is met. This is the check File-signoff runs in CI. |
| `aisignoff report --files` | The declaration of each file. With `[history]` turned on, a file whose lines have different declarations shows the share of each. |
| `aisignoff diff HEAD^1 --files` | The levels of the lines that the latest commit added. On a merge commit, `HEAD^1` is the first parent, so this shows what the merge brought into `main`. |
| `aisignoff report --json` | Every file with its levels, and every line run with its source. |

### Lint

```bash
aisignoff lint
```

It fails when a file has no valid declaration or when the policy in `SIGNOFF.toml` is not met (see [policy](../concepts/policy.md)). A annotation for a path that does not exist makes it warn but pass. `aisignoff lint --strict` fails on such warnings too.

### Report per file

```bash
aisignoff report --files
```

Use it after a merge to see how the lines landed. For example, a file that was mostly declared as G0 · H2 · A0 and then changed through a pull request shows a share at the levels ticked in that pull request.

### Diff of a commit

```bash
aisignoff diff HEAD^1 --files
```

This is how you check what a merged pull request declared for the lines it added. The reviewer recorded for them is the author of the merge commit, that is, whoever clicked *Merge*.

### JSON report

```bash
aisignoff report --json
```

Use it when you want to process the result with another tool. With `[history]`, it lists every line run together with where its declaration came from.

## Why the version should match CI

CI runs `aisignoff` at a fixed version. Anything you generate locally that CI later checks again should come from the same version:

- **Snapshots.** `SIGNOFF.snapshot.json` records the version that wrote it in its `aisignoff` field. Lint works the snapshot out again and compares, so a snapshot written by a different version than CI's can fail the check.
- **Results.** Reports and lint results can differ between versions, so a local green run is only a good predictor of CI when the versions agree.

To see which version CI uses, look at `aisignoff-version:` in `.github/workflows/file-signoff.yml`. If it is unset, the organisation's default applies.

## Next

- [Try-out scenarios](../usage/scenarios.md) use these commands to check the expected results.
- [Snapshots and freezing](../concepts/snapshots-and-freeze.md) explains `aisignoff freeze` and `freeze --check`.
