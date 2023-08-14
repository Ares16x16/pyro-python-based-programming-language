from pyroProgram import *
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