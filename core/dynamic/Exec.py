import platform


class Interpret(object):

    def __init__(self, filename: str):
        self.py_version = platform.python_version()

        self.filename = filename
        self.py_string = None

    def exec(self, py_string: str):
        self.py_string = py_string
        """try:
            exec(
                compile(
                    self.py_string,
                    self.filename, "exec"
                )
            )

        except Exception as err:
            print("err")
            traceback.print_exc()
            exit(err)"""
        print("interpreter=>" + self.py_string)
        exec(self.py_string, globals())
