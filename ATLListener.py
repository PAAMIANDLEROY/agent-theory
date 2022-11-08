# Generated from ATL.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ATLParser import ATLParser
else:
    from ATLParser import ATLParser

# This class defines a complete listener for a parse tree produced by ATLParser.
class ATLListener(ParseTreeListener):

    # Enter a parse tree produced by ATLParser#Evaluation.
    def enterEvaluation(self, ctx:ATLParser.EvaluationContext):
        pass

    # Exit a parse tree produced by ATLParser#Evaluation.
    def exitEvaluation(self, ctx:ATLParser.EvaluationContext):
        pass


    # Enter a parse tree produced by ATLParser#Universal.
    def enterUniversal(self, ctx:ATLParser.UniversalContext):
        pass

    # Exit a parse tree produced by ATLParser#Universal.
    def exitUniversal(self, ctx:ATLParser.UniversalContext):
        pass


    # Enter a parse tree produced by ATLParser#Negation.
    def enterNegation(self, ctx:ATLParser.NegationContext):
        pass

    # Exit a parse tree produced by ATLParser#Negation.
    def exitNegation(self, ctx:ATLParser.NegationContext):
        pass


    # Enter a parse tree produced by ATLParser#Grouping.
    def enterGrouping(self, ctx:ATLParser.GroupingContext):
        pass

    # Exit a parse tree produced by ATLParser#Grouping.
    def exitGrouping(self, ctx:ATLParser.GroupingContext):
        pass


    # Enter a parse tree produced by ATLParser#Disjunction.
    def enterDisjunction(self, ctx:ATLParser.DisjunctionContext):
        pass

    # Exit a parse tree produced by ATLParser#Disjunction.
    def exitDisjunction(self, ctx:ATLParser.DisjunctionContext):
        pass


    # Enter a parse tree produced by ATLParser#Implies.
    def enterImplies(self, ctx:ATLParser.ImpliesContext):
        pass

    # Exit a parse tree produced by ATLParser#Implies.
    def exitImplies(self, ctx:ATLParser.ImpliesContext):
        pass


    # Enter a parse tree produced by ATLParser#Next.
    def enterNext(self, ctx:ATLParser.NextContext):
        pass

    # Exit a parse tree produced by ATLParser#Next.
    def exitNext(self, ctx:ATLParser.NextContext):
        pass


    # Enter a parse tree produced by ATLParser#Eventually.
    def enterEventually(self, ctx:ATLParser.EventuallyContext):
        pass

    # Exit a parse tree produced by ATLParser#Eventually.
    def exitEventually(self, ctx:ATLParser.EventuallyContext):
        pass


    # Enter a parse tree produced by ATLParser#Conjunction.
    def enterConjunction(self, ctx:ATLParser.ConjunctionContext):
        pass

    # Exit a parse tree produced by ATLParser#Conjunction.
    def exitConjunction(self, ctx:ATLParser.ConjunctionContext):
        pass


    # Enter a parse tree produced by ATLParser#Existential.
    def enterExistential(self, ctx:ATLParser.ExistentialContext):
        pass

    # Exit a parse tree produced by ATLParser#Existential.
    def exitExistential(self, ctx:ATLParser.ExistentialContext):
        pass


    # Enter a parse tree produced by ATLParser#Always.
    def enterAlways(self, ctx:ATLParser.AlwaysContext):
        pass

    # Exit a parse tree produced by ATLParser#Always.
    def exitAlways(self, ctx:ATLParser.AlwaysContext):
        pass


    # Enter a parse tree produced by ATLParser#Release.
    def enterRelease(self, ctx:ATLParser.ReleaseContext):
        pass

    # Exit a parse tree produced by ATLParser#Release.
    def exitRelease(self, ctx:ATLParser.ReleaseContext):
        pass


    # Enter a parse tree produced by ATLParser#Until.
    def enterUntil(self, ctx:ATLParser.UntilContext):
        pass

    # Exit a parse tree produced by ATLParser#Until.
    def exitUntil(self, ctx:ATLParser.UntilContext):
        pass


    # Enter a parse tree produced by ATLParser#atomExpr.
    def enterAtomExpr(self, ctx:ATLParser.AtomExprContext):
        pass

    # Exit a parse tree produced by ATLParser#atomExpr.
    def exitAtomExpr(self, ctx:ATLParser.AtomExprContext):
        pass



del ATLParser