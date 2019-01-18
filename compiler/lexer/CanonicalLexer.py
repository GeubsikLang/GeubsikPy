import itertools

from compiler.codegen import FnCodegen
from compiler.parser.Keyword import *


class PythonGenerator(object):

    def gen(self, loader: iter):
        iterables = loader.iterable_tokens()
        for line, token in enumerate(iterables):
            token_type = token[0]

            if not token:
                continue

            elif token_type == FNDECL:
                fncode = tuple(itertools.takewhile(lambda x: x[0] != FNEND, tuple(loader.iterable_tokens())[line:]))
                for i in range(len(tuple(fncode))):
                    next(iterables)
                yield (tuple(fncode))
                continue

            yield (token)

