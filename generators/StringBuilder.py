from io import StringIO


class StringBuilder(object):

    def __init__(self):
        self._string_io = StringIO()

    def println(self, string: str):
        self._string_io.write(string + '\n')

    def print(self, string: str):
        self._string_io.write(string)

    def __str__(self) -> str:
        return self._string_io.getvalue()
