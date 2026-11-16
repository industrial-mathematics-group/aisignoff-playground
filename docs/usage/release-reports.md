# Release reports and Zenodo

Every published GitHub release gets the AI signoff reports attached as assets, and Zenodo can archive the release under a DOI. Together they let anyone see how a version was made and reviewed, and cite the exact files behind a paper, without cloning the repository.

## The release report workflow

`.github/workflows/signoff-release.yml` runs when a release is published (`release: types: [published]`). It checks out the release tag with the whole history (`fetch-depth: 0`), so line-by-line declarations from `[history]` can be worked out. It installs aisignoff at the version set in `AISIGNOFF_VERSION` (`1.0.0rc8` in this repository) and uploads three files to the release.

| Asset | Content | Command |
|---|---|---|
| `aisignoff-report.txt` | The summary per axis and the level mix per folder | `aisignoff report --landed` and `aisignoff report --tree --landed` |
| `aisignoff-report.json` | Every file with its levels, names and source | `aisignoff report --json --landed` |
| `aisignoff-report.html` | The interactive folder report | `aisignoff report --html <file> --landed` |

You find them under the release's *Assets*.

The reports describe the code at the release tag. They are written to a temporary directory outside the work tree, so `aisignoff lint` does not count them as undeclared files.

### Why `--landed`

With `--landed`, the release is reported as it is, also when it is cut from a release branch. Commits on such a branch would otherwise not count as landed. The workflow comment names aisignoff 0.12 as the first version with this option.

### Undeclared files do not block the release

After writing the reports, the workflow runs `aisignoff lint --landed`. If some files have no valid declaration, it does not fail. It writes a warning (`Some files in this release have no valid declaration`), and the reports list those files as undeclared.

!!! note
    The workflow needs `contents: write` to upload the assets. Upload uses `gh release upload --clobber`, so running it again for the same tag replaces the earlier files.

## Archiving releases on Zenodo

[Zenodo](https://zenodo.org) is a free research archive. Connected to GitHub, it archives every published release and gives it a DOI. Drafts, ordinary pushes and merges are never archived.

### Once per repository

1. Log in at <https://zenodo.org> with **Log in with GitHub**.
2. Open your account menu, choose **GitHub**, click **Sync now**, find the repository and switch it **On**. For an organisation repository you need admin rights, and the organisation may first have to allow Zenodo.
3. Keep a `CITATION.cff` in the repository. GitHub then shows **Cite this repository**, and Zenodo takes its metadata from the file.

The repository must be public. It should also have a licence (a `LICENSE` file, or `license:` in `CITATION.cff`) so people know what they may do with the files.

### The CITATION.cff of this repository

`CITATION.cff` here sets the title, an abstract, the author, the repository URL, `type: software` and some keywords. Its message says this is a playground for trying aisignoff.

### Every release

1. On GitHub, choose **Releases → Draft a new release**.
2. Choose a tag, type a new version such as `v1.0.0`, and select **Create new tag**.
3. Add a title and a few lines on what is new. **Generate release notes** lists the merged pull requests.
4. Select **Publish release**.

A few minutes later Zenodo has archived the release. Two DOIs exist:

| DOI | Points to | Use it for |
|---|---|---|
| Version DOI | Exactly this release | A paper: the files you actually used |
| Concept DOI | Always the newest release | The README badge, "cite this software" |

To add a badge, copy the Markdown of the DOI badge from the Zenodo record into the README. To make **Cite this repository** show the DOI as well, add the concept DOI under `identifiers:` in `CITATION.cff`.

!!! warning
    A published DOI is permanent. Zenodo records cannot be deleted, only followed by newer versions. To practise, use the [Zenodo Sandbox](https://sandbox.zenodo.org), which works the same with test DOIs. Do not put anything in a release you could not publish.

## What ends up in the archive

- `SIGNOFF.toml` is a file in the repository, so it is archived with every release. The declarations of the files go to Zenodo too.
- Declarations of single pull requests live in the git history, which Zenodo does not archive. Before a release, a maintainer can take a snapshot with `aisignoff freeze`. It writes them into `SIGNOFF.snapshot.json`, which is archived as well. See [snapshots and freezing](../concepts/snapshots-and-freeze.md).
- The release report assets are attached to the GitHub release by the workflow above. Whether Zenodo's copy contains them depends on Zenodo, so the files in the repository (`SIGNOFF.toml`, `SIGNOFF.snapshot.json`) are the part that is certain to be archived.
