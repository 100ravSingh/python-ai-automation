from ai.mcp.tools.base import BaseTool


class NodeApiTool(BaseTool):
    name = "NodeApiAgent"
    description = "Generates a starter Node.js/Express API recommendation based on a prompt describing the desired API behavior."

    def run(self, prompt: str) -> str:
        """Generate a starter Node.js/Express API recommendation.

        Args:
            prompt (str): Description of the desired API behavior.

        Returns:
            str: A short scaffold or guidance for implementing the API.
        """

        if not prompt:
            raise ValueError("Prompt cannot be empty")

        return f"NodeApiAgent: Received task: {prompt}\n\n" \
               "(This is a placeholder response. Implement real generation logic here.)"
