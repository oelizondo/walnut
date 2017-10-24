from semantic_cube import SemanticCube
class Operation:
    def __init__(self, program_engine):
        self.operator_stack = []
        self.type_stack = []
        self.identifier_stack = []
        self.semantic_cube = SemanticCube()
        self.program_engine = program_engine

    def generate_cuad(self, operation, left_side=None, right_side=None, result=None):
        cuad = Cuadruple(operation, left_side, right_side, result)
        program_engine.send_cuad(cuad)

    def add_identifier(self, identifier):
        print(type(identifier))
        if identifier != None:
            starting_context = self.program_engine.current_context
            while starting_context != None and identifier == None:
                identifier = starting_context.variable_directory.variables.get(identifier, None)
                starting_context = starting_context.parent

            if identifier != None:
                print()
                # self.type_stack.append(identifier['type'])
                # self.identifier_stack.append(identifier['value'])

    def compare_op(self):
        if self.operator_stack[len(self.type_stack) - 1] == '&&' or self.operator_stack[len(self.type_stack) - 1] == '||':
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
        if operator_stack[type_stack.length - 1] == '*' or operator_stack[type_stack.length - 1] == '/':
            print(1)
            #  type_right_side = self.semantic_cube.converter.get(self.type_stack.pop(), None))
            #  type_left_side = self.semantic_cube.converter.get(self.type_stack.pop(), None)
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
    def add_substract_op(self):
        if operator_stack[type_stack.length - 1] == '-' or operator_stack[type_stack.length - 1] == '+':
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
    def power_of_op(self):
        if operator_stack[type_stack.length - 1] == '^':
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
