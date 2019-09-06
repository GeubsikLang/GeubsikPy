from generators.StringBuilder import StringBuilder


class PrintBuilder(StringBuilder):

    def __init__(self):
        super().__init__()

    def format(self, k):
        self.print(
            "print" + '(' + k + ')'
        )

        return self.__str__()


class InputBuilder(StringBuilder):

    def __init__(self):
        super().__init__()

    def format(self, v):
        self.print(
            v + '=' + 'input()\n'
                      f'{v} = {v} or "니얼굴"'
        )

        return self.__str__()


class WhileBuilder(StringBuilder):

    def __init__(self):
        super().__init__()

    def format(self, k):
        self.print(
            "while" + '(' + k + ')' + ':'
        )

        return self.__str__()
