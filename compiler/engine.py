# Engine module: Compilation main head, one of the modules in direct contact with the parser.
# The engine is responsable of managing the contexts and also
# the entrance to all new objects(classes, variables, functions, objects, arrays and matrix)
# along with the insertion of important cuadruples such as: function and method 'eras' and return types,
# 'main'-goto and program end.
#
# attributes:
# cuadruples: stack that stores the cuadruples created through compilation
# context: the global context
# current_context: active context
# current_object: helper attribute to settle object 'era'
# jump_stack: helper attribute to fill goto's
# memory_direction: attribute that has the next memory available to set to a variable
# global_goto: attribute that has the direction of the goto to fill if global variables are present.

from context import Context
from cuadruple import Cuadruple
import sys

class Engine:
    def __init__(self):
        self.cuadruples = []
        self.context = Context('GLOBAL')
        self.current_context = self.context
        self.current_object = ''
        self.jump_stack = []
        self.memory_direction = 1000
        self.global_goto = 0

    # Name: register_variable
    # This function registers a new variable (being an array or method as well) and sets it in the current_context
    # variable directory.
    #
    # parameters
    #
    # var_type: the type of the variable
    # identifier: the identifier that wants to be registered
    # dimension: if a variable is dimensioned it will recieve a empty stack
    # finish: will be the upper limit of the dimension.
    #
    # error_handle
    #
    # 1) returns if a dimension limit is less or equal to than 0
    #
    def register_variable(self, var_type, identifier, dimension=None, finish=None):
        vm_direction = self.get_next_virtual_memory()
        if(finish != None and int(finish) <= 0):
            print("Out of bounds, cannot declare an array with: " + finish + ", value must be bigger than 0")
            sys.exit()
        self.current_context.variable_directory.register(var_type, identifier, vm_direction, dimension, finish)

    # Name: register_function
    # This function registers in the global context the function that is being declared
    # setting its name, context and starting point as well as chaging the current context to the function's.
    #
    # parameters
    #
    # header: is the name of the function to be registered
    #
    def register_function(self, header):
        child_context = Context(header, self.current_context)
        self.current_context.function_directory.register(header, child_context, len(self.cuadruples))
        self.current_context = child_context

    # Name: register_class
    # This function registers the class under the current context, thus giving the oportunity to create a class under
    # the scope of another, achieving inheritance.
    #
    # parameters
    #
    # header: name of the class to be registered
    # extends: is the name of the parent class.
    #
    def register_class(self, header, extend=None):
        child_context = Context(header, self.context)
        self.context.class_directory.add_class(header, extend, child_context)
        self.current_context = child_context

    # Name: register_new_object
    # This function registers a new object under the scope of the class in which he is being called.
    # verifying that the class indeed exists by checking in the class directory of the global context.
    #
    # parameters
    #
    # header: the name of the new object to be registered
    #
    # error_handle
    #
    # 1) returns if an object wants to be declared under the scope of a nonexistent class.
    #
    def register_new_object(self,header):
        walnut_class = self.context.class_directory.classes.get(header,None)
        if(walnut_class != None):
            self.current_context.object_directory.add_object(walnut_class)
        else:
            print("Cannot instantiate object, class: " + str(header) + " does not exist")

    # Name: register_function_return_type
    # This function gets a virtual memory direction for a variable that is going to be created (with the name of the function)
    # in the function directory and calls the fuction directory method to insert the return type
    # in the specified function (in the correct context, because a class method and a function can have the same name).
    #
    # parameters
    #
    # header: name of the function
    # var_type: the return type of the function that is going to be applied to the new variable.
    #
    def register_function_return_type(self,header,var_type):
        vm_direction = self.get_next_virtual_memory()
        self.current_context.function_directory.register_return_type(header, var_type, vm_direction)

    # Name: register_method_era
    # This function creates the method era for a method call, which inserts the name of the object
    # in the cuadruple as well.
    #
    # parameters
    #
    # header: name of the function
    #
    def register_method_era(self,header):
        self.register_function_era(str(header),self.current_object)

    # Name: register_function_era
    # This function registers the cuadruple that marks the beginning of a function call
    #
    # parameters
    #
    # header: name of the function
    # obj: object name, used when it comes from a method era.
    #
    def register_function_era(self, header, obj=None):
        cuad = Cuadruple('era',obj,None,str(header))
        self.cuadruples.append(cuad)

    # Name: register_run_proc
    # This function registers the main context, where our program will begin to run.
    # It fills the goto that is waiting for the program main start.
    #
    def register_run_proc(self):
        child_context = Context('main', self.current_context)
        self.context.function_directory.register('main', child_context, len(self.cuadruples)+1)
        self.current_context = child_context
        if(self.cuadruples[0].result == None):
            self.cuadruples[0].result = len(self.cuadruples)
        else:
            self.cuadruples[self.global_goto].result = len(self.cuadruples)

    # Name: insert_first_cuad
    # Simple function that initialize the cuadruple stack with an empty goto.
    #
    def insert_first_cuad(self):
        cuad = Cuadruple('GOTO',None, None, None)
        self.cuadruples.append(cuad)

    # Name: register_end_proc
    # This function registers the cuadruple for the end of a function.
    #
    def register_end_proc(self):
        cuad = Cuadruple('endproc', None, None, None)
        self.cuadruples.append(cuad)

    # Name: register_return
    # This function validates that the return type is the same as the one declared in the function.
    # if the return type and expression type does not match, it throws and exception and shuts.
    #
    # parameters
    #
    # function_name: the name of the function to be searched.
    # return_variable: the vm_direction of the return expression
    # return_type: variable used to match the intended return tyoe of the function and the expression
    #
    # error_handle
    #
    # 1) returns if a function name recieves a diferent type rather than the expected one.
    #
    def register_return(self, function_name, return_variable, return_type):
        function = self.current_context.parent.function_directory.functions.get(function_name)
        function_return_type = function.get("return_type")
        if function_return_type == return_type:
            cuad = Cuadruple('return', None, None, return_variable)
            self.cuadruples.append(cuad)

        else:
            print("Return value type in " + function_name + " does not match, received " + return_type + " expected: " + function_return_type)
            sys.exit()

    # Name: register_program_end
    # This function registers the cuadruple of the end of the program.
    #
    def register_program_end(self):
        cuad = Cuadruple('endprogram', None, None, None)
        self.cuadruples.append(cuad)

    # Name: reset_context
    # This function resets the current context to the previous one that enbedded it.
    # it is used in class and function declarations.
    #
    def reset_context(self):
        self.current_context = self.current_context.parent

    # Name: set_global_environment
    # This function sets a special enviroment for the globals, in which the memory_direction
    # is drastically increased to avoid overlap, so global variables will have a 100000 >= vm_direction
    # and sets the first goto to the global cuadruples if they exist (to initialize object and variables with values).
    #
    def set_global_environment(self):
        self.memory_direction += 100000
        self.cuadruples[0].result = len(self.cuadruples)

    # Name: remove_global_enviroment
    # This function is called when the globals are done being declared, removing the 100000 cap given to the vm_directions
    # and setting a new goto that will be fill with the cuadruple of the main starting point.
    #
    def remove_global_enviroment(self):
        self.memory_direction -= 100000
        cuad = Cuadruple('GOTO',None,None,None)
        self.global_goto = len(self.cuadruples)
        self.cuadruples.append(cuad)

    # Name: reset_to_global
    # This function is a helper that resets to global context. This is used at the
    # end of the declaration of classes, so that globals and functions are under they
    # global context
    #
    def reset_to_global(self):
        self.current_context = self.context

    # Name: send_cuad
    # Helper method that is called from operation and jump_engine to insert cuadruples
    # to the cuadruple stack
    #
    # parameters
    #
    # cuad: cuadruple to be stacked in the cuadruples_stack
    #
    def send_cuad(self, cuad):
        self.cuadruples.append(cuad)

    # Name: get_next_virtual_memory
    # Helper method that is called when a new variable is going to be registered, to give
    # the next vm_direction available, and updating it. This method is used in operation.py too.
    #
    def get_next_virtual_memory(self):
        next_avail = self.memory_direction
        self.memory_direction += 1
        return next_avail

    def print_quads(self):
        count = 0
        for cuad in self.cuadruples:
            print(count, cuad.operation, cuad.left_side, cuad.right_side, cuad.result)
            count += 1

    # Name: write_quads
    # Method that writes the finished cuadruples in walnut.obj file.
    #
    def write_quads(self):
        with open('walnut.obj', 'wb') as f:
            for cuad in self.cuadruples:
                f.write(str(cuad.operation) + ',')
                f.write(str(cuad.left_side) + ',')
                f.write(str(cuad.right_side) + ',')
                f.write(str(cuad.result))
                f.write('\n')
