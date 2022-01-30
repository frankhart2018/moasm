from typing import List

from ..pretokenizer.pretoken import PreToken
from .groupmap import MAP


class Grouper:
    def __init__(self, tokens: List[PreToken]) -> None:
        self.__tokens: List[PreToken] = tokens

    def group(self) -> List[List[str]]:
        groups: List[List[str]] = []
        stack: List[str] = []

        for token in self.__tokens:
            if token in [PreToken.DOT, PreToken.DASH]:
                stack.append(token.value)
            elif token == PreToken.TILDE:
                stack.append(" ")
            elif token in [PreToken.WHITESPACE, PreToken.NEWLINE]:
                current_morse = ""

                while stack:
                    if stack[-1].isalnum() or stack[-1] in [' ', '\n', '%', '$']:
                        break
                    current_morse += stack.pop()

                morse_to_str = MAP.get(current_morse[::-1], "")
                stack.append(morse_to_str)

                if token == PreToken.NEWLINE:
                    groups.append("".join(stack).split())
                    groups[-1].append("\n")
                    stack = []

        return groups