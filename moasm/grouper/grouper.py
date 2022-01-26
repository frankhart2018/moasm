from typing import List

from ..pretokenizer.pretoken import PreToken
from .groupmap import MAP


class Grouper:
    def __init__(self, tokens: List[PreToken]) -> None:
        self.__tokens: List[PreToken] = tokens

    def group(self) -> List[List[str]]:
        groups: List[List[str]] = []
        current_group: List[str] = []
        current_morse: str = ""
        current_str: str = ""

        for token in self.__tokens:
            if token == PreToken.DOT:
                current_morse += "."
            elif token == PreToken.DASH:
                current_morse += "-"
            elif token == PreToken.WHITESPACE:
                current_str += MAP.get(current_morse, "")
                current_morse = ""
            elif token == PreToken.TILDE:
                current_group.append(current_str)
                current_str = ""
            elif token == PreToken.NEWLINE:
                if current_morse:
                    current_str += MAP.get(current_morse, "")
                    current_group.append(current_str)
                groups.append(current_group)
                current_group = []

        return groups