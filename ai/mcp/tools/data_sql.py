from ai.mcp.tools.base import BaseTool


class DataSQLTool(BaseTool):
    name = "DataSQLAgent"
    description = "Generates a starter SQL query or data workflow recommendation based on a prompt describing the data task."

    def run(self, prompt: str) -> str:
        """Generate a starter SQL query or data workflow recommendation.

        Args:
            prompt (str): Description of the data task.

        Returns:
            str: A short scaffold or guidance for implementing the query/workflow.
        """

        if not prompt:
            raise ValueError("Prompt cannot be empty")

        return f"DataSQLAgent: Received task: {prompt}\n\n" \
               "(This is a placeholder response. Implement real generation logic here.)"
