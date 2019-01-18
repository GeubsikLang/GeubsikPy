import argparse

from core.static.Loader import LoadFromFile


def main():
    args = args_parser.parse_args()
    args.FILE = "tests/앙.기모띠"

    if args.FILE:
        program_loader = LoadFromFile(args.FILE)

        for token in program_loader.iterable_tokens():
            print(token)


if __name__ == '__main__':
    args_parser = argparse.ArgumentParser(
        description=str()
    )
    # args_parser.add_argument("FILE", metavar="FILE", type=str, help="Program read from source file")

    main()
