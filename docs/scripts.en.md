# Scripts and Commands

For daily work, prefer one entry point:

```bash
python tools/dev.py <command>
```

Lower-level scripts are still available for CI and advanced debugging.

[中文](scripts.md)

## Common Commands

### Create a project from this template

Use this command to copy the template into a new Maa game project and replace the project name, repository, package name, and CI artifact prefix.

```bash
python tools/dev.py bootstrap \
  --output ../maa-demo-game \
  --project-name maa-demo-game \
  --title "MAA Demo Game" \
  --github-repo owner/maa-demo-game \
  --package com.example.game \
  --project-id MaaDemoGame \
  --yes
```

The lower-level script is:

```bash
python tools/bootstrap_project.py ...
```

### Run local checks

Use this before committing to validate resources, schemas, and Maa project structure.

```bash
python tools/dev.py check
```

It runs:

```bash
npm ci
npx @nekosu/maa-tools check
python tools/validate_schema.py \
  --schema-dir deps/tools \
  --resource-dirs assets/resource/pipeline \
  --interface-files assets/interface.json \
  --task-dirs assets/resource/tasks
```

The first `maa-tools` run may need network access to prepare the MaaFramework checking runtime.

### Build the local install directory

Use this to simulate the CI package flow locally. It outputs `install/`.

Apple Silicon Mac example:

```bash
python tools/dev.py package \
  --version v0.0.0 \
  --os macos \
  --arch aarch64
```

Intel Mac example:

```bash
python tools/dev.py package \
  --version v0.0.0 \
  --os macos \
  --arch x86_64
```

Windows x64 example:

```bash
python tools/dev.py package \
  --version v0.0.0 \
  --os win \
  --arch x86_64
```

This command requires local MaaFramework files:

```text
deps/
  bin/
  share/MaaAgentBinary/
```

### Generate a resource update package

This is usually used by the CI release workflow. Run it locally when debugging release packaging.

```bash
python tools/dev.py update-package \
  --version v0.0.0 \
  --github-repo owner/repo \
  --root install
```

Output files:

```text
resource-manifest.json
resource-update-v0.0.0.zip
```

## Script Categories

### Daily Entry Point

`tools/dev.py`

The unified command wrapper for daily development. Prefer this over memorizing every lower-level script.

### Project Bootstrap

`tools/bootstrap_project.py`

Copies this template into a new project and replaces metadata. Usually called through `tools/dev.py bootstrap`.

### Local and CI Packaging

`tools/install.py`

Builds `install/` from `assets/`, `agent/`, and local `deps/`. CI calls this directly. Locally, prefer `tools/dev.py package`.

`tools/configure.py`

Called by `install.py`. If `assets/MaaCommonAssets/OCR` exists, it copies the default OCR model into `assets/resource/model/ocr`.

### Validation

`tools/validate_schema.py`

Validates pipeline, task, and interface JSON files. Usually called by `tools/dev.py check` or CI.

### Release Resource Updates

`tools/generate_update.py`

Generates a resource update zip and manifest. Usually called by the release workflow. Locally, prefer `tools/dev.py update-package`.

### CI Embedded Python

These scripts are CI-only. You usually do not run them manually:

```text
ci/setup_embed_python.sh
ci/setup_embed_python.ps1
ci/setup_pip.py
```

### Runtime Agent

These are not developer commands. MaaFramework uses them at runtime:

```text
agent/main.py
agent/actions.py
```

`agent/main.py` starts the Python AgentServer.

`agent/actions.py` registers default custom actions such as `CenterClick`, `OffsetClick`, `NodeOverride`, and `DisableNode`.

## Local MaaFramework Files

Local debugging and packaging use MaaFramework runtime files under:

```text
deps/
  bin/
  share/MaaAgentBinary/
```

These runtime files are ignored by Git and should not be committed.

The repository only commits:

```text
deps/tools/*.schema.json
```

These schema files are used for local and CI JSON validation.
