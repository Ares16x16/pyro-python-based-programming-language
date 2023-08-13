from pyroProgram import *

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
