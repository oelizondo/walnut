# Context module: One of the main modules for compilation
# Context have a name (context), and a parent context.
# The compilation of a program is based on contexts. Every context belongs to a another
# context except the global one.
# When a context is created, the current context becomes its parent, thus creating a nested network of contexts.

# The search of functions, methods, attributes and ids are all based in the context search system.

# When a class is declared it creates its own context.
# When a function is declared it creates its own context.
# The "main" is a context itself.

from function_directory import FunctionDirectory
from variable_directory import VariableDirectory
from class_directory import ClassDirectory
from object_directory import ObjectDirectory

class Context:
    def __init__(self, context, parent=None):
        self.context = context                             # stores the name of the context
        self.parent = parent                               # stores the parent context
        self.function_directory = FunctionDirectory(self)  # context function directory
        self.variable_directory = VariableDirectory()      # context variable directory
        self.class_directory = ClassDirectory()            # context class directory (only used in global context)
        self.object_directory = ObjectDirectory()          # context object directory
