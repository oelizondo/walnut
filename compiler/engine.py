from context import Context

class Engine:
    def __init__(self):
        self.cuadrples = []
        self.operatorStack = []
        self.typeStack = []
        self.IDStack = []
        self.breakStack = []
        self.gotoStack = []
        self.context = Context('GLOBAL')
        self.current_context = self.context

    def generate_cuad(self):
        cuad = Cuadruple(operation, left_side, right_side, result)
        self.cuadruples.append(cuad)

    def register_variable(self, var_type, identifier, value=None):
        self.current_context.global_directory.register(var_type, identifier, value)

    def register_function(self, header, params=None, return_type=None):
        child_context = Context(header, self.context)
        print(child_context.context)
        self.current_context = child_context
        self.context.function_directory.register(header, params, return_type, child_context)

    def reset_context(self):
        self.current_context = self.context
