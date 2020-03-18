import re
from re import search

import tossi

from compiler.parser.Keywords import (
    ASSIGN,
    PRINT,
    FNDECL,
    FNCALL,
    WHILE,
    IF,
    ELSEIF,
    INPUT,
    INPUT_INT,
)


class Expression(object):
    def __init__(self):
        self.tokens: re.search = None
        self.expr: str = ""

    def elements(self):
        if self.tokens:
            return True


class AssignExpr(Expression):
    def __init__(self, expr: str):
        super().__init__()
        self.expr = expr
        self.tokens = search(
            r"(?P<var_name>[a-zA-Z가-힣][a-zA-Z가-힣0-9_]*)[은는]"
            r"(?P<value>.+)인거 ㅇㅈ\?( *ㅇ ?ㅇㅈ~)?",
            self.expr,
        )

    @property
    def elements(self) -> tuple:
        if super().elements():
            return (ASSIGN, self.tokens.group("var_name"), self.tokens.group("value"))


class PrintExpr(Expression):
    def __init__(self, expr: str):
        super().__init__()
        self.expr = expr
        self.tokens = search(r"앙 +(?P<context>.+)[띠띵띸]~?ㅋ?", self.expr)

    @property
    def elements(self) -> tuple:
        if super().elements():
            return (PRINT, self.tokens.group("context"))


class InputExpr(Expression):
    def __init__(self, expr: str):
        super().__init__()
        self.expr = expr
        self.tokens = search(
            r"(?P<var>[a-zA-Z가-힣_][0-9a-zA-Z가-힣_]*) +이거 *ㄹㅇ ㅆㅅㅌㅊ *인거 +ㅇㅈ\? *(ㅇ[ ]ㅇㅈ[~]*)?",
            self.expr,
        )

    @property
    def elements(self) -> tuple:
        if super().elements():
            return (INPUT, self.tokens.group("var"))


class InputIntExpr(Expression):
    def __init__(self, expr: str):
        super().__init__()
        self.expr = expr
        self.tokens = search(
            r"(?P<var>[a-zA-Z가-힣_][0-9a-zA-Z가-힣_]*) +이거 *ㄹㅇ ㅆㅎㅌㅊ *인거 +ㅇㅈ\? *(ㅇ[ ]ㅇㄴㅇ[~]*)?",
            self.expr,
        )

    @property
    def elements(self) -> tuple:
        if super().elements():
            return (INPUT_INT, self.tokens.group("var"))


class FnDeclExpr(Expression):
    def __init__(self, expr):
        super().__init__()
        self.expr = expr
        self.tokens = search(
            r"이거 ㄹㅇ (?P<fn_name>[a-zA-Z가-힣_][0-9a-zA-Z가-힣_]*)인 *부분 *ㅋㅋ*", self.expr
        )

    @property
    def elements(self) -> tuple:
        if super().elements():
            return (FNDECL, self.tokens.group("fn_name"))


class FnCallExpr(Expression):
    def __init__(self, expr, k):
        super().__init__()
        self.expr = expr
        k[3] = re.sub(r"(?P<_>.+)고", r"\g<_>", k[3])
        if tossi.pick(k[3][-2], "고") == "이고":
            k[3] = re.sub(r"(?P<_>.+)이", r"\g<_>", k[3])
        self.tokens = search(
            r"오지고 *지리고 *렛잇고 +"
            r"(?P<fn_name>[a-zA-Z가-힣_][0-9a-zA-Z가-힣_]*){}(?P<args>.+)? *미쳐버린 *부분".format(
                tossi.pick(k[3], "고")
            ),
            self.expr,
        )

    @property
    def elements(self) -> tuple:
        if super().elements():
            return (FNCALL, self.tokens.group("fn_name"), self.tokens.group("args"))


class WhileExpr(Expression):
    def __init__(self, expr: str):
        super().__init__()
        self.expr = expr
        self.tokens = search(r"와 *방금 *개꿀잼 *시나리오 *생각해냄(?P<condition>.*)\?+", self.expr)

    @property
    def elements(self) -> tuple:
        if super().elements():
            c = self.tokens.group("condition")
            return (WHILE, c if c.strip() != "" else True.__str__())


class IfExpr(Expression):
    def __init__(self, expr):
        super().__init__()
        self.expr = expr
        self.tokens = search(r"(?P<condition>.+) *일 ?때 시청자들이", self.expr)

    @property
    def elements(self) -> tuple:
        if super().elements():
            return (IF, self.tokens.group("condition"))


class ElseifExpr(Expression):
    def __init__(self, expr):
        super().__init__()
        self.expr = expr
        self.tokens = search(r"(?P<condition>.+) *일 ?때 열혈팬", self.expr)

    @property
    def elements(self) -> tuple:
        if super().elements():
            return (ELSEIF, self.tokens.group("condition"))
