class StructuresEngine:
    def __init__(self, program_engine):
        self.program_engine = program_engine
        self.current_collection = None
        self.R = 1

    def set_current_collection(self, identifier):
        self.current_collection = self.program_engine.current_context.variable_directory.variables.get(identifier)

    def inject_cell(self, limit):
        self.current_collection['dimension'].append(self.generate_cell(int(limit)))
        self.update_r()

    def generate_cell(self, limit):
        return {
            'limit': limit - 1,
            'k': 0
        }

    def update_r(self):
        self.R = self.R * (self.current_collection['dimension'][-1]['limit'] + 1)


    def fill_k(self):
        if len(self.current_collection['dimension']) == 1:
            self.current_collection['dimension'][0]['k'] = 0
        else:
            self.current_collection['dimension'][0]['k'] = self.R / int(self.current_collection['dimension'][0]['limit'] + 1)
            self.current_collection['dimension'][-1]['k'] = 0

    def set_next_memory_avail(self):
        self.program_engine.memory_direction += self.R
        self.R = 1
