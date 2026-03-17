class BaseTool:
    name = "BaseTool"

    def run(self, input_data):
        raise NotImplementedError("Tool must implement run()")