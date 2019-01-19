import argparse
import time

from compiler.lexer import CanonicalLexer
from core.dynamic.Exec import Interpret
from core.static.Loader import LoadFromFile
from generators.GenerateProgram import ProgramStringBuilder


def main():
    args = args_parser.parse_args()
    args.FILE = "tests/앙.기모띠"

    if args.FILE:
        start_time = time.time()
        program_loader = LoadFromFile(args.FILE)

        generator = CanonicalLexer.PythonGenerator()

        for token in generator.gen(program_loader):
            print(token)

            program_string = ProgramStringBuilder()
            program_string.build(token)

            Interpret(program_string.to_string(), args.FILE)

        complete_time = time.time() - start_time

        print("Compile finished in %fs" % complete_time)


if __name__ == '__main__':
    args_parser = argparse.ArgumentParser(
        description=str()
    )
    # args_parser.add_argument("FILE", metavar="FILE", type=str, help="Program read from source file")

    main()
