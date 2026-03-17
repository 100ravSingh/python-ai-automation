from ai.mcp.tools.base import BaseTool


class DocTool(BaseTool):
    name = "DocAgent"

    def run(self, prompt: str) -> str:
        """Generate a documentation snippet or recommendation.

        Args:
            prompt (str): Description of the doc need.

        Returns:
            str: A short draft or guidance for documentation.
        """

        if not prompt:
            raise ValueError("Prompt cannot be empty")

        return f"DocAgent: Received task: {prompt}\n\n" \
               "(This is a placeholder response. Implement real generation logic here.)"
