from ai.mcp.tools.base import BaseTool


class ReactFrontendTool(BaseTool):
    name = "ReactFrontendAgent"

    def run(self, prompt: str) -> str:
        """Generate a starter React component or UI guidance.

        Args:
            prompt (str): Description of the UI feature.

        Returns:
            str: A short scaffold or guidance for implementing the UI.
        """

        if not prompt:
            raise ValueError("Prompt cannot be empty")

        return f"ReactFrontendAgent: Received task: {prompt}\n\n" \
               "(This is a placeholder response. Implement real generation logic here.)"
