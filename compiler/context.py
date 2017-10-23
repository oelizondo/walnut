from function_directory import FunctionDirectory
from global_directory import GlobalDirectory

class Context:
    def __init__(self, context, parent=None):
        self.context = context
        self.parent = parent
        self.function_directory = FunctionDirectory(context)
        self.global_directory = GlobalDirectory()
