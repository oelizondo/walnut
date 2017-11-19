from cuadruple import Cuadruple

class JumpEngine:
    def __init__(self, program_engine, operation_system):
        self.program_engine = program_engine
        self.operation_system = operation_system
        self.goto_stack = []

    def register_conditional(self):
        cuads = self.program_engine.cuadruples
        last_cuad = cuads[len(cuads) - 1]
        cuad = Cuadruple('GOTOF', self.operation_system.identifier_stack[-1], None, None)
        self.program_engine.send_cuad(cuad)
        self.program_engine.jump_stack.append(len(cuads) - 1)

    def register_goto(self):
        cuads = self.program_engine.cuadruples
        cuad = Cuadruple('GOTO', None, None, None)
        last_gotof = self.program_engine.jump_stack.pop()
        self.program_engine.send_cuad(cuad)
        self.program_engine.cuadruples[last_gotof].result = len(cuads) + 1
        self.goto_stack.append(len(cuads) - 1)

    def register_elseif(self):
        cuads = self.program_engine.cuadruples
        last_cuad = cuads[len(cuads) - 1]
        cuad = Cuadruple('GOTOF', self.operation_system.identifier_stack[-1], None, None)
        self.program_engine.send_cuad(cuad)
        self.program_engine.jump_stack.append(len(cuads) - 1)

    def fill_gotof(self):
        cuads = self.program_engine.cuadruples
        gotof = self.program_engine.jump_stack.pop()
        while_cuad = cuads[gotof]
        while_cuad.result = len(cuads) + 1;
        while_start = self.program_engine.jump_stack.pop()
        cuad = Cuadruple('GOTO', None, None, while_start)
        self.program_engine.send_cuad(cuad)

    def fill_gotos(self):
        cuads = self.program_engine.cuadruples
        while len(self.goto_stack):
            goto = self.goto_stack.pop()
            cuad = cuads[goto]
            cuad.result = len(cuads)+1
    def insert_jump(self):
        cuads = self.program_engine.cuadruples
        jump = len(cuads)
        self.program_engine.jump_stack.append(jump)
