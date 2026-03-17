from ai.mcp.tools import TOOLS


def build_registry(agent_names):
    """
    Map agent names → tool instances dynamically
    """
    registry = {}

    for agent in agent_names:
        if agent in TOOLS:
            registry[agent] = TOOLS[agent]
        else:
            print(f"[WARNING] No tool found for agent: {agent}")

    return registry