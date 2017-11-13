from semantic_cube import SemanticCube
from cuadruple import Cuadruple
import sys

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
        self.semantic_cube = SemanticCube()
        self.program_engine = program_engine
        self.counter = 0
        self.current_function = ''
        self.parameter_counter = 0

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
            starting_context = self.program_engine.current_context
            var = None
            while var == None and starting_context != None:
                var = starting_context.variable_directory.variables.get(variable, None)
                starting_context = starting_context.parent

            if starting_context == None and var == None:
                print("Variable " + variable + " doesn't exist")
                sys.exit()

            if variable != None:
                self.type_stack.append(str(var['type']))
                # self.identifier_stack.append(var['value'])
                self.identifier_stack.append(str(variable))

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
        function_recieved = self.program_engine.context.function_directory.functions.get(header,None)
        if function_recieved != None:
            if (function_recieved.get("return_type") != None):
                self.type_stack.append(function_recieved["return_type"])
            else:
                self.type_stack.append('void')
            self.identifier_stack.append(header)
        else:
            print("function" + str(header) + "does not exist")

    # This function validates the parameter that is given in a function call. It checks that the argument type and parameter type
    # are compatible and can be assigned. It also checks that the number of arguments given does not exeeds the permited.
    def argument_validation(self):
        function_parameters = self.program_engine.context.function_directory.functions[self.current_function].get('parameters')
        if self.parameter_counter < len(function_parameters):
            parameter_type = function_parameters[self.parameter_counter]
            argument_type = self.type_stack[len(self.type_stack) - 1]
            if parameter_type != argument_type :
                print("Type error in "+ str(self.current_function) +" function call in (" + str(self.parameter_counter + 1) + ") argument given: " + str(argument_type) + " expected: " + str(parameter_type))
                sys.exit()
            self.parameter_counter += 1
        else:
            print("Argument error in "+ str(self.current_function) +" function call, expected only " + str(self.parameter_counter) + " argument(s)")
            sys.exit()

    # This function checks that the number of arguments given to the function call are complete and resets the parameter counter to 0
    # to prepare it for next function calls
    def argument_number_validation(self):
        function_parameters = self.program_engine.context.function_directory.functions[self.current_function].get('parameters')
        if self.parameter_counter == len(function_parameters):
            self.parameter_counter = 0
        else:
            print("Argument error in "+ str(self.current_function) +" function call, expected " + str(len(function_parameters)) + " argument(s)")
            sys.exit()

    def compare_op(self):
        if len(self.operator_stack) == 0:
            return
        op = self.operator_stack[len(self.operator_stack) - 1]
        if op == '&&' or op == '||' or op == 'and' or op == 'or':
            op = self.semantic_cube.converter.get(self.operator_stack.pop(), None)
            type_right_side = self.semantic_cube.converter.get(self.type_stack.pop(), None)
            type_left_side = self.semantic_cube.converter.get(self.type_stack.pop(), None)
            right_side = extract_value(self.identifier_stack.pop())
            left_side = extract_value(self.identifier_stack.pop())
            res_type = self.semantic_cube.semantic_cube.get((type_right_side, type_left_side, int(op)), None)
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
                print("Type Error cannot \"" + str(self.semantic_cube.inverter[op]) + "\" values " + str(right_side) + " and " + str(left_side))
                print("incompatible types: " + str(self.semantic_cube.inverter[type_right_side]) + " and " + str(self.semantic_cube.inverter[type_left_side]))

    def is_relational_op(self, op):
        return op == '<' or op == '>' or op =='>=' or op == '<=' or op == '==' or op == 'is' or op == '!=' or op == 'not'

    def compare_relational_op(self):
        if len(self.operator_stack) == 0:
            return
        op = self.operator_stack[len(self.operator_stack) - 1]
        if self.is_relational_op(op):
            op = self.semantic_cube.converter.get(self.operator_stack.pop(), None)
            type_right_side = self.semantic_cube.converter.get(self.type_stack.pop(), None)
            type_left_side = self.semantic_cube.converter.get(self.type_stack.pop(), None)
            right_side = extract_value(self.identifier_stack.pop())
            left_side = extract_value(self.identifier_stack.pop())
            res_type = self.semantic_cube.semantic_cube.get((type_right_side, type_left_side, int(op)), None)
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
                print("Type Error cannot \"" + str(self.semantic_cube.inverter[op]) + "\" values " + str(right_side) + " and " + str(left_side))
                print("incompatible types: " + str(self.semantic_cube.inverter[type_right_side]) + " and " + str(self.semantic_cube.inverter[type_left_side]))
                sys.exit()

    def multiply_divide_op(self):
        if len(self.operator_stack) == 0:
            return
        if self.operator_stack[len(self.operator_stack) - 1] == '*' or self.operator_stack[len(self.operator_stack) - 1] == '/':
            op = self.semantic_cube.converter.get(self.operator_stack.pop(), None)
            type_right_side = self.semantic_cube.converter.get(self.type_stack.pop(), None)
            type_left_side = self.semantic_cube.converter.get(self.type_stack.pop(), None)
            right_side = extract_value(self.identifier_stack.pop())
            left_side = extract_value(self.identifier_stack.pop())
            res_type = self.semantic_cube.semantic_cube.get((type_right_side, type_left_side, int(op)), None)
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
                print("Type Error cannot \"" + str(self.semantic_cube.inverter[op]) + "\" values " + str(right_side) + " and " + str(left_side))
                print("incompatible types: " + str(self.semantic_cube.inverter[type_right_side]) + " and " + str(self.semantic_cube.inverter[type_left_side]))
                sys.exit()

    def add_substract_op(self):
        if len(self.operator_stack) == 0:
            return

        if self.operator_stack[len(self.operator_stack) - 1] == '-' or self.operator_stack[len(self.operator_stack) - 1] == '+':
            op = self.semantic_cube.converter.get(self.operator_stack.pop(), None)
            type_right_side = self.semantic_cube.converter.get(self.type_stack.pop(), None)
            type_left_side = self.semantic_cube.converter.get(self.type_stack.pop(), None)
            right_side = extract_value(self.identifier_stack.pop())
            left_side = extract_value(self.identifier_stack.pop())
            res_type = self.semantic_cube.semantic_cube.get((type_right_side, type_left_side, int(op)), None)
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
                print("Type Error cannot \"" + str(self.semantic_cube.inverter[op]) + "\" values " + str(right_side) + " and " + str(left_side))
                print("incompatible types: " + str(self.semantic_cube.inverter[type_right_side]) + " and " + str(self.semantic_cube.inverter[type_left_side]))
                sys.exit()

    def power_of_op(self):
        if len(self.operator_stack) == 0:
            return
        if self.operator_stack[len(self.operator_stack) - 1] == '^':
            op = self.semantic_cube.converter.get(self.operator_stack.pop(), None)
            type_right_side = self.semantic_cube.converter.get(self.type_stack.pop(), None)
            type_left_side = self.semantic_cube.converter.get(self.type_stack.pop(), None)
            right_side = extract_value(self.identifier_stack.pop())
            left_side = extract_value(self.identifier_stack.pop())
            res_type = self.semantic_cube.semantic_cube.get((type_right_side, type_left_side, int(op)), None)
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
                print("Type Error cannot \"" + str(self.semantic_cube.inverter[op]) + "\" values " + str(right_side) + " and " + str(left_side))
                print("incompatible types: " + str(self.semantic_cube.inverter[type_right_side]) + " and " + str(self.semantic_cube.inverter[type_left_side]))
                sys.exit()

    def assign_operation(self, identifier):
        if identifier != None:
            starting_context = self.program_engine.current_context
            var = None
            while var == None and starting_context != None:
                var = starting_context.variable_directory.variables.get(identifier, None)
                starting_context = starting_context.parent

            if starting_context == None and var == None:
                print("Variable " + identifier + " doesn't exist")
                sys.exit()
            else:
                to_assign_value = self.identifier_stack[len(self.identifier_stack) - 1]
                to_assign_type = self.type_stack[len(self.type_stack) - 1]
                if var['type'] == to_assign_type:
                    var['value'] = to_assign_value
                    self.generate_cuad(self.semantic_cube.converter['='], to_assign_value, None, var['name'])
                else:
                    print("Type Error cannot assign the value " + str(to_assign_value) + " to " + str(var['name']))
                    if to_assign_type == 'void':
                        print(str(to_assign_value) + " is a void function")
                    else:
                        print("incompatible types: " + str(to_assign_t) + " and " + str(var['type']))
                    sys.exit()
