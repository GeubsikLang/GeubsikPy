import re

from generators.context.Context import get_variable


class ValueLoader(object):
    @staticmethod
    def build_context(expr: str):
        def _match(exp):
            return re.match(exp, expr)

        is_arg_access = _match(r"머머리의 *(?P<index>[0-9]+) *번 *머리털")
        is_arg_access_with_var = _match(r"머머리의 *(?P<index>.+) *번? *머리털")

        if is_arg_access:
            return "".join(("args", "[", is_arg_access.group("index"), "]"))
        if is_arg_access_with_var:
            return "".join(
                ("args", "[", get_variable(is_arg_access_with_var.group("index")), "]")
            )

        return expr
