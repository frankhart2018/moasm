from enum import Enum


class OpCodeType(Enum):
    SHOW = 0
    LOAD_CONST = 1
    ADD = 2
    SUB = 3
    MUL = 4
    DIV = 5
    MOD = 6
    LOAD_VAR = 7
    PUSH_VAR = 8
    LABEL = 9
    JZ = 10
    JMP = 11
    JN = 12
