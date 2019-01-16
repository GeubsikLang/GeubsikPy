import argparse

from core.static.Loader import LoadFromFile

if __name__ == '__main__':
    args_parser = argparse.ArgumentParser(
        description=str()
    )
    # args_parser.add_argument("FILE", metavar="FILE", type=str, help="Program read from source file")

    args = args_parser.parse_args()

    bytecode = LoadFromFile("tests/앙.기모띠").bytecode
