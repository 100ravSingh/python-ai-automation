from ai.mcp.tools.base import BaseTool


class DebugTool(BaseTool):
    name = "DebugAgent"
    description = "Generates a debugging analysis or troubleshooting guidance based on a prompt describing the error or issue."

    def run(self, prompt: str) -> str:
        """Generate a debugging analysis or troubleshooting guidance.

        Args:
            prompt (str): Description of the error or issue.

        Returns:
            str: A short analysis or steps to investigate.
        """

        if not prompt:
            raise ValueError("Prompt cannot be empty")

        return f"DebugAgent: Received task: {prompt}\n\n" \
               "(This is a placeholder response. Implement real generation logic here.)"
