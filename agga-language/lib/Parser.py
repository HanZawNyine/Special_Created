from .Types import *
from .Error import *
from .Variable import *
from .Statement import *


class NumberNode:
    def __init__(self, tok):
        self.tok = tok

        self.pos_start = self.tok.pos_start
        self.pos_end = self.tok.pos_end

    def __repr__(self):
        return f'{self.tok}'


class BinOpNode:
    def __init__(self, left_node, op_tok, right_node):
        self.left_node = left_node
        self.op_tok = op_tok
        self.right_node = right_node

        self.pos_start = self.left_node.pos_start
        self.pos_end = self.right_node.pos_end

    def __repr__(self):
        return f'({self.left_node}, {self.op_tok}, {self.right_node})'


class UnaryOpNode:
    def __init__(self, op_tok, node):
        self.op_tok = op_tok
        self.node = node

        self.pos_start = self.op_tok.pos_start
        self.pos_end = node.pos_end

    def __repr__(self):
        return f'{self.op_tok}, {self.node}'


class ParserResult:
    def __init__(self):
        self.error = None
        self.node = None
        self.advanve_count = 0

    def register_advancement(self):
        self.advanve_count += 1

    def register(self, res):
        self.advanve_count += res.advanve_count
        if res.error: self.error = res.error
        return res.node

    def success(self, node):
        self.node = node
        return self

    def failure(self, error):
        if not self.error or self.advanve_count == 0:
            self.error = error
        self.error = error
        return self


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.tok_idx = -1
        self.advance()

    def advance(self, ):
        self.tok_idx += 1
        if self.tok_idx < len(self.tokens):
            self.current_tok = self.tokens[self.tok_idx]
        return self.current_tok

    def parse(self):
        res = self.expr()
        if not res.error and self.current_tok.type != TT_EOF:
            return res.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                "Expected '+', '-', '*' or '/'",
            ))
        return res

    def atom(self):
        res = ParserResult()
        tok = self.current_tok

        if tok.type in (TT_INT, TT_FLOAT):
            res.register_advancement()
            self.advance()
            return res.success(NumberNode(tok))
        elif tok.type == TT_IDENTIFIER:
            res.register_advancement()
            self.advance()
            return res.success(VarAccessNode(tok))
        elif tok.type == TT_LPAREN:
            res.register_advancement()
            self.advance()
            expr = res.register(self.expr())
            if res.error: return res
            if self.current_tok.type == TT_RPAREN:
                res.register_advancement()
                self.advance()
                return res.success(expr)
            else:
                return res.failure(InvalidSyntaxError(
                    self.current_tok.pos_start, self.current_tok.pos_end,
                    "Expected ')'"
                ))
        elif tok.matches(TT_KEYWORD, 'IF'):
            if_expr = res.register(self.if_expr())
            if res.error: return res
            return res.success(if_expr)
        return res.failure(InvalidSyntaxError(
            self.current_tok.pos_start, self.current_tok.pos_end,
            "Expected int, float, identifier,'+', '-', '*' or '/'",
        ))

    def if_expr(self):
        res= ParserResult()
        cases = []
        else_case = None

        if not self.current_tok.matches(TT_KEYWORD, 'IF'):
            return res.failure(InvalidSyntaxError(
                self.current_tok.pos_start,self.current_tok.pos_end,
                f"Expected 'IF'"
            ))

        res.register_advancement()
        self.advance()

        condition = res.register(self.expr())
        if res.error: return res

        if not self.current_tok.matches(TT_KEYWORD,'THEN'):
            return res.failure(InvalidSyntaxError(
                self.current_tok.pos_start,self.current_tok.pos_end,
                f"Expected 'THEN'"
            ))
        res.register_advancement()
        self.advance()

        expr = res.register(self.expr())
        if res.error:return res
        cases.append((condition,expr))

        while self.current_tok.matches(TT_KEYWORD,'ELIF'):
            res.register_advancement()
            self.advance()

            condition = res.register(self.expr())
            if res.error: return res

            if not self.current_tok.matches (TT_KEYWORD,'THEN'):
                return res.failure(InvalidSyntaxError(
                    self.current_tok.pos_start,self.current_tok.pos_end,
                    f"Expected Token 'THEN'"
                ))

            res.register_advancement()
            self.advance()

            expr = res.register(self.expr())
            if res.error: return res
            cases.append((condition,expr))

        if self.current_tok.matches(TT_KEYWORD,'ELSE'):
            res.register_advancement()
            self.advance()

            expr = res.register(self.expr())
            if res.error: return res
            else_case = expr
        return res.success(IfNode(cases,else_case))


    def power(self):
        return self.bin_op(self.atom, (TT_POW,), self.factor)

    def factor(self):
        res = ParserResult()
        tok = self.current_tok

        if tok.type in (TT_PLUS, TT_MINUS):
            res.register_advancement()
            self.advance()
            factor = res.register(self.factor())
            if res.error: return res
            return res.success(UnaryOpNode(tok, factor))

        return self.power()

    def term(self):
        return self.bin_op(self.factor, (TT_MUL, TT_DIV))

    def com_expr(self):
        res = ParserResult()

        if self.current_tok.matches(TT_KEYWORD, 'NOT'):
            op_tok = self.current_tok
            res.register_advancement()
            self.advance()

            node = res.register(self.com_expr())
            if res.error: return res
            return res.success(UnaryOpNode(op_tok, node))

        node = res.register(self.bin_op(self.arith_expr, (TT_EE, TT_NE, TT_LT, TT_GT, TT_LTE, TT_GTE)))
        if res.error: return res.failure(InvalidSyntaxError(
            self.current_tok.pos_start, self.current_tok.pos_end,
            "Expected int, float, identifier,'+', '-', '(' or 'NOT'",
        ))
        return res.success(node)

    def arith_expr(self):
        return self.bin_op(self.term, (TT_PLUS, TT_MINUS))

    def expr(self):
        res = ParserResult()
        if self.current_tok.matches(TT_KEYWORD, 'VAR'):
            res.register_advancement()
            self.advance()

            if self.current_tok.type != TT_IDENTIFIER:
                return res.failure(InvalidSyntaxError(
                    self.current_tok.pos_start, self.current_tok.pos_end,
                    "Expected identifier"
                ))
            var_name = self.current_tok
            res.register_advancement()
            self.advance()
            if self.current_tok.type != TT_EQ:
                return res.failure(InvalidSyntaxError(
                    self.current_tok.pos_start, self.current_tok.pos_end,
                    "Expected '='"
                ))
            res.register_advancement()
            self.advance()
            expr = res.register(self.expr())
            if res.error: return res
            return res.success(VarAssignNode(var_name, expr))

        node = res.register(self.bin_op(self.com_expr, ((TT_KEYWORD, "AND"), (TT_KEYWORD, "OR"))))
        if res.error:
            return res.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                "Expected 'VAR',int, float, identifier,'+', '-', '*' or '/'",
            ))
        return res.success(node)

    def bin_op(self, func_a, ops, func_b=None):
        if func_b == None:
            func_b = func_a
        res = ParserResult()
        left = res.register(func_a())
        if res.error:
            return res
        while self.current_tok.type in ops or (self.current_tok.type, self.current_tok.value) in ops:
            op_tok = self.current_tok
            res.register_advancement()
            self.advance()
            right = res.register(func_a())
            if res.error: return res
            left = BinOpNode(left, op_tok, right)
        return res.success(left)
