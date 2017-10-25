from cuadruple import Cuadruple

class JumpEngine:
    def __init__(self, program_engine):
        self.program_engine = program_engine
        self.goto_stack = []

    def register_conditional(self):
        cuads = self.program_engine.cuadruples
        last_cuad = cuads[len(cuads) - 1]
        cuad = Cuadruple('GOTOF', last_cuad.result, None, None)
        self.program_engine.send_cuad(cuad)
        self.program_engine.jump_stack.append(len(cuads) - 1)

    def register_goto(self):
        cuads = self.program_engine.cuadruples
        cuad = Cuadruple('GOTO', None, None, None)
        last_gotof = self.program_engine.jump_stack.pop()
        self.program_engine.cuadruples[last_gotof].result = len(cuads) + 1
        self.program_engine.send_cuad(cuad)
        self.goto_stack.append(len(cuads) - 1)

    def register_elseif(self):
        cuads = self.program_engine.cuadruples
        last_cuad = cuads[len(cuads) - 1]
        cuad = Cuadruple('GOTOF', last_cuad.result, None, None)
        self.program_engine.send_cuad(cuad)
        self.program_engine.jump_stack.append(len(cuads) - 1)

    def fill_gotof(self):
        cuads = self.program_engine.cuadruples
        last_cuad = cuads[len(cuads) - 1]
        gotof = self.program_engine.jump_stack.pop()
        last_cuad.result = gotof

    def fill_gotos(self):
        cuads = self.program_engine.cuadruples
        while len(self.goto_stack):
            goto = self.goto_stack.pop()
            cuad = cuads[goto]
            cuad.result = len(cuads)
