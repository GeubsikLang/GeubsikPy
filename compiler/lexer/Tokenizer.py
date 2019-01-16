from compiler.lexer import Expr
from extlib.soynlp import RegexTokenizer


class Lexer(object):

    def __init__(self, lines: str):
        self.lines: list = lines.splitlines()
        self.korean_lexer = RegexTokenizer()

    def analyze(self):
        for line in self.lines:
            yield self.korean_lexer(line)
