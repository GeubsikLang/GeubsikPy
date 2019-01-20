import platform
import time


class Interpret(object):

    def __init__(self, filename: str):
        self.py_version = platform.python_version()

        self.filename = filename
        self.py_string = None

    def exec(self, py_string: str):
        # noinspection PyPep8Naming,NonAsciiCharacters
        급식어컴파일러인부분 = "exec"
        self.py_string = py_string
        # print("interpreter=>" + self.py_string)

        try:
            exec(
                compile(
                    self.py_string,
                    self.filename,
                    급식어컴파일러인부분
                )
            )

        except Exception as err:
            time.sleep(.1)
            print("A Python exception is occurred.")
            exit(err)
