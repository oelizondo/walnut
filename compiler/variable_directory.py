class VariableDirectory:
    def __init__(self):
        self.variables = {}

    def register(self, var_type, identifier, value):
        self.variables[identifier] = {
            'type': var_type,
            'name': identifier,
            'value': value
        }
