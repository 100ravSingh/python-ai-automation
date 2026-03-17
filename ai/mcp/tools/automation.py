from ai.mcp.tools.base import BaseTool

class PythonAutomationTool(BaseTool):
    name = "PythonAutomationAgent"
    description = "Generates a basic Python automation script based on a prompt describing the task."

    def run(self, prompt: str) -> str:
        """
        Generate a basic Python automation script.

        Args:
            prompt (str): Description of the task.

        Returns:
            str: Generated Python script.
        """

        if not prompt:
            raise ValueError("Prompt cannot be empty")

        return f"""# Auto-generated script
# Task: {prompt}

def main():
    print("Processing task: {prompt}")

if __name__ == "__main__":
    main()
"""