from pyroLexer import *

class ASTNode:
    pass

class Program(ASTNode):
    def __init__(self, statements):
        self.statements = statements

class DeclarationStatement(ASTNode):
    def __init__(self, identifier):
        self.identifier = identifier

class AssignmentStatement(ASTNode):
    def __init__(self, identifier, value):
        self.identifier = identifier
        self.value = value

class IntLiteral(ASTNode):
    def __init__(self, value):
        self.value = value

class BinaryOperation(ASTNode):
    def __init__(self, operator, left_operand, right_operand):
        self.operator = operator
        self.left_operand = left_operand
        self.right_operand = right_operand

class PrintStatement(ASTNode):
    def __init__(self, identifier):
        self.identifier = identifier

class IntVariable:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"INT {self.name}"

def parse_assignment(tokens):
    identifier = tokens.pop(0)[1]
    if tokens[0][0] != ASSIGN:
        raise SyntaxError(f"Invalid assignment, expected assignment operator '{ASSIGN}' but found {tokens[0][1]}")
    tokens.pop(0)
    expression = parse_expression(tokens)
    return AssignmentStatement(identifier, expression)


def parse_expression(tokens):
    current_token = tokens.pop(0)

    if current_token[0] == INT:
        return IntVariable(current_token[1])
    elif current_token[0] == ID:
        return current_token[1]
    elif current_token[0] == LPAREN:
        expr = parse_expression(tokens)
        op = tokens.pop(0)[1]
        right = parse_expression(tokens)
        if tokens.pop(0)[0] != RPAREN:
            raise SyntaxError("Missing closing parenthesis ')'")
        return BinaryOperation(op, expr, right)
    else:
        raise SyntaxError(f"Invalid expression: {current_token[1]}")


def parse_print(tokens):
    identifier = tokens.pop(0)[1]
    return PrintStatement(identifier)

def parse_statement(tokens):
    current_token = tokens[0]

    if current_token[0] == ID:
        return parse_expression(tokens)
    elif current_token[0] == PRINT:
        return parse_print(tokens)
    else:
        return parse_expression(tokens)
        #raise SyntaxError(f"Invalid statement: {current_token[1]}")

def parse_program(tokens):
    statements = []

    while tokens:
        current_token = tokens.pop(0)

        if current_token[0] == SEMICOLON:
            continue

        statement = parse_statement([current_token] + tokens)
        statements.append(statement)

        if len(tokens) > 1 and tokens[1][0] != SEMICOLON:
            print(tokens)
            raise SyntaxError(f"Missing semicolon at the end of the line")

    return Program(statements)