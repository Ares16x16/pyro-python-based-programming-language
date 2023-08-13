class Token:
    def __init__(self, token_type, value):
        self.token_type = token_type
        self.value = value

def lex(code):
    tokens = []
    lines = code.strip().split('\n')
    
    #print(lines)
    
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
    #for o in tokens:
    #    print(o.token_type, o.value)
        
    return tokens