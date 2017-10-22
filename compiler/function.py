class Function:
    def __init__(self, header, arguments, return_type):
        self.header = header
        self.return_type = return_type
        self.arguments = arguments
        self.argument_types = ArgumentDirectory()
        self.local_variables = VariableDirectory('local')
