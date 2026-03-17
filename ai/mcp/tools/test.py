from ai.mcp.tools.base import BaseTool


class TestTool(BaseTool):
    name = "TestAgent"
    description = "Generates a starter test plan or test code snippet based on a prompt describing what should be tested."

    def run(self, prompt: str) -> str:
        """Generate a starter test plan or test code snippet.

        Args:
            prompt (str): Description of what should be tested.

        Returns:
            str: A short scaffold or guidance for writing tests.
        """

        if not prompt:
            raise ValueError("Prompt cannot be empty")

        return f"TestAgent: Received task: {prompt}\n\n" \
               "(This is a placeholder response. Implement real generation logic here.)"
