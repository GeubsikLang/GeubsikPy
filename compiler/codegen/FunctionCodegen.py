from generators.StringBuilder import StringBuilder


class FunctionBuilder(StringBuilder):

    def __init__(self):
        super().__init__()

    def format(self, k):
        self.print(
            "def " + k + "():"
        )

        return self.__str__()
