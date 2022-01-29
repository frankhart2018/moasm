from typing import List

from .value_node import ValueNode
from ...compiler.opcode import OpCode
from ...compiler.opcode_type import OpCodeType


class IdentifierNode(ValueNode):
    def __init__(self, identifier_name: str, emit_push: bool = False):
        self.__identifier_name = identifier_name
        self.__emit_push = emit_push

    def walk_and_print(self, tab_level: int) -> str:
        ast_string = self.add_tab_level(tab_level)
        ast_string += self.__identifier_name + " (identifier) \n"

        return ast_string

    def walk_and_compile(self, opcodes: List[OpCode]) -> None:
        opcode_type: OpCodeType = OpCodeType.PUSH_VAR if self.__emit_push else OpCodeType.LOAD_VAR

        opcodes.append(OpCode(
            opcode_type=opcode_type,
            opcode_value=self.__identifier_name,
            opcode_dtype="identifer"
        ))