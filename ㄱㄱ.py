import argparse

from core.static.Loader import LoadFromFile


def main():
    args = args_parser.parse_args()
    args.FILE = "tests/앙.기모띠"

    if args.FILE:
        LoadFromFile(args.FILE).ast


if __name__ == '__main__':
    args_parser = argparse.ArgumentParser(
        description=str()
    )
    # args_parser.add_argument("FILE", metavar="FILE", type=str, help="Program read from source file")

    main()
