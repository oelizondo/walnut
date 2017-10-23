class GlobalDirectory:
    def __init__(self):
        self.globals = {}

    def register(self, var_type, identifier, value):
        self.globals[identifier] = {
            'type': var_type,
            'name': identifier,
            'value': value
        }
