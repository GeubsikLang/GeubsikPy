import pathlib


class FileGenerator(object):

    @staticmethod
    def gen(filename: str, content: str):
        print("야 \"{}\"\n\n\"넣을게\"\n".format(filename))

        if pathlib.Path(filename).exists():
            print("그치만... 이미 가득 차버렸는걸...\n")
        else:
            print("응...\n")

        with open(filename, 'w', encoding="utf8") as f:
            f.write(content)
