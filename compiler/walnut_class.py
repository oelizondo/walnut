# WalnutClass module
# This module is individual for each class, it stores
# the information of a walnut class, with its context
#
# attributes:
#
# name: the name of the walnut class
# context: the context to which the class belongs
# extends: (optional) the name of the parent class
#
import sys
class WalnutClass:
    def __init__(self, name, context, extend=None):
        self.name = name
        self.extend = extend
        self.context = context

    # Name: register_parent_class
    # The parent context of any class is the global unless specified otherwise
    # This function changes the class parent context (previously global)
    # to the one it wants to extends.
    #
    # parameter
    #
    # extends: name of the class to which the class context will now belong to.
    #
    # error_handle
    #
    # 1) returns when the class you want to extend to does not exist
    #
    def register_parent_class(self, extend):
        global_context = self.context.parent
        parent_class = global_context.class_directory.classes.get(extend, None)
        if parent_class != None:
            self.context.parent = parent_class.context
            self.extend = parent_class.name
        else:
            print("Class " + extend + " doesn't exist")
            sys.exit()
