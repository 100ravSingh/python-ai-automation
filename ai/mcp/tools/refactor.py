from ai.mcp.tools.base import BaseTool


class RefactorTool(BaseTool):
    name = "RefactorAgent"

    def run(self, prompt: str) -> str:
        """Generate refactoring suggestions or code improvements.

        Args:
            prompt (str): Description of the code or refactor need.

        Returns:
            str: A short set of refactoring suggestions.
        """

        if not prompt:
            raise ValueError("Prompt cannot be empty")

        return f"RefactorAgent: Received task: {prompt}\n\n" \
               "(This is a placeholder response. Implement real generation logic here.)"
