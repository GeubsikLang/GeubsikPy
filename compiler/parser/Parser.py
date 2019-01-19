from compiler.parser.Expr import PrintExpr, AssignExpr, FnDeclExpr, FnCallExpr
from compiler.parser.Keywords import PRINT, ASSIGN, FNDECL, FNEND, FNCALL


def parse(token_arr: tuple or list, origin: str) -> list or tuple:
    if not token_arr:
        return str()

    _type = token_arr[0]

    if not _type:
        return str()

    elif _type == PRINT:
        return PrintExpr(origin).elements

    elif token_arr[-5] == ASSIGN:
        return AssignExpr(origin).elements

    elif _type == FNDECL:
        return FnDeclExpr(origin).elements

    elif _type == FNEND:
        return FNEND,

    elif _type == FNCALL:
        return FnCallExpr(origin, token_arr.copy()).elements

    else:
        return None
