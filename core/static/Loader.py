import pathlib

from compiler.lexer.Tokenizer import Lexer
from compiler.parser.Parser import parse


class LoadFromFile(object):

    def __init__(self, program: str):
        self.program_object = pathlib.Path(program)

        if not self.program_object.exists():
            raise FileNotFoundError(
                f"{self.program_object.name} <= 솔직히 이 파일 없는거 ㅇㅈ하자"
            )

        self.lexer = Lexer(self.program_object.read_text(encoding="UTF-8"))

        for line, script in enumerate(self.lexer.analyze()):
            print(parse(script, self.lexer.lines[line]))
            line += 1  # For human

    @property
    def ast(self) -> str:
        return ""
