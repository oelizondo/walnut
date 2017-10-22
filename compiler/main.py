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
    program = open(sys.argv[1])
    with program as fp:
        line = fp.readline()
        instruction_pointer = 1
        while line:
            if(line.strip() != '{' & line.strip() != '}' & line.strip() != '\n')
                print("Line {}: {}".format(instruction_pointer, line.strip()))
                line = fp.readline()
                instruction_pointer += 1
