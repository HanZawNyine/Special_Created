from lib.Lexer import *


def run(fn,text):
    lexer = Lexer(fn,text)
    tokens, errors = lexer.make_tokens()
    return tokens, errors


if __name__ == "__main__":
    while True:
        text = input("Agga> ")
        tokens, errors = run("<stdin>",text)
        if errors:
            print(errors.as_string())
        else:
            print(tokens)
