from semantic_cube import SemanticCube
from cuadruple import Cuadruple
from variable import Variable
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

    def generate_cuad(self, operation, left_side=None, right_side=None, result=None):
        cuad = Cuadruple(operation, left_side, right_side, result)
        self.program_engine.send_cuad(cuad)

    def add_identifier(self, identifier, constant, obj, function, array):
        if identifier != None:
            self.add(identifier)
        elif constant != None:
            self.add_constant(constant)
        elif obj != None:
            self.add_constant(obj)
        elif function != None:
            self.add_constant(function)
        else:
            self.add_constant(array)

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
                self.identifier_stack.append(var['value'])

    def add_constant(self, constant):
        if is_int(constant):
            self.type_stack.append('int')
            self.identifier_stack.append(int(constant))
        elif is_float(constant):
            self.type_stack.append('float')
            self.identifier_stack.append(float(constant))
        else:
            print("Type Error")
            sys.exit()

    def compare_op(self):
        if len(self.operator_stack) == 0:
            return
        if self.operator_stack[len(self.operator_stack) - 1] == '&&' or self.operator_stack[len(self.operator_stack) - 1] == '||':
            op = self.operator_stack.pop()
            # type_right_side = self.semantic_cube.converter.get(self.type_stack.pop(), None)
            # type_left_side = self.semantic_cube.converter.get(self.type_stack.pop(), None)
            right_side = self.identifier_stack.pop()
            left_side = self.identifier_stack.pop()
            # res_type = self.semantic_cube.get((type_right_side, type_left_side, op), None)
            # if res_type != None:
            #     if op == '&&':
            #         res = left_side & right_side
            #     else:
            #         res = left_side | right_side
            #     self.identifier_stack.append(res)
            self.generate_cuad(op, left_side, right_side, 0)
            # else:
            #     print("something")

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
                self.generate_cuad(op, left_side, right_side, Variable(temporal_id, None, res_type))
                self.program_engine.register_variable(res_type, temporal_id, None)
                # if op == 20:
                #     res = left_side * right_side
                # else:
                #     res = left_side / right_side
                self.counter += 1
                self.identifier_stack.append(temporal_id)
                # self.generate_cuad(op, left_side, right_side, res)
            else:
                print("Type Error")
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
                self.generate_cuad(op, left_side, right_side, Variable(temporal_id, None, res_type))
                self.program_engine.register_variable(res_type, temporal_id, None)
                # if op == 21:
                #     res = left_side + right_side
                # else:
                #     res = left_side - right_side
                self.counter += 1
                self.identifier_stack.append(temporal_id)
                # self.generate_cuad(op, left_side, right_side, res)
            else:
                print("Type Error")
                sys.exit()

    def power_of_op(self):
        if len(self.operator_stack) == 0:
            return
        if self.operator_stack[len(self.operator_stack) - 1] == '^':
            print(1)
            # type_right_side = self.semantic_cube.converter.get(self.type_stack.pop(), None)
            # type_left_side = self.semantic_cube.converter.get(self.type_stack.pop(), None)
            # right_side = self.identifier_stack.pop()
            # left_side = self.identifier_stack.pop()
            # res_type = self.semantic_cube.get((type_right_side, type_left_side, op), None)
            # if res_type != None:
            #     if op == '*':
            #         res = left_side * right_side
            #     else:
            #         res = left_side / right_side
            #     self.identifier_stack.append(res)
        # program_engine.generate_cuad(op, left_side, right_side, 0)
            # else:
            #     print("something")
