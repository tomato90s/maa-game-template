import unittest
from pathlib import Path

from tools import dev


class DevCliTest(unittest.TestCase):
    def test_check_builds_validation_commands(self):
        commands = dev.build_commands(["check"])

        self.assertEqual(commands[0], ["npm", "ci"])
        self.assertEqual(commands[1], ["npx", "@nekosu/maa-tools", "check"])
        self.assertIn("tools/validate_schema.py", commands[2])

    def test_package_builds_install_command(self):
        commands = dev.build_commands(
            ["package", "--version", "v0.1.0", "--os", "macos", "--arch", "aarch64"]
        )

        self.assertEqual(
            commands,
            [["python", "tools/install.py", "v0.1.0", "macos", "aarch64"]],
        )

    def test_update_package_builds_manifest_command(self):
        commands = dev.build_commands(
            [
                "update-package",
                "--version",
                "v0.1.0",
                "--github-repo",
                "owner/repo",
                "--root",
                "install",
            ]
        )

        self.assertEqual(commands[0][:7], [
            "python",
            "tools/generate_update.py",
            "--version",
            "v0.1.0",
            "--root",
            "install",
            "--output-dir",
        ])
        self.assertIn("--github-repo", commands[0])
        self.assertIn("owner/repo", commands[0])
        self.assertIn("resource/image/**/*", commands[0])

    def test_bootstrap_forwards_arguments(self):
        commands = dev.build_commands(
            [
                "bootstrap",
                "--output",
                "../demo",
                "--project-name",
                "maa-demo",
                "--title",
                "MAA Demo",
                "--github-repo",
                "owner/demo",
                "--package",
                "com.example.demo",
                "--project-id",
                "MaaDemo",
                "--yes",
            ]
        )

        self.assertEqual(commands[0][0:2], ["python", "tools/bootstrap_project.py"])
        self.assertIn("--project-name", commands[0])
        self.assertIn("maa-demo", commands[0])


if __name__ == "__main__":
    unittest.main()
