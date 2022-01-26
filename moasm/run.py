import argparse
from typing import List

from .pretokenizer.pretokenizer import PreTokenizer
from .pretokenizer.pretoken import PreToken
from .grouper.grouper import Grouper


def run() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser("MoASM assembler")
    parser.add_argument("-i", "--input", type=str, help="Input file")
    parser.add_argument("-t1", "--pretokens", default=False, action="store_true", help="Display pre-tokens")
    parser.add_argument("-g", "--groups", default=False, action="store_true", help="Display groups")

    args: argparse.Namespace = parser.parse_args()

    tokens: List[PreToken] = PreTokenizer(source_file_path=args.input).tokenize()
    if args.pretokens:
        for token in tokens:
            print(token)

    groups: List[List[str]] = Grouper(tokens=tokens).group()
    if args.groups:
        for i, group in enumerate(groups):
            print(f"{i+1}: {group}")