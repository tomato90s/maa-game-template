# Release Packaging

## Create a Release

Create and push a `v*` tag:

```bash
git tag v0.1.0
git push origin v0.1.0
```

The `install.yml` workflow will:

1. Download MaaFramework.
2. Set up embedded Python.
3. Copy `assets/resource`, `assets/interface.json`, and `agent`.
4. Install Python dependencies.
5. Upload platform artifacts.
6. Create a GitHub Release for the tag.
7. Generate resource update packages and manifests.

## Manual Test Build

Use GitHub Actions **Run workflow** on `install.yml` to produce artifacts without creating a GitHub Release.

## Resource Update Packages

The release workflow includes these paths in update packages:

```text
agent/**/*.py
resource/**/*.json
resource/image/**/*
resource/model/**/*
interface.json
```

Add more include patterns in `.github/workflows/install.yml` if your project needs to update other resources.
