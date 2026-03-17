from ai.mcp.tools import TOOLS


def list_tools():
    """Return all available tools with metadata"""
    return [
        {
            "name": tool.name,
            "description": tool.description,
        }
        for tool in TOOLS.values()
    ]


def run_tool(name: str, input_data: str):
    """Execute a tool by name"""
    tool = TOOLS.get(name)

    if not tool:
        raise Exception(f"Tool not found: {name}")

    return tool.run(input_data)