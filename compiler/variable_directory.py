# VariableDirectory module
# It is in charge of having the record of all the information of
# all variables in its current context.
#
# attribute
#
# variables: the dictionary that contains all the information of the variables
#            under its context.
import sys

class VariableDirectory:
    def __init__(self):
        self.variables = {}

    # Name: register
    # This function is charge to load a new identifier with all the information given
    #
    # parameters
    #
    # var_type: its the variable type
    # identifier: the name of the variable
    # vm_direction: the virtual memory direction
    # dimension: (only if its a collection) the dimension quantity (1-2)
    # finish: (only if its a collection) memory location needed for the collection
    #
    # error_handler
    #
    # 1) returns if a variable is already defined.
    #
    def register(self, var_type, identifier, vm_direction, dimension=None, finish=None):
        identifier = str(identifier)
        if self.variables.get(identifier, None) is None:
          self.variables[identifier] = {
              'type': var_type,
              'name': identifier,
              'dimension': dimension,
              'finish': finish,
              'vm_direction': vm_direction
          }
        else:
          print("Variable " + identifier + " is already defined.")
          sys.exit()
