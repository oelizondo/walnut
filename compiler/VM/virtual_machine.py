from decimal import Decimal
import sys

class Cuadruple:
    def __init__(self, operation, left_side, right_side, result):
        self.operation = operation
        self.left_side = left_side
        self.right_side = right_side
        self.result = result


class VirtualMachine:
    def __init__(self, file):
        self.file = file
        self.cuadruples = []
        self.cuadruple_pointer = 0
        self.context_stack = []
        self.current_context = {}
        self.new_context = {}
        self.global_context = {}
        self.function_stack = []
        self.pointer_stack = []
        self.objects = {}
        self.file_size = 0

    def start(self):
        with open('walnut.obj', 'rb') as f:
            for line in f:
                line = line[:-1]
                args = line.split(',')
                cuad = Cuadruple(args[0], args[1], args[2], args[3])
                self.cuadruples.append(cuad)
                self.file_size += 1

        self.start_program()

    def clean_argument(self, arg):
        arg = arg[1:]
        if self.is_int(arg):
            return int(arg)
        elif self.is_float(arg):
            return float(arg)
        elif arg == 'true':
            return True
        elif arg == 'false':
            return False
        else:
            return arg


    def is_int(self, num):
        try:
            int(num)
            return True
        except ValueError:
            return False

    def is_float(self, num):
        try:
            float(num)
            return True
        except ValueError:
            return False

    def get_id_context(self,value):
        if(value[0] == '('):
            value = value[1:-1]

        if(self.is_int(value) and int(value) >= 100000):
            return self.global_context
        else:
            return self.current_context

    def get_division(self,left,right):
        if(self.is_int(left) and self.is_int(right)):
            return left // right
        else:
            return Decimal(left) / Decimal(right)
    def parse_side(self,value):
        if(value[0] == "%"):
            return self.clean_argument(value)
        elif value[0] == '(':
            value = value[1:-1]
            context = self.get_id_context(value)
            vm_direction = context[value]
            return context[vm_direction]
        else:
            context = self.get_id_context(value)
            _id = context.get(value, None)
            if _id == None:
                print("Operation with unassigned identifier. " + str(self.cuadruple_pointer))
                sys.exit()
            else:
                return _id

    def parse_result(self,value):
        context = self.get_id_context(value)
        if value[0] == '(':
            value = value[1:-1]
            return context[value]
        else:
            return value

    def start_program(self):
        while self.cuadruple_pointer < self.file_size:
            next_process = self.cuadruples[self.cuadruple_pointer]
            if next_process.operation == '10':
                right = self.parse_side(next_process.right_side)
                left = self.parse_side(next_process.left_side)
                res = left == right
                context = self.get_id_context(next_process.result)
                context[next_process.result] = res
            elif next_process.operation == '11':
                right = self.parse_side(next_process.right_side)
                left = self.parse_side(next_process.left_side)
                res = left != right
                context = self.get_id_context(next_process.result)
                context[next_process.result] = res
            elif next_process.operation == '12':
                right = self.parse_side(next_process.right_side)
                left = self.parse_side(next_process.left_side)
                res = left and right
                context = self.get_id_context(next_process.result)
                context[next_process.result] = res
            elif next_process.operation == '13':
                right = self.parse_side(next_process.right_side)
                left = self.parse_side(next_process.left_side)
                res = left or right
                context = self.get_id_context(next_process.result)
                context[next_process.result] = res
            elif next_process.operation == '14':
                right = self.parse_side(next_process.right_side)
                left = self.parse_side(next_process.left_side)
                res = left <= right
                context = self.get_id_context(next_process.result)
                context[next_process.result] = res
            elif next_process.operation == '15':
                right = self.parse_side(next_process.right_side)
                left = self.parse_side(next_process.left_side)
                res = left >= right
                context = self.get_id_context(next_process.result)
                context[next_process.result] = res
            elif next_process.operation == '16':
                right = self.parse_side(next_process.right_side)
                left = self.parse_side(next_process.left_side)
                res = left < right
                context = self.get_id_context(next_process.result)
                context[next_process.result] = res
            elif next_process.operation == '17':
                right = self.parse_side(next_process.right_side)
                left = self.parse_side(next_process.left_side)
                res = left > right
                context = self.get_id_context(next_process.result)
                context[next_process.result] = res
            elif next_process.operation == '18':
                right = self.parse_side(next_process.right_side)
                left = self.parse_side(next_process.left_side)
                res = self.get_division(left,right)
                context = self.get_id_context(next_process.result)
                context[next_process.result] = res
            elif next_process.operation == '19':
                right = self.parse_side(next_process.right_side)
                left = self.parse_side(next_process.left_side)
                res = left ** right
                context = self.get_id_context(next_process.result)
                context[next_process.result] = res
            elif next_process.operation == '20':
                right = self.parse_side(next_process.right_side)
                left = self.parse_side(next_process.left_side)
                res = left * right
                context = self.get_id_context(next_process.result)
                context[next_process.result] = res
            elif next_process.operation == '21':
                right = self.parse_side(next_process.right_side)
                left = self.parse_side(next_process.left_side)
                res = left + right
                context = self.get_id_context(next_process.result)
                context[next_process.result] = res
            elif next_process.operation == '22':
                right = self.parse_side(next_process.right_side)
                left = self.parse_side(next_process.left_side)
                res = left - right
                context = self.get_id_context(next_process.result)
                context[next_process.result] = res
            elif next_process.operation == '23':
                left = self.parse_side(next_process.left_side)
                context = self.get_id_context(next_process.result)
                result = self.parse_result(next_process.result)
                context[result] = left
            # elif next_process.operation == 24:
            elif next_process.operation == 'ver':
                number_to_check = self.parse_side(next_process.left_side)
                lower_limit = self.parse_side(next_process.right_side)
                upper_limit = self.parse_side(next_process.result)

                if(number_to_check < lower_limit or number_to_check > upper_limit):
                    print("Access to the dimensioned variable is out of bounds,")
                    print("The number: " + str(number_to_check) + " expected to be between: "+str(lower_limit)+" and "+str(upper_limit))
                    sys.exit()
            elif next_process.operation == 'GOTO':
                self.cuadruple_pointer = int(next_process.result) - 1
            elif next_process.operation == 'GOTOF':
                left = self.parse_side(next_process.left_side)
                if not left:
                    self.cuadruple_pointer = int(next_process.result) - 1
            elif next_process.operation == 'return':
                prev_context = self.context_stack[-1]
                prev_context[self.function_stack[-1]] = self.parse_side(next_process.result)
            elif next_process.operation == 'era':
                object_name = next_process.left_side
                self.context_stack.append(self.current_context)
                self.function_stack.append(next_process.result)
                if object_name != 'None':
                    _object = self.objects.get(object_name, None)
                    if _object == None:
                        self.objects[object_name] = {}
                        _object = self.objects[object_name]
                    self.new_context = _object
                else:
                    self.new_context = {}

                # self.context_stack.append([function_name, self.cuadruple_pointer, ])
            elif next_process.operation == 'param':
                self.new_context[next_process.result] = self.parse_side(next_process.left_side)
            elif next_process.operation == 'endproc':
                prev_context = self.context_stack.pop()
                func = self.function_stack.pop()
                if(prev_context.get(func,None) == None):
                    prev_context[func] = -1
                self.current_context = prev_context
                self.cuadruple_pointer = self.pointer_stack.pop()
            elif next_process.operation == 'gosub':
                self.current_context = self.new_context
                self.pointer_stack.append(self.cuadruple_pointer)
                self.cuadruple_pointer = int(next_process.result) - 1
            elif next_process.operation == 'puts':
                print(self.parse_side(next_process.result))
            else:
                print("Program finished successfully")

            self.cuadruple_pointer += 1


if __name__ == '__main__':
    vm = VirtualMachine('walnut.obj')
    vm.start()
