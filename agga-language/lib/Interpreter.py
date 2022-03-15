from .Types import *
from .Error import *
from .Context import *

class RTResult:
    def __init__(self):
        self.value = None
        self.error = None

    def register(self, res):
        if res.error: self.error = res.error
        return res.value

    def success(self, value):
        self.value = value
        return self

    def failure(self, error):
        self.error = error
        return self


class Number:
    def __init__(self, value):
        self.value = value
        self.set_pos()
        self.set_context()

    def set_pos(self, pos_start=None, pos_end=None):
        self.pos_start = pos_start
        self.pos_end = pos_end
        return self

    def set_context(self,context=None):
        self.context = context
        return self

    def added_to(self, other):
        if isinstance(other, Number):
            return Number(self.value + other.value).set_context(self.context),None

    def subbed_by(self, other):
        if isinstance(other, Number):
            return Number(self.value - other.value).set_context(self.context),None

    def multed_by(self, other):
        if isinstance(other, Number):
            return Number(self.value * other.value).set_context(self.context),None

    def dived_by(self, other):
        if isinstance(other, Number):
            if other.value == 0:
                return None,RTError(
                    other.pos_start,other.pos_end,
                    'Division by zero',
                    self.context
                )
            return Number(self.value / other.value).set_context(self.context),None

    def powed_by(self,other):
        if isinstance(other,Number):
            return Number(self.value ** other.value).set_context(self.context),None

    def __repr__(self):
        return str(self.value)


class Interpreter:
    def visit(self, node,context):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name, self.no_visit_method)
        return method(node,context)

    def no_visit_method(self, node,context):
        raise Exception(f'No Visit_{type(node).__name__} method defined')

    def visit_NumberNode(self, node,context):
        return RTResult().success(
            Number(node.tok.value).set_context(context).set_pos(node.pos_start, node.pos_end)
        )

    def visit_BinOpNode(self, node,context):
        res = RTResult()
        left = res.register(self.visit(node.left_node,context))
        if res.error: return res
        right = res.register(self.visit(node.right_node,context))
        if res.error: return res

        # error,result = None,None
        if node.op_tok.type == TT_PLUS:
            result, error = left.added_to(right)
        elif node.op_tok.type == TT_MINUS:
            result, error = left.subbed_by(right)
        elif node.op_tok.type == TT_MUL:
            result, error = left.multed_by(right)
        elif node.op_tok.type == TT_DIV:
            result, error = left.dived_by(right)
        elif node.op_tok.type == TT_POW:
            result, error = left.powed_by(right)

        if error:
            return res.failure(error)
        else:
            return res.success(result.set_pos(node.pos_start, node.pos_end))

    def visit_UnaryOpNode(self, node,context):
        res = RTResult()
        number = res.register(self.visit(node.node,context))
        if res.error: return res

        error = None

        if node.op_tok.type == TT_MINUS:
            number,error = number.multed_by(Number(-1))

        if error:
            res.failure(error)
        else:
            return res.success(number.set_pos(node.pos_start, node.pos_end))



