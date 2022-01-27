from abc import abstractmethod


class Node:
    def add_tab_level(self, tab_level: int) -> str:
        return "\t" * tab_level

    @abstractmethod
    def walk_and_print(self, tab_level: int) -> str:
        pass