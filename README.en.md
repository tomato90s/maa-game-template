# MAA Game Template

[中文](README.md) | English

A clean public template for building game automation projects with [MaaFramework](https://github.com/MaaXYZ/MaaFramework).

Use this repository when you want a small Maa project skeleton with:

- ProjectInterface v2 metadata in `assets/interface.json`
- Sample task wrappers under `assets/resource/tasks/`
- Sample pipeline files under `assets/resource/pipeline/`
- Optional Python agent entrypoint under `agent/`
- GitHub Actions for resource checks and release packaging

## Quick Start

1. Click **Use this template** on GitHub, or clone this repository.
2. Implement or edit `assets/interface.json` according to the Maa ProjectInterface protocol:
   - `name`
   - `title`
   - `description`
   - `github`
   - `welcome`
3. Replace the sample task in `assets/resource/pipeline/example.json` with real recognition and action nodes.
4. Run local checks:

```bash
python tools/dev.py check
```

See [Scripts and commands](docs/scripts.en.md) for the full command list.

## Repository Layout

```text
assets/
  interface.json
  resource/
    pipeline/
    tasks/
agent/
ci/
tools/
.github/workflows/
docs/
```

## Documentation

- [Project bootstrap checklist](docs/bootstrap.en.md)
- [Add a task](docs/add-task.en.md)
- [Default Python custom actions](docs/custom-actions.en.md)
- [Scripts and commands](docs/scripts.en.md)
- [CI workflows](docs/ci.en.md)
- [Release packaging](docs/release.en.md)

## Release

Push a `v*` tag to create a GitHub Release:

```bash
git tag v0.1.0
git push origin v0.1.0
```

Branch and pull request builds only produce CI artifacts. GitHub Releases are created only for `v*` tags.

## License

This template is released under the MIT License. Replace it if your project needs a different license.
