from moasm.pretokenizer.pretokenizer import PreTokenizer
from moasm.grouper.grouper import Grouper


pretokens = PreTokenizer("test.moasm").tokenize()

groups = Grouper(pretokens).group()