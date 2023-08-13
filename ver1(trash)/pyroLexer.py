import re

# Token types
INT = "INT"
ID = "ID"
ASSIGN = "ASSIGN"
SEMICOLON = "SEMICOLON"
PLUS = "PLUS"
MULTIPLY = "MULTIPLY"
PRINT = "PRINT"
LPAREN = "LPAREN"
RPAREN = "RPAREN"

# regex patterns
patterns = [
    (INT, r"INT"),
    (ID, r"[a-zA-Z_][a-zA-Z0-9_]*"),
    (ASSIGN, r"="),
    (SEMICOLON, r":"),
    (PLUS, r"\+"),
    (MULTIPLY, r"\*"),
    (PRINT, r"PRINT"),
    (LPAREN, r"\("),
    (RPAREN, r"\)"),
]

regex_pattern = '|'.join(f'(?P<{token_type}>{pattern})' for token_type, pattern in patterns)

def lex(code):
    tokens = []
    for match in re.finditer(regex_pattern, code):
        token_type = match.lastgroup
        token_value = match.group()
        tokens.append((token_type, token_value.strip())) 

    return tokens