import os.path
import sys
from typing import List

from .token import Token
from .tokentype import TokenType
from .keyword_list import KEYWORD_LIST
from ..utils.file_paths import LIBS_DIR
from ..pretokenizer.pretoken import PreToken
from ..pretokenizer.pretokenizer import PreTokenizer
from ..grouper.grouper import Grouper


class Tokenizer:
    def __init__(self, groups: List[List[str]]) -> None:
        self.__groups: List[List[str]] = groups

    def __get_groups_for_lib(self, module_name: str, func_name: str) -> List[List[str]]:
        module_path = os.path.join(module_name.lower(), func_name.lower() + ".moasm")
        module_path = os.path.join(LIBS_DIR, module_path)

        pretokens: List[PreToken] = PreTokenizer(source_file_path=module_path).tokenize()
        groups: List[List[str]] = Grouper(tokens=pretokens).group()

        return groups

    def __tokenize(self, tokens: List[Token]) -> bool:
        is_module_name = False
        module_name = ""
        func_name = ""

        for i, group_line in enumerate(self.__groups):
            for j, word in enumerate(group_line):
                if word in KEYWORD_LIST:
                    if word.upper() == 'INC':
                        is_module_name = True
                        continue

                    tokens.append(Token(TokenType[word.upper()]))
                elif word.isalpha():
                    tokens.append(Token(TokenType.STRING, " ".join(group_line[j:-1]), "string"))
                    tokens.append(Token(TokenType.NEWLINE))
                    break
                elif word.isdigit():
                    tokens.append(Token(TokenType.NUMBER, word, "number"))
                elif word == "\n":
                    if is_module_name:
                        self.__groups = self.__groups[:i] + self.__get_groups_for_lib(module_name, func_name) + self.__groups[i+1:]
                        return False
                    tokens.append(Token(TokenType.NEWLINE))
                elif word.startswith("%"):
                    tokens.append(Token(TokenType.IDENTIFIER, word[1:], "identifier"))
                elif word.startswith("$"):
                    if is_module_name:
                        if module_name == "":
                            module_name = word[1:]
                        elif module_name != "" and func_name == "":
                            func_name = word[1:]
                        continue
                    tokens.append(Token(TokenType.LABEL, word[1:], "label"))

        return True


    def tokenize(self, dump_late_groups: bool, file_name) -> List[Token]:
        tokens: List[Token] = []

        if not self.__tokenize(tokens):
            tokens = []
            self.__tokenize(tokens)

        if dump_late_groups:
            out_filename = file_name + ".eng"

            with open(out_filename, 'w') as f:
                for group in self.__groups:
                    f.write(" ".join(group))
            print(f"File converted to english after tokenization at: {out_filename}")
            sys.exit()

        tokens.append(Token(TokenType.END))
        return tokens