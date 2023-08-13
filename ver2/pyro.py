import sys

from pyroInterpreter import *
from pyroLexer import *
from pyroParser import *
from pyroProgram import *

if len(sys.argv) < 2:
    print("\nError: Wrong format.\n    Format: python pyro.py [your_file_name].pyro")
    sys.exit(1)

filename = sys.argv[1]
with open(filename, 'r') as file:
    code = file.read()
    
tokens = lex(code)
parser = Parser(tokens)
program = parser.parse()

interpreter = Interpreter(program)
interpreter.interpret()