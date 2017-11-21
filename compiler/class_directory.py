# Class directory:
# Module that stores the classes in the global context.
#
# attributes:
#
# classes:  atribute where it stores walnut classes.
# current_class: attribute that helps to settle which class the new object will belong to.

from walnut_class import WalnutClass
class ClassDirectory:
    def __init__(self):
        self.classes = {}
        self.current_class = None


    # add_class:
    # Method that creates a new Walnut class and sets it in the directory.
    # This method is called when a class is declared.
    #
    # parameters:
    #
    # name: is the name of the class to be registered
    # context: is the context to which the class will belong to
    # extend: parameter that will only be used when a class belongs to another.
    def add_class(self, name, context, extend=None):
        cl = WalnutClass(name, extend, context)
        self.current_class = cl
        self.classes[name] = cl
