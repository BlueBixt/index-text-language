class Interpreter:
    def run(self, statements):
        for stmt in statements:
            if stmt in ("start", "end"):
                continue
            print(stmt)
