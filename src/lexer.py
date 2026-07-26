import re
TOKEN_SPEC = [
    ('ITL_LANG', r'itl-lang'),
    ('IF', r'if'),
    ('ELSE', r'else'),
    ('LOOP', r'loop'),
    ('PRINT', r'print'),
    ('VAR', r'var'),
    ('INPUT', r'input'),
    ('STATEMENT', r'statement'),
    ('WHEN_ME', r'when-me'),
    ('NUMBER', r'number'),
    ('COUNT', r'count'),
    ('STRING', r'"[^"]*"'),
    ('INT', r'\d+'),
    ('EQEQ', r'=='),
    ('EQUALS', r'='),
    ('PLUS', r'\+'),
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('LBRACE', r'\{'),
    ('RBRACE', r'\}'),
    ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_\-]*'),
    ('SEMICOLON', r';'),
    ('COMMA', r','),
    ('SKIP', r'[ \t\n]+'),
]
class Lexer:
    def __init__(self, code):
        self.code = code
    def tokenize(self):
        tokens = []
        tok_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_SPEC)
        for mo in re.finditer(tok_regex, self.code):
            kind = mo.lastgroup
            value = mo.group()
            if kind == 'SKIP': continue
            tokens.append((kind, value))
        return tokens
