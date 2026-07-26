from lexer import Lexer
from parser import Parser
from interpreter import Interpreter
import sys
def run_itl_file(path):
    with open(path, 'r') as f:
        code = f.read()
    if 'itl-lang("start");' not in code:
        print('Error: ITL file must start with itl-lang("start");')
        return
    if 'itl-lang("end");' not in code and 'itl-lang("when-end");' not in code:
        print('Error: must end with itl-lang("end");')
        return
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    statements = parser.parse()
    Interpreter().run(statements)
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("ITL Numbered v1.3.0 - BlueBixt - Tools: xxx{} is a Tool - loop{} number{} else{}")
    else:
        run_itl_file(sys.argv[1])
