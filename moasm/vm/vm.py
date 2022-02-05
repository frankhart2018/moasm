import sys
from typing import List, Any

from ..compiler.opcode import OpCode
from ..compiler.opcode_type import OpCodeType


class VM:
    def __init__(self, opcodes: List[OpCode]) -> None:
        self.__opcodes = opcodes
        self.__const_stack = []
        self.__instruction_stack = []
        self.__memory = {}

    def __get_file_desc(self, file_name: str) -> Any:
        if file_name == "stdout":
            return sys.stdout
        return open(file_name, "w")

    def run(self, out_file) -> None:
        i = 0
        with self.__get_file_desc(file_name=out_file) as f:
            while i < len(self.__opcodes):
                opcode = self.__opcodes[i]

                if opcode.opcode_type == OpCodeType.LOAD_CONST:
                    self.__const_stack.append(opcode.opcode_value)
                elif opcode.opcode_type == OpCodeType.LOAD_VAR:
                    identifier = opcode.opcode_value
                    self.__memory[identifier] = self.__const_stack.pop()
                elif opcode.opcode_type == OpCodeType.PUSH_VAR:
                    identifier = opcode.opcode_value
                    self.__const_stack.append(self.__memory[identifier])
                elif opcode.opcode_type == OpCodeType.SHOW:
                    print(self.__const_stack.pop(), file=f)
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
                elif opcode.opcode_type == OpCodeType.LABEL:
                    pass
                elif opcode.opcode_type == OpCodeType.JZ:
                    stack_top = self.__const_stack.pop()

                    if not stack_top:
                        i = opcode.opcode_value
                elif opcode.opcode_type == OpCodeType.JMP:
                    i = opcode.opcode_value
                elif opcode.opcode_type == OpCodeType.JN:
                    stack_top = self.__const_stack.pop()

                    if stack_top < 0:
                        i = opcode.opcode_value
                elif opcode.opcode_type == OpCodeType.CALL:
                    self.__instruction_stack.append(i)
                    i = opcode.opcode_value
                elif opcode.opcode_type == OpCodeType.RET:
                    i = self.__instruction_stack.pop()

                i += 1