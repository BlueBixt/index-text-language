class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else (None, None)

    def advance(self):
        t = self.tokens[self.pos]
        self.pos += 1
        return t

    def parse(self):
        statements = []
        while self.pos < len(self.tokens):
            kind, val = self.peek()

            if kind == 'VAR':
                self.advance() # var
                _, name = self.advance() # identifier
                self.advance() # =
                _, string_val = self.advance() # "text"
                statements.append({'type': 'var', 'name': name, 'value': string_val.strip('"')})
                # skip ;
                if self.pos < len(self.tokens) and self.tokens[self.pos][0] == 'SEMICOLON':
                    self.advance()

            elif kind == 'PRINT':
                self.advance()
                k2, v2 = self.advance()
                if k2 == 'STRING':
                    statements.append({'type': 'print_str', 'value': v2.strip('"')})
                else: # IDENTIFIER
                    statements.append({'type': 'print_var', 'name': v2})
                if self.pos < len(self.tokens) and self.tokens[self.pos][0] == 'SEMICOLON':
                    self.advance()

            elif kind == 'INPUT':
                self.advance()
                _, name = self.advance()
                statements.append({'type': 'input', 'name': name})
                if self.pos < len(self.tokens) and self.tokens[self.pos][0] == 'SEMICOLON':
                    self.advance()
            else:
                self.advance()
        return statements
