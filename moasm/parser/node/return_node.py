from typing import List

from .statement_node import StatementNode
from ...compiler.opcode_type import OpCodeType
from ...compiler.opcode import OpCode


class ReturnNode(StatementNode):
    def walk_and_print(self, tab_level: int) -> str:
        ast_string = self.add_tab_level(tab_level=tab_level) + 'ReturnNode()\n'

        return ast_string

    def walk_and_compile(self, opcodes: List[OpCode]) -> None:
        opcodes.append(OpCode(opcode_type=OpCodeType.RET))