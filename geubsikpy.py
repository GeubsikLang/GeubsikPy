import argparse
import pathlib
import sys
import time

from compiler.lexer import CanonicalLexer
from core.dynamic.Exec import Interpret
from core.static.Loader import LoadFromFile
from generators.GenerateFile import FileGenerator
from generators.GenerateProgram import ProgramStringBuilder


def main(command: str, s: str) -> int:
    if not s.endswith(".기모띠"):
        print(
            "확장자는 기모띠여야지 바보야"
        )
        return 0

    start_time = time.time()
    program_loader = LoadFromFile(s)

    generator = CanonicalLexer.PythonGenerator()
    program_string = ProgramStringBuilder()

    for token in generator.gen(program_loader):
        # print(token)

        program_string.build(token)

    complete_time = time.time() - start_time

    if command == "run":
        Interpret(s).exec(program_string.to_string())

    elif command == "build":
        FileGenerator.gen(pathlib.Path(s).name.replace(".기모띠", "") + ".py", program_string.to_string())

    print("\n%.5f초만에 끝났다." % complete_time)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")

    parser_run = subparsers.add_parser("run")
    parser_run.add_argument("FILE", metavar="FILE", type=str)

    parser_build = subparsers.add_parser("build")
    parser_build.add_argument("FILE", metavar="FILE", type=str)

    args = parser.parse_args()

    if not hasattr(args, "FILE"):
        parser.print_help()
        sys.exit(0)

    sys.exit(main(command=args.command, s=args.FILE))
