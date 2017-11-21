# Operation module
# This module is one of the most important for the compiler.
# it is in charge of all the logic operations that need to be validated
# in order for the program to have a valid flow of events. This includes:
# 1) validation of arithmetic operations
# 2) validation of arrays and matrix calls
# 3) validation of function call, correct number of parameters and expression types as well of return types
# 4) validation of method call, correct number of parameters and expression types as well of return types
# 5) generation of cuadruples of valid calls for numbers 2) to 4)
# 6) generation of cuadruples of number 1)
#
# any constant that is inserted to a cuadruple is given a token '%' to
# notify the virtual machine that it is indeed a constant
#
# id's are inserted to the cuadruples as virtual memory directions
#
# attributes
#
# operator stack: This stack has all the pending operations signs of the compiler
# type stack: This stack has the type of the referenced virtual memory id
# identifier stack: This stack contains the virtual memory direction of the id's
# param_counter_stack: This stack has the number of parameter that a function or method call
#                      left pending. This is used for correct nested function calls.
# dimension_stack: This stack has the control for nested dimension access.
# semantic_cube: This is a class that validates if an operation can be done, returning true or false.
# program_engine: The main module, this is given to be able to insert cuadruples to the cuadruple stack
#                 as well as access to the contexts of the program.
# counter: this is used to give temporal values a name by giving 'temp' + str(counter)
# current_function: helper attribute that keeps track to which function are the validations acting on.
# current_object: helper attribute that keeps track to which object are the validations acting on.
# parameter counter: helper attribute that keeps track in which parameter are the validations acting on.
# collection: helper attribute that keeps track of the current collection being validated.
# collection_names: stack that keeps track of pending collection validations, this is used for nested collection access.
#
from semantic_cube import SemanticCube
from cuadruple import Cuadruple
import sys

# Name: is_int
# As python does not work with types, a function was created
# to be able to identify if a constant is a int value or not.
# order between is_int and is_float was necessary because python
# returns true when an int wants to be parsed as float, but
# not the other way around.
#
# parameter
#
# num: value of the expression that is going to be validated.
#
def is_int(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

# Name: is_float
# As python does not work with types, a function was created
# to be able to identify if a constant is a float or not.
#
# parameter
#
# num: value of the expression that is going to be validated.
#
def is_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

# Name: extract_value
# This function was created to return the real value
# of the string that is given.
#
# parameter
#
# num: value of the expression that is going to be validated.
#
def extract_value(num):
    if is_int(num):
        return int(num)
    elif is_float(num):
        return float(num)
    elif num == 'true':
        return True
    elif num == 'false':
        return False
    else:
        return num


class Operation:
    def __init__(self, program_engine):
        self.operator_stack = []
        self.type_stack = []
        self.identifier_stack = []
        self.param_counter_stack = []
        self.function_stack = []
        self.dimension_stack = []
        self.semantic_cube = SemanticCube()
        self.program_engine = program_engine
        self.counter = 0
        self.current_function = ''
        self.current_object = ''
        self.parameter_counter = 0
        self.collection = None
        self.collection_names = []

    # Name: generate_cuad
    # This function is in charge to create cuadruples and send them to the program_engine
    #
    # parameters
    #
    # operation: is the operation sign to be applied.
    # left_side: optional, this is the left side of the operation
    # right_side: optional, this is the right side of the operation
    # result: optional, this is the memory direction where the result will be stored.
    def generate_cuad(self, operation, left_side=None, right_side=None, result=None):
        cuad = Cuadruple(operation, left_side, right_side, result)
        self.program_engine.send_cuad(cuad)

    # Name: add_identifier
    # This method is called from the parser.
    # It calls a function depending of what it recieved, as all parameters are optional
    #
    # parameters
    #
    # identifier: this attribute is not null when an id is found.
    # constant: this attribute is not null when a constant is found.
    # array: this attribute is not null when an array call is found.
    #
    def add_identifier(self, identifier, constant, array):
        if identifier != None:
            self.add(identifier)
        elif constant != None:
            self.add_constant(constant)
        elif array != None:
            self.add_array(array)

    # Name: add
    # This function validates that the id that it found is correct to its context.
    # It is achieved by the search by context method of the function find_var.
    # Then it validates that the id is not dimensioned (only called when its a single id)
    # and inserts the vm_direction to the id stack and its type to the type stack.
    #
    # parameter
    #
    # variable: id name of the variable to add to the stacks.
    #
    # error_handle
    #
    # 1) returns if an id is dimensioned
    #
    def add(self, variable):
        if variable != None:
            var = self.find_var(variable)
            if var['dimension'] == None:
                self.type_stack.append(str(var['type']))
                # self.identifier_stack.append(var['value'])
                self.identifier_stack.append(var['vm_direction'])
            else:
                print("Variable " + var['name'] + " is dimensioned.")
                sys.exit()

    # Name: add_constant
    # This function purpose is to insert to the correct type of the constant
    # to the type stack, as well as to add the '%' token in front of it to
    # identify it as a constant.
    #
    # parameter
    #
    # constant: raw string of the constant value
    #
    # error_handle
    #
    # 1) returns extraneous input.
    #
    def add_constant(self, constant):
        if is_int(constant):
            self.type_stack.append('int')
            # self.identifier_stack.append(int(constant))
            self.identifier_stack.append("%" + str(constant))
        elif is_float(constant):
            self.type_stack.append('float')
            # self.identifier_stack.append(float(constant))
            self.identifier_stack.append("%" + str(constant))
        elif constant == 'true' or constant == 'false':
            self.type_stack.append('boolean')
            self.identifier_stack.append("%" + str(constant))
        elif str(constant)[0] == "\"":
            self.type_stack.append('string')
            self.identifier_stack.append("%" + str(constant))
        else:
            print("Type Error could not add constant " + constant)
            sys.exit()

    # Name: add_array
    # This function is only in charge to validate that the id that is trying to
    # call as a collection is indeed a collection.
    #
    # parameter
    #
    # array: id to be validated as a collection.
    #
    # 1) it returns that the id called is not a collection.
    #
    def add_array(self,array):
        if array != None:
            arr = self.find_var(array)
            if arr['dimension'] == None:
                print("Variable "+ arr['name'] +" is not dimensioned.")

    # Name: function_call
    # This function checks that the function called exists and
    # sets the function "variable" in the identifier/type stack
    # for return purposes. If the function does not have a return type
    # it inserts a void type to the stack to detonate an error if an operation
    # wants to take place with the function call.
    #
    # parameter
    #
    # header: name of the function.
    #
    # error_handle
    #
    # 1) it returns that the function does not exists.
    #
    def function_call(self, header):
        function_recieved = self.find_function(header, self.program_engine.current_context)
        if function_recieved != None:
            if (function_recieved.get("return_type") != None):
                self.type_stack.append(function_recieved["return_type"])
            else:
                self.type_stack.append('void')
            self.identifier_stack.append(header)
            self.generate_cuad('gosub',None,None, str(function_recieved.get("starting_point")))
        else:
            print("function" + str(header) + "does not exist")

    # Name: function_return_save
    # This function is in charge to set the return value of the function to a
    # temporal value memory direction, to avoid override of the return value of that
    # call with a new call from the same function.
    #
    def function_return_save(self):
        function_id = self.identifier_stack.pop()
        temp_var = self.generate_temporal(self.type_stack[-1])
        self.identifier_stack.append(temp_var['vm_direction'])
        self.counter += 1
        self.generate_cuad(23,str(function_id),None,temp_var['vm_direction'])

    # Name: function_argument_validation
    # This function validates the parameter that is given in a function call.
    # It checks that the argument type and parameter type are compatible and can be assigned.
    # It also checks that the number of arguments given does not exeeds the permited.
    #
    # error_handle
    #
    # 1) returns that the function call recieves a certain type, and your input type.
    # 2) returns that the function call is being call with more parameters than expected
    #
    def function_argument_validation(self):
        func = self.find_function(self.current_function, self.program_engine.current_context)
        function_parameters = func.get('parameters')
        if self.parameter_counter < len(function_parameters):
            parameter_type = function_parameters[self.parameter_counter]
            argument_type = self.type_stack.pop()
            if parameter_type != argument_type :
                print("Type error in "+ str(self.current_function) +" function call in (" + str(self.parameter_counter + 1) + ") argument given: " + str(argument_type) + " expected: " + str(parameter_type))
                sys.exit()
            self.parameter_counter += 1
            self.generate_cuad('param',self.identifier_stack[len(self.identifier_stack)-1],None,'param'+str(self.parameter_counter))
            self.identifier_stack.pop()
        else:
            print("Argument error in "+ str(self.current_function) +" function call, expected only " + str(self.parameter_counter) + " argument(s)")
            sys.exit()

    # Name: argument_number_validation
    # This function checks that the number of arguments given to
    # the function call are complete and resets the parameter counter to 0
    # to prepare it for next function calls.
    #
    # error_handle
    #
    # 1) returns if not all parameters where filled in a function call and how many where expected.
    #
    def argument_number_validation(self):
        func = self.find_function(self.current_function, self.program_engine.current_context)
        function_parameters = func.get('parameters')
        if self.parameter_counter == len(function_parameters):
            self.reset_parameter_counter()
        else:
            print("Argument error in "+ str(self.current_function) +" function call, expected " + str(len(function_parameters)) + " argument(s)")
            sys.exit()

    # Name: method_argument_validation
    # This function validates the parameter that is given in a method call.
    # It checks that the argument type and parameter type are compatible and can be assigned.
    # It also checks that the number of arguments given does not exeeds the permited.
    #
    # error_handle
    #
    # 1) returns that the method call recieves a certain type, and your input type.
    # 2) returns that the method call is being call with more parameters than expected
    #
    def method_argument_validation(self):
        obj_context = self.get_object_context()
        func = self.find_obj_function(self.current_function, obj_context)
        function_parameters = func.get('parameters')
        if self.parameter_counter < len(function_parameters):
            parameter_type = function_parameters[self.parameter_counter]
            argument_type = self.type_stack.pop()
            if parameter_type != argument_type :
                print("Type error in "+ str(self.current_function) +" function call in (" + str(self.parameter_counter + 1) + ") argument given: " + str(argument_type) + " expected: " + str(parameter_type))
                sys.exit()
            self.parameter_counter += 1
            self.generate_cuad('param',self.identifier_stack[len(self.identifier_stack)-1],None,'param'+str(self.parameter_counter))
            self.identifier_stack.pop()
        else:
            print("Argument error in object "+ str(self.current_function) +" function call, expected only " + str(self.parameter_counter) + " argument(s)")
            sys.exit()

    # Name: method_argument_number_validation
    # This function checks that the number of arguments given to
    # the method call are complete and resets the parameter counter to 0
    # to prepare it for next function calls.
    #
    # error_handle
    #
    # 1) returns if not all parameters where filled in a function call and how many where expected.
    #
    def method_argument_number_validation(self):
        obj_context = self.get_object_context()
        func = self.find_obj_function(self.current_function, obj_context)
        function_parameters = func.get('parameters')
        if self.parameter_counter == len(function_parameters):
            self.reset_parameter_counter()
        else:
            print("Argument error in object "+ str(self.current_function) +" function call, expected " + str(len(function_parameters)) + " argument(s)")
            sys.exit()

    # Name: method_call
    # This function checks that the method called exists and
    # sets the method "variable" in the identifier/type stack
    # for return purposes. If the method does not have a return type
    # it inserts a void type to the stack to detonate an error if an operation
    # wants to take place with the method call.
    #
    # parameter
    #
    # header: name of the method.
    #
    # error_handle
    #
    # 1) it returns that the object does not have a method with that name.
    #
    def method_call(self, header):
        obj_context = self.get_object_context()
        function_recieved = self.find_obj_function(header, obj_context)
        if function_recieved != None:
            if (function_recieved.get("return_type") != None):
                self.type_stack.append(function_recieved["return_type"])
            else:
                self.type_stack.append('void')
            self.identifier_stack.append(header)
            self.generate_cuad('gosub',None,None, str(function_recieved.get("starting_point")))
        else:
            print("function" + str(header) + "does not exist")

    # Name: register_parameter
    # This function is called in the declaration of a function
    # it registers a variable to the function context, it also
    # creates an assignation cuadruple so the parameter is loaded with a value when
    # the function call is triggered.
    #
    # parameters
    #
    # var_type: new variable type.
    # header: new variable name.
    #
    def register_parameter(self,var_type,header):
        vm_direction = self.program_engine.get_next_virtual_memory()
        self.program_engine.current_context.function_directory.register_parameter(var_type, header, vm_direction)
        var = self.find_var(header)
        self.generate_cuad(23,'param'+ str(self.parameter_counter+1), None, var['vm_direction'])
        self.parameter_counter += 1

    # Name: compare_op
    # This function checks if the next operation to do is a comparison.
    # if true, the function semantic validation will run the
    # following semantic validation of the expression.
    #
    def compare_op(self):
        if len(self.operator_stack) == 0:
            return
        op = self.operator_stack[-1]
        if op == '&&' or op == '||' or op == 'and' or op == 'or':
            self.operation_semantic_validation()

    # Name: is_relational_op
    # This function checks if the next operation token is relational.
    #
    # parameters
    #
    # op: the poped operator to be compared.
    #
    def is_relational_op(self, op):
        return op == '<' or op == '>' or op =='>=' or op == '<=' or op == '==' or op == 'is' or op == '!=' or op == 'not'

    # Name: compare_relational_op
    # This function checks if the next operation to do is a comparison.
    # if true, the function semantic validation will run the
    # following semantic validation of the expression.
    # The function is_relational_op is called to validate if the token is relational.
    #
    def compare_relational_op(self):
        if len(self.operator_stack) == 0:
            return
        op = self.operator_stack[-1]
        if self.is_relational_op(op):
            self.operation_semantic_validation()

    # Name: multiply_divide_op
    # This function checks if the next operation to do is a division or multiplication.
    # if true, the function semantic validation will run the
    # following semantic validation of the expression.
    #
    def multiply_divide_op(self):
        if len(self.operator_stack) == 0:
            return
        if self.operator_stack[-1] == '*' or self.operator_stack[-1] == '/':
            self.operation_semantic_validation()

    # Name: add_substract_op
    # This function checks if the next operation to do is a sum or substraction.
    # if true, the function semantic validation will run the
    # following semantic validation of the expression.
    #
    def add_substract_op(self):
        if len(self.operator_stack) == 0:
            return
        if self.operator_stack[-1] == '-' or self.operator_stack[-1] == '+':
            self.operation_semantic_validation()

    # Name: power_of_op
    # This function checks if the next operation to do is an exponential.
    # if true, the function semantic validation will run the
    # following semantic validation of the expression.
    #
    def power_of_op(self):
        if len(self.operator_stack) == 0:
            return
        if self.operator_stack[-1] == '^':
            self.operation_semantic_validation()

    # Name: assign_operation
    # This function is called when an assignation is done in the parser.
    # First it finds the variable information in the correct context with
    # the find_var function. Then it calls the semantic cube to validate that
    # the assignation is accepted and creates a cuadruple of the assignation.
    #
    # parameter
    #
    # identifier: name of the variable to be assigned.
    #
    # error_handle
    #
    # 1) returns that a operation is not viable
    # 1.1) returns that the operation was not viable do to a void function or method call
    #      trying to be assigned.
    # 1.2) returns which types where incompatible while trying to assign
    #
    def assign_operation(self, identifier):
        if identifier != None:
            var = self.find_var(identifier)
            to_assign_value = self.identifier_stack[len(self.identifier_stack) - 1]
            to_assign_type = self.type_stack[len(self.type_stack) - 1]
            to_assign_type = self.semantic_cube.converter[str(to_assign_type)]
            to_be_assigned = self.semantic_cube.converter[str(var['type'])]
            res_type = self.semantic_cube.semantic_cube.get((to_be_assigned, to_assign_type, 23), None)
            if res_type != None:
                self.generate_cuad(self.semantic_cube.converter['='], to_assign_value, None, var['vm_direction'])
            else:
                print("Type Error: cannot assign the value to " + str(var['name']))
                if to_assign_type == 'void':
                    print("value is from a void function")
                else:
                    print("incompatible types: " + self.semantic_cube.inverter[to_assign_type] + " and " + str(var['type']))
                sys.exit()

    # Name: operation_semantic_validation
    # This function validates that the operation taking place is valid,
    # through the SemanticCube.
    #
    # error_handle
    #
    # 1) returns which operation token was not valid and which types where in the error.
    #
    def operation_semantic_validation(self):
        op = self.semantic_cube.converter.get(self.operator_stack.pop(), None)
        type_right_side = self.semantic_cube.converter.get(self.type_stack.pop(), None)
        type_left_side = self.semantic_cube.converter.get(self.type_stack.pop(), None)
        right_side = extract_value(self.identifier_stack.pop())
        left_side = extract_value(self.identifier_stack.pop())
        res_type = self.semantic_cube.semantic_cube.get((type_left_side, type_right_side, int(op)), None)
        if res_type != None:
            temp_var = self.generate_temporal(res_type)
            self.generate_cuad(op, left_side, right_side, temp_var['vm_direction'])
            self.counter += 1
            self.type_stack.append(self.semantic_cube.inverter[res_type])
            self.identifier_stack.append(temp_var['vm_direction'])
        else:
            print("Type Error, cannot \"" + str(self.semantic_cube.inverter[op]) + "\" values")
            print("incompatible types: " + str(self.semantic_cube.inverter[type_right_side]) + " and " + str(self.semantic_cube.inverter[type_left_side]))
            sys.exit()

    # Name: collection_assignment
    # validates that a collection call is able to recieve the incoming expression
    # using the semanic cube.
    #
    # error_handle
    #
    # 1) returns that the assignation could not take place.
    # 1.1) returns if the error comes from a void function call.
    # 1.2) returns the incompatible types of the assignation.
    def collection_assignment(self):
        expression = self.identifier_stack.pop()
        collection_direction = self.identifier_stack.pop()

        expression_type = self.type_stack.pop()
        collection_type = self.type_stack.pop()

        to_assign_type = self.semantic_cube.converter[str(expression_type)]
        to_be_assigned = self.semantic_cube.converter[str(collection_type)]
        res_type = self.semantic_cube.semantic_cube.get((to_be_assigned, to_assign_type, 23), None)

        if res_type == to_be_assigned:
            self.generate_cuad(self.semantic_cube.converter['='], expression, None, collection_direction)
        else:
            print("Type Error: cannot assign the value to dimensioned variable")
            if to_assign_type == 'void':
                print("value is from a void function")
            else:
                print("incompatible types: " + self.semantic_cube.inverter[to_assign_type] + " and " + self.semantic_cube.inverter[to_be_assigned])
            sys.exit()

    # Name: find_var
    # This function is one of the most important in the operation module.
    # It recieves an id and it searches for it through contexts.
    # This works because every context is nested, the search starts in
    # the current context and goes up by searching in the parent context.
    # The search stops when a variable with that name is found a context
    # variable directory or no variable was found in any context
    # (which ends in the global context).
    # If a variable is found, the whole variable information is returned.
    #
    # parameters
    #
    # variable: name of the variable to be found.
    #
    # error_handle
    #
    # 1) returns that a variable with that name does not exist.
    #
    def find_var(self, variable):
        starting_context = self.program_engine.current_context
        var = None
        while var == None and starting_context != None:
            var = starting_context.variable_directory.variables.get(variable, None)
            starting_context = starting_context.parent

        if starting_context == None and var == None:
            print("Variable " + variable + " doesn't exist")
            sys.exit()
        else:
            return var

    # Name: find_function
    # This function recieves the name of the function to be searched and
    # the starting context to which the search should begin.
    # if the function is found, it returns all the function information from
    # the context function directory.
    #
    # parameters
    #
    # function: name of the function
    # starting_context: te context in which the search should begin.
    #
    # error_handle
    #
    # 1) returns when a function is not found in the given contexts.
    #
    def find_function(self, function, starting_context):
        func = None
        while func == None and starting_context != None:
            func = starting_context.function_directory.functions.get(function, None)
            starting_context = starting_context.parent

        if starting_context == None and func == None:
            print("Function " + function + " doesn't exist")
            sys.exit()
        else:
            return func

    # Name: find_obj_function
    # This function recieves the name of the function to be searched and
    # the starting context to which the search should begin.
    # if the function is found, it returns all the function information from
    # the context function directory.
    # the difference is that in an object function search, you need to stop
    # before the global context is reached to avoid method calls with function calls
    #
    # parameters
    #
    # function: name of the function
    # starting_context: te context in which the search should begin.
    #
    # error_handle
    #
    # 1) returns when a function is not found in the object contexts.
    #
    def find_obj_function(self, function, starting_context):
        func = None
        while func == None and starting_context.parent != None:
            func = starting_context.function_directory.functions.get(function, None)
            starting_context = starting_context.parent

        if func == None:
            print("function: " + function + " for object: " + self.current_object + " doesn't exist")
            sys.exit()
        else:
            return func

    # Name: get_object_context
    # This function is to recieve the current object class context.
    # This is called when an object method wants to activate, to validate
    # that the object indeed exists and to return the context to which it belongs.
    # to be able to do correct method calls.
    #
    # error_handle
    #
    # 1) returns when an object does not exist within the available contexts
    #
    def get_object_context(self):
        obj = None
        starting_context = self.program_engine.current_context

        while obj == None and starting_context != None:
            obj = starting_context.object_directory.objects.get(self.current_object,None)
            starting_context = starting_context.parent

        if starting_context == None and obj == None:
            print("Object " + self.current_object + " is not declared")
            sys.exit()
        else:
            return obj['obj'].walnut_class.context

    # Name: set_current_object
    # This method is called from the parser, it is a helper method for both
    # program engine and operation to set the name of the object being handled.
    #
    def set_current_object(self, header):
        self.current_object = header
        self.program_engine.current_object = header

    # Name: reset_parameter_counter
    # This function is called from the parser to handle nested function and methods calls
    #
    def reset_parameter_counter(self):
        self.parameter_counter = 0

    # Name: reset_status
    # This function is called when a function call ends its parameters validation, to reset it
    # for dormant function calls to continue its parameters validations.
    #
    def reset_status(self):
        self.parameter_counter = self.param_counter_stack.pop()
        self.current_function = self.function_stack.pop()

    # Name: save_status
    # This function is called when a nested function or method call is activated to
    # save the location of the parameter when the nested function call ends.
    #
    def save_status(self):
        self.param_counter_stack.append(self.parameter_counter)
        self.function_stack.append(self.current_function)
        self.reset_parameter_counter()

    # Name: verify_boolean
    # This function is called when a conditional statement is called (if, elseif, while)
    # This to validate that the last expression is indeed a boolean
    #
    # error_handle
    #
    # 1) returns that the conditional statement expected a boolean.
    #
    def verify_boolean(self):
        to_assign_type = self.type_stack[len(self.type_stack) - 1]
        if(to_assign_type != 'boolean'):
            print("Conditional statement expected boolean, recieved: " + str(to_assign_type))
            sys.exit()

    # Name: verify_dimensions
    # This function verifies that a variable trying to be accessed as a collection
    # is indeed a collection
    #
    # parameter
    #
    # identifier: the name of the id
    #
    # error_handle
    #
    # 1) returns that a var is not dimentioned.
    #
    def verify_dimensions(self, identifier):
        self.collection_names.append(identifier)
        self.collection = self.find_var(self.collection_names[-1])

        if self.collection['dimension'] != None and len(self.collection['dimension']) > 0:
            self.dimension_stack.append([self.collection_names[-1], 1])
            self.operator_stack.append('[')
        else:
            print("Error var not dimensioned")
            sys.exit()

    # Name: generate_access_cuad
    # This function creates the cuadruples of the collection correct access
    #
    # parameter
    #
    # cell: binary value to access the correct collection dimension
    #
    # error_handle
    #
    # 1) returns if the expression to access the collection is different from
    #    an integer.
    #
    def generate_access_cuad(self, cell):
        if (self.type_stack[-1] == 'int'):
            self.generate_cuad('ver', self.identifier_stack[-1], '%' + str(0), '%' + str(self.collection['dimension'][cell]['limit']))

            if len(self.collection['dimension']) > self.dimension_stack[-1][1]:
                aux = self.identifier_stack.pop()
                self.type_stack.pop()
                temp = self.generate_temporal('int')
                self.generate_cuad(self.semantic_cube.converter['*'], aux, '%' + str(self.collection['dimension'][cell]['k']), temp['vm_direction'])
                self.identifier_stack.append(temp['vm_direction'])
                self.type_stack.append('int')


            if  self.dimension_stack[-1][1] > 1:
                aux1 = self.identifier_stack.pop()
                self.type_stack.pop()
                aux2 = self.identifier_stack.pop()
                self.type_stack.pop()
                temp = self.generate_temporal('int')
                self.generate_cuad(self.semantic_cube.converter['+'], aux1, aux2, temp['vm_direction'])
                self.identifier_stack.append(temp['vm_direction'])
                self.type_stack.append('int')
        else:
            print("Type error for collection access expected int got " + self.type_stack[-1])
            sys.exit()

    # Name: update_dimension
    # This function gets called from a parser when a matrix
    # is declared.
    #
    def update_dimension(self):
        self.dimension_stack[-1][1] += 1

    # Name: verify_array
    # This function is called when an array call is present, it
    # validates that the array call comes from an array
    #
    def verify_array(self):
        dimensions = len(self.collection['dimension'])
        if self.dimension_stack[-1][1] != dimensions:
            print("Variable " + self.collection['name'] + " is a matrix.")
            sys.exit()

    # Name: verify_matrix
    # This function verifies that a matrix call comes from a matrix.
    #
    def verify_matrix(self):
        dimensions = len(self.collection['dimension'])
        if  self.dimension_stack[-1][1] > dimensions:
            print("Variable " + self.collection['name'] + " is an array.")
            sys.exit()

    # Name: finish_collection_access
    # This function is in charge to create final cuadruples of
    # the collection access, adding the base virtual memory direction to access
    # the correct vm direction
    #
    def finish_collection_access(self):
        aux = self.identifier_stack.pop()
        self.type_stack.pop()
        temp = self.generate_temporal(self.collection['type'])
        base = self.find_var(self.dimension_stack[-1][0])
        self.generate_cuad(self.semantic_cube.converter['+'], aux, '%' + str(0), temp['vm_direction'])
        self.generate_cuad(self.semantic_cube.converter['+'], temp['vm_direction'],'%' + str(base['vm_direction']), temp['vm_direction'])
        self.identifier_stack.append('('+str(temp['vm_direction'])+')')
        self.type_stack.append(self.collection['type'])
        self.operator_stack.pop()
        self.dimension_stack.pop()
        self.collection_names.pop()
        if len(self.collection_names) > 0:
            self.collection = self.find_var(str(self.collection_names[-1]))

    # Name: register_print
    # this function is called from the parser to add the printing
    # cuadruple with the corresponding direction of the expression given.
    #
    def register_print(self):
        value_to_print = self.identifier_stack[-1]
        self.generate_cuad('puts',None,None,str(value_to_print))

    # Name: register_read
    # This function is called from the parser to add a write cuadruple
    # This includes creating a read statement and a parse, which the
    # virtual machine will later use to check that the value matches with
    # the variable type.
    #
    # parameters
    #
    # phrase: is the string constant that will be displayed in the input.
    # header: is the name of the id.
    #
    # error_handle
    #
    # 1) returns if the input is going to be stored in a dimensioned array.
    #
    def register_read(self, phrase, header):
        var = self.find_var(str(header))
        if(var['finish'] == None):
            self.generate_cuad('read', '%'+ str(phrase), None, var['vm_direction'])
            self.generate_cuad('parse', str(var['type']), None, var['vm_direction'])
        else:
            print("dimensioned array cannot have a read input.")
            sys.exit()

    # Name: generate_temporal
    # This function creates a temporal value and inserts it to the current_context
    # variable directory for further use.
    #
    # parameter
    #
    # temporal_type: is the type that the temporal will be registered with.
    #
    def generate_temporal(self, temporal_type):
        temporal_id = "temp" + str(self.counter)
        self.counter += 1
        self.program_engine.register_variable(temporal_type, temporal_id)
        temp_var = self.find_var(temporal_id)
        return temp_var
