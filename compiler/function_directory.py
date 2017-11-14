class FunctionDirectory:
    def __init__(self, context):
        self.context = context
        self.functions = {}
        self.last_registered = ''

    def register(self, header, context, starting_point):
        self.functions[header] = {
            'name': str(header),
            'context': context,
            'starting_point': str(starting_point),
            'parameters' : []
        }
        self.last_registered = header

    # This function sets the return type that the function is specting
    def register_return_type(self, header, return_type):
         self.context.parent.function_directory.functions[header].update({'return_type' : return_type})
         self.context.parent.variable_directory.register(return_type,header,None)

    # This function recieves the parameter type and name and inserts it to the function parameter stack
    def register_parameter(self, param_type, name):
        self.context.variable_directory.register(param_type,name,None)
        params_stack = self.context.parent.function_directory.functions[str(self.context.parent.function_directory.last_registered)].get('parameters')
        params_stack.append(str(param_type))
        self.context.parent.function_directory.functions[str(self.context.parent.function_directory.last_registered)].update({'parameters' : params_stack})
