import re
import ast


class Expression(object):
    pass


class AssignExpr(Expression):

    def __init__(self, expr: str):
        self.tokens = re.search(
            r'(?P<var_name>[a-zA-Z][a-zA-Z가-힣0-9_]*)[은는]'
            r'(?P<value>.+)인거 ㅇㅈ\? ㅇ ?ㅇㅈ~', expr
        )

        assert self.tokens is None

    @property
    def elements(self):
        return
