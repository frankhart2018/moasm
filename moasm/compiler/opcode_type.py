from enum import Enum


class OpCodeType(Enum):
    SHOW = 0
    LOAD_CONST = 1
    ADD = 2
    SUB = 3
    MUL = 4
    DIV = 5
    MOD = 6