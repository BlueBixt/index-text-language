class Interpreter:
    def __init__(self):
        self.vars = {}
    def eval_expr(self, expr):
        out = ""
        for k, v in expr:
            if k == 'STRING':
                out += v
            elif k == 'INT':
                out += v
            else:
                out += self.vars.get(v, "")
        return out
    def run_block(self, block):
        for stmt in block:
            if stmt['type'] == 'print_expr':
                print(self.eval_expr(stmt['expr']))
    def run(self, statements):
        for stmt in statements:
            t = stmt['type']
            if t == 'var':
                self.vars[stmt['name']] = stmt['value']
            elif t == 'print_expr':
                print(self.eval_expr(stmt['expr']))
            elif t == 'input':
                self.vars[stmt['name']] = input()
            elif t == 'if':
                if self.vars.get(stmt['var'], "") == stmt['value']:
                    self.run_block(stmt['block'])
                else:
                    if stmt.get('else_block'):
                        self.run_block(stmt['else_block'])
            elif t == 'loop':
                for _ in range(stmt['count']):
                    self.run_block(stmt['block'])
