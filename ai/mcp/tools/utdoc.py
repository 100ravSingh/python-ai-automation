from ai.mcp.tools.base import BaseTool


class UTDocTool(BaseTool):
    name = "UTDocAgent"

    def run(self, prompt: str) -> str:
        """Generate unit test documentation guidance.

        Args:
            prompt (str): Description of the tests or code under test.

        Returns:
            str: A short draft or guidance for documenting unit tests.
        """

        if not prompt:
            raise ValueError("Prompt cannot be empty")

        return f"UTDocAgent: Received task: {prompt}\n\n" \
               "(This is a placeholder response. Implement real generation logic here.)"
