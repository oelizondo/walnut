class ClassDirectory:
    def __init__(self):
        self.classes = {}
    def add_class(self, name, attributes, methods):
        cl = Class(name, attributes, methods)
        self.classes[name] = cl
