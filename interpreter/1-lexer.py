from enum import Enum, auto


class Token:
    class Type(Enum):
        PLUS = auto()
        MINUS = auto()
        LPARAN = auto()
        RPARAN = auto()
        INTEGER = auto()

    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"`{self.value}`"


def lex(expression: str):
    tokens = []
    i = 0
    while i < len(expression):
        char = expression[i]

        if char == "+":
            token = Token(Token.Type.PLUS, "+")
        elif char == "-":
            token = Token(Token.Type.MINUS, "-")
        elif char == "(":
            token = Token(Token.Type.LPARAN, "(")
        elif char == ")":
            token = Token(Token.Type.RPARAN, ")")
        elif char.isdigit():
            digits = [char]
            for offset in expression[i + 1 : len(expression)]:
                if not offset.isdigit():
                    break
                digits.append(offset)
                i += 1
            integer = "".join(digits)
            token = Token(Token.Type.INTEGER, integer)
        else:
            raise NotImplementedError(f"Don't know how to handle {char}")
        i += 1

        tokens.append(token)
    return tokens


def calc(expression: str):
    tokens = lex(expression)
    return tokens


if __name__ == "__main__":
    expression = "(27+3)-(1+2)"
    print(calc(expression))
