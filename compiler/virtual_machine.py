semantic_cube = [[[0,1,2,3]],[[0,1,2,3]],[[4,5,6,7]]]

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
