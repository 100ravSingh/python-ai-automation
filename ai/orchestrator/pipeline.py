import yaml

from ai.agents.loader import load_agents
from ai.agents.registry import build_registry


def load_config():
    with open("ai/config.yaml") as f:
        return yaml.safe_load(f)


def run_pipeline(user_input: str):
    config = load_config()

    agents_dir = config["paths"]["agents_dir"]
    steps = config["pipeline"]
    routing = config["routing"]

    agent_names = load_agents(agents_dir)
    registry = build_registry(agent_names)

    # 🧠 Dynamic context
    context = {
        "input": user_input
    }

    print("\n Pipeline Started\n")

    for step in steps:
        print(f"➡️ Running: {step}")

        tool = registry.get(step)
        if not tool:
            raise Exception(f"Tool not found for: {step}")

        # Dynamic routing
        route = routing.get(step)
        if not route:
            raise Exception(f"No routing defined for: {step}")

        input_key = route["input"]
        output_key = route["output"]

        if input_key not in context:
            raise Exception(f"Missing input '{input_key}' for {step}")

        result = tool.run(context[input_key])

        # store output
        context[output_key] = result

        print(f"Done: {step}\n")

    print("🎯 Pipeline Finished\n")

    return context

if __name__ == "__main__":

    result = run_pipeline("Create CSV automation script")
    print("\n=== FINAL OUTPUT ===")

    for key, value in result.items():
        print(f"\n--- {key.upper()} ---\n")
        print(value)