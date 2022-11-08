# Generated from ATL.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ATLParser import ATLParser
else:
    from ATLParser import ATLParser

# This class defines a complete generic visitor for a parse tree produced by ATLParser.

class ATLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ATLParser#Evaluation.
    def visitEvaluation(self, ctx:ATLParser.EvaluationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ATLParser#Universal.
    def visitUniversal(self, ctx:ATLParser.UniversalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ATLParser#Negation.
    def visitNegation(self, ctx:ATLParser.NegationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ATLParser#Grouping.
    def visitGrouping(self, ctx:ATLParser.GroupingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ATLParser#Disjunction.
    def visitDisjunction(self, ctx:ATLParser.DisjunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ATLParser#Implies.
    def visitImplies(self, ctx:ATLParser.ImpliesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ATLParser#Next.
    def visitNext(self, ctx:ATLParser.NextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ATLParser#Eventually.
    def visitEventually(self, ctx:ATLParser.EventuallyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ATLParser#Conjunction.
    def visitConjunction(self, ctx:ATLParser.ConjunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ATLParser#Existential.
    def visitExistential(self, ctx:ATLParser.ExistentialContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ATLParser#Always.
    def visitAlways(self, ctx:ATLParser.AlwaysContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ATLParser#Release.
    def visitRelease(self, ctx:ATLParser.ReleaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ATLParser#Until.
    def visitUntil(self, ctx:ATLParser.UntilContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ATLParser#atomExpr.
    def visitAtomExpr(self, ctx:ATLParser.AtomExprContext):
        return self.visitChildren(ctx)



del ATLParser