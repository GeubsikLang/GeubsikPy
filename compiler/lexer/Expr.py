import re

from compiler.parser.keyword import *


class Expression(object):

    def __init__(self):
        self.tokens: re.search = None
        self.expr: str = None

    def elements(self):
        if not self.tokens:
            raise SyntaxError(
                self.expr +
                f"{self.fmt_err}↑ 이거 솔직히 답없다 ㅇㅈ?"
            )

    @property
    def fmt_err(self) -> str:
        return "\n\t\t\t\t"


class AssignExpr(Expression):

    def __init__(self, expr: str):
        super().__init__()
        self.expr = expr
        self.tokens = re.search(
            r'(?P<var_name>[a-zA-Z가-힣][a-zA-Z가-힣0-9_]*)[은는]'
            r'(?P<value>.+)인거 ㅇㅈ\? ㅇ ?ㅇㅈ~', self.expr
        )

    @property
    def elements(self) -> tuple:
        super().elements()
        return (
            ASSIGN,
            self.tokens.group("var_name"),
            self.tokens.group("value")
        )


class PrintExpr(Expression):

    def __init__(self, expr: str):
        super().__init__()
        self.expr = expr
        self.tokens = re.search(
            r'앙 +(?P<context>.+)[띠띵띸]~?ㅋ?',
            expr
        )

    @property
    def elements(self) -> tuple:
        super().elements()
        return (
            PRINT,
            self.tokens.group("context")
        )
