from typing import List

from .value_node import ValueNode
from ...compiler.opcode import OpCode
from ...compiler.opcode_type import OpCodeType


class StringNode(ValueNode):
    def __init__(self, value: str):
        self.__value: str = value

    def walk_and_print(self, tab_level: int) -> str:
        ast_string = self.add_tab_level(tab_level)
        ast_string += self.__value + " (string) \n"

        return ast_string

    def walk_and_compile(self, opcodes: List[OpCode]) -> None:
        opcodes.append(OpCode(
            opcode_type=OpCodeType.LOAD_CONST,
            opcode_value=self.__value,
            opcode_dtype="string"
        ))
