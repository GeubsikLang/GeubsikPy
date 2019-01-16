import pathlib

from compiler.lexer.Tokenizer import Lexer


class LoadFromFile(object):

    def __init__(self, program: str):
        self.program_object = pathlib.Path(program)

        if not self.program_object.exists():
            raise FileNotFoundError(
                f"{self.program_object.name} <= 솔직히 이 파일 없는거 ㅇㅈ하자"
            )

        self.lexer = Lexer(self.program_object.read_text(encoding="UTF-8"))

        for line in self.lexer.analyze():
            print(line)

    @property
    def bytecode(self) -> bytes:
        return b''
