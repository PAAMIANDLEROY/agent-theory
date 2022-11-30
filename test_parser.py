from antlr4 import *
from LTLLexer import *
from LTLParser import *
from LTLListener import *
from LTLVisitor import *

Formula='a or not b'
Logic='LTL'

print("logic")
print(Logic)
if Logic=='LTL':
    print("formula")
    print(Formula)
    lexer = LTLLexer(Formula)
    print("lexer")
    print(lexer)
    stream = CommonTokenStream(lexer)
    print("stream")
    print(stream)
    parser = LTLParser(stream)
    print("parser")
    print(parser)
    tree = parser.ltlExpr()
    visitor = YOUR_VISITOR_CLASS()
    print(visitor.visit(tree))
