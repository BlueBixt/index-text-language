class Interpreter:
    def __init__(self):
        self.vars = {}

    def run(self, statements):
        for stmt in statements:
            t = stmt['type']
            if t == 'var':
                self.vars[stmt['name']] = stmt['value']
            elif t == 'print_str':
                print(stmt['value'])
            elif t == 'print_var':
                print(self.vars.get(stmt['name'], f"[undef {stmt['name']}]"))
            elif t == 'input':
                self.vars[stmt['name']] = input()
