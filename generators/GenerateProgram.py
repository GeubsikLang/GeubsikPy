from compiler.codegen.BuiltinsCodegen import PrintBuilder, WhileBuilder
from compiler.codegen.FunctionCodegen import FunctionBuilder
from compiler.parser.Keywords import *
from generators.StringBuilder import StringBuilder


class ProgramStringBuilder(object):

    def __init__(self):
        self.program_string = StringBuilder()
        self.indent: int = 0

    def build(self, items: list):
        # Analyze if token is multidimensional
        if isinstance(items[0], tuple):
            for item in items:
                _type = item[0]
                if _type == FNDECL:
                    self.println(FunctionBuilder().format(item[1]))
                    self.indent += 1
                elif _type == WHILE:
                    self.println(WhileBuilder().format(item[1]))
                    self.indent += 1
                else:
                    self._build(item)

        else:
            _type = items[0]
            if (_type == FNEND
                    or _type == WHILEEND):
                self.indent -= 1
                if self.indent < 0:
                    raise IndentationError("너 왜 똑같은거 한번 더쓰냐?")
            else:
                self._build(items)

    def _build(self, item):
        do = self.println
        token_t = item[0]
        if type(token_t) != str:
            return

        elif token_t == PRINT:
            do(PrintBuilder().format(item[1]))
        elif token_t == ASSIGN:
            do(f"{item[1]} = {item[2]}")
        elif token_t == FNCALL:
            do(f"{item[1]}()")  # TODO: Recognize parameters

    def __str__(self) -> str:
        return self.program_string.__str__()

    def println(self, s):
        self.program_string.println(
            ' ' * self.indent + s
        )

    def to_string(self) -> str:
        return self.__str__()
