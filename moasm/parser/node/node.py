from abc import abstractmethod
from typing import List

from ...compiler.opcode import OpCode


class Node:
    def add_tab_level(self, tab_level: int) -> str:
        return "\t" * tab_level

    @abstractmethod
    def walk_and_print(self, tab_level: int) -> str:
        pass

    @abstractmethod
    def walk_and_compile(self, opcodes: List[OpCode]) -> None:
        pass