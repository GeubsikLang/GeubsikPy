from generators.StringBuilder import StringBuilder


class PrintBuilder(StringBuilder):

    def __init__(self):
        super().__init__()

    def format(self, k):
        self.print(
            "print" + '(' + k + ')'
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
