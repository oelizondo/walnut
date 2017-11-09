class FunctionDirectory:
    def __init__(self, context):
        self.context = context
        self.functions = {}
        self.last_registered = ''

    def register(self, header, context, starting_point):
        self.functions[header] = {
            'name': header,
            'context': context,
            'starting_point': starting_point,
            'parameters' : []
        }
        self.last_registered = header

    def register_return_type(self, header, return_type):
         self.context.parent.function_directory.functions[header].update({'return_type' : return_type})
         self.context.parent.variable_directory.register(return_type,header,None)

    def register_parameter(self, param_type, name):
        self.context.variable_directory.register(param_type,name,None)
        # self.context.parent.function_directory.last_registered)
        print(str(self.context.parent.function_directory.last_registered))
        self.functions[str(self.context.parent.function_directory.last_registered)]['parameters'].append(param_type)
