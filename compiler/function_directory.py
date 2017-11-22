# FunctionDirectory module:
# It is in charge of having the record of all the information of
# all functions in its current context.
#
# attributes
#
# context: the context to which the function directory belongs to.
# functions: the dictionary that contains all the information of the functions
#            under its context.
# last_registered: helper attribute that contains the current function that is being accessed
#
class FunctionDirectory:
    def __init__(self, context):
        self.context = context
        self.functions = {}
        self.last_registered = ''

    # Name: register
    # This function sets a new function in the function directory.
    # it also sets this function as the last registered to facilitate the
    # the insertion of its parameters
    #
    # parameters
    #
    # header: name of the function
    # context: to which context will the function will belong to.
    # starting_point: the cuadruple number in which this function will start to run
    #
    def register(self, header, context, starting_point):
        self.functions[header] = {
            'name': str(header),
            'context': context,
            'starting_point': str(starting_point),
            'parameters' : []
        }
        self.last_registered = header

    # Name: register_return_type
    # This function sets the return type that the function is specting
    # Mainly used by program engine.
    #
    # parameters
    #
    # header: name of the function
    # return_type: type that the function is going to be specting
    # vm_direction: vm_direction that the variable with the function name is going to use
    #
    def register_return_type(self, header, return_type, vm_direction):
         self.context.parent.function_directory.functions[header].update({'return_type' : return_type})
         self.context.parent.variable_directory.register(return_type,header,vm_direction,None)

    # Name: register_parameter
    # This function recieves the parameter type and name and inserts it to the function parameter stack
    #
    # parameters
    #
    # param_type: the type of the variable
    # name: the name of the parameter.
    # vm_direction: the direction to be assigned to the new variable
    #
    def register_parameter(self, param_type, name, vm_direction):
        self.context.variable_directory.register(param_type,name,vm_direction,None)
        params_stack = self.context.parent.function_directory.functions[str(self.context.parent.function_directory.last_registered)].get('parameters')
        params_stack.append(str(param_type))
        self.context.parent.function_directory.functions[str(self.context.parent.function_directory.last_registered)].update({'parameters' : params_stack})
