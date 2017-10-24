# int = 0
# float = 1
# boolean = 2
# string = 3
#
# logic operations
# == = 10
# not_equal = 11
# and = 12
# or = 13
# <= = 14
# >= = 15
# < = 16
# > = 17
#
# math operations
# / = 18
# -------
# ^ = 19
# * = 20
# + = 21
# - = 22
#
# unique
# = = 23
# ! = 24

class SemanticCube:
    def __init__(self):
        self.semantic_cube = {}
        self.converter = {'int': 0 , 'float' : 1, 'boolean': 2, 'string':3, '==':10, '!': 11, 'not': 11, 'and':12, '&&':12, 'or':13, '||':13, '<=': 14}
        self.converter.update({'>=': 15, '<': 16, '>':17, '/':18, '^':19, '*':20, '+':21, '-':22, '=':23, '!':24})
        for counter in range(0,4):
            # logic operations
            for i in range(10,18):
                self.semantic_cube[(counter,counter,i)] = 2
        # assing operations
            self.semantic_cube[(counter,counter,23)] = counter
        self.semantic_cube[(1,0,23)] = 1

        # mathematic operations with numbers
        for counter in range(0,2):
            self.semantic_cube[(counter,counter,18)] = 1
            for i in range(19,23):
                self.semantic_cube[(counter,counter,i)] = counter
            if(counter == 0):
                aux = 1
            else:
                aux = 0
            for i in range(18,23):
                self.semantic_cube[(counter,aux,i)] = 1

        # string concatenation
        self.semantic_cube[(3,3,21)] = 3

        #negation
        self.semantic_cube[(2,None,24)] = 2
