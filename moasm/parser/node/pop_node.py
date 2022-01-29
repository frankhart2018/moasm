from typing import List

from .statement_node import StatementNode
from .identifier_node import IdentifierNode
from ...compiler.opcode import OpCode
from ...compiler.opcode_type import OpCodeType


class PopNode(StatementNode):
    def __init__(self, target: IdentifierNode) -> None:
        self.__target = target

    def walk_and_print(self, tab_level: int) -> str:
        ast_string = self.add_tab_level(tab_level=tab_level)
        ast_string += 'PopNode(\n'

        tab_level += 1
        ast_string += self.add_tab_level(tab_level=tab_level)
        ast_string += "TargetNode=[\n"
        tab_level += 1

        ast_string += self.__target.walk_and_print(tab_level=tab_level)

        tab_level -= 1
        ast_string += self.add_tab_level(tab_level=tab_level)
        ast_string += "]\n"
        tab_level -= 1
        ast_string += self.add_tab_level(tab_level=tab_level)
        ast_string += ")\n"

        return ast_string

    def walk_and_compile(self, opcodes: List[OpCode]) -> None:
        self.__target.walk_and_compile(opcodes=opcodes)