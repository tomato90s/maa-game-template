import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from maa.agent.agent_server import AgentServer
from maa.toolkit import Toolkit

from agent import actions


def main():
    Toolkit.init_option("./")

    if len(sys.argv) < 2:
        print("Usage: python main.py <socket_id>")
        print("socket_id is provided by MaaFramework when the agent is launched.")
        sys.exit(1)

    socket_id = sys.argv[-1]
    AgentServer.start_up(socket_id)
    AgentServer.join()
    AgentServer.shut_down()


if __name__ == "__main__":
    main()
