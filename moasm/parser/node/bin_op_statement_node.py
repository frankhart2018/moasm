from typing import List

from .statement_node import StatementNode
from ...compiler.opcode import OpCode
from ...compiler.opcode_type import OpCodeType
from .value_node import ValueNode


class BinOpStatementNode(StatementNode):
    def __init__(self, left: ValueNode, op: OpCodeType, right: ValueNode) -> None:
        self.__left = left
        self.__op = op
        self.__right = right

    def walk_and_print(self, tab_level: int) -> str:
        ast_string = self.add_tab_level(tab_level=tab_level)
        ast_string += "BinOpStatementNode(\n"

        tab_level += 1
        ast_string += self.add_tab_level(tab_level=tab_level)
        ast_string += "left=[\n"
        tab_level += 1
        ast_string += self.__left.walk_and_print(tab_level=tab_level)
        tab_level -= 1
        ast_string += self.add_tab_level(tab_level=tab_level)
        ast_string += "],\n"

        ast_string += self.add_tab_level(tab_level=tab_level) + "op=" + str(self.__op).split(".")[1] + ",\n"
        tab_level -= 1

        tab_level += 1
        ast_string += self.add_tab_level(tab_level=tab_level)
        ast_string += "right=[\n"
        tab_level += 1
        ast_string += self.__right.walk_and_print(tab_level=tab_level)
        tab_level -= 1
        ast_string += self.add_tab_level(tab_level=tab_level)
        ast_string += "],\n"

        tab_level -= 1
        ast_string += self.add_tab_level(tab_level=tab_level)
        ast_string += ")\n"

        return ast_string

    def walk_and_compile(self, opcodes: List[OpCode]) -> None:
        self.__left.walk_and_compile(opcodes=opcodes)
        self.__right.walk_and_compile(opcodes=opcodes)
        opcodes.append(OpCode(opcode_type=self.__op))