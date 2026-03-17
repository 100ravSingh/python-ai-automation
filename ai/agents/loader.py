import os
import re


def load_agents(agents_dir: str):
    """
    Load agent names from .github/agents/*.agent.md
    """
    agents = []

    for file in os.listdir(agents_dir):
        if file.endswith(".agent.md"):
            path = os.path.join(agents_dir, file)

            with open(path, "r") as f:
                content = f.read()

            match = re.search(r"## Agent:\s*(\w+)", content)
            if match:
                agents.append(match.group(1))

    return agents