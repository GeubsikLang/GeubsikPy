from compiler.parser.Expr import *
from compiler.parser.Keywords import *
from re import search


def parse(token_arr: tuple or list, origin: str) -> list or tuple:
    if not token_arr:
        return str()

    _type = token_arr[0]

    if not _type:
        return str()

    elif _type == PRINT:
        return PrintExpr(origin).elements

    # 와 어려웠다;;
    elif search(r'.+[은는].+인거', origin):
        return AssignExpr(origin).elements

    elif _type == FNDECL:
        return FnDeclExpr(origin).elements

    elif _type == FNEND:
        return FNEND,

    elif _type == FNCALL:
        return FnCallExpr(origin, token_arr.copy()).elements

    elif _type == WHILE:
        return WhileExpr(origin).elements

    elif _type == WHILEEND:
        return WHILEEND,

    else:
        return None
