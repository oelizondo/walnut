# JumpEngine module:
# This module is in charge of managing the jumps of the
# conditional statements and cycle statements
#
# parameters
#
# program_engine: the core of the compiler, this to have access to the cuadruple stack and jump_stack
# operation_system: the core of all logical validations, this to have access to the identifier_stack
#
# attribute:
#
# goto_stack: stack that is used to fill all the pending goto cuadruples
#
from cuadruple import Cuadruple

class JumpEngine:
    def __init__(self, program_engine, operation_system):
        self.program_engine = program_engine
        self.operation_system = operation_system
        self.goto_stack = []

    # Name: register_conditional
    # This function is called from the parser to insert and if or elseif and while gotof
    # Operation already checked that the id belongs to a boolean type.
    # it inserts the pointer of the gotof so it can be later filled.
    #
    def register_conditional(self):
        cuads = self.program_engine.cuadruples
        cuad = Cuadruple('GOTOF', self.operation_system.identifier_stack.pop(), None, None)
        self.program_engine.send_cuad(cuad)
        self.program_engine.jump_stack.append(len(cuads) - 1)

    # Name: register_goto
    # This function is called from the parse to insert the pending goto of a
    # conditional or cycle statement and to fill the last pending gotof.
    # it inserts the pointer to the goto_stack to latter be filled.
    #
    def register_goto(self):
        cuads = self.program_engine.cuadruples
        cuad = Cuadruple('GOTO', None, None, None)
        last_gotof = self.program_engine.jump_stack.pop()
        self.program_engine.send_cuad(cuad)
        self.program_engine.cuadruples[last_gotof].result = len(cuads)
        self.goto_stack.append(len(cuads) - 1)

    # Name: fill_gotos
    # This function is in charge to fill all pending gotos in the
    # goto_stack, this is mainly used in conditional statements because
    # of the use of sequential elseifs that walnut language permits.
    #
    def fill_gotos(self):
        cuads = self.program_engine.cuadruples
        while len(self.goto_stack):
            goto = self.goto_stack.pop()
            cuad = cuads[goto]
            cuad.result = len(cuads)

    # Name: fill_gotof
    # This function is used in the cycle statements to fill the pending gotof
    # with the next number of cuadruples after the goto of the while statement.
    # this also creates a goto cuadruple that is filled with the jump insterted
    # in the insert_jump function.
    #
    def fill_gotof(self):
        cuads = self.program_engine.cuadruples
        gotof = self.program_engine.jump_stack.pop()
        while_cuad = cuads[gotof]
        while_cuad.result = len(cuads) + 1;
        while_start = self.program_engine.jump_stack.pop()
        cuad = Cuadruple('GOTO', None, None, while_start)
        self.program_engine.send_cuad(cuad)

    # Name: insert_jump
    # This function is used to know where does the cycle goto needs to return when
    # the cycle is completed.
    #
    def insert_jump(self):
        cuads = self.program_engine.cuadruples
        jump = len(cuads)
        self.program_engine.jump_stack.append(jump)
