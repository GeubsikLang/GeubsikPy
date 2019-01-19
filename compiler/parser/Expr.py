import re
from re import search

import tossi

from compiler.parser.Keywords import ASSIGN, PRINT, FNDECL, FNCALL, WHILE


class Expression(object):

    def __init__(self):
        self.tokens: re.search = None
        self.expr: str = None

    def elements(self):
        if self.tokens:
            return True


class AssignExpr(Expression):

    def __init__(self, expr: str):
        super().__init__()
        self.expr = expr
        self.tokens = search(
            r'(?P<var_name>[a-zA-Z가-힣][a-zA-Z가-힣0-9_]*)[은는]'
            r'(?P<value>.+)인거 ㅇㅈ\?( *ㅇ ?ㅇㅈ~)?', self.expr
        )

    @property
    def elements(self) -> tuple:
        if super().elements():
            return (
                ASSIGN,
                self.tokens.group("var_name"),
                self.tokens.group("value")
            )


class PrintExpr(Expression):

    def __init__(self, expr: str):
        super().__init__()
        self.expr = expr
        self.tokens = search(
            r'앙 +(?P<context>.+)[띠띵띸]~?ㅋ?',
            self.expr
        )

    @property
    def elements(self) -> tuple:
        if super().elements():
            return (
                PRINT,
                self.tokens.group("context")
            )


class FnDeclExpr(Expression):

    def __init__(self, expr):
        super().__init__()
        self.expr = expr
        self.tokens = search(
            # TODO: Recognize parameters
            r'이거 ㄹㅇ (?P<fn_name>[a-zA-Z가-힣_][0-9a-zA-Z가-힣_]*)인 *부분 *ㅋㅋ*',
            self.expr
        )

    @property
    def elements(self) -> tuple:
        if super().elements():
            return (
                FNDECL,
                self.tokens.group("fn_name")
            )


class FnCallExpr(Expression):

    def __init__(self, expr, k):
        super().__init__()
        self.expr = expr
        k[3] = re.sub(r'(?P<_>.+)고', r'\g<_>', k[3])
        if tossi.pick(k[3][-2], '고') == '이고':
            k[3] = re.sub(r'(?P<_>.+)이', r'\g<_>', k[3])
        self.tokens = search(
            # TODO: Recognize parameters
            r'오지고 *지리고 *렛잇고 +'
            r'(?P<fn_name>[a-zA-Z가-힣_][0-9a-zA-Z가-힣_]*){} *미쳐버린 *부분'.format(
                tossi.pick(k[3], '고')
            ),
            self.expr
        )

    @property
    def elements(self) -> tuple:
        if super().elements():
            return (
                FNCALL,
                self.tokens.group("fn_name")
            )


class WhileExpr(Expression):

    def __init__(self, expr: str):
        super().__init__()
        self.expr = expr
        self.tokens = search(
            r'와 *방금 *개꿀잼 *시나리오 *생각해냄(?P<condition>.+)\?+',
            self.expr
        )

    @property
    def elements(self) -> tuple:
        if super().elements():
            return (
                WHILE,
                self.tokens.group("condition")
            )
