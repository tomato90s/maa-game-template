# Project Bootstrap Checklist

[中文](bootstrap.md)

After creating a repository with GitHub **Use this template**, use this checklist to adapt the project.

The template does not generate or rewrite `interface.json`. Implement it yourself according to the Maa ProjectInterface protocol and your project needs.

## 1. Project Metadata

Edit `assets/interface.json`:

- `name`: machine-readable project id, such as `maa-example-game`
- `title`: display title, such as `MAA Example Game`
- `description`: short project description
- `github`: your repository URL
- `welcome`: first-run message shown by compatible launchers

## 2. CI Project Name

Edit `.github/workflows/install.yml`:

```yaml
env:
  PROJECT_ID: MaaGameTemplate
```

`PROJECT_ID` is the prefix for CI artifacts and release packages. For a real project, change it to your project name, such as `MaaExampleGame`.

## 3. README

Edit `README.md`:

- Replace the template description with your game-specific description.
- Document supported emulator, resolution, language, and login assumptions.
- Remove sample notes that do not fit your project.

## 4. Sample Tasks

`assets/resource/pipeline/startup.json` and `assets/resource/pipeline/example.json` are only examples.

Not every project needs to start the game automatically. If you do not need it, delete the sample startup task or replace it with a node that verifies the game is already open.

## 5. Assets

Put screenshots and template images in:

```text
assets/resource/image/
```

Put OCR models in:

```text
assets/resource/model/ocr/
```

The template does not include OCR model files by default. Add your own models or copy them from Maa common assets when your project needs OCR.

## 6. Schema Files

The template keeps MaaFramework JSON schema files in:

```text
deps/tools/
```

Refresh these files from MaaFramework when you upgrade to a new schema version.
