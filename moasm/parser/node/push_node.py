from typing import List

from .statement_node import StatementNode
from .value_node import ValueNode
from ...compiler.opcode import OpCode
from ...compiler.opcode_type import OpCodeType


class PushNode(StatementNode):
    def __init__(self, value: ValueNode) -> None:
        self.__value = value

    def walk_and_print(self, tab_level: int) -> str:
        ast_string = self.add_tab_level(tab_level=tab_level)
        ast_string += 'PushNode(\n'

        tab_level += 1
        ast_string += self.add_tab_level(tab_level=tab_level)
        ast_string += "ValueNode=[\n"
        tab_level += 1

        ast_string += self.__value.walk_and_print(tab_level=tab_level)

        tab_level -= 1
        ast_string += self.add_tab_level(tab_level=tab_level)
        ast_string += "]\n"
        tab_level -= 1
        ast_string += self.add_tab_level(tab_level=tab_level)
        ast_string += ")\n"

        return ast_string

    def walk_and_compile(self, opcodes: List[OpCode]) -> None:
        self.__value.walk_and_compile(opcodes=opcodes)