from typing import List

from .statement_node import StatementNode
from ...compiler.opcode import OpCode
from ...compiler.opcode_type import OpCodeType


class LabelNode(StatementNode):
    def __init__(self, label_name: str, opcode_num) -> None:
        self.__label_name = label_name
        self.__opcode_num = opcode_num

    def walk_and_print(self, tab_level: int) -> str:
        ast_string = self.add_tab_level(tab_level=tab_level)
        ast_string += "Label(\n"

        tab_level += 1
        ast_string += self.add_tab_level(tab_level=tab_level)
        ast_string += self.__label_name + " (label)\n"
        tab_level -= 1
        ast_string += self.add_tab_level(tab_level=tab_level)
        ast_string += ")\n"

        return ast_string

    def walk_and_compile(self, opcodes: List[OpCode]) -> None:
        opcodes.append(OpCode(
            opcode_type=OpCodeType.LABEL,
            opcode_value=self.__opcode_num,
            opcode_dtype="label"
        ))