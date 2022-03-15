from lib.Lexer import *
from lib.Parser import *
from lib.Interpreter import *
from lib.Context import *
from lib.SymbolTable import *

global_Symbol_table = SymbolTable()
global_Symbol_table.set("NULL",Number(0))
global_Symbol_table.set("TRUE",Number(1))
global_Symbol_table.set("FALSE",Number(0))

def run(fn, text):
    lexer = Lexer(fn, text)
    tokens, errors = lexer.make_tokens()
    if errors: return None, errors

    # AST Abstract syntax tree
    praser = Parser(tokens)
    ast = praser.parse()

    if ast.error: return None, ast.error
    # print(ast.node)

    # interpreter
    interpreter = Interpreter()

    context = Context('<program>')
    context.symbol_table = global_Symbol_table
    result = interpreter.visit(ast.node,context)
    return result.value, result.error


if __name__ == "__main__":
    while True:
        text = input("Agga> ")
        tokens, errors = run("<stdin>", text)
        if errors:
            print(errors.as_string())
        else:
            print(tokens)
