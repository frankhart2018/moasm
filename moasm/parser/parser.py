from typing import List, Dict

from ..tokenizer.token import Token
from ..tokenizer.tokentype import TokenType
from .node.node import Node
from .node.value_node import ValueNode
from .node.program_node import ProgramNode
from .node.show_node import ShowNode
from .node.string_node import StringNode
from .node.statement_node import StatementNode
from .node.number_node import NumberNode
from ..compiler.opcode_type import OpCodeType
from .node.bin_op_node import BinOpNode
from .node.push_node import PushNode
from .node.pop_node import PopNode
from .node.identifier_node import IdentifierNode
from .node.jump_statement_node import JumpStatementNode
from .node.label_node import LabelNode


class Parser:
    def __init__(self, tokens: List[Token]) -> None:
        self.__tokens = tokens
        self.__current_token_idx = 0

        self.__label_bind_map: Dict[str, List[StatementNode]] = {}
        self.__num_opcodes: int = 0

    def __peek(self) -> Token:
        return self.__tokens[self.__current_token_idx]

    def __advance(self) -> None:
        self.__current_token_idx += 1

    def __expect(self, expected_ttypes: List[TokenType]) -> None:
        if self.__peek().ttype not in  expected_ttypes:
            raise Exception(f"Expected one of {expected_ttypes} but got {self.__peek().ttype}")

    def __is_end(self) -> bool:
        return self.__peek().ttype == TokenType.END

    def __add_to_label_bind_map(self, label_name: str, statement_node: StatementNode) -> None:
        if label_name not in self.__label_bind_map:
            self.__label_bind_map[label_name] = []

        self.__label_bind_map[label_name].append(statement_node)

    def __parse_identifier(self) -> IdentifierNode:
        return IdentifierNode(identifier_name=self.__peek().val)

    def __parse_value(self) -> ValueNode:
        self.__num_opcodes += 1

        if self.__peek().ttype == TokenType.STRING:
            return StringNode(value=self.__peek().val)
        elif self.__peek().ttype == TokenType.NUMBER:
            return NumberNode(value=self.__peek().val)
        elif self.__peek().ttype == TokenType.IDENTIFIER:
            return IdentifierNode(identifier_name=self.__peek().val, emit_push=True)

    def __parse_show_statement(self) -> StatementNode:
        self.__advance()
        value_nodes: List[ValueNode] = []
        while self.__peek().ttype != TokenType.NEWLINE:
            value_nodes.append(self.__parse_value())
            self.__advance()

        self.__advance()

        return ShowNode(value_nodes=value_nodes)

    def __parse_bin_op_statement(self) -> StatementNode:
        op = OpCodeType[str(self.__peek().ttype).split(".")[1]]

        self.__advance()
        left = self.__parse_value()

        self.__advance()
        right = self.__parse_value()

        self.__advance()
        self.__advance()

        return BinOpNode(left=left, op=op, right=right)

    def __parse_push_statement(self) -> StatementNode:
        self.__advance()
        value_node = self.__parse_value()
        self.__advance()
        self.__advance()

        return PushNode(value=value_node)

    def __parse_pop_statement(self) -> StatementNode:
        self.__advance()
        target_node = self.__parse_identifier()
        self.__advance()
        self.__advance()

        return PopNode(target=target_node)

    def __parse_jump_statement(self) -> StatementNode:
        opcode_type = OpCodeType.JMP if self.__peek().ttype == TokenType.JMP else OpCodeType.JZ
        self.__advance()
        label_name = self.__peek().val
        self.__advance()
        self.__advance()

        dummy_label_node = LabelNode(label_name="dummy", opcode_num=-1)
        jmp_node = JumpStatementNode(label_node=dummy_label_node, opcode_type=opcode_type)
        self.__add_to_label_bind_map(label_name=label_name, statement_node=jmp_node)

        return jmp_node

    def __parse_label(self) -> StatementNode:
        label_name = self.__peek().val
        self.__advance()
        self.__advance()

        label_node = LabelNode(label_name=label_name, opcode_num=self.__num_opcodes - 2)

        late_bind_candidates = self.__label_bind_map.get(label_name, [])
        for late_bind_candidate in late_bind_candidates:
            late_bind_candidate.late_bind(bind_node=label_node)
        del self.__label_bind_map[label_name]

        return label_node

    def __parse_statement(self) -> StatementNode:
        self.__num_opcodes += 1

        if self.__peek().ttype == TokenType.SHOW:
            return self.__parse_show_statement()
        elif self.__peek().ttype in [TokenType.ADD, TokenType.SUB, TokenType.MUL, TokenType.DIV, TokenType.MOD]:
            return self.__parse_bin_op_statement()
        elif self.__peek().ttype == TokenType.PUSH:
            return self.__parse_push_statement()
        elif self.__peek().ttype == TokenType.POP:
            return self.__parse_pop_statement()
        elif self.__peek().ttype in [TokenType.JZ, TokenType.JMP]:
            return self.__parse_jump_statement()
        elif self.__peek().ttype == TokenType.LABEL:
            return self.__parse_label()

    def __parse_program(self) -> Node:
        statements: List[StatementNode] = []

        while not self.__is_end():
            statements.append(self.__parse_statement())

        return ProgramNode(function="<main>", statements=statements)

    def parse(self) -> Node:
        ast_head = self.__parse_program()
        return ast_head