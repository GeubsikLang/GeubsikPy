import platform
import traceback


class Interpret(object):

    def __init__(self, interpretable, filename: str):
        self.py_version = platform.python_version()

        self.filename = filename
        self.py_string = interpretable.code

        print(self.py_string)

    def _exec(self):
        try:
            exec(
                compile(
                    self.py_string,
                    self.filename, "exec"
                )
            )

        except Exception as err:
            traceback.print_exc()
            exit(err)
