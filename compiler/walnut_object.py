import sys
class WalnutObject:
    def __init__(self, walnut_class):
        self.walnut_class = walnut_class
        self.name = ''

# The parent context of any class is the global unless specified otherwise
    # def register_parent_class(self, extend):
    #     global_context = self.context.parent
    #     parent_class = global_context.class_directory.classes.get(extend, None)
    #     if parent_class != None:
    #         self.context.parent = parent_class.context
    #         self.extend = parent_class.name
    #     else:
    #         print("Class " + extend + " doesn't exist")
    #         sys.exit()
