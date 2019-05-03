import argparse
import time

from compiler.lexer import CanonicalLexer
from core.dynamic.Exec import Interpret
from core.static.Loader import LoadFromFile
from generators.GenerateProgram import ProgramStringBuilder


def main():
    args = args_parser.parse_args()

    if args.FILE.endswith(".기모띠"):
        start_time = time.time()
        program_loader = LoadFromFile(args.FILE)

        generator = CanonicalLexer.PythonGenerator()
        program_string = ProgramStringBuilder()
        interpreter = Interpret(args.FILE)

        for token in generator.gen(program_loader):
            # print(token)

            program_string.build(token)

        complete_time = time.time() - start_time

        start_time = time.time()
        interpreter.exec(program_string.to_string())
        run_complete_time = time.time() - start_time

        # print("Compile finished in %fs execute time: %fs" % (complete_time, run_complete_time))

    else:
        print(
            "확장자는 기모띠여야지 바보야"
        )


if __name__ == '__main__':
    args_parser = argparse.ArgumentParser(
        description=str()
    )
    args_parser.add_argument("FILE", metavar="FILE", type=str)

    main()
