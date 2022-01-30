from typing import List

from .statement_node import StatementNode
from ...compiler.opcode import OpCode
from ...compiler.opcode_type import OpCodeType


class JumpStatementNode(StatementNode):
    def __init__(self, label_node: StatementNode, opcode_type: OpCodeType) -> None:
        self.__label_position: StatementNode = label_node
        self.__opcode_type = opcode_type

    def walk_and_print(self, tab_level: int) -> str:
        ast_string = self.add_tab_level(tab_level=tab_level)
        ast_string += f"JumpStatementNode(\n"

        tab_level += 1
        ast_string += self.add_tab_level(tab_level=tab_level)
        ast_string += "label_node=[\n"
        tab_level += 1
        ast_string += self.__label_position.walk_and_print(tab_level=tab_level)
        tab_level -= 1
        ast_string += self.add_tab_level(tab_level=tab_level)
        ast_string += "],\n"
        ast_string += self.add_tab_level(tab_level=tab_level)
        ast_string += f"opcode_type={self.__opcode_type}\n"
        tab_level -= 1

        ast_string += self.add_tab_level(tab_level=tab_level)
        ast_string += ")\n"

        return ast_string

    def walk_and_compile(self, opcodes: List[OpCode]) -> None:
        self.__label_position.walk_and_compile(opcodes=opcodes)

        opcodes[-1].opcode_type = self.__opcode_type

    def late_bind(self, bind_node: 'StatementNode') -> None:
        self.__label_position = bind_node
