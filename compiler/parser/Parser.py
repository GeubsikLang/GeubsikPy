from compiler.parser.Expr import PrintExpr, AssignExpr, FnDeclExpr, FnCallExpr
from compiler.parser.Keyword import PRINT, ASSIGN, FNDECL, FNEND, FNCALL


def parse(token_arr: tuple or list, origin: str) -> list or tuple:
    if not token_arr:
        return str()

    elif token_arr[0] == PRINT:
        return PrintExpr(origin).elements

    elif token_arr[-5] == ASSIGN:
        return AssignExpr(origin).elements

    elif token_arr[0] == FNDECL:
        return FnDeclExpr(origin).elements

    elif token_arr[0] == FNEND:
        return FNEND,

    elif token_arr[0] == FNCALL:
        return FnCallExpr(origin, token_arr.copy()).elements

    else:
        return None
