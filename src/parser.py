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
            kind, _ = self.peek()
            if kind == 'VAR':
                self.advance()
                if self.peek()[0]!= 'IDENTIFIER':
                    continue
                _, name = self.advance()
                if self.peek()[0] in ('EQUALS','STATEMENT'): self.advance()
                # skip LBRACE RBRACE if statement{} used as =
                if self.peek()[0]=='LBRACE':
                    self.advance()
                    if self.peek()[0]=='RBRACE': self.advance()
                _, sval = self.advance() # STRING or INT
                val = sval.strip('"') if sval.startswith('"') else sval
                statements.append({'type': 'var', 'name': name, 'value': val})
                while self.pos < len(self.tokens) and self.peek()[0] not in ('SEMICOLON',):
                    if self.peek()[0] == 'VAR': break
                    self.advance()
                if self.pos < len(self.tokens) and self.peek()[0] == 'SEMICOLON': self.advance()
                if self.pos < len(self.tokens) and self.peek()[0] == 'VAR': self.advance()
            elif kind == 'PRINT':
                self.advance()
                if self.peek()[0]=='LBRACE': # print{} tool
                    self.advance()
                    if self.peek()[0]=='RBRACE': self.advance()
                k2, v2 = self.advance()
                expr = []
                if k2 in ('STRING','IDENTIFIER','INT'):
                    expr.append((k2, v2.strip('"') if k2=='STRING' else v2))
                    while self.pos < len(self.tokens) and self.peek()[0] == 'PLUS':
                        self.advance()
                        k3, v3 = self.advance()
                        expr.append((k3, v3.strip('"') if k3=='STRING' else v3))
                    statements.append({'type': 'print_expr', 'expr': expr})
                if self.pos < len(self.tokens) and self.peek()[0] == 'SEMICOLON': self.advance()
            elif kind == 'INPUT':
                self.advance()
                if self.peek()[0]=='LBRACE':
                    self.advance()
                    if self.peek()[0]=='RBRACE': self.advance()
                var_name = "input_var"
                for i in range(self.pos, min(self.pos+10, len(self.tokens))):
                    if self.tokens[i][0] == 'IDENTIFIER':
                        var_name = self.tokens[i][1]
                        break
                statements.append({'type': 'input', 'name': var_name})
                while self.pos < len(self.tokens) and self.peek()[0]!= 'SEMICOLON':
                    self.advance()
                if self.pos < len(self.tokens) and self.peek()[0] == 'SEMICOLON': self.advance()
            elif kind == 'LOOP':
                self.advance()
                if self.peek()[0]=='LBRACE':
                    self.advance()
                    if self.peek()[0]=='RBRACE': self.advance()
                # loop{} 3 or loop{} count{}
                count_val = 3
                if self.pos < len(self.tokens) and self.peek()[0]=='INT':
                    count_val = int(self.advance()[1])
                elif self.pos < len(self.tokens) and self.peek()[0]=='IDENTIFIER':
                    # count{} tool -> use 5 as default or var
                    self.advance()
                    count_val = 3
                while self.pos < len(self.tokens) and self.peek()[0]!= 'LBRACE':
                    self.advance()
                if self.pos < len(self.tokens) and self.peek()[0] == 'LBRACE': self.advance()
                block = []
                while self.pos < len(self.tokens) and self.peek()[0]!= 'RBRACE':
                    if self.peek()[0] == 'PRINT':
                        self.advance()
                        if self.peek()[0]=='LBRACE':
                            self.advance()
                            if self.peek()[0]=='RBRACE': self.advance()
                        k2, v2 = self.advance()
                        expr = []
                        if k2 in ('STRING','IDENTIFIER','INT'):
                            expr.append((k2, v2.strip('"') if k2=='STRING' else v2))
                            while self.pos < len(self.tokens) and self.peek()[0] == 'PLUS':
                                self.advance()
                                k3, v3 = self.advance()
                                expr.append((k3, v3.strip('"') if k3=='STRING' else v3))
                            block.append({'type': 'print_expr', 'expr': expr})
                        if self.pos < len(self.tokens) and self.peek()[0] == 'SEMICOLON': self.advance()
                    else:
                        self.advance()
                if self.pos < len(self.tokens) and self.peek()[0] == 'RBRACE': self.advance()
                statements.append({'type': 'loop', 'count': count_val, 'block': block})
            elif kind == 'IF':
                self.advance()
                if self.pos >= len(self.tokens): break
                _, var_name = self.advance()
                while self.pos < len(self.tokens) and self.peek()[0] not in ('STRING','EQEQ','STATEMENT'):
                    self.advance()
                if self.peek()[0] in ('EQEQ','STATEMENT'): self.advance()
                if self.peek()[0]=='LBRACE':
                    self.advance()
                    if self.peek()[0]=='RBRACE': self.advance()
                if self.pos >= len(self.tokens): break
                _, comp_val = self.advance()
                while self.pos < len(self.tokens) and self.peek()[0]!= 'LBRACE':
                    self.advance()
                if self.pos < len(self.tokens) and self.peek()[0] == 'LBRACE': self.advance()
                block = []
                else_block = []
                in_else = False
                while self.pos < len(self.tokens) and self.peek()[0]!= 'RBRACE':
                    if self.peek()[0] == 'PRINT':
                        self.advance()
                        if self.peek()[0]=='LBRACE':
                            self.advance()
                            if self.peek()[0]=='RBRACE': self.advance()
                        k2, v2 = self.advance()
                        expr = []
                        if k2 in ('STRING','IDENTIFIER','INT'):
                            expr.append((k2, v2.strip('"') if k2=='STRING' else v2))
                            while self.pos < len(self.tokens) and self.peek()[0] == 'PLUS':
                                self.advance()
                                k3, v3 = self.advance()
                                expr.append((k3, v3.strip('"') if k3=='STRING' else v3))
                            if not in_else:
                                block.append({'type': 'print_expr', 'expr': expr})
                            else:
                                else_block.append({'type': 'print_expr', 'expr': expr})
                        if self.pos < len(self.tokens) and self.peek()[0] == 'SEMICOLON': self.advance()
                    elif self.peek()[0] in ('ELSE',):
                        self.advance()
                        if self.pos < len(self.tokens) and self.peek()[0]=='LBRACE':
                            self.advance()
                            if self.peek()[0]=='RBRACE': self.advance()
                        in_else = True
                    else:
                        self.advance()
                if self.pos < len(self.tokens) and self.peek()[0] == 'RBRACE': self.advance()
                statements.append({'type': 'if', 'var': var_name, 'value': comp_val.strip('"'), 'block': block, 'else_block': else_block})
            else:
                self.advance()
        return statements
