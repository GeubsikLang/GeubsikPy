import itertools

from compiler.parser.Keywords import *


class PythonGenerator(object):

    @staticmethod
    def gen(loader: iter):
        iterables = loader.iterable_tokens()
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

            yield token
