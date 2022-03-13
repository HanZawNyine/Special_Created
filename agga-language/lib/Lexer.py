from lib.Token import Token
from lib.Types import (
    DIGITS,
    TT_PLUS, TT_MINUS,
    TT_MUL, TT_DIV,
    TT_LPAREN, TT_RPAREN,
    TT_INT, TT_FLOAT)
from lib.Error import IllegalCharacterError


class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def make_tokens(self):
        tokens = []
        while self.current_char != None:
            if self.current_char in '\t':
                self.advance()
            elif self.current_char in DIGITS:
                tokens.append(Token((self.make_number())))
                self.advance()
            elif self.current_char == '+':
                tokens.append(Token(TT_PLUS))
                self.advance()
            elif self.current_char == "-":
                tokens.append(Token(TT_MINUS))
                self.advance()
            elif self.current_char == "*":
                tokens.append(Token(TT_MUL))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token(TT_DIV))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(TT_LPAREN))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(TT_RPAREN))
                self.advance()
            else:
                char = self.current_char
                self.advance()
                return [], IllegalCharacterError(char)
        return tokens, None

    def make_number(self):
        num_str = ''
        dot_count = 0

        while self.current_char != None and self.current_char in DIGITS + ".":
            if self.current_char == '.':
                if dot_count == 1:
                    break
                dot_count += 1
                num_str = '.'
            else:
                num_str += self.current_char

            if dot_count == 0:
                return Token(TT_INT, int(num_str))
            else:
                return Token(TT_FLOAT, float(num_str))
