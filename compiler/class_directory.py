from walnut_class import WalnutClass
class ClassDirectory:
    def __init__(self):
        self.classes = {}
        self.current_class = None
    def add_class(self, name, context, extend=None):
        cl = WalnutClass(name, extend, context)
        self.current_class = cl
        self.classes[name] = cl
