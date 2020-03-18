from extlib.soynlp import RegexTokenizer as KoreanTokenizer


class Lexer(object):
    def __init__(self, lines: str):
        self.lines: list = lines.splitlines()
        self.korean_lexer = KoreanTokenizer()

    def analyze(self):
        for line in self.lines:
            yield self.korean_lexer(line)
