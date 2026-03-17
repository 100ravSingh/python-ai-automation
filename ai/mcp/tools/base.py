class BaseTool:
    name = "BaseTool"
    description = "Base tool class. Subclasses should implement the run() method."

    def run(self, input_data):
        raise NotImplementedError("Tool must implement run()")