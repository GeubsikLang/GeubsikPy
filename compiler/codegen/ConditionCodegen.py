from compiler.parser.Keywords import IF, ELSEIF, ELSE
from generators.StringBuilder import StringBuilder

if_condition_tokens = {
    IF: 'if',
    ELSEIF: 'elif',
    ELSE: 'else'
}


class ConditionalCodeBuilder(StringBuilder):

    def __init__(self):
        super().__init__()

    def format(self, token: tuple):
        self.print(
            ' '.join((if_condition_tokens[token[0]], token[1], ':'))
        )

        return self.__str__()
