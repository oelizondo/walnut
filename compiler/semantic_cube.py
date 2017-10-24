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
        self.semantic_cube = self.generate_cube()
        self.converter = self.generate_operator_converter()
        self.inverter = self.generate_invert_converter()

    def generate_cube(self):
        sem = {}
        for counter in range(0,4):
            # logic operations
            for i in range(10,18):
                sem[(counter,counter,i)] = 2
        # assing operations
            sem[(counter,counter,23)] = counter
        sem[(1,0,23)] = 1

        # mathematic operations with numbers
        for counter in range(0,2):
            sem[(counter,counter,18)] = 1
            for i in range(19,23):
                sem[(counter,counter,i)] = counter
            if(counter == 0):
                aux = 1
            else:
                aux = 0
            for i in range(18,23):
                sem[(counter,aux,i)] = 1
        # string concatenation
        sem[(3,3,21)] = 3
        #negation
        sem[(2,None,24)] = 2
        return sem

    def generate_operator_converter(self):
        return {'int':0,'float':1,'boolean':2,'string':3,'==':10,'!': 11,'not': 11,'and':12,'&&':12,'or':13,'||':13,'<=': 14,'>=': 15,'<': 16,'>':17,'/':18,'^':19,'*':20,'+':21,'-':22,'=':23,'!':24}

    def generate_invert_converter(self):
        return {v: k for k, v in self.converter.iteritems()}
