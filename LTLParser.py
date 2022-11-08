# Generated from LTL.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\30")
        buf.write("-\4\2\t\2\4\3\t\3\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\5\2\25\n\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\7\2&\n\2\f\2\16")
        buf.write("\2)\13\2\3\3\3\3\3\3\2\3\2\4\2\4\2\13\3\2\3\4\3\2\5\6")
        buf.write("\3\2\7\b\3\2\t\n\3\2\13\f\3\2\r\16\3\2\17\20\3\2\21\22")
        buf.write("\3\2\23\24\2\64\2\24\3\2\2\2\4*\3\2\2\2\6\7\b\2\1\2\7")
        buf.write("\b\t\2\2\2\b\25\5\2\2\r\t\n\t\3\2\2\n\25\5\2\2\f\13\f")
        buf.write("\t\4\2\2\f\25\5\2\2\13\r\16\t\5\2\2\16\25\5\2\2\n\17\20")
        buf.write("\7\25\2\2\20\21\5\2\2\2\21\22\7\26\2\2\22\25\3\2\2\2\23")
        buf.write("\25\5\4\3\2\24\6\3\2\2\2\24\t\3\2\2\2\24\13\3\2\2\2\24")
        buf.write("\r\3\2\2\2\24\17\3\2\2\2\24\23\3\2\2\2\25\'\3\2\2\2\26")
        buf.write("\27\f\t\2\2\27\30\t\6\2\2\30&\5\2\2\n\31\32\f\b\2\2\32")
        buf.write("\33\t\7\2\2\33&\5\2\2\t\34\35\f\7\2\2\35\36\t\b\2\2\36")
        buf.write("&\5\2\2\b\37 \f\6\2\2 !\t\t\2\2!&\5\2\2\7\"#\f\5\2\2#")
        buf.write("$\t\n\2\2$&\5\2\2\6%\26\3\2\2\2%\31\3\2\2\2%\34\3\2\2")
        buf.write("\2%\37\3\2\2\2%\"\3\2\2\2&)\3\2\2\2\'%\3\2\2\2\'(\3\2")
        buf.write("\2\2(\3\3\2\2\2)\'\3\2\2\2*+\7\27\2\2+\5\3\2\2\2\5\24")
        buf.write("%\'")
        return buf.getvalue()


class LTLParser ( Parser ):

    grammarFileName = "LTL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'!'", "'not'", "'next'", "'X'", "'eventually'", 
                     "'F'", "'always'", "'G'", "'until'", "'U'", "'release'", 
                     "'R'", "'&&'", "'and'", "'||'", "'or'", "'->'", "'implies'", 
                     "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ATOM", "WS" ]

    RULE_ltlExpr = 0
    RULE_atomExpr = 1

    ruleNames =  [ "ltlExpr", "atomExpr" ]

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
    ATOM=21
    WS=22

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class LtlExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LTLParser.RULE_ltlExpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class EvaluationContext(LtlExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LTLParser.LtlExprContext
            super().__init__(parser)
            self.child = None # AtomExprContext
            self.copyFrom(ctx)

        def atomExpr(self):
            return self.getTypedRuleContext(LTLParser.AtomExprContext,0)


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


    class DisjunctionContext(LtlExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LTLParser.LtlExprContext
            super().__init__(parser)
            self.left = None # LtlExprContext
            self.right = None # LtlExprContext
            self.copyFrom(ctx)

        def ltlExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LTLParser.LtlExprContext)
            else:
                return self.getTypedRuleContext(LTLParser.LtlExprContext,i)


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


    class ImpliesContext(LtlExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LTLParser.LtlExprContext
            super().__init__(parser)
            self.left = None # LtlExprContext
            self.right = None # LtlExprContext
            self.copyFrom(ctx)

        def ltlExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LTLParser.LtlExprContext)
            else:
                return self.getTypedRuleContext(LTLParser.LtlExprContext,i)


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


    class NegationContext(LtlExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LTLParser.LtlExprContext
            super().__init__(parser)
            self.child = None # LtlExprContext
            self.copyFrom(ctx)

        def ltlExpr(self):
            return self.getTypedRuleContext(LTLParser.LtlExprContext,0)


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


    class NextContext(LtlExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LTLParser.LtlExprContext
            super().__init__(parser)
            self.child = None # LtlExprContext
            self.copyFrom(ctx)

        def ltlExpr(self):
            return self.getTypedRuleContext(LTLParser.LtlExprContext,0)


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


    class EventuallyContext(LtlExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LTLParser.LtlExprContext
            super().__init__(parser)
            self.child = None # LtlExprContext
            self.copyFrom(ctx)

        def ltlExpr(self):
            return self.getTypedRuleContext(LTLParser.LtlExprContext,0)


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


    class ConjunctionContext(LtlExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LTLParser.LtlExprContext
            super().__init__(parser)
            self.left = None # LtlExprContext
            self.right = None # LtlExprContext
            self.copyFrom(ctx)

        def ltlExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LTLParser.LtlExprContext)
            else:
                return self.getTypedRuleContext(LTLParser.LtlExprContext,i)


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


    class GroupingContext(LtlExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LTLParser.LtlExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ltlExpr(self):
            return self.getTypedRuleContext(LTLParser.LtlExprContext,0)


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


    class AlwaysContext(LtlExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LTLParser.LtlExprContext
            super().__init__(parser)
            self.child = None # LtlExprContext
            self.copyFrom(ctx)

        def ltlExpr(self):
            return self.getTypedRuleContext(LTLParser.LtlExprContext,0)


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


    class ReleaseContext(LtlExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LTLParser.LtlExprContext
            super().__init__(parser)
            self.left = None # LtlExprContext
            self.right = None # LtlExprContext
            self.copyFrom(ctx)

        def ltlExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LTLParser.LtlExprContext)
            else:
                return self.getTypedRuleContext(LTLParser.LtlExprContext,i)


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


    class UntilContext(LtlExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LTLParser.LtlExprContext
            super().__init__(parser)
            self.left = None # LtlExprContext
            self.right = None # LtlExprContext
            self.copyFrom(ctx)

        def ltlExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LTLParser.LtlExprContext)
            else:
                return self.getTypedRuleContext(LTLParser.LtlExprContext,i)


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



    def ltlExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LTLParser.LtlExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_ltlExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LTLParser.T__0, LTLParser.T__1]:
                localctx = LTLParser.NegationContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 5
                _la = self._input.LA(1)
                if not(_la==LTLParser.T__0 or _la==LTLParser.T__1):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 6
                localctx.child = self.ltlExpr(11)
                pass
            elif token in [LTLParser.T__2, LTLParser.T__3]:
                localctx = LTLParser.NextContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 7
                _la = self._input.LA(1)
                if not(_la==LTLParser.T__2 or _la==LTLParser.T__3):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 8
                localctx.child = self.ltlExpr(10)
                pass
            elif token in [LTLParser.T__4, LTLParser.T__5]:
                localctx = LTLParser.EventuallyContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 9
                _la = self._input.LA(1)
                if not(_la==LTLParser.T__4 or _la==LTLParser.T__5):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 10
                localctx.child = self.ltlExpr(9)
                pass
            elif token in [LTLParser.T__6, LTLParser.T__7]:
                localctx = LTLParser.AlwaysContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 11
                _la = self._input.LA(1)
                if not(_la==LTLParser.T__6 or _la==LTLParser.T__7):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 12
                localctx.child = self.ltlExpr(8)
                pass
            elif token in [LTLParser.T__18]:
                localctx = LTLParser.GroupingContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 13
                self.match(LTLParser.T__18)
                self.state = 14
                self.ltlExpr(0)
                self.state = 15
                self.match(LTLParser.T__19)
                pass
            elif token in [LTLParser.ATOM]:
                localctx = LTLParser.EvaluationContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 17
                localctx.child = self.atomExpr()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 37
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 35
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = LTLParser.UntilContext(self, LTLParser.LtlExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_ltlExpr)
                        self.state = 20
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 21
                        _la = self._input.LA(1)
                        if not(_la==LTLParser.T__8 or _la==LTLParser.T__9):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 22
                        localctx.right = self.ltlExpr(8)
                        pass

                    elif la_ == 2:
                        localctx = LTLParser.ReleaseContext(self, LTLParser.LtlExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_ltlExpr)
                        self.state = 23
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 24
                        _la = self._input.LA(1)
                        if not(_la==LTLParser.T__10 or _la==LTLParser.T__11):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 25
                        localctx.right = self.ltlExpr(7)
                        pass

                    elif la_ == 3:
                        localctx = LTLParser.ConjunctionContext(self, LTLParser.LtlExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_ltlExpr)
                        self.state = 26
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 27
                        _la = self._input.LA(1)
                        if not(_la==LTLParser.T__12 or _la==LTLParser.T__13):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 28
                        localctx.right = self.ltlExpr(6)
                        pass

                    elif la_ == 4:
                        localctx = LTLParser.DisjunctionContext(self, LTLParser.LtlExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_ltlExpr)
                        self.state = 29
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 30
                        _la = self._input.LA(1)
                        if not(_la==LTLParser.T__14 or _la==LTLParser.T__15):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 31
                        localctx.right = self.ltlExpr(5)
                        pass

                    elif la_ == 5:
                        localctx = LTLParser.ImpliesContext(self, LTLParser.LtlExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_ltlExpr)
                        self.state = 32
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 33
                        _la = self._input.LA(1)
                        if not(_la==LTLParser.T__16 or _la==LTLParser.T__17):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 34
                        localctx.right = self.ltlExpr(4)
                        pass

             
                self.state = 39
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
            return self.getToken(LTLParser.ATOM, 0)

        def getRuleIndex(self):
            return LTLParser.RULE_atomExpr

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

        localctx = LTLParser.AtomExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_atomExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(LTLParser.ATOM)
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
        self._predicates[0] = self.ltlExpr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def ltlExpr_sempred(self, localctx:LtlExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         




