from typing import List

from .token import Token
from .tokentype import TokenType
from .keyword_list import KEYWORD_LIST


class Tokenizer:
    def __init__(self, groups: List[List[str]]) -> None:
        self.__groups: List[List[str]] = groups

    def tokenize(self) -> List[Token]:
        tokens: List[Token] = []
        is_next_token_identifier = False

        for group_line in self.__groups:
            for i, word in enumerate(group_line):
                if word in KEYWORD_LIST:
                    tokens.append(Token(TokenType[word.upper()]))
                elif word.isalpha():
                    tokens.append(Token(TokenType.STRING, " ".join(group_line[i:-1]), "string"))
                    tokens.append(Token(TokenType.NEWLINE))
                    break
                elif word.isdigit():
                    tokens.append(Token(TokenType.NUMBER, word, "number"))
                elif word == "\n":
                    tokens.append(Token(TokenType.NEWLINE))
                elif word.startswith("%"):
                    tokens.append(Token(TokenType.IDENTIFIER, word[1:], "identifier"))
                elif word.startswith("$"):
                    tokens.append(Token(TokenType.LABEL, word[1:], "label"))

        tokens.append(Token(TokenType.END))

        return tokens