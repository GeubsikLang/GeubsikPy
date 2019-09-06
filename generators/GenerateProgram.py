from compiler.codegen.BuiltinsCodegen import PrintBuilder, WhileBuilder, InputBuilder
from compiler.codegen.ConditionCodegen import ConditionalCodeBuilder
from compiler.codegen.FunctionCodegen import FunctionBuilder
from compiler.parser.Keywords import *
from generators.StringBuilder import StringBuilder
from generators.context.Context import add_variable
from generators.context.ValueContext import ValueLoader


class ProgramStringBuilder(object):

    def __init__(self):
        self.conditional_builder: ConditionalCodeBuilder = ConditionalCodeBuilder()
        self.program_string = StringBuilder()
        self.indent: int = 0
        self.load_value = ValueLoader()

    def build(self, items: list):
        # Analyze if token is multidimensional
        if isinstance(items[0], tuple):
            for item in items:
                _type = item[0]
                if _type == FNDECL:
                    self.println(FunctionBuilder().format(item[1]))
                elif _type == WHILE:
                    self.println(WhileBuilder().format(item[1]))
                elif _type == IF:
                    self.println(self.conditional_builder.format(item))
                elif _type == ELSEIF:
                    self.indent -= 1
                    self.println(self.conditional_builder.format(item))
                elif _type == ELSE:
                    self.indent -= 1
                    self.println('else:')
                else:
                    self._build(item)
                    continue

                self.indent += 1

        else:
            self._build(items)

    def _build(self, item):
        do = self.println
        token_t = item[0]
        if token_t in (FNEND, WHILEEND, IFEND):
            self.indent -= 1
            if self.indent < 0:
                raise IndentationError("너 왜 똑같은거 한번 더쓰냐?")

        elif token_t == PRINT:
            do(PrintBuilder().format(self.load_value.build_context(item[1])))
        elif token_t == INPUT:
            do(InputBuilder().format(item[1]))
        elif token_t == ASSIGN:
            add_variable(item[1], item[2])
            do(f"{item[1]} = {self.load_value.build_context(item[2])}")
        elif token_t == FNCALL:
            do(f"{item[1]}({self.load_value.build_context(item[2])})")

    def __str__(self) -> str:
        return self.program_string.__str__()

    def println(self, s):
        self.program_string.println(
            ' ' * self.indent + s
        )

    def to_string(self) -> str:
        return self.__str__()
