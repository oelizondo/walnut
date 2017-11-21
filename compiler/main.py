# Main module:
# This module is in charge to connect antlr4 parsed program
# with the code that is trying to compile to be able to create
# the object code.

import sys
from antlr4 import *
from walnutLexer import walnutLexer
from walnutParser import walnutParser

def main(argv):
    input = FileStream(argv[1])
    lexer = walnutLexer(input)
    stream = CommonTokenStream(lexer)
    parser = walnutParser(stream)
    tree = parser.program()
if __name__ == '__main__':
    main(sys.argv)
