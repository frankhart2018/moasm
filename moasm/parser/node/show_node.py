from typing import List

from .statement_node import StatementNode
from .value_node import ValueNode


class ShowNode(StatementNode):
    def __init__(self, value_nodes: List[ValueNode]) -> None:
        self.__value_nodes = value_nodes

    def walk_and_print(self, tab_level: int) -> str:
        ast_string = self.add_tab_level(tab_level) + "ShowNode(\n"
        tab_level += 1
        ast_string += self.add_tab_level(tab_level=tab_level)
        ast_string += "ValueNodes=[\n"
        tab_level += 1

        for value_node in self.__value_nodes:
            ast_string += value_node.walk_and_print(tab_level=tab_level)

        tab_level -= 1
        ast_string += self.add_tab_level(tab_level=tab_level)
        ast_string += "]\n"
        tab_level -= 1
        ast_string += self.add_tab_level(tab_level=tab_level)
        ast_string += ")\n"

        return ast_string