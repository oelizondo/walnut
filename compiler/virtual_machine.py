semantic_cube = [[[]],[[]],[[]]]

class Cuadruple:
    def __init__(self, operation, left_side, right_side, result):
        self.operation = operation
        self.left_side = left_side
        self.right_side = right_side
        self.result = result

class Engine:
    def __init__(self):
        self.cuadrples = []
        self.operatorStack = []
        self.typeStack = []
        self.IDStack = []
        self.breakStack = []
        self.gotoStack = []

    def generate_cuad(self):
        cuad = Cuadruple(operation, left_side, right_side, result)
        self.cuadruples.append(cuad)

class Memory:
    def __init__(self):
        self.global_memory = {}
        self.local_memory = {}
        self.temporal_memory = {}
        self.constant_memory = {}
        self.addresses = [0, 1000, 10000, 20000]

    def generate_mem_address(self, ctx):
        if ctx == 'global':
            self.addresses[0] += 1
            return self.addresses[0]
        elif ctx == 'temporal':
            self.addresses[2] += 1
            return self.addresses[2]

    def allocate_function(self, ctx, function):
        if ctx == 'global':
            self.global_memory[function.header] = (function, self.generate_mem_address(ctx))
        else:
            self.temporal_memory[function.header] = function

    def allocate_class(self, cl):
        self.global_memory[cl.name] = (cl, self.generate_mem_address('global'))

global memory
memory = Memory()

class Function:
    def __init__(self, header, arguments, return_type):
        self.header = header
        self.return_type = return_type
        self.arguments = arguments
        self.argument_types = ArgumentDirectory()
        self.local_variables = VariableDirectory('local')

class Class:
    def __init__(self, name, attributes, methods):
        self.name = name
        self.attributes = VariableDirectory('local')
        self.methods = FunctionDirectory('temporal')

class Variable:
    def __init__(self, name, var_type, value):
        self.nombre = name
        self.var_type = var_type
        self.value = value

class FunctionDirectory:
    def __init__(self, context):
        self.context = context
        self.functions = {}

    def add_function(self, header, arguments, return_type):
        func = Function(header, arguments, return_type)
        memory.allocate_function(self.context, func)
        self.functions[header] = func

class ClassDirectory:
    def __init__(self):
        self.classes = {}
    def add_class(self, name, attributes, methods):
        cl = Class(name, attributes, methods)
        memory.allocate_class(cl)
        self.classes[name] = cl

class GlobalDirectory:
    def __init__(self):
        self.gobals = {}

class VariableDirectory:
    def __init__(self, ctx):
        self.ctx = ctx
        self.variables = {}

class ArgumentDirectory:
    def __init__(self):
        self.arguments = {}

class VirtualMachine:
    def __init__(self):
        self.function_directory = FunctionDirectory('global')
        self.class_directory = ClassDirectory()
        self.global_directory = GlobalDirectory()

vm = VirtualMachine()
print(vm)
print(vm.function_directory)
print(vm.class_directory)
print(vm.global_directory)

vm.function_directory.add_function('add', [1,2,3], None)
vm.function_directory.add_function('substract', [1,2,3], None)

vm.class_directory.add_class('Hola', ['some', 'attrs'], ['some', 'methods'])
print(vm.function_directory.functions)
print(memory.global_memory)
