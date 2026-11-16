# Updating and pinning aisignoff

The aisignoff version is set in several places. Keep them in step: a snapshot or check produced by one version can fail when read by another.

## Where the version is set

| Place | How it is set | What it controls |
|---|---|---|
| The organisation's shared `file-signoff.yml` workflow | Its default (1.0.0rc8 at the time of writing) | The version used by [File-signoff](workflows.md) when you do not pin one |
| `.github/workflows/file-signoff.yml` | `aisignoff-version:` under `with:` (commented out) | Overrides the organisation default for the File-signoff check |
| `.github/workflows/signoff-release.yml` | `AISIGNOFF_VERSION` under `env:` (currently `"1.0.0rc8"`) | The version that writes the release reports |
| `extras/workflows/signoff-pr-diff.yml`, `extras/workflows/signoff-pr-files.yml` | `AISIGNOFF_VERSION` under `env:` (currently `"0.14.0"`) | The version used by the [optional workflows](optional-workflows.md) |
| `extras/workflows/file-signoff.yml` | `aisignoff-ref:` under `with:` (commented out) | Pins a release of aisignoff by tag; the default is `main` |
| Your local install | `pipx install aisignoff==<version>` | The version of `aisignoff` on your machine |

The `signoff-request.yml` workflow is also meant to carry its own pin. The README names it together with `file-signoff.yml` when it says where to set `aisignoff-version:`.

## Pin a version in File-signoff

By default File-signoff uses the organisation's default version. To use another release, uncomment the line in `.github/workflows/file-signoff.yml`:

```yaml
jobs:
  file-signoff:
    uses: industrial-mathematics-group/.github/.github/workflows/file-signoff.yml@main
    with:
      weight: lines
      aisignoff-version: "1.0.0rc3"
```

The value `1.0.0rc3` in the file is only an example of another release. Use the version you want.

## Pin a version in the release workflow

`signoff-release.yml` installs aisignoff itself and pins the version in an environment variable, so a new release cannot break the workflow without notice:

```yaml
env:
  AISIGNOFF_VERSION: "1.0.0rc8"
```

Change the value and the `pip install "aisignoff==${AISIGNOFF_VERSION}"` step installs that version. The optional workflows in `extras/workflows/` use the same mechanism. Their copies pin `0.14.0`, so update them when you copy them into `.github/workflows/`.

## Keep CI and your local install the same

Install the same version locally as CI uses:

```bash
pipx install aisignoff==1.0.0rc8
```

This matters most for snapshots. `SIGNOFF.snapshot.json` records the aisignoff version that wrote it (`"aisignoff": "1.0.0rc6"` in this repository). The check works the snapshot out again, so a snapshot written by one version than CI's can fail the check. See [snapshots and freezing](../concepts/snapshots-and-freeze.md) and [running aisignoff locally](../getting-started/local-commands.md).

## Update checklist

1. Choose the new version.
2. Set it in every place from the table above that you pin: `aisignoff-version:` in `file-signoff.yml` and `signoff-request.yml`, and `AISIGNOFF_VERSION` in `signoff-release.yml` and the copies of the `extras/` workflows.
3. Reinstall locally with `pipx install aisignoff==<version>`.
4. Run `aisignoff lint` and check that the File-signoff run is green.
5. If a snapshot check fails, see [troubleshooting](../troubleshooting.md).
