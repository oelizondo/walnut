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
