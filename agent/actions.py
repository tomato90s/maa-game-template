import json

try:
    from maa.agent.agent_server import AgentServer
    from maa.custom_action import CustomAction
    from maa.context import Context
except ModuleNotFoundError:
    AgentServer = None
    CustomAction = None
    Context = None


def center_point(box, offset_x=0, offset_y=0):
    x, y, width, height = box
    return x + width // 2 + offset_x, y + height // 2 + offset_y


def parse_offset(raw_param):
    if not raw_param:
        return 0, 0

    param = json.loads(raw_param)
    return int(param.get("x", 0)), int(param.get("y", 0))


def _register_actions():
    @AgentServer.custom_action("CenterClick")
    class CenterClick(CustomAction):
        def run(
            self,
            context: Context,
            argv: CustomAction.RunArg,
        ) -> CustomAction.RunResult:
            x, y = center_point(argv.box)
            context.tasker.controller.post_click(x, y).wait()
            return CustomAction.RunResult(success=True)

    @AgentServer.custom_action("OffsetClick")
    class OffsetClick(CustomAction):
        def run(
            self,
            context: Context,
            argv: CustomAction.RunArg,
        ) -> CustomAction.RunResult:
            offset_x, offset_y = parse_offset(argv.custom_action_param)
            x, y = center_point(argv.box, offset_x, offset_y)
            context.tasker.controller.post_click(x, y).wait()
            return CustomAction.RunResult(success=True)

    @AgentServer.custom_action("NodeOverride")
    class NodeOverride(CustomAction):
        def run(
            self,
            context: Context,
            argv: CustomAction.RunArg,
        ) -> CustomAction.RunResult:
            override = json.loads(argv.custom_action_param or "{}")
            if override:
                context.override_pipeline(override)
            return CustomAction.RunResult(success=True)

    @AgentServer.custom_action("DisableNode")
    class DisableNode(CustomAction):
        def run(
            self,
            context: Context,
            argv: CustomAction.RunArg,
        ) -> CustomAction.RunResult:
            param = json.loads(argv.custom_action_param or "{}")
            node_name = param.get("node_name")
            if node_name:
                context.override_pipeline({node_name: {"enabled": False}})
            return CustomAction.RunResult(success=True)


if AgentServer and CustomAction and Context:
    _register_actions()
