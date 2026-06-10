# Bootstrap a New Game Project

Start with the smallest working rename, then add real game resources.

## Bootstrap Helper

From this template repository, run:

```bash
python tools/bootstrap_project.py \
  --output ../maa-demo-game \
  --project-name maa-demo-game \
  --title "MAA Demo Game" \
  --github-repo your-name/maa-demo-game \
  --package com.example.game \
  --project-id MaaDemoGame \
  --yes
```

The helper copies the template to the output directory, skips local build/runtime artifacts, and replaces the main project fields.

## Maintainer Note: Enable GitHub Template Mode

If you maintain the template repository itself, enable GitHub template mode after pushing it:

1. Open the repository on GitHub.
2. Go to **Settings**.
3. Enable **Template repository**.
4. Return to the repository home page and use **Use this template** to create new projects.

Repositories created from a template start with a fresh history. They are not forks and do not automatically receive later template updates.

## Required Renames

Edit `assets/interface.json`:

- `name`: machine-readable project id, such as `maa-example-game`
- `title`: display title, such as `MAA Example Game`
- `description`: short project description
- `github`: your repository URL
- `welcome`: first-run message shown by compatible launchers

Edit `.github/workflows/install.yml`:

- `PROJECT_ID`: artifact prefix used by CI and GitHub Releases

Edit `README.md`:

- Replace the template description with your game-specific description.
- Document supported emulator, resolution, language, and login assumptions.

## Startup Package

Replace the placeholder package in `assets/resource/pipeline/startup.json`:

```json
"package": "com.example.game"
```

Use your actual Android package name. If your project does not start the game automatically, replace `StartApp` with a node that verifies the game is already open.

## Assets

Put screenshots and template images in:

```text
assets/resource/image/
```

Put OCR models in:

```text
assets/resource/model/ocr/
```

The template does not include OCR model files by default. Add your own models or copy them from Maa common assets when your project needs OCR.

## Schema Files

The template keeps MaaFramework JSON schema files in:

```text
deps/tools/
```

Refresh these files from MaaFramework when you upgrade to a new schema version.
