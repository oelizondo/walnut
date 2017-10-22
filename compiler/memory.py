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
