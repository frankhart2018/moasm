from typing import List

from .node import Node
from .statement_node import StatementNode
from ...compiler.opcode import OpCode


class ProgramNode(Node):
    def __init__(self, function: str,  statements: List[StatementNode]):
        self.__function: str = function
        self.__statements: List[StatementNode] = statements

    def walk_and_print(self, tab_level: int) -> str:
        ast_string = "ProgramNode(\n"
        tab_level = 1
        ast_string += self.add_tab_level(tab_level)
        ast_string += f"function={self.__function},\n"
        ast_string += self.add_tab_level(tab_level)
        ast_string += f"statements=[\n"
        tab_level += 1

        for statement in self.__statements:
            ast_string += statement.walk_and_print(tab_level=tab_level)

        tab_level -= 1
        ast_string += self.add_tab_level(tab_level)
        ast_string += "]\n"
        tab_level -= 1
        ast_string += self.add_tab_level(tab_level)
        ast_string += ")"

        return ast_string

    def walk_and_compile(self, opcodes: List[OpCode]) -> None:
        for statement in self.__statements:
            statement.walk_and_compile(opcodes=opcodes)