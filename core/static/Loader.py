import pathlib

from compiler.lexer.Tokenizer import Lexer
from compiler.parser.Parser import parse
from core.Except import syntax_error


class LoadFromFile(object):

    def __init__(self, program: str):
        self.program_object = pathlib.Path(program)

        if not self.program_object.exists():
            raise FileNotFoundError(
                f"{self.program_object.name} <= 솔직히 이 파일 없는거 ㅇㅈ하자"
            )

        self.lexer = Lexer(self.program_object.read_text(encoding="UTF-8"))
        # self.tokens = list()

    def iterable_tokens(self):
        for self.line, script in enumerate(self.lexer.analyze()):
            tokens = parse(
                script,
                self.lexer.lines[self.line]
            )

            if tokens == str():
                continue

            # self.line += 1  # For human

            # print(script, tokens)

            if tokens is None:
                syntax_error(agent=self)

            yield tokens
