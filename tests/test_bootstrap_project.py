import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "tools" / "bootstrap_project.py"


class BootstrapProjectTest(unittest.TestCase):
    def test_bootstrap_copies_template_and_replaces_project_values(self):
        with tempfile.TemporaryDirectory() as tmp:
            output_dir = Path(tmp) / "generated"

            subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--output",
                    str(output_dir),
                    "--project-name",
                    "maa-demo-game",
                    "--title",
                    "MAA Demo Game",
                    "--github-repo",
                    "example/maa-demo-game",
                    "--package",
                    "com.example.demo",
                    "--project-id",
                    "MaaDemoGame",
                    "--yes",
                ],
                cwd=ROOT,
                check=True,
            )

            interface = json.loads((output_dir / "assets" / "interface.json").read_text())
            startup = json.loads(
                (output_dir / "assets" / "resource" / "pipeline" / "startup.json").read_text()
            )
            workflow = (output_dir / ".github" / "workflows" / "install.yml").read_text()

            self.assertEqual(interface["name"], "maa-demo-game")
            self.assertEqual(interface["title"], "MAA Demo Game")
            self.assertEqual(interface["github"], "https://github.com/example/maa-demo-game")
            self.assertEqual(
                startup["StartApp"]["action"]["param"]["package"],
                "com.example.demo",
            )
            self.assertIn("PROJECT_ID: MaaDemoGame", workflow)
            self.assertFalse((output_dir / "node_modules").exists())
            self.assertFalse((output_dir / ".git").exists())


if __name__ == "__main__":
    unittest.main()
