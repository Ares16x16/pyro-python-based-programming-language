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