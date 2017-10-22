class Class:
    def __init__(self, name, attributes, methods):
        self.name = name
        self.attributes = VariableDirectory('local')
        self.methods = FunctionDirectory('temporal')
