from typing import List

from .pretoken import PreToken


class PreTokenizer:
    def __init__(self, source_file_path: str) -> None:
        self.__source_file_path: str = source_file_path

        self.__source = self.__read_source()

    def __read_source(self) -> str:
        with open(self.__source_file_path, 'r') as file:
            source = file.read()

        if not source.endswith("\n"):
            source += "\n"

        return source

    def tokenize(self) -> List[PreToken]:
        tokens: List[PreToken] = []

        for char in self.__source:
            if char == '.':
                tokens.append(PreToken.DOT)
            elif char == '-':
                tokens.append(PreToken.DASH)
            elif char == '~':
                tokens.append(PreToken.TILDE)
            elif char == '\n':
                tokens.append(PreToken.NEWLINE)
            elif char == ' ':
                tokens.append(PreToken.WHITESPACE)

        return tokens