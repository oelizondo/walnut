class FunctionDirectory:
    def __init__(self, context):
        self.context = context
        self.functions = {}

    def add_function(self, header, arguments, return_type):
        func = Function(header, arguments, return_type)
        # memory.allocate_function(self.context, func)
        self.functions[header] = func
