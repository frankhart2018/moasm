import argparse
from typing import List

from .pretokenizer.pretokenizer import PreTokenizer
from .pretokenizer.pretoken import PreToken
from .grouper.grouper import Grouper
from .tokenizer.tokenizer import Tokenizer
from .tokenizer.token import Token
from .parser.parser import Parser
from .parser.node.node import Node
from .compiler.compiler import Compiler
from .compiler.opcode import OpCode
from .vm.vm import VM


def print_topic(topic: str) -> None:
    print("*" * 50)
    print(f"* {topic}")
    print("*" * 50)

def end_topic() -> None:
    print("-" * 50)


def run() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser("MoASM assembler")
    parser.add_argument("-i", "--input", type=str, help="Input file")
    parser.add_argument("-t1", "--pretokens", default=False, action="store_true", help="Display pre-tokens")
    parser.add_argument("-g", "--groups", default=False, action="store_true", help="Display groups")
    parser.add_argument("-t2", "--tokens", default=False, action="store_true", help="Display tokens")
    parser.add_argument("-a", "--ast", default=False, action="store_true", help="Display AST")
    parser.add_argument("-b", "--bytecode", default=False, action="store_true", help="Display bytecode")
    parser.add_argument("-c", '--convert', default=False, action='store_true',
                        help='Convert source to english alphabets')
    parser.add_argument("-r", "--redirect", type=str, help="Redirect output to file")

    args: argparse.Namespace = parser.parse_args()

    tokens: List[PreToken] = PreTokenizer(source_file_path=args.input).tokenize()
    if args.pretokens:
        print_topic("Pre-Tokens")
        for token in tokens:
            print(token)
        end_topic()

    groups: List[List[str]] = Grouper(tokens=tokens).group()
    if args.groups:
        print_topic("Groups")
        for i, group in enumerate(groups):
            print(f"{i+1}: {group}")
        end_topic()

    if args.convert:
        out_filename = args.input + ".eng"

        with open(out_filename, 'w') as f:
            for group in groups:
                f.write(" ".join(group))
        print(f"File converted to english at: {out_filename}")
        return

    tokens: List[Token] = Tokenizer(groups=groups).tokenize()
    if args.tokens:
        print_topic("Tokens")
        for token in tokens:
            print(token)
        end_topic()

    ast_root: Node = Parser(tokens=tokens).parse()
    if args.ast:
        print_topic("AST")
        print(ast_root.walk_and_print(tab_level=1))
        end_topic()

    bytecode: List[OpCode] = Compiler(ast_root=ast_root).compile()
    if args.bytecode:
        print_topic("ByteCode")
        for opcode in bytecode:
            print(opcode)
        end_topic()

    vm: VM = VM(opcodes=bytecode)
    vm.run(out_file="stdout" if not args.redirect else args.redirect)