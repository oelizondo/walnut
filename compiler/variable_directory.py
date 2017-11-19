import sys

class VariableDirectory:
    def __init__(self):
        self.variables = {}

    def register(self, var_type, identifier, value, vm_direction, dimension=None, finish=None):
        identifier = str(identifier)
        if self.variables.get(identifier, None) is None:
          self.variables[identifier] = {
              'type': var_type,
              'name': identifier,
              'value': value,
              'dimension': dimension,
              'finish': finish,
              'vm_direction': vm_direction
          }
        else:
          print("Variable " + identifier + " is already defined.")
          sys.exit()
