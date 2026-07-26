class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
    def parse(self):
        statements = []
        for kind, value in self.tokens:
            if kind == 'STRING':
                statements.append(value.strip('"'))
        return statements
