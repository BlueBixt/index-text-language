class Interpreter:
    def __init__(self):
        self.vars = {}
        self.funcs = {}
    def eval_expr(self, expr):
        out = ""
        for k, v in expr:
            if k == 'STRING': out += v
            elif k == 'INT': out += v
            else: out += self.vars.get(v, "")
        return out
    def run_block(self, block):
        for stmt in block:
            if stmt['type'] == 'print_expr':
                print(self.eval_expr(stmt['expr']))
            elif stmt['type'] == 'loop':
                for _ in range(stmt['count']):
                    self.run_block(stmt['block'])
            elif stmt['type'] == 'if':
                if self.vars.get(stmt['var'], "") == stmt['value']:
                    self.run_block(stmt['block'])
                else:
                    if stmt.get('else_block'):
                        self.run_block(stmt['else_block'])
            elif stmt['type'] == 'call':
                self.do_call(stmt)
    def do_call(self, stmt):
        f = self.funcs.get(stmt['name'])
        if not f: return
        # save old vars
        old = dict(self.vars)
        for i, param in enumerate(f['params']):
            if i < len(stmt['args']):
                arg_name = stmt['args'][i]
                self.vars[param] = self.vars.get(arg_name, arg_name)
        self.run_block(f['block'])
        # restore but keep changes to existing? simple restore not
        # keep global vars but params local
        for p in f['params']:
            if p in old:
                self.vars[p] = old[p]
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
            elif t == 'func':
                self.funcs[stmt['name']] = stmt
            elif t == 'call':
                self.do_call(stmt)
