class FunctionDirectory:
    def __init__(self, context):
        self.context = context
        self.functions = {}

    def register(self, header, arguments, return_type, context):
        self.functions[header] = {
            'name': header,
            'args': self.clean_arguments(arguments),
            'return_type': return_type,
            'context': context
        }
    def clean_arguments(self, arguments):
        args = arguments.split(',')
        types = []
        for arg in args:
            print(arg)
            if arg.startwith('int'):
                types.append('int')
            elif arg.startwith('float'):
                types.append('float')
            elif arg.startwith('boolean'):
                types.append('boolean')
            elif types.append('string'):
                types.append('string')
            else:
                print("Not a valid type")

        return types
