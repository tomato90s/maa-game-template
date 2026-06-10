#!/usr/bin/env python3
import argparse
import re
import subprocess
import sys


RESOURCE_PATTERNS = [
    "agent/**/*.py",
    "resource/**/*.json",
    "resource/image/**/*",
    "resource/model/**/*",
    "interface.json",
]


def build_parser():
    parser = argparse.ArgumentParser(
        description="Developer command wrapper for the Maa game template."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("check", help="Run local resource and schema checks.")

    package = subparsers.add_parser("package", help="Build the local install/ directory.")
    package.add_argument("--version", required=True)
    package.add_argument("--os", required=True, choices=["win", "macos", "linux", "android"])
    package.add_argument("--arch", required=True, choices=["x86_64", "aarch64"])

    update = subparsers.add_parser(
        "update-package",
        help="Generate a resource update zip and manifest from an install root.",
    )
    update.add_argument("--version", required=True)
    update.add_argument(
        "--github-repo",
        default="",
        help="GitHub repository in owner/repo format. Defaults to git origin.",
    )
    update.add_argument("--root", default="install")
    update.add_argument("--output-dir", default=".")
    update.add_argument("--platform", default="")

    return parser


def infer_github_repo():
    try:
        result = subprocess.run(
            ["git", "remote", "get-url", "origin"],
            check=True,
            capture_output=True,
            text=True,
        )
    except subprocess.CalledProcessError:
        return "OWNER/REPO"

    return _parse_github_repo(result.stdout.strip())


def _parse_github_repo(remote):
    patterns = [
        r"github\.com[:/](?P<repo>[^/]+/[^/.]+)(?:\.git)?$",
        r"github\.com/(?P<repo>[^/]+/[^/.]+)(?:\.git)?$",
    ]
    for pattern in patterns:
        match = re.search(pattern, remote)
        if match:
            return match.group("repo")

    return "OWNER/REPO"


def build_commands(argv):
    args = build_parser().parse_args(argv)

    if args.command == "check":
        return [
            ["npm", "ci"],
            ["npx", "@nekosu/maa-tools", "check"],
            [
                "python",
                "tools/validate_schema.py",
                "--schema-dir",
                "deps/tools",
                "--resource-dirs",
                "assets/resource/pipeline",
                "--interface-files",
                "assets/interface.json",
                "--task-dirs",
                "assets/resource/tasks",
            ],
        ]

    if args.command == "package":
        return [["python", "tools/install.py", args.version, args.os, args.arch]]

    if args.command == "update-package":
        github_repo = args.github_repo or infer_github_repo()
        return [
            [
                "python",
                "tools/generate_update.py",
                "--version",
                args.version,
                "--root",
                args.root,
                "--output-dir",
                args.output_dir,
                "--github-repo",
                github_repo,
                "--include",
                *RESOURCE_PATTERNS,
                *(
                    ["--platform", args.platform]
                    if args.platform
                    else []
                ),
            ]
        ]

    raise ValueError(f"Unknown command: {args.command}")


def run_commands(commands):
    for command in commands:
        print("+ " + " ".join(command))
        subprocess.run(command, check=True)


def main(argv=None):
    commands = build_commands(sys.argv[1:] if argv is None else argv)
    run_commands(commands)
    return 0


if __name__ == "__main__":
    sys.exit(main())
