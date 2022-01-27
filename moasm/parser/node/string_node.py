from .value_node import ValueNode


class StringNode(ValueNode):
    def __init__(self, value: str):
        self.__value: str = value

    def walk_and_print(self, tab_level: int) -> str:
        ast_string = self.add_tab_level(tab_level)
        ast_string += self.__value + " (string) \n"

        return ast_string