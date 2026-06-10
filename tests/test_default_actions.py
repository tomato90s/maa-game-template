import ast
import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_actions_module():
    spec = importlib.util.spec_from_file_location(
        "template_actions", ROOT / "agent" / "actions.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class DefaultActionsTest(unittest.TestCase):
    def test_center_point_uses_box_center_and_optional_offset(self):
        actions = load_actions_module()

        self.assertEqual(actions.center_point((10, 20, 30, 40)), (25, 40))
        self.assertEqual(actions.center_point((10, 20, 30, 40), 3, -5), (28, 35))

    def test_parse_offset_accepts_empty_and_json_params(self):
        actions = load_actions_module()

        self.assertEqual(actions.parse_offset(None), (0, 0))
        self.assertEqual(actions.parse_offset(""), (0, 0))
        self.assertEqual(actions.parse_offset('{"x": 12, "y": -4}'), (12, -4))

    def test_main_imports_actions_to_register_decorators(self):
        tree = ast.parse((ROOT / "agent" / "main.py").read_text(encoding="utf-8"))
        imports = [
            alias.name
            for node in tree.body
            if isinstance(node, ast.ImportFrom) and node.module == "agent"
            for alias in node.names
        ]

        self.assertIn("actions", imports)


if __name__ == "__main__":
    unittest.main()
