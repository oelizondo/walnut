from context import Context
from cuadruple import Cuadruple

class Engine:
    def __init__(self):
        self.cuadruples = []
        self.context = Context('GLOBAL')
        self.current_context = self.context
        self.jump_stack = []

    def register_variable(self, var_type, identifier, value=None):
        self.current_context.variable_directory.register(var_type, identifier, value)

    def register_function(self, header):
        child_context = Context(header, self.current_context)
        self.current_context.function_directory.register(header, child_context, len(self.cuadruples)+1)
        self.current_context = child_context

    def register_class(self, header, extend=None):
        child_context = Context(header, self.context)
        self.context.class_directory.add_class(header, extend, child_context)
        self.current_context = child_context

    def register_run_proc(self):
        child_context = Context('main', self.current_context)
        self.context.function_directory.register('main', child_context, len(self.cuadruples)+1)
        self.current_context = child_context

        cuad = Cuadruple('goto',None, None, len(self.cuadruples)+1)
        self.cuadruples.insert(0,cuad)

    def register_end_proc(self):
        cuad = Cuadruple('endproc', None, None, None)
        self.cuadruples.append(cuad)

    def register_program_end(self):
        cuad = Cuadruple('endprogram', None, None, None)
        self.cuadruples.append(cuad)


    def reset_context(self):
        print(str(self.current_context.context) + " -> father -> " + str(self.current_context.parent.context))
        self.current_context = self.current_context.parent

    def reset_to_global(self):
        self.current_context = self.context

    def send_cuad(self, cuad):
        self.cuadruples.append(cuad)

    def print_quads(self):
        count = 0
        for cuad in self.cuadruples:
            print(count, cuad.operation, cuad.left_side, cuad.right_side, cuad.result)
            count += 1

    def print_main(self):
        print(self.context.function_directory.functions)

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
