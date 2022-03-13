from lib.Lexer import Lexer


def run(text):
    lexer = Lexer(text)
    tokens, errors = lexer.make_tokens()
    return tokens, errors.as_string()


if __name__ == '__main__':
    while True:
        text = input('basic >')
        tokens, errors = run(text)
        if errors:
            print(errors)
        else:
            print(tokens)
