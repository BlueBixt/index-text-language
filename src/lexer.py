import re
TOKEN_SPEC = [
    ('ITL_LANG', r'itl-lang'),
    ('PRINT', r'print'),
    ('STRING', r'"[^"]*"'),
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('SEMICOLON', r';'),
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
