# Context module: One of the main modules for compilation
# Context have a name (context), and a parent context.
# The compilation of a program is based on contexts. Every context belongs to a another
# context except the global one.
# When a context is created, the current context becomes its parent, thus creating a nested network of contexts.
#
# The search of functions, methods, attributes and ids are all based in the context search system.
#
# When a class is declared it creates its own context.
# When a function is declared it creates its own context.
# The "main" is a context itself.
#
# attributes:
# context: stores the name of the context
# parent: stores the parent context
# function_directory: context's function directory
# variable_directory: context's variable directory
# class_directory: context's class directory (only used in global context)
# object_directory: context's object directory

from function_directory import FunctionDirectory
from variable_directory import VariableDirectory
from class_directory import ClassDirectory
from object_directory import ObjectDirectory

#
class Context:
    def __init__(self, context, parent=None):
        self.context = context
        self.parent = parent
        self.function_directory = FunctionDirectory(self)
        self.variable_directory = VariableDirectory()
        self.class_directory = ClassDirectory()
        self.object_directory = ObjectDirectory()
