from semantic_cube import SemanticCube
from cuadruple import Cuadruple
import sys
# % mark: refers to a constant

def is_int(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

def is_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

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

    def generate_cuad(self, operation, left_side=None, right_side=None, result=None):
        cuad = Cuadruple(operation, left_side, right_side, result)
        self.program_engine.send_cuad(cuad)

    def add_identifier(self, identifier, constant, function):
        if identifier != None:
            self.add(identifier)
        elif constant != None:
            self.add_constant(constant)
        # elif obj != None:
        #     self.add_constant(obj)
        #  else:
        #     self.add_constant(array)

    def add(self, variable):
        if variable != None:
            var = self.find_var(variable)
            if var['dimension'] == None:
                self.type_stack.append(str(var['type']))
                # self.identifier_stack.append(var['value'])
                self.identifier_stack.append(str(variable))
            else:
                print("Variable " + var['name'] + " is dimensioned.")
                sys.exit()

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

    # This function checks that the function called exists and sets the function "variable" in the identifier/type stack
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

    def function_return_save(self):
        function_id = self.identifier_stack.pop()
        temporal_id = "temp" + str(self.counter)
        self.identifier_stack.append(temporal_id)
        self.counter += 1
        self.generate_cuad(23,function_id,None,temporal_id)

    # This function validates the parameter that is given in a function call. It checks that the argument type and parameter type
    # are compatible and can be assigned. It also checks that the number of arguments given does not exeeds the permited.
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

    # This function checks that the number of arguments given to the function call are complete and resets the parameter counter to 0
    # to prepare it for next function calls
    def argument_number_validation(self):
        func = self.find_function(self.current_function, self.program_engine.current_context)
        function_parameters = func.get('parameters')
        if self.parameter_counter == len(function_parameters):
            self.reset_parameter_counter()
        else:
            print("Argument error in "+ str(self.current_function) +" function call, expected " + str(len(function_parameters)) + " argument(s)")
            sys.exit()


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

    def method_argument_number_validation(self):
        obj_context = self.get_object_context()
        func = self.find_obj_function(self.current_function, obj_context)
        function_parameters = func.get('parameters')
        if self.parameter_counter == len(function_parameters):
            self.reset_parameter_counter()
        else:
            print("Argument error in object "+ str(self.current_function) +" function call, expected " + str(len(function_parameters)) + " argument(s)")
            sys.exit()

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

    def register_parameter(self,var_type,header):
        self.program_engine.current_context.function_directory.register_parameter(var_type, header)
        var = self.find_var(header)
        self.generate_cuad(23,'param'+ str(self.parameter_counter+1), None, var['name'])
        self.parameter_counter += 1

    def compare_op(self):
        if len(self.operator_stack) == 0:
            return
        op = self.operator_stack[-1]
        if op == '&&' or op == '||' or op == 'and' or op == 'or':
            op = self.semantic_cube.converter.get(self.operator_stack.pop(), None)
            type_right_side = self.semantic_cube.converter.get(self.type_stack.pop(), None)
            type_left_side = self.semantic_cube.converter.get(self.type_stack.pop(), None)
            right_side = extract_value(self.identifier_stack.pop())
            left_side = extract_value(self.identifier_stack.pop())
            res_type = self.semantic_cube.semantic_cube.get((type_left_side, type_right_side, int(op)), None)
            if res_type != None:
                temporal_id = "temp" + str(self.counter)
                self.generate_cuad(op, left_side, right_side, temporal_id)
                self.program_engine.register_variable(res_type, temporal_id, None)
                self.counter += 1
                self.type_stack.append(self.semantic_cube.inverter[res_type])
                self.identifier_stack.append(temporal_id)
                # if op == 20:
                #     res = left_side * right_side
                # else:
                #     res = left_side / right_side
            else:
                print("Type Error, cannot \"" + str(self.semantic_cube.inverter[op]) + "\" values")
                print("incompatible types: " + str(self.semantic_cube.inverter[type_right_side]) + " and " + str(self.semantic_cube.inverter[type_left_side]))
                sys.exit()

    def is_relational_op(self, op):
        return op == '<' or op == '>' or op =='>=' or op == '<=' or op == '==' or op == 'is' or op == '!=' or op == 'not'

    def compare_relational_op(self):
        if len(self.operator_stack) == 0:
            return
        op = self.operator_stack[-1]
        if self.is_relational_op(op):
            op = self.semantic_cube.converter.get(self.operator_stack.pop(), None)
            type_right_side = self.semantic_cube.converter.get(self.type_stack.pop(), None)
            type_left_side = self.semantic_cube.converter.get(self.type_stack.pop(), None)
            right_side = extract_value(self.identifier_stack.pop())
            left_side = extract_value(self.identifier_stack.pop())
            res_type = self.semantic_cube.semantic_cube.get((type_left_side, type_right_side, int(op)), None)
            if res_type != None:
                temporal_id = "temp" + str(self.counter)
                self.generate_cuad(op, left_side, right_side, temporal_id)
                self.program_engine.register_variable(res_type, temporal_id, None)
                self.counter += 1
                self.type_stack.append(self.semantic_cube.inverter[res_type])
                self.identifier_stack.append(temporal_id)
                # if op == 20:
                #     res = left_side * right_side
                # else:
                #     res = left_side / right_side
            else:
                print("Type Error, cannot \"" + str(self.semantic_cube.inverter[op]) + "\" values")
                print("incompatible types: " + str(self.semantic_cube.inverter[type_right_side]) + " and " + str(self.semantic_cube.inverter[type_left_side]))
                sys.exit()

    def multiply_divide_op(self):
        if len(self.operator_stack) == 0:
            return
        if self.operator_stack[-1] == '*' or self.operator_stack[-1] == '/':
            op = self.semantic_cube.converter.get(self.operator_stack.pop(), None)
            type_right_side = self.semantic_cube.converter.get(self.type_stack.pop(), None)
            type_left_side = self.semantic_cube.converter.get(self.type_stack.pop(), None)
            right_side = extract_value(self.identifier_stack.pop())
            left_side = extract_value(self.identifier_stack.pop())
            res_type = self.semantic_cube.semantic_cube.get((type_left_side, type_right_side, int(op)), None)
            if res_type != None:
                temporal_id = "temp" + str(self.counter)
                self.generate_cuad(op, left_side, right_side, temporal_id)
                self.program_engine.register_variable(res_type, temporal_id, None)
                self.counter += 1
                self.type_stack.append(self.semantic_cube.inverter[res_type])
                self.identifier_stack.append(temporal_id)
                # if op == 20:
                #     res = left_side * right_side
                # else:
                #     res = left_side / right_side

            else:
                print("Type Error, cannot \"" + str(self.semantic_cube.inverter[op]) + "\" values")
                print("incompatible types: " + str(self.semantic_cube.inverter[type_right_side]) + " and " + str(self.semantic_cube.inverter[type_left_side]))
                sys.exit()

    def add_substract_op(self):
        if len(self.operator_stack) == 0:
            return

        if self.operator_stack[-1] == '-' or self.operator_stack[-1] == '+':
            op = self.semantic_cube.converter.get(self.operator_stack.pop(), None)
            type_right_side = self.semantic_cube.converter.get(self.type_stack.pop(), None)
            type_left_side = self.semantic_cube.converter.get(self.type_stack.pop(), None)
            right_side = extract_value(self.identifier_stack.pop())
            left_side = extract_value(self.identifier_stack.pop())
            res_type = self.semantic_cube.semantic_cube.get((type_left_side, type_right_side, int(op)), None)
            if res_type != None:
                temporal_id = "temp" + str(self.counter)
                self.generate_cuad(op, left_side, right_side, temporal_id)
                self.program_engine.register_variable(res_type, temporal_id, None)
                self.counter += 1
                self.type_stack.append(self.semantic_cube.inverter[res_type])
                self.identifier_stack.append(temporal_id)
                # if op == 21:
                #     res = left_side + right_side
                # else:
                #     res = left_side - right_side
            else:
                print("Type Error, cannot \"" + str(self.semantic_cube.inverter[op]) + "\" values")
                print("incompatible types: " + str(self.semantic_cube.inverter[type_right_side]) + " and " + str(self.semantic_cube.inverter[type_left_side]))
                sys.exit()

    def power_of_op(self):
        if len(self.operator_stack) == 0:
            return
        if self.operator_stack[-1] == '^':
            op = self.semantic_cube.converter.get(self.operator_stack.pop(), None)
            type_right_side = self.semantic_cube.converter.get(self.type_stack.pop(), None)
            type_left_side = self.semantic_cube.converter.get(self.type_stack.pop(), None)
            right_side = extract_value(self.identifier_stack.pop())
            left_side = extract_value(self.identifier_stack.pop())
            res_type = self.semantic_cube.semantic_cube.get((type_left_side, type_right_side, int(op)), None)
            if res_type != None:
                temporal_id = "temp" + str(self.counter)
                self.generate_cuad(op, left_side, right_side, temporal_id)
                self.program_engine.register_variable(res_type, temporal_id, None)
                self.counter += 1
                self.type_stack.append(self.semantic_cube.inverter[res_type])
                self.identifier_stack.append(temporal_id)
                # if op == '*':
                #     res = left_side * right_side
                # else:
                #     res = left_side / right_side
            else:
                print("Type Error, cannot \"" + str(self.semantic_cube.inverter[op]) + "\" values")
                print("incompatible types: " + str(self.semantic_cube.inverter[type_right_side]) + " and " + str(self.semantic_cube.inverter[type_left_side]))
                sys.exit()

    def assign_operation(self, identifier):
        if identifier != None:
            var = self.find_var(identifier)
            to_assign_value = self.identifier_stack[len(self.identifier_stack) - 1]
            to_assign_type = self.type_stack[len(self.type_stack) - 1]
            to_assign_type = self.semantic_cube.converter[str(to_assign_type)]
            to_be_assigned = self.semantic_cube.converter[str(var['type'])]
            res_type = self.semantic_cube.semantic_cube.get((to_be_assigned, to_assign_type, 23), None)
            if res_type != None:
                var['value'] = to_assign_value
                self.generate_cuad(self.semantic_cube.converter['='], to_assign_value, None, var['name'])
            else:
                print("Type Error: cannot assign the value to " + str(var['name']))
                if to_assign_type == 'void':
                    print("value is from a void function")
                else:
                    print("incompatible types: " + str(to_assign_type) + " and " + str(var['type']))
                sys.exit()

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

    def set_current_object(self, header):
        self.current_object = header
        self.program_engine.current_object = header

    def reset_parameter_counter(self):
        self.parameter_counter = 0

    def reset_status(self):
        self.parameter_counter = self.param_counter_stack.pop()
        self.current_function = self.function_stack.pop()

    def save_status(self):
        self.param_counter_stack.append(self.parameter_counter)
        self.function_stack.append(self.current_function)
        self.reset_parameter_counter()

    def verify_boolean(self):
        to_assign_type = self.type_stack[len(self.type_stack) - 1]
        if(to_assign_type != 'boolean'):
            print("Conditional statement expected boolean, recieved: " + str(to_assign_type))
            sys.exit()

    def verify_dimensions(self):
        self.collection_names.append(self.identifier_stack.pop())
        self.collection = self.find_var(str(self.collection_names[-1]))

        if len(self.collection['dimension']) > 0:
            self.dimension_stack.append([self.collection_names[-1], 1])
            self.operator_stack.append('[')
        else:
            print("Error var not dimensioned")
            sys.exit()

    def generate_access_cuad(self, cell):
        if (self.type_stack[-1] == 'int'):
            self.generate_cuad('ver', self.identifier_stack[-1], 0, self.collection['dimension'][cell]['limit'])

            if len(self.collection['dimension']) > self.dimension_stack[-1][1]:
                aux = self.identifier_stack.pop()
                temp = self.generate_temporal()
                self.generate_cuad(self.semantic_cube.converter['*'], aux, '%' + str(self.collection['dimension'][cell]['k']), temp)
                self.identifier_stack.append(temp)
                self.type_stack.append('int')


            if  self.dimension_stack[-1][1] > 1:
                aux1 = self.identifier_stack.pop()
                aux2 = self.identifier_stack.pop()
                temp = self.generate_temporal()
                self.generate_cuad(self.semantic_cube.converter['+'], aux1, aux2, temp)
                self.identifier_stack.append(temp)
                self.type_stack.append('int')
        else:
            print("Type error for collection access expected int got " + self.type_stack[-1])
            sys.exit()

    def update_dimension(self):
        self.dimension_stack[-1][1] += 1

    def verify_array(self):
        dimensions = len(self.collection['dimension'])
        if self.dimension_stack[-1][1] != dimensions:
            print("Variable " + self.collection['name'] + " is a matrix.")
            sys.exit()

    def verify_matrix(self):
        dimensions = len(self.collection['dimension'])
        if  self.dimension_stack[-1][1] > dimensions:
            print("Variable " + self.collection['name'] + " is an array.")
            sys.exit()


    def finish_collection_access(self):
        aux = self.identifier_stack.pop()
        temp = self.generate_temporal()
        self.generate_cuad(self.semantic_cube.converter['+'], aux, 0, temp)
        self.generate_cuad(self.semantic_cube.converter['+'], temp, self.dimension_stack[-1][0], temp)
        self.identifier_stack.append('('+temp+')')
        self.type_stack.append(self.collection['type'])
        self.operator_stack.pop()
        self.dimension_stack.pop()
        self.collection_names.pop()
        if len(self.collection_names) > 0:
            self.collection = self.find_var(str(self.collection_names[-1]))

    def register_print(self):
        value_to_print = self.identifier_stack[len(self.type_stack) - 1]
        self.generate_cuad('puts',None,None,str(value_to_print))

    def generate_temporal(self):
        self.counter += 1
        return "temp" + str(self.counter)
