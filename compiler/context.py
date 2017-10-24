from function_directory import FunctionDirectory
from variable_directory import VariableDirectory

class Context:
    def __init__(self, context, parent=None):
        self.context = context
        self.parent = parent
        self.function_directory = FunctionDirectory(context)
        self.variable_directory = VariableDirectory()
