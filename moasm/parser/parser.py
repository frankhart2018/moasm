from typing import List

from ..tokenizer.token import Token
from ..tokenizer.tokentype import TokenType
from .node.node import Node
from .node.value_node import ValueNode
from .node.program_node import ProgramNode
from .node.show_node import ShowNode
from .node.string_node import StringNode
from .node.statement_node import StatementNode


class Parser:
    def __init__(self, tokens: List[Token]) -> None:
        self.__tokens = tokens
        self.__current_token_idx = 0

    def __peek(self) -> Token:
        return self.__tokens[self.__current_token_idx]

    def __advance(self) -> None:
        self.__current_token_idx += 1

    def __expect(self, expected_ttypes: List[TokenType]) -> None:
        if self.__peek().ttype not in  expected_ttypes:
            raise Exception(f"Expected one of {expected_ttypes} but got {self.__peek().ttype}")

    def __is_end(self) -> bool:
        return self.__peek().ttype == TokenType.END

    def __parse_value(self) -> ValueNode:
        if self.__peek().ttype == TokenType.STRING:
            return StringNode(value=self.__peek().val)

    def __parse_show_statement(self) -> StatementNode:
        self.__advance()
        value_nodes: List[ValueNode] = []
        while self.__peek().ttype != TokenType.NEWLINE:
            value_nodes.append(self.__parse_value())
            self.__advance()

        self.__advance()

        return ShowNode(value_nodes=value_nodes)

    def __parse_statement(self) -> StatementNode:
        if self.__peek().ttype == TokenType.SHOW:
            return self.__parse_show_statement()

    def __parse_program(self) -> Node:
        statements: List[StatementNode] = []

        while not self.__is_end():
            statements.append(self.__parse_statement())

        return ProgramNode(function="<main>", statements=statements)

    def parse(self) -> Node:
        ast_head = self.__parse_program()
        return ast_head