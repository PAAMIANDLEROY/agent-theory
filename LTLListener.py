# Generated from LTL.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LTLParser import LTLParser
else:
    from LTLParser import LTLParser

# This class defines a complete listener for a parse tree produced by LTLParser.
class LTLListener(ParseTreeListener):

    # Enter a parse tree produced by LTLParser#Evaluation.
    def enterEvaluation(self, ctx:LTLParser.EvaluationContext):
        pass

    # Exit a parse tree produced by LTLParser#Evaluation.
    def exitEvaluation(self, ctx:LTLParser.EvaluationContext):
        pass


    # Enter a parse tree produced by LTLParser#Disjunction.
    def enterDisjunction(self, ctx:LTLParser.DisjunctionContext):
        pass

    # Exit a parse tree produced by LTLParser#Disjunction.
    def exitDisjunction(self, ctx:LTLParser.DisjunctionContext):
        pass


    # Enter a parse tree produced by LTLParser#Implies.
    def enterImplies(self, ctx:LTLParser.ImpliesContext):
        pass

    # Exit a parse tree produced by LTLParser#Implies.
    def exitImplies(self, ctx:LTLParser.ImpliesContext):
        pass


    # Enter a parse tree produced by LTLParser#Negation.
    def enterNegation(self, ctx:LTLParser.NegationContext):
        pass

    # Exit a parse tree produced by LTLParser#Negation.
    def exitNegation(self, ctx:LTLParser.NegationContext):
        pass


    # Enter a parse tree produced by LTLParser#Next.
    def enterNext(self, ctx:LTLParser.NextContext):
        pass

    # Exit a parse tree produced by LTLParser#Next.
    def exitNext(self, ctx:LTLParser.NextContext):
        pass


    # Enter a parse tree produced by LTLParser#Eventually.
    def enterEventually(self, ctx:LTLParser.EventuallyContext):
        pass

    # Exit a parse tree produced by LTLParser#Eventually.
    def exitEventually(self, ctx:LTLParser.EventuallyContext):
        pass


    # Enter a parse tree produced by LTLParser#Conjunction.
    def enterConjunction(self, ctx:LTLParser.ConjunctionContext):
        pass

    # Exit a parse tree produced by LTLParser#Conjunction.
    def exitConjunction(self, ctx:LTLParser.ConjunctionContext):
        pass


    # Enter a parse tree produced by LTLParser#Grouping.
    def enterGrouping(self, ctx:LTLParser.GroupingContext):
        pass

    # Exit a parse tree produced by LTLParser#Grouping.
    def exitGrouping(self, ctx:LTLParser.GroupingContext):
        pass


    # Enter a parse tree produced by LTLParser#Always.
    def enterAlways(self, ctx:LTLParser.AlwaysContext):
        pass

    # Exit a parse tree produced by LTLParser#Always.
    def exitAlways(self, ctx:LTLParser.AlwaysContext):
        pass


    # Enter a parse tree produced by LTLParser#Release.
    def enterRelease(self, ctx:LTLParser.ReleaseContext):
        pass

    # Exit a parse tree produced by LTLParser#Release.
    def exitRelease(self, ctx:LTLParser.ReleaseContext):
        pass


    # Enter a parse tree produced by LTLParser#Until.
    def enterUntil(self, ctx:LTLParser.UntilContext):
        pass

    # Exit a parse tree produced by LTLParser#Until.
    def exitUntil(self, ctx:LTLParser.UntilContext):
        pass


    # Enter a parse tree produced by LTLParser#atomExpr.
    def enterAtomExpr(self, ctx:LTLParser.AtomExprContext):
        pass

    # Exit a parse tree produced by LTLParser#atomExpr.
    def exitAtomExpr(self, ctx:LTLParser.AtomExprContext):
        pass



del LTLParser