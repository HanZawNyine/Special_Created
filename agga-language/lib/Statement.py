class IfNode:
    def __init__(self, cases, else_case):
        self.cases = cases
        self.else_case = else_case

        self.pos_start = self.cases[0][0].pos_start
        self.pos_end = (self.else_case or self.cases[len(self.cases) - 1][0]).pos_end


class ForNode:
    def __init__(self, var_name_tok, start_value_node, end_value_node, step_value_node, body_node):
        self.var_name_tok = var_name_tok
        self.start_value_node = start_value_node
        self.end_value_node = end_value_node
        self.step_value_node = step_value_node
        self.body_node = body_node

        self.pos_start = self.var_name_tok.pos_start
        self.pos_end = self.body_node.pos_end


class WhileNode:
    def __init__(self, condition_node, body_node):
        self.condition_node = condition_node
        self.body_node = body_node

        self.pos_start = self.condition_node.pos_start
        self.pos_end = self.body_node.pos_end
