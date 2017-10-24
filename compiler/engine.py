from context import Context

class Engine:
    def __init__(self):
        self.cuadruples = []
        self.context = Context('GLOBAL')
        self.current_context = self.context

    def register_variable(self, var_type, identifier, value=None):
        self.current_context.global_directory.register(var_type, identifier, value)

    def register_function(self, header, params=None, return_type=None):
        child_context = Context(header, self.context)
        self.current_context = child_context
        self.context.function_directory.register(header, params, return_type, child_context)

    def reset_context(self):
        self.current_context = self.context

    def send_cuad(cuad):
        self.cuadruples.append(cuad)
