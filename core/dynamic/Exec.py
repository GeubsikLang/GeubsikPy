import os
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

        try:
            exec(
                compile(
                    self.py_string,
                    "급식급식",
                    급식어컴파일러인부분
                )
            )

        except Exception as err:
            time.sleep(.1)
            print("런타임 에러는 너굴맨이 처리했으니 안심하라구!")

            with open(self.filename + '.log', 'w', encoding="utf8") as el:
                el.write(str(err))

            os.system(self.filename + '.log')
