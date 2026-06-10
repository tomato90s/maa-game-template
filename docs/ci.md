# CI Workflows

## check.yml

`check.yml` runs on pushes, pull requests, and manual dispatch. It does two things:

- Installs npm dependencies and runs `npx @nekosu/maa-tools check`
- Validates pipeline, task, and interface JSON files with `tools/validate_schema.py`

Use this workflow to catch broken task imports, invalid JSON, and schema errors before release packaging.

Schema files are stored in `deps/tools/*.schema.json` so local checks and CI can run without a separate bootstrap step.

## sync_schema_files.yml

`sync_schema_files.yml` is manual-only. Run it from GitHub Actions when you want to refresh `deps/tools/*.schema.json` from MaaFramework `main`.

## install.yml

`install.yml` packages the project with MaaFramework and embedded Python. By default it builds:

- Windows x64
- macOS arm64

The release job runs only for refs that start with `refs/tags/v`. Normal branch and pull request runs upload CI artifacts but do not create GitHub Releases.

## Project Variables

Edit these values when you create a real project:

- `PROJECT_ID` in `.github/workflows/install.yml`
- `MAAFW_VERSION` in `.github/workflows/install.yml` if you want to pin MaaFramework

The update manifest repository is passed from GitHub Actions as `${{ github.repository }}`.
