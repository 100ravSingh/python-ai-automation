from ai.mcp.tools.base import BaseTool


class ArchitectureAdvisorTool(BaseTool):
    name = "ArchitectureAdvisor"
    description = "Generates architecture guidance or system design suggestions based on a prompt describing the system or requirement."

    def run(self, prompt: str) -> str:
        """Generate architecture guidance or system design suggestions.

        Args:
            prompt (str): Description of the system or requirement.

        Returns:
            str: A short architecture recommendation.
        """

        if not prompt:
            raise ValueError("Prompt cannot be empty")

        return f"ArchitectureAdvisor: Received task: {prompt}\n\n" \
               "(This is a placeholder response. Implement real generation logic here.)"
