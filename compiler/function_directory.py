class FunctionDirectory:
    def __init__(self, context):
        self.context = context
        self.functions = {}

    def register(self, header, context, starting_point):
        self.functions[header] = {
            'name': header,
            'context': context,
            'starting_point': starting_point
        }
    def register_return_type(self, header, return_type):
         self.context.parent.function_directory.functions[header].update({'return_type' : return_type})

    def register_parameter(self, param_type, name):
        self.context.variable_directory.register(param_type,name,None)
