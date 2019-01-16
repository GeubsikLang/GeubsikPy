from compiler.parser.Expr import *
from compiler.parser.Keyword import *


def parse(token_arr: tuple or list, origin: str) -> list or tuple:
    if type(token_arr) not in (tuple, list):
        raise TypeError()

    elif token_arr[0] == PRINT:
        return PrintExpr(origin).elements

    elif token_arr[-5] == ASSIGN:
        return AssignExpr(origin).elements
