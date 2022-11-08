# Generated from ATL.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\34")
        buf.write("\65\4\2\t\2\4\3\t\3\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\5\2\35\n\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\7\2.\n\2\f\2\16\2\61\13\2\3\3\3\3\3")
        buf.write("\3\2\3\2\4\2\4\2\13\3\2\3\4\3\2\5\6\3\2\7\b\3\2\t\n\3")
        buf.write("\2\13\f\3\2\r\16\3\2\17\20\3\2\21\22\3\2\23\24\2>\2\34")
        buf.write("\3\2\2\2\4\62\3\2\2\2\6\7\b\2\1\2\7\b\t\2\2\2\b\35\5\2")
        buf.write("\2\17\t\n\t\3\2\2\n\35\5\2\2\16\13\f\t\4\2\2\f\35\5\2")
        buf.write("\2\r\r\16\t\5\2\2\16\35\5\2\2\f\17\20\7\25\2\2\20\21\7")
        buf.write("\33\2\2\21\22\7\26\2\2\22\35\5\2\2\6\23\24\7\27\2\2\24")
        buf.write("\25\7\33\2\2\25\26\7\30\2\2\26\35\5\2\2\5\27\30\7\31\2")
        buf.write("\2\30\31\5\2\2\2\31\32\7\32\2\2\32\35\3\2\2\2\33\35\5")
        buf.write("\4\3\2\34\6\3\2\2\2\34\t\3\2\2\2\34\13\3\2\2\2\34\r\3")
        buf.write("\2\2\2\34\17\3\2\2\2\34\23\3\2\2\2\34\27\3\2\2\2\34\33")
        buf.write("\3\2\2\2\35/\3\2\2\2\36\37\f\13\2\2\37 \t\6\2\2 .\5\2")
        buf.write("\2\f!\"\f\n\2\2\"#\t\7\2\2#.\5\2\2\13$%\f\t\2\2%&\t\b")
        buf.write("\2\2&.\5\2\2\n\'(\f\b\2\2()\t\t\2\2).\5\2\2\t*+\f\7\2")
        buf.write("\2+,\t\n\2\2,.\5\2\2\b-\36\3\2\2\2-!\3\2\2\2-$\3\2\2\2")
        buf.write("-\'\3\2\2\2-*\3\2\2\2.\61\3\2\2\2/-\3\2\2\2/\60\3\2\2")
        buf.write("\2\60\3\3\2\2\2\61/\3\2\2\2\62\63\7\33\2\2\63\5\3\2\2")
        buf.write("\2\5\34-/")
        return buf.getvalue()


class ATLParser ( Parser ):

    grammarFileName = "ATL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'!'", "'not'", "'next'", "'X'", "'eventually'", 
                     "'F'", "'always'", "'G'", "'until'", "'U'", "'release'", 
                     "'R'", "'&&'", "'and'", "'||'", "'or'", "'->'", "'implies'", 
                     "'<'", "'>'", "'['", "']'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ATOM", "WS" ]

    RULE_atlExpr = 0
    RULE_atomExpr = 1

    ruleNames =  [ "atlExpr", "atomExpr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    ATOM=25
    WS=26

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class AtlExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ATLParser.RULE_atlExpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class EvaluationContext(AtlExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ATLParser.AtlExprContext
            super().__init__(parser)
            self.child = None # AtomExprContext
            self.copyFrom(ctx)

        def atomExpr(self):
            return self.getTypedRuleContext(ATLParser.AtomExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEvaluation" ):
                listener.enterEvaluation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEvaluation" ):
                listener.exitEvaluation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEvaluation" ):
                return visitor.visitEvaluation(self)
            else:
                return visitor.visitChildren(self)


    class UniversalContext(AtlExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ATLParser.AtlExprContext
            super().__init__(parser)
            self.group = None # Token
            self.child = None # AtlExprContext
            self.copyFrom(ctx)

        def ATOM(self):
            return self.getToken(ATLParser.ATOM, 0)
        def atlExpr(self):
            return self.getTypedRuleContext(ATLParser.AtlExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUniversal" ):
                listener.enterUniversal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUniversal" ):
                listener.exitUniversal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUniversal" ):
                return visitor.visitUniversal(self)
            else:
                return visitor.visitChildren(self)


    class NegationContext(AtlExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ATLParser.AtlExprContext
            super().__init__(parser)
            self.child = None # AtlExprContext
            self.copyFrom(ctx)

        def atlExpr(self):
            return self.getTypedRuleContext(ATLParser.AtlExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegation" ):
                listener.enterNegation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegation" ):
                listener.exitNegation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegation" ):
                return visitor.visitNegation(self)
            else:
                return visitor.visitChildren(self)


    class GroupingContext(AtlExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ATLParser.AtlExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atlExpr(self):
            return self.getTypedRuleContext(ATLParser.AtlExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGrouping" ):
                listener.enterGrouping(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGrouping" ):
                listener.exitGrouping(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGrouping" ):
                return visitor.visitGrouping(self)
            else:
                return visitor.visitChildren(self)


    class DisjunctionContext(AtlExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ATLParser.AtlExprContext
            super().__init__(parser)
            self.left = None # AtlExprContext
            self.right = None # AtlExprContext
            self.copyFrom(ctx)

        def atlExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ATLParser.AtlExprContext)
            else:
                return self.getTypedRuleContext(ATLParser.AtlExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDisjunction" ):
                listener.enterDisjunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDisjunction" ):
                listener.exitDisjunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDisjunction" ):
                return visitor.visitDisjunction(self)
            else:
                return visitor.visitChildren(self)


    class ImpliesContext(AtlExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ATLParser.AtlExprContext
            super().__init__(parser)
            self.left = None # AtlExprContext
            self.right = None # AtlExprContext
            self.copyFrom(ctx)

        def atlExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ATLParser.AtlExprContext)
            else:
                return self.getTypedRuleContext(ATLParser.AtlExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImplies" ):
                listener.enterImplies(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImplies" ):
                listener.exitImplies(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplies" ):
                return visitor.visitImplies(self)
            else:
                return visitor.visitChildren(self)


    class NextContext(AtlExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ATLParser.AtlExprContext
            super().__init__(parser)
            self.child = None # AtlExprContext
            self.copyFrom(ctx)

        def atlExpr(self):
            return self.getTypedRuleContext(ATLParser.AtlExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNext" ):
                listener.enterNext(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNext" ):
                listener.exitNext(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNext" ):
                return visitor.visitNext(self)
            else:
                return visitor.visitChildren(self)


    class EventuallyContext(AtlExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ATLParser.AtlExprContext
            super().__init__(parser)
            self.child = None # AtlExprContext
            self.copyFrom(ctx)

        def atlExpr(self):
            return self.getTypedRuleContext(ATLParser.AtlExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEventually" ):
                listener.enterEventually(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEventually" ):
                listener.exitEventually(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEventually" ):
                return visitor.visitEventually(self)
            else:
                return visitor.visitChildren(self)


    class ConjunctionContext(AtlExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ATLParser.AtlExprContext
            super().__init__(parser)
            self.left = None # AtlExprContext
            self.right = None # AtlExprContext
            self.copyFrom(ctx)

        def atlExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ATLParser.AtlExprContext)
            else:
                return self.getTypedRuleContext(ATLParser.AtlExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConjunction" ):
                listener.enterConjunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConjunction" ):
                listener.exitConjunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConjunction" ):
                return visitor.visitConjunction(self)
            else:
                return visitor.visitChildren(self)


    class ExistentialContext(AtlExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ATLParser.AtlExprContext
            super().__init__(parser)
            self.group = None # Token
            self.child = None # AtlExprContext
            self.copyFrom(ctx)

        def ATOM(self):
            return self.getToken(ATLParser.ATOM, 0)
        def atlExpr(self):
            return self.getTypedRuleContext(ATLParser.AtlExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExistential" ):
                listener.enterExistential(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExistential" ):
                listener.exitExistential(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExistential" ):
                return visitor.visitExistential(self)
            else:
                return visitor.visitChildren(self)


    class AlwaysContext(AtlExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ATLParser.AtlExprContext
            super().__init__(parser)
            self.child = None # AtlExprContext
            self.copyFrom(ctx)

        def atlExpr(self):
            return self.getTypedRuleContext(ATLParser.AtlExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAlways" ):
                listener.enterAlways(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAlways" ):
                listener.exitAlways(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAlways" ):
                return visitor.visitAlways(self)
            else:
                return visitor.visitChildren(self)


    class ReleaseContext(AtlExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ATLParser.AtlExprContext
            super().__init__(parser)
            self.left = None # AtlExprContext
            self.right = None # AtlExprContext
            self.copyFrom(ctx)

        def atlExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ATLParser.AtlExprContext)
            else:
                return self.getTypedRuleContext(ATLParser.AtlExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelease" ):
                listener.enterRelease(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelease" ):
                listener.exitRelease(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelease" ):
                return visitor.visitRelease(self)
            else:
                return visitor.visitChildren(self)


    class UntilContext(AtlExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ATLParser.AtlExprContext
            super().__init__(parser)
            self.left = None # AtlExprContext
            self.right = None # AtlExprContext
            self.copyFrom(ctx)

        def atlExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ATLParser.AtlExprContext)
            else:
                return self.getTypedRuleContext(ATLParser.AtlExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUntil" ):
                listener.enterUntil(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUntil" ):
                listener.exitUntil(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUntil" ):
                return visitor.visitUntil(self)
            else:
                return visitor.visitChildren(self)



    def atlExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ATLParser.AtlExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_atlExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ATLParser.T__0, ATLParser.T__1]:
                localctx = ATLParser.NegationContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 5
                _la = self._input.LA(1)
                if not(_la==ATLParser.T__0 or _la==ATLParser.T__1):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 6
                localctx.child = self.atlExpr(13)
                pass
            elif token in [ATLParser.T__2, ATLParser.T__3]:
                localctx = ATLParser.NextContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 7
                _la = self._input.LA(1)
                if not(_la==ATLParser.T__2 or _la==ATLParser.T__3):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 8
                localctx.child = self.atlExpr(12)
                pass
            elif token in [ATLParser.T__4, ATLParser.T__5]:
                localctx = ATLParser.EventuallyContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 9
                _la = self._input.LA(1)
                if not(_la==ATLParser.T__4 or _la==ATLParser.T__5):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 10
                localctx.child = self.atlExpr(11)
                pass
            elif token in [ATLParser.T__6, ATLParser.T__7]:
                localctx = ATLParser.AlwaysContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 11
                _la = self._input.LA(1)
                if not(_la==ATLParser.T__6 or _la==ATLParser.T__7):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 12
                localctx.child = self.atlExpr(10)
                pass
            elif token in [ATLParser.T__18]:
                localctx = ATLParser.ExistentialContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 13
                self.match(ATLParser.T__18)
                self.state = 14
                localctx.group = self.match(ATLParser.ATOM)
                self.state = 15
                self.match(ATLParser.T__19)
                self.state = 16
                localctx.child = self.atlExpr(4)
                pass
            elif token in [ATLParser.T__20]:
                localctx = ATLParser.UniversalContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 17
                self.match(ATLParser.T__20)
                self.state = 18
                localctx.group = self.match(ATLParser.ATOM)
                self.state = 19
                self.match(ATLParser.T__21)
                self.state = 20
                localctx.child = self.atlExpr(3)
                pass
            elif token in [ATLParser.T__22]:
                localctx = ATLParser.GroupingContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 21
                self.match(ATLParser.T__22)
                self.state = 22
                self.atlExpr(0)
                self.state = 23
                self.match(ATLParser.T__23)
                pass
            elif token in [ATLParser.ATOM]:
                localctx = ATLParser.EvaluationContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 25
                localctx.child = self.atomExpr()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 45
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 43
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = ATLParser.UntilContext(self, ATLParser.AtlExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_atlExpr)
                        self.state = 28
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 29
                        _la = self._input.LA(1)
                        if not(_la==ATLParser.T__8 or _la==ATLParser.T__9):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 30
                        localctx.right = self.atlExpr(10)
                        pass

                    elif la_ == 2:
                        localctx = ATLParser.ReleaseContext(self, ATLParser.AtlExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_atlExpr)
                        self.state = 31
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 32
                        _la = self._input.LA(1)
                        if not(_la==ATLParser.T__10 or _la==ATLParser.T__11):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 33
                        localctx.right = self.atlExpr(9)
                        pass

                    elif la_ == 3:
                        localctx = ATLParser.ConjunctionContext(self, ATLParser.AtlExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_atlExpr)
                        self.state = 34
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 35
                        _la = self._input.LA(1)
                        if not(_la==ATLParser.T__12 or _la==ATLParser.T__13):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 36
                        localctx.right = self.atlExpr(8)
                        pass

                    elif la_ == 4:
                        localctx = ATLParser.DisjunctionContext(self, ATLParser.AtlExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_atlExpr)
                        self.state = 37
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 38
                        _la = self._input.LA(1)
                        if not(_la==ATLParser.T__14 or _la==ATLParser.T__15):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 39
                        localctx.right = self.atlExpr(7)
                        pass

                    elif la_ == 5:
                        localctx = ATLParser.ImpliesContext(self, ATLParser.AtlExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_atlExpr)
                        self.state = 40
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 41
                        _la = self._input.LA(1)
                        if not(_la==ATLParser.T__16 or _la==ATLParser.T__17):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 42
                        localctx.right = self.atlExpr(6)
                        pass

             
                self.state = 47
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AtomExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ATOM(self):
            return self.getToken(ATLParser.ATOM, 0)

        def getRuleIndex(self):
            return ATLParser.RULE_atomExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomExpr" ):
                listener.enterAtomExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomExpr" ):
                listener.exitAtomExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomExpr" ):
                return visitor.visitAtomExpr(self)
            else:
                return visitor.visitChildren(self)




    def atomExpr(self):

        localctx = ATLParser.AtomExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_atomExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(ATLParser.ATOM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.atlExpr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def atlExpr_sempred(self, localctx:AtlExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 5)
         




