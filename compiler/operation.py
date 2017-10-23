class Operation:
    def __init__(self):
        self.operator_stack = []
        self.type_stack = []
        self.identifier_stack = []

    def add_identifier(self, identifier):
        if identifier != None:
            starting_context = program_engine.current_context
            while starting_context != None and identifier == None:
                identifier = starting_context.variable_directory.variables.get(identifier, None)
                starting_context = starting_context.parent

            if identifier != None:
                self.type_stack.append(identifier['type'])
                self.identifier_stack.append(identifier_stack['value'])

    def multiply_divide(self):
        if operator_stack[type_stack.length - 1] == '*' or operator_stack[type_stack.length - 1] == '/':
            op = operator_stack.pop()
            type_right_side = type_stack.pop()
            type_left_side = type_stack.pop()
            right_side = identifier_stack.pop()
            left_side = identifier_stack.pop()
            res_type = semantic_cube.get((type_right_side, type_left_side, op), None)
            if res_type != None:
                if op == '*':
                    res = left_side * right_side
                else:
                    res = left_side / right_side
                self.identifier_stack.append(res)
                cuad(op, left_side, right_side, res)
            else:
                # generar error de tipos
