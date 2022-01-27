from typing import List

from .token import Token
from .tokentype import TokenType
from .keyword_list import KEYWORD_LIST


class Tokenizer:
    def __init__(self, groups: List[List[str]]) -> None:
        self.__groups: List[List[str]] = groups

    def tokenize(self) -> List[Token]:
        tokens: List[Token] = []

        for group_line in self.__groups:
            for word in group_line:
                if word in KEYWORD_LIST:
                    tokens.append(Token(TokenType.SHOW))
                elif word.isalpha():
                    tokens.append(Token(TokenType.STRING, word, "string"))
                elif word == "\n":
                    tokens.append(Token(TokenType.NEWLINE))

        tokens.append(Token(TokenType.END))

        return tokens