from typing import List

from ..compiler.opcode import OpCode
from ..compiler.opcode_type import OpCodeType


class VM:
    def __init__(self, opcodes: List[OpCode]) -> None:
        self.__opcodes = opcodes
        self.__const_stack = []

    def run(self) -> None:
        for opcode in self.__opcodes:
            if opcode.opcode_type == OpCodeType.LOAD_CONST:
                self.__const_stack.append(opcode.opcode_value)
            elif opcode.opcode_type == OpCodeType.SHOW:
                val_to_print = ""
                while self.__const_stack:
                    val_to_print += str(self.__const_stack.pop(0)) + " "

                print(val_to_print)