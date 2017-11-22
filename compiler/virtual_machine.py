# VirtualMachine module
# This module recieves the cuadruples created by the parsing of
# the walnut program which were stored in the walnut.obj file.
#
# It is responsable to run the cuadruples generated in the correct
# order, by following the flow directed by the information of the
# cuadruples.
#
# helper class:
# Cuadruple
#   This class is used to create cuadruples and fill the cuadruple container with the information
#   recieved from the walnut.obj file.
#
# VirtualMachine
# attributes
#
# file: the walnut.obj file
# cuadruples: cuadruples container
# cuadruple_pointer: pointer that states the cuadruple action to take place
# context_stack: stack of the dormant contexts
# current_context: helper, the current context memory dictionary
# new_context: helper, new context memory dictionary. This is used
#              while changing context to fill the parameters of the function
#              being called before sending the current context to the stack
# global_context: global memory directions dictionary
# function_stack: function name stack for return values, this is done to be able to
#                 return the expression value to the previous context inside the name
#                 of the function that was called.
# pointer_stack: this are filled when a new context is called, it stores its current value
#                and sets the new one to the starting point of the function that is called.
# objects: this dictionary is used for object management, when a method is called, the context that
#                is set is the one of the object
# file_size: the number of cuadruples listed in the walnut.obj
# input_value: helper attribute that has the input stream data when read cuadruple is activated.
#

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
        self.input_value = ''

    # Name: start
    # Function that fills the cuadruple stack from walnut.obj in order to access them.
    #
    def start(self):
        with open('walnut.obj', 'rb') as f:
            for line in f:
                line = line[:-1]
                args = line.split(',')
                cuad = Cuadruple(args[0], args[1], args[2], args[3])
                self.cuadruples.append(cuad)
                self.file_size += 1

        self.start_program()

    # Name: clean_argument
    # Helper method that returns the marks free primitive element (constant)
    #
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
            return arg[1:-1]

    # Name: is_int
    # Helper method that return if a value is an integer or not.
    #
    # parameter
    #
    # num: the value of the element going to be validated.
    #
    def is_int(self, num):
        try:
            int(num)
            return True
        except ValueError:
            return False

    # Name: is_float
    # Helper method that returns if a value is a float or not.
    #
    # parameter
    #
    # num: the value of the element going to be validated.
    #
    def is_float(self, num):
        try:
            float(num)
            return True
        except ValueError:
            return False

    # Name: get_id_context
    # Helper method that obtains the context which needs to be accessed in
    # order to obtain the correct value
    #
    # parameter
    #
    # value: the id that is going to be verified
    #
    def get_id_context(self,value):
        if(value[0] == '('):
            value = value[1:-1]
            vm_direction = self.current_context[value]
            if(int(vm_direction) >= 100000):
                return self.global_context
            else:
                return self.current_context
        if(self.is_int(value) and int(value) >= 100000):
            return self.global_context
        else:
            return self.current_context

    # Name: get_division
    # Helper method that gets the correct type of division.
    # Only when both values are int, a division will return an int.
    #
    # parameters
    #
    # left: the left side of the operation
    # right: the right side of the operation
    #
    def get_division(self,left,right):
        if(self.is_int(left) and self.is_int(right)):
            return left // right
        else:
            return Decimal(left) / Decimal(right)

    # Name: parse_side
    # Helper method that obtains the value of the memory direction
    # you are searching, from the correct context.
    #
    # parameter
    #
    # value: the value can be a constant, a memory location storage
    #        or a memory direction
    #
    # error_handle
    #
    # 1) returns if a memory access does not have a value inside.
    # 2) return if memory collection access does not have a value inside.
    #
    def parse_side(self,value):
        if(value[0] == "%"):
            return self.clean_argument(value)
        elif value[0] == '(':
            value = value[1:-1]
            vm_direction = self.current_context[value]

            if(vm_direction >= 100000):
                _id = self.global_context.get(vm_direction, None)
            else:
                _id = self.current_context.get(vm_direction, None)
            if _id == None:
                print("Operation with empty collection index. " + str(self.cuadruple_pointer))
                sys.exit()
            else:
                return _id
        else:
            context = self.get_id_context(value)
            _id = context.get(value, None)
            if _id == None:
                print("Operation with unassigned identifier. " + str(self.cuadruple_pointer))
                sys.exit()
            else:
                return _id

    # Name: parse_result
    # Helper method that obtains the value of the result
    # if a value is a memory direction storage, it returns what's inside.
    #
    # parameter
    #
    # value: the value can be a constant, a memory location storage
    #        or a memory direction
    #
    def parse_result(self,value):
        if value[0] == '(':
            value = value[1:-1]
            return self.current_context[value]
        else:
            return value

    # Name: input_validation
    # This function is called from the parse cuadruple command, it validates
    # that the input given matches with the type of the variable.
    #
    # parameter
    #
    # var_type: the type that the input is expected to be.
    #
    # error_handle
    #
    # 1) returns if an input does not match the expected type.
    #
    def input_validation(self, var_type):
        if var_type == 'int':
            if not self.is_int(self.input_value):
                print("Type error, recieved a diferent type value, expected int")
                sys.exit()
            else:
                return int(self.input_value)
        elif var_type == 'float':
            if not self.is_float(self.input_value):
                print("Type error, recieved a diferent type value, expected float")
                sys.exit()
            else:
                return float(self.input_value)
        elif var_type == 'boolean':
            if self.input_value.lower() != 'true' and self.input_value.lower() != 'false':
                print("Type error, recieved a diferent type value, expected boolean")
                sys.exit()
            elif self.input_value.lower() == "true":
                return True;
            else:
                return False;
        else:
            return self.input_value

    # Name: start_program
    # Program main function which runs the object code based on the
    # cuadruple that must be executed.
    #
    def start_program(self):
        while self.cuadruple_pointer < self.file_size:
            next_process = self.cuadruples[self.cuadruple_pointer]

            # '==' Equals comparison cuadruple command
            if next_process.operation == '10':
                right = self.parse_side(next_process.right_side)
                left = self.parse_side(next_process.left_side)
                res = left == right
                context = self.get_id_context(next_process.result)
                context[next_process.result] = res

            # '!=' Not equal comparison cuadruple command
            elif next_process.operation == '11':
                right = self.parse_side(next_process.right_side)
                left = self.parse_side(next_process.left_side)
                res = left != right
                context = self.get_id_context(next_process.result)
                context[next_process.result] = res

            # 'and|&&' AND comparison cuadruple command
            elif next_process.operation == '12':
                right = self.parse_side(next_process.right_side)
                left = self.parse_side(next_process.left_side)
                res = left and right
                context = self.get_id_context(next_process.result)
                context[next_process.result] = res

            # 'or | ||' OR comparison cuadruple command
            elif next_process.operation == '13':
                right = self.parse_side(next_process.right_side)
                left = self.parse_side(next_process.left_side)
                res = left or right
                context = self.get_id_context(next_process.result)
                context[next_process.result] = res
            # '<=' Less or equal comparison cuadruple command
            elif next_process.operation == '14':
                right = self.parse_side(next_process.right_side)
                left = self.parse_side(next_process.left_side)
                res = left <= right
                context = self.get_id_context(next_process.result)
                context[next_process.result] = res

            # '>=' Greater or equal comparison cuadruple command
            elif next_process.operation == '15':
                right = self.parse_side(next_process.right_side)
                left = self.parse_side(next_process.left_side)
                res = left >= right
                context = self.get_id_context(next_process.result)
                context[next_process.result] = res

            # '<' Less than comparison cuadruple command
            elif next_process.operation == '16':
                right = self.parse_side(next_process.right_side)
                left = self.parse_side(next_process.left_side)
                res = left < right
                context = self.get_id_context(next_process.result)
                context[next_process.result] = res

            # '>' Greater than comparison cuadruple command
            elif next_process.operation == '17':
                right = self.parse_side(next_process.right_side)
                left = self.parse_side(next_process.left_side)
                res = left > right
                context = self.get_id_context(next_process.result)
                context[next_process.result] = res

            # '/' Division operand cuadruple command
            elif next_process.operation == '18':
                right = self.parse_side(next_process.right_side)
                left = self.parse_side(next_process.left_side)
                res = self.get_division(left,right)
                context = self.get_id_context(next_process.result)
                context[next_process.result] = res

            # '^' Exponential operand cuadruple command
            elif next_process.operation == '19':
                right = self.parse_side(next_process.right_side)
                left = self.parse_side(next_process.left_side)
                res = left ** right
                context = self.get_id_context(next_process.result)
                context[next_process.result] = res

            # '*' Multiplication operand cuadruple command
            elif next_process.operation == '20':
                right = self.parse_side(next_process.right_side)
                left = self.parse_side(next_process.left_side)
                res = left * right
                context = self.get_id_context(next_process.result)
                context[next_process.result] = res

            # '+' Addition operand cuadruple command
            elif next_process.operation == '21':
                right = self.parse_side(next_process.right_side)
                left = self.parse_side(next_process.left_side)
                res = left + right
                context = self.get_id_context(next_process.result)
                context[next_process.result] = res

            # '-' Substraction operand cuadruple command
            elif next_process.operation == '22':
                right = self.parse_side(next_process.right_side)
                left = self.parse_side(next_process.left_side)
                res = left - right
                context = self.get_id_context(next_process.result)
                context[next_process.result] = res

            # '=' Assignment operand cuadruple command
            elif next_process.operation == '23':
                left = self.parse_side(next_process.left_side)
                result = self.parse_result(next_process.result)
                context = self.get_id_context(next_process.result)
                context[result] = left

            # 'ver' cuadruple command: Verifies that the expression
            # is between the intended range
            elif next_process.operation == 'ver':
                number_to_check = self.parse_side(next_process.left_side)
                lower_limit = self.parse_side(next_process.right_side)
                upper_limit = self.parse_side(next_process.result)

                if(number_to_check < lower_limit or number_to_check > upper_limit):
                    print("Access to the dimensioned variable is out of bounds,")
                    print("The number: " + str(number_to_check) + " expected to be between: "+str(lower_limit)+" and "+str(upper_limit))
                    sys.exit()

            # 'GOTO' cuadruple command: A jump in the cuadruple linear flow.
            elif next_process.operation == 'GOTO':
                self.cuadruple_pointer = int(next_process.result) - 1

            # 'GOTOF' cuadruple command: A jump that is activated only when an expression is false.
            elif next_process.operation == 'GOTOF':
                left = self.parse_side(next_process.left_side)
                if not left:
                    self.cuadruple_pointer = int(next_process.result) - 1

            # 'return' cuadruple command: It returns the expression given to the past context
            # inside the key (name) of the function that called it.
            elif next_process.operation == 'return':
                prev_context = self.context_stack[-1]
                prev_context[self.function_stack[-1]] = self.parse_side(next_process.result)

            # 'era' cuadruple command: Starts the context of the function that is being called.
            # If a function is a method from a class, the loaded context will come from the
            # object context rather than a new one.
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

            # 'param' cuadruple command: Sets the parameter value in the new context before
            # jumping to the new context.
            elif next_process.operation == 'param':
                self.new_context[next_process.result] = self.parse_side(next_process.left_side)

            # 'endproc' cuadruple command: States that the current context is about to terminate,
            # it liberates the current context and sets the previous one as the new current and
            # resets the cuadruple pointer to continue the past context flow.
            # if a function is a void, it sets a dummy as a return value.
            elif next_process.operation == 'endproc':
                prev_context = self.context_stack.pop()
                func = self.function_stack.pop()
                if(prev_context.get(func,None) == None):
                    prev_context[func] = -1
                self.current_context = prev_context
                self.cuadruple_pointer = self.pointer_stack.pop()

            # 'gosub' cuadruple command: States that the new context is now the current context.
            # it stacks the current cuadruple pointer and sets the new context one.
            elif next_process.operation == 'gosub':
                self.current_context = self.new_context
                self.pointer_stack.append(self.cuadruple_pointer)
                self.cuadruple_pointer = int(next_process.result) - 1

            # 'puts' cuadruple command: prints the result of an expression
            elif next_process.operation == 'puts':
                print(self.parse_side(next_process.result))

            # 'read' cuadruple command: runs the input command and stores the input
            # in the input_value attribute.
            elif next_process.operation == 'read':
                 self.input_value = str(input(self.parse_side(next_process.left_side)))

            # 'parse' cuadruple command: runs a validation to dictate if it is proper
            # to inject the input to the desired memory location.
            elif next_process.operation == 'parse':
                var_type = next_process.left_side
                value = self.input_validation(var_type)
                context = self.get_id_context(next_process.result)
                context[next_process.result] = value

            # This else states the end of the program
            else:
                sys.exit()

            self.cuadruple_pointer += 1


if __name__ == '__main__':
    vm = VirtualMachine('walnut.obj')
    vm.start()
