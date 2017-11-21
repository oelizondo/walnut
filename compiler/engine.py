# Engine module: Compilation main head, one of the modules in direct contact with the parser.
# The engine is responsable of managing the contexts and also
# the entrance to all new objects(classes, variables, functions, objects, arrays and matrix)
# along with the insertion of important cuadruples such as: function and method 'eras' and return types,
# 'main'-goto and program end.

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

    # This function registers a new variable (being an array or method as well) and sets it in the current_context
    # variable directory.
    def register_variable(self, var_type, identifier, value=None, dimension=None, finish=None):
        vm_direction = self.get_next_virtual_memory()
        if(finish != None and int(finish) <= 0):
            print("Out of bounds, cannot declare an array with: " + finish + ", value must be bigger than 0")
            sys.exit()
        self.current_context.variable_directory.register(var_type, identifier, value, vm_direction, dimension, finish)

    # This function registers in the global context the function that is being declared
    # setting its name, context and starting point as well as chaging the current context to the function's.
    def register_function(self, header):
        child_context = Context(header, self.current_context)
        self.current_context.function_directory.register(header, child_context, len(self.cuadruples))
        self.current_context = child_context

    # This function registers the class under the current context, thus giving the oportunity to create a class under
    # the scope of another, achieving inheritance.
    def register_class(self, header, extend=None):
        child_context = Context(header, self.context)
        self.context.class_directory.add_class(header, extend, child_context)
        self.current_context = child_context

    # This function registers a new object under the scope of the class in which he is being called.
    # verifying that the class indeed exists by checking in the class directory of the global context.
    def register_new_object(self,header):
        walnut_class = self.context.class_directory.classes.get(header,None)
        if(walnut_class != None):
            self.current_context.object_directory.add_object(walnut_class)
        else:
            print("Cannot instantiate object, class: " + str(header) + " does not exist")

    # This function gets a virtual memory direction for a variable that is going to be created
    # in the function directory and calls the fuction directory method to insert the return type
    # in the specified function (in the correct context, because a class method and a function can have the same name).
    def register_function_return_type(self,header,var_type):
        vm_direction = self.get_next_virtual_memory()
        self.current_context.function_directory.register_return_type(header, var_type, vm_direction)

    # This function creates the method era for a method call, which inserts the name of the object as well.
    def register_method_era(self,header):
        self.register_function_era(str(header),self.current_object)

    # This function registers the cuadruple that marks the beginning of a function call
    def register_function_era(self, header, obj=None):
        cuad = Cuadruple('era',obj,None,str(header))
        self.cuadruples.append(cuad)

    # This function registers the main context, where our program will begin to run.
    # It fills the goto that is waiting for the program main start.
    def register_run_proc(self):
        child_context = Context('main', self.current_context)
        self.context.function_directory.register('main', child_context, len(self.cuadruples)+1)
        self.current_context = child_context
        if(self.cuadruples[0].result == None):
            self.cuadruples[0].result = len(self.cuadruples)
        else:
            self.cuadruples[self.global_goto].result = len(self.cuadruples)

    # Simple function that initialize the cuadruple stack with an empty goto.
    def insert_first_cuad(self):
        cuad = Cuadruple('GOTO',None, None, None)
        self.cuadruples.append(cuad)

    # This function registers the cuadruple for the end of a function.
    def register_end_proc(self):
        cuad = Cuadruple('endproc', None, None, None)
        self.cuadruples.append(cuad)

    # This function validates that the return type is the same as the one declared in the function
    def register_return(self, function_name, return_variable, return_type):
        function = self.current_context.parent.function_directory.functions.get(function_name)
        function_return_type = function.get("return_type")
        if function_return_type == return_type:
            cuad = Cuadruple('return', None, None, return_variable)
            self.cuadruples.append(cuad)

        else:
            print("Return value type in " + function_name + " does not match, received " + return_type + " expected: " + function_return_type)
            sys.exit()

    # This function registers the cuadruple of the end of the program.
    def register_program_end(self):
        cuad = Cuadruple('endprogram', None, None, None)
        self.cuadruples.append(cuad)

    # This function resets the current context to the previous one that enbedded it.
    # it is used in class and function declarations.
    def reset_context(self):
        self.current_context = self.current_context.parent

    # This function sets a special enviroment for the globals, in which the memory_direction
    # is drastically increased to avoid overlap, so global variables will have a 100000 >= vm_direction
    # and sets the first goto to the global cuadruples if they exist (to initialize object and variables with values).
    def set_global_environment(self):
        self.memory_direction += 100000
        self.cuadruples[0].result = len(self.cuadruples)

    # This function is called when the globals are done being declared, removing the 100000 cap given to the vm_directions
    # and setting a new goto that will be fill with the cuadruple of the main starting point.
    def remove_global_enviroment(self):
        self.memory_direction -= 100000
        cuad = Cuadruple('GOTO',None,None,None)
        self.global_goto = len(self.cuadruples)
        self.cuadruples.append(cuad)

    # This function is a helper that resets to global context. This is used at the
    # end of the declaration of classes, so that globals and functions are under they
    # global context
    def reset_to_global(self):
        self.current_context = self.context

    # Helper method that is called from operation and jump_engine to insert cuadruples
    # to the cuadruple stack
    def send_cuad(self, cuad):
        self.cuadruples.append(cuad)

    # Helper method that is called when a new variable is going to be registered, to give
    # the next vm_direction available, and updating it. This method is used in operation.py too.
    def get_next_virtual_memory(self):
        next_avail = self.memory_direction
        self.memory_direction += 1
        return next_avail

    def print_quads(self):
        count = 0
        for cuad in self.cuadruples:
            print(count, cuad.operation, cuad.left_side, cuad.right_side, cuad.result)
            count += 1

    # Method that writes the finished cuadruples in walnut.obj file.
    def write_quads(self):
        with open('walnut.obj', 'wb') as f:
            for cuad in self.cuadruples:
                f.write(str(cuad.operation) + ',')
                f.write(str(cuad.left_side) + ',')
                f.write(str(cuad.right_side) + ',')
                f.write(str(cuad.result))
                f.write('\n')

    def print_classes(self):
        for key, value in self.context.class_directory.classes.iteritems():
            print('')
            print("----------------------------------------------------Class----------------------------------------------------")
            print("class : " + str(key) + " parent_class " +  str(value.extend))
            print("--------------------------Attributes--------------------------")
            for attributes, types in value.context.variable_directory.variables.iteritems():
                print("attribute : " + str(attributes))
            print("--------------------------Functions--------------------------")
            for function, methods in value.context.function_directory.functions.iteritems():
                print("function : " + str(function))
                print(str(value.context.function_directory.functions[function]))
            print("--------------------------ParentAtributes--------------------------")
            for attributes, types in value.context.parent.variable_directory.variables.iteritems():
                print("parent attribute: " + str(attributes))
        print('')
