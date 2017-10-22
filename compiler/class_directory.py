class ClassDirectory:
    def __init__(self):
        self.classes = {}
    def add_class(self, name, attributes, methods):
        cl = Class(name, attributes, methods)
        memory.allocate_class(cl)
        self.classes[name] = cl
