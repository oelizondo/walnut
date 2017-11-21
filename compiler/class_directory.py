# Class directory: Module that stores the classes in the global context.

from walnut_class import WalnutClass
class ClassDirectory:
    def __init__(self):
        self.classes = {}
        self.current_class = None   # This attribute helps the settle to which class the new object will belong to

    # Method that creates a new Walnut class and sets it in the directory.
    # This method is called when a class is declared.
    def add_class(self, name, context, extend=None):
        cl = WalnutClass(name, extend, context)
        self.current_class = cl
        self.classes[name] = cl
