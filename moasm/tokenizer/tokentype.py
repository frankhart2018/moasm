from enum import Enum


class TokenType(Enum):
    SHOW = 1
    STRING = 2
    NUMBER = 3
    NEWLINE = 4
    END = 5
    ADD = 6
    SUB = 7
    MUL = 8
    DIV = 9
    MOD = 10