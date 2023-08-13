from pyroParser import *


def interpret(program):
    variables = {}
    
    for statement in program.statements:
        if isinstance(statement, DeclarationStatement):
            variables[statement.identifier] = None
        elif isinstance(statement, AssignmentStatement):
            value = evaluate_expression(statement.value, variables)
            variables[statement.identifier] = value
        elif isinstance(statement, PrintStatement):
            value = variables.get(statement.identifier)
            if value is not None:
                print(value)
            else:
                raise RuntimeError(f"Undefined variable: {statement.identifier}")

def evaluate_expression(expression, variables):
    if isinstance(expression, IntLiteral):
        return expression.value
    elif isinstance(expression, str):  # Identifier
        value = variables.get(expression)
        if value is not None:
            return value
        else:
            raise RuntimeError(f"Undefined variable: {expression}")
    elif isinstance(expression, BinaryOperation):
        left = evaluate_expression(expression.left_operand, variables)
        right = evaluate_expression(expression.right_operand, variables)
        op = expression.operator
        if op == PLUS:
            return left + right
        elif op == MULTIPLY:
            return left * right
    else:
        raise RuntimeError("Invalid expression")


if __name__ == '__main__':
    code = """
    INT x: 
    x = 5:
    PRINT x:
    """

    tokens = lex(code)
    print(tokens)
    program = parse_program(tokens)
    interpret(program)