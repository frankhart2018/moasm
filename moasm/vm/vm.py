from typing import List

from ..compiler.opcode import OpCode
from ..compiler.opcode_type import OpCodeType


class VM:
    def __init__(self, opcodes: List[OpCode]) -> None:
        self.__opcodes = opcodes
        self.__const_stack = []
        self.__memory = {}

    def run(self) -> None:
        for opcode in self.__opcodes:
            if opcode.opcode_type == OpCodeType.LOAD_CONST:
                self.__const_stack.append(opcode.opcode_value)
            elif opcode.opcode_type == OpCodeType.LOAD_VAR:
                identifier = opcode.opcode_value
                self.__memory[identifier] = self.__const_stack.pop()
            elif opcode.opcode_type == OpCodeType.PUSH_VAR:
                identifier = opcode.opcode_value
                self.__const_stack.append(self.__memory[identifier])
            elif opcode.opcode_type == OpCodeType.SHOW:
                print(self.__const_stack.pop())
            elif opcode.opcode_type in [OpCodeType.ADD, OpCodeType.SUB,
                                        OpCodeType.MUL, OpCodeType.DIV, OpCodeType.MOD]:
                op2 = int(self.__const_stack.pop())
                op1 = int(self.__const_stack.pop())

                if opcode.opcode_type == OpCodeType.ADD:
                    self.__const_stack.append(op1 + op2)
                elif opcode.opcode_type == OpCodeType.SUB:
                    self.__const_stack.append(op1 - op2)
                elif opcode.opcode_type == OpCodeType.MUL:
                    self.__const_stack.append(op1 * op2)
                elif opcode.opcode_type == OpCodeType.DIV:
                    self.__const_stack.append(op1 // op2)
                elif opcode.opcode_type == OpCodeType.MOD:
                    self.__const_stack.append(op1 % op2)