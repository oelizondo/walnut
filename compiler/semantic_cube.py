# Semantic cube
# This module its in charge to validate if a operation is valid or not.
# It recieves three keys which will go to a dictionary of tuples and recieves
# a response if true or a None if false.
# keys goes as follows: (left_side,rigth_side,operator)
#
# attributes
#
# semantic_cube: this is the attribute that will be loaded with the permitted operations
# converter: this attribute is a filled dictionary with the conversion of strings to the corresponding int value.
# inverter: this attribute is a filled dictionary with the conversion of int to the corresponding int value.

# Cheatsheet
# void = -1
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

    # Name: generate_cube
    # This function is the logical part to fill the semantic cube with
    # the corresponding tuples -> values of valid operations
    # starting with logic operations, then to assing operations, and mathematic operations
    # finishing with string concatenations
    #
    def generate_cube(self):
        sem = {}
        for counter in range(0,4):
            # logic operations are done here. from 10 to 17
            for i in range(10,18):
                sem[(counter,counter,i)] = 2
                if counter == 0:
                    sem[(1,counter,i)] = 2
                elif counter == 1:
                    sem[(0,counter,i)] = 2
        # assing operations are done here, only float and int can assing to each.
            sem[(counter,counter,23)] = counter
        sem[(0,1,23)] = 1
        sem[(1,0,23)] = 0

        # mathematic operations with numbers are done here, only int and floats are in.
        for counter in range(0,2):
            sem[(counter,counter,18)] = 1
            for i in range(19,23):
                sem[(counter,counter,i)] = counter
            if(counter == 0):
                aux = 1
            else:
                aux = 0
            for i in range(18,23):
                sem[(aux,counter,i)] = 1
        # string concatenation
        sem[(3,3,21)] = 3
        #negation
        sem[(2,None,24)] = 2
        return sem

    # Name: generate_operator_converter
    # This function is in charge to create a dictionary with string keys that
    # change to its corresponding int value.
    #
    def generate_operator_converter(self):
        return {'void':-1,'int':0,'float':1,'boolean':2,'string':3,'==':10, 'is': 10, '!=': 11,'not': 11,'and':12,'&&':12,'or':13,'||':13,'<=': 14,'>=': 15,'<': 16,'>':17,'/':18,'^':19,'*':20,'+':21,'-':22,'=':23,'!':24}

    # Name: generate_invert_converter
    # This function is in charge to create a dictionary with int keys that
    # change to its corresponding string value.
    #
    def generate_invert_converter(self):
        return {v: k for k, v in self.converter.iteritems()}
