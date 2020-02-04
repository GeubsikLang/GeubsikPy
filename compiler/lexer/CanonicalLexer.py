import itertools

from compiler.parser.Keywords import *


class PythonGenerator(object):

    @staticmethod
    def _formatter(loader, iterables):
        for line, token in enumerate(iterables):
            token_type = token[0]

            if not token:
                continue

            elif token_type == FNDECL:
                lv = tuple(itertools.takewhile(lambda t: t[0] != FNEND, tuple(loader.iterable_tokens())[line:]))
                for i in range(len(lv) - 1):
                    next(iterables)
                yield lv
                continue

            elif token_type == WHILE:
                lv = tuple(itertools.takewhile(lambda t: t[0] != WHILEEND, tuple(loader.iterable_tokens())[line:]))
                for i in range(len(lv) - 1):
                    next(iterables)
                yield lv
                continue

            elif token_type == IF:
                lv = tuple(itertools.takewhile(lambda t: t[0] != IFEND, tuple(loader.iterable_tokens())[line:]))
                for i in range(len(lv) - 1):
                    next(iterables)
                yield lv
                continue

            yield token

    @staticmethod
    def gen(loader: iter):
        yield from PythonGenerator._formatter(loader, loader.iterable_tokens()) \
            or tuple()
