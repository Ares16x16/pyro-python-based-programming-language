# Lexer
class Token:
    def __init__(self, token_type, value):
        self.token_type = token_type
        self.value = value

def lex(code):
    tokens = []
    lines = code.strip().split('\n')
    print(lines)
    for line in lines:
        line = line.strip()
        if line.startswith('INT'):
            identifier = line[3:].strip().rstrip(':')
            tokens.append(Token('INT', identifier))
            line = identifier

        if line.startswith('INT'):
            identifier = line[3:].strip()
            tokens.append(Token('INT', identifier))
            line = identifier

        if '=' in line:
            identifier, value = line.split('=')
            tokens.append(Token('IDENTIFIER', identifier.strip()))
            tokens.append(Token('ASSIGN', '='))
            tokens.append(Token('INTEGER', int(value.strip(':'))))

        if line.startswith('PRINT'):
            identifier = line[5:].strip()
            tokens.append(Token('PRINT', identifier.strip(':')))
    
    # Debug        
    for o in tokens:
        print(o.token_type, o.value)
        
    return tokens

class Program:
    def __init__(self, statements):
        self.statements = statements
    
class AssignmentStatement:
    def __init__(self, identifier, value):
        self.identifier = identifier
        self.value = value

class PrintStatement:
    def __init__(self, identifier):
        self.identifier = identifier

# Parser
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0
    
    def parse(self):
        statements = self.parse_statements()
        return Program(statements)
    
    def parse_statements(self):
        statements = []
        while self.current_token_index < len(self.tokens):
            statement = self.parse_statement()
            statements.append(statement)
            self.current_token_index += 1

        return statements
    
    def parse_statement(self):
        token = self.current_token()
        #print(token.token_type)
        if token.token_type == 'IDENTIFIER':
            return self.parse_assignment_statement()
        
        if token.token_type == 'PRINT':
            return self.parse_print_statement()
    
    def parse_assignment_statement(self):
        identifier_token = self.current_token()
        self.next_token()
        self.expect_token('ASSIGN')
        value_token = self.current_token()
        #print(value_token.value)

        identifier = identifier_token.value
        value = value_token.value
        return AssignmentStatement(identifier, value)
    
    def parse_print_statement(self):
        identifier_token = self.current_token()
        self.next_token()
        
        identifier = identifier_token.value
        return PrintStatement(identifier)
    
    def current_token(self):
        return self.tokens[self.current_token_index]
    
    def next_token(self):
        self.current_token_index += 1
    
    def expect_token(self, token_type):
        token = self.current_token()
        
        if token.token_type != token_type:
            raise Exception(f'Expected token type {token_type}, got {token.token_type}')
        
        self.next_token()        
        
code = """
INT 6
6 = 5
6 = 5
PRINT 6
"""

tokens = lex(code)
parser = Parser(tokens)
program = parser.parse()

# Debug

for statement in program.statements:
    if isinstance(statement, AssignmentStatement):
        print(f'Assignment: {statement.identifier} = {statement.value}')
    if isinstance(statement, PrintStatement):
        print(f'Print: {statement.identifier}')
        
class Interpreter:
    def __init__(self, program):
        self.program = program
        self.variables = {}
    
    def interpret(self):
        for statement in self.program.statements:
            if isinstance(statement, AssignmentStatement):
                self.evaluate_assignment_statement(statement)
            elif isinstance(statement, PrintStatement):
                self.evaluate_print_statement(statement)
    
    def evaluate_assignment_statement(self, assignment_statement):
        identifier = assignment_statement.identifier
        value = assignment_statement.value
        self.variables[identifier] = value
    
    def evaluate_print_statement(self, print_statement):
        identifier = print_statement.identifier
        
        if identifier not in self.variables:
            raise Exception(f'Variable {identifier} is not defined')
        
        value = self.variables[identifier]
        print(value)


interpreter = Interpreter(program)
interpreter.interpret()