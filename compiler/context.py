from function_directory import FunctionDirectory
from variable_directory import VariableDirectory
from class_directory import ClassDirectory

class Context:
    def __init__(self, context, parent=None):
        self.context = context
        self.parent = parent
        self.function_directory = FunctionDirectory(self)
        self.variable_directory = VariableDirectory()
        self.class_directory = ClassDirectory()
