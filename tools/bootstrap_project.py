#!/usr/bin/env python3
import argparse
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_NAMES = {
    ".DS_Store",
    ".git",
    ".idea",
    ".vscode",
    ".worktrees",
    "node_modules",
    "install",
    "release-artifacts",
    "__pycache__",
}
SKIP_SUFFIXES = {
    ".pyc",
    ".log",
}


def parse_args():
    parser = argparse.ArgumentParser(
        description="Create a new MaaFramework project from this template."
    )
    parser.add_argument("--output", required=True, type=Path, help="Output directory.")
    parser.add_argument(
        "--project-name",
        required=True,
        help="Project id for interface.json, for example maa-demo-game.",
    )
    parser.add_argument(
        "--title",
        required=True,
        help="Display title, for example MAA Demo Game.",
    )
    parser.add_argument(
        "--github-repo",
        required=True,
        help="GitHub repository in owner/repo format.",
    )
    parser.add_argument(
        "--package",
        required=True,
        help="Android package name, for example com.example.game.",
    )
    parser.add_argument(
        "--project-id",
        required=True,
        help="CI artifact prefix, for example MaaDemoGame.",
    )
    parser.add_argument(
        "--description",
        default="A MaaFramework game automation project.",
        help="Project description for interface.json and README.",
    )
    parser.add_argument(
        "--yes",
        action="store_true",
        help="Run without an interactive confirmation prompt.",
    )
    return parser.parse_args()


def should_skip(path: Path) -> bool:
    return path.name in SKIP_NAMES or path.suffix in SKIP_SUFFIXES


def copy_template(output: Path):
    if output.exists() and any(output.iterdir()):
        raise SystemExit(f"Output directory is not empty: {output}")

    output.mkdir(parents=True, exist_ok=True)

    for item in ROOT.iterdir():
        if should_skip(item):
            continue

        target = output / item.name
        if item.is_dir():
            shutil.copytree(
                item,
                target,
                ignore=shutil.ignore_patterns(
                    ".git",
                    ".idea",
                    ".vscode",
                    ".worktrees",
                    "node_modules",
                    "install",
                    "release-artifacts",
                    "__pycache__",
                    "*.pyc",
                    "*.log",
                ),
            )
        elif item.is_file():
            shutil.copy2(item, target)


def update_interface(output: Path, args):
    interface_path = output / "assets" / "interface.json"
    interface = json.loads(interface_path.read_text(encoding="utf-8"))
    interface["name"] = args.project_name
    interface["title"] = args.title
    interface["description"] = args.description
    interface["github"] = f"https://github.com/{args.github_repo}"
    interface["welcome"] = (
        f"Welcome to {args.title}. Configure emulator settings, replace sample "
        "resources, and add project tasks before release."
    )
    interface_path.write_text(
        json.dumps(interface, ensure_ascii=False, indent=4) + "\n",
        encoding="utf-8",
    )


def update_startup(output: Path, package_name: str):
    startup_path = output / "assets" / "resource" / "pipeline" / "startup.json"
    startup = json.loads(startup_path.read_text(encoding="utf-8"))
    startup["StartApp"]["action"]["param"]["package"] = package_name
    startup_path.write_text(
        json.dumps(startup, ensure_ascii=False, indent=4) + "\n",
        encoding="utf-8",
    )


def replace_text(path: Path, replacements: dict[str, str]):
    text = path.read_text(encoding="utf-8")
    for old, new in replacements.items():
        text = text.replace(old, new)
    path.write_text(text, encoding="utf-8")


def update_text_files(output: Path, args):
    replacements = {
        "MAA Game Template": args.title,
        "maa-game-template": args.project_name,
        "MaaGameTemplate": args.project_id,
        "https://github.com/OWNER/REPO": f"https://github.com/{args.github_repo}",
        "OWNER/REPO": args.github_repo,
        "com.example.game": args.package,
        "A clean public template for building game automation projects with [MaaFramework](https://github.com/MaaXYZ/MaaFramework).": args.description,
    }

    for relative in [
        "README.md",
        "package.json",
        "package-lock.json",
        ".github/workflows/install.yml",
        "docs/bootstrap.md",
        "docs/release.md",
    ]:
        path = output / relative
        if path.exists():
            replace_text(path, replacements)


def main():
    args = parse_args()
    output = args.output.resolve()

    if not args.yes:
        answer = input(f"Create project at {output}? [y/N] ")
        if answer.lower() not in {"y", "yes"}:
            print("Cancelled.")
            return 1

    copy_template(output)
    update_interface(output, args)
    update_startup(output, args.package)
    update_text_files(output, args)

    print(f"Created {args.title} at {output}")
    print("Next steps:")
    print("  1. Review assets/interface.json")
    print("  2. Replace sample pipeline nodes and resources")
    print("  3. Run npm ci && npx @nekosu/maa-tools check")
    return 0


if __name__ == "__main__":
    sys.exit(main())
