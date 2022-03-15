# Generated from c:\Users\bryan\Documents\Semestre Feb-Jun 2022\Compiladores\Parcial 1\Ejercicios\antlr\marzo.g4 by ANTLR 4.9.3
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\r")
        buf.write("\65\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\6\2\16")
        buf.write("\n\2\r\2\16\2\17\3\3\3\3\3\3\3\3\3\3\3\3\7\3\30\n\3\f")
        buf.write("\3\16\3\33\13\3\3\4\3\4\3\4\3\4\3\4\3\4\5\4#\n\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\5\4,\n\4\3\5\3\5\3\5\3\6\3\6\3")
        buf.write("\6\3\6\3\6\2\3\4\7\2\4\6\b\n\2\2\2\66\2\r\3\2\2\2\4\21")
        buf.write("\3\2\2\2\6+\3\2\2\2\b-\3\2\2\2\n\60\3\2\2\2\f\16\5\4\3")
        buf.write("\2\r\f\3\2\2\2\16\17\3\2\2\2\17\r\3\2\2\2\17\20\3\2\2")
        buf.write("\2\20\3\3\2\2\2\21\22\b\3\1\2\22\23\7\13\2\2\23\31\3\2")
        buf.write("\2\2\24\25\f\4\2\2\25\26\7\3\2\2\26\30\5\4\3\5\27\24\3")
        buf.write("\2\2\2\30\33\3\2\2\2\31\27\3\2\2\2\31\32\3\2\2\2\32\5")
        buf.write("\3\2\2\2\33\31\3\2\2\2\34\35\7\4\2\2\35\36\5\4\3\2\36")
        buf.write("\37\7\5\2\2\37\"\5\6\4\2 !\7\6\2\2!#\5\6\4\2\" \3\2\2")
        buf.write("\2\"#\3\2\2\2#,\3\2\2\2$,\5\n\6\2%,\5\b\5\2&\'\5\4\3\2")
        buf.write("\'(\7\7\2\2()\5\4\3\2),\3\2\2\2*,\7\f\2\2+\34\3\2\2\2")
        buf.write("+$\3\2\2\2+%\3\2\2\2+&\3\2\2\2+*\3\2\2\2,\7\3\2\2\2-.")
        buf.write("\7\b\2\2./\7\n\2\2/\t\3\2\2\2\60\61\7\n\2\2\61\62\7\t")
        buf.write("\2\2\62\63\7\13\2\2\63\13\3\2\2\2\6\17\31\"+")
        return buf.getvalue()


class marzoParser ( Parser ):

    grammarFileName = "marzo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'if'", "'then'", "'else'", "'>'", 
                     "'int'", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "Var", "Numero", "Print", "WS" ]

    RULE_program = 0
    RULE_expression = 1
    RULE_statement = 2
    RULE_dec = 3
    RULE_asig = 4

    ruleNames =  [ "program", "expression", "statement", "dec", "asig" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    Var=8
    Numero=9
    Print=10
    WS=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(marzoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(marzoParser.ExpressionContext,i)


        def getRuleIndex(self):
            return marzoParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = marzoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.expression(0)
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==marzoParser.Numero):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return marzoParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class SumaContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(marzoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(marzoParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuma" ):
                listener.enterSuma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuma" ):
                listener.exitSuma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuma" ):
                return visitor.visitSuma(self)
            else:
                return visitor.visitChildren(self)


    class PrimariaContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Numero(self):
            return self.getToken(marzoParser.Numero, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaria" ):
                listener.enterPrimaria(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaria" ):
                listener.exitPrimaria(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaria" ):
                return visitor.visitPrimaria(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = marzoParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = marzoParser.PrimariaContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 16
            self.match(marzoParser.Numero)
            self._ctx.stop = self._input.LT(-1)
            self.state = 23
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = marzoParser.SumaContext(self, marzoParser.ExpressionContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 18
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 19
                    self.match(marzoParser.T__0)
                    self.state = 20
                    self.expression(3) 
                self.state = 25
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return marzoParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AsignacionContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def asig(self):
            return self.getTypedRuleContext(marzoParser.AsigContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)


    class PrintContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Print(self):
            return self.getToken(marzoParser.Print, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)


    class DeclaracionContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def dec(self):
            return self.getTypedRuleContext(marzoParser.DecContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion" ):
                listener.enterDeclaracion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion" ):
                listener.exitDeclaracion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracion" ):
                return visitor.visitDeclaracion(self)
            else:
                return visitor.visitChildren(self)


    class MayorContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(marzoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(marzoParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMayor" ):
                listener.enterMayor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMayor" ):
                listener.exitMayor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMayor" ):
                return visitor.visitMayor(self)
            else:
                return visitor.visitChildren(self)


    class IfContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(marzoParser.ExpressionContext,0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(marzoParser.StatementContext)
            else:
                return self.getTypedRuleContext(marzoParser.StatementContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf" ):
                listener.enterIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf" ):
                listener.exitIf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf" ):
                return visitor.visitIf(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = marzoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 41
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [marzoParser.T__1]:
                localctx = marzoParser.IfContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.match(marzoParser.T__1)
                self.state = 27
                self.expression(0)
                self.state = 28
                self.match(marzoParser.T__2)
                self.state = 29
                self.statement()
                self.state = 32
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 30
                    self.match(marzoParser.T__3)
                    self.state = 31
                    self.statement()


                pass
            elif token in [marzoParser.Var]:
                localctx = marzoParser.AsignacionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.asig()
                pass
            elif token in [marzoParser.T__5]:
                localctx = marzoParser.DeclaracionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 35
                self.dec()
                pass
            elif token in [marzoParser.Numero]:
                localctx = marzoParser.MayorContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 36
                self.expression(0)
                self.state = 37
                self.match(marzoParser.T__4)
                self.state = 38
                self.expression(0)
                pass
            elif token in [marzoParser.Print]:
                localctx = marzoParser.PrintContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 40
                self.match(marzoParser.Print)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Var(self):
            return self.getToken(marzoParser.Var, 0)

        def getRuleIndex(self):
            return marzoParser.RULE_dec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDec" ):
                listener.enterDec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDec" ):
                listener.exitDec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDec" ):
                return visitor.visitDec(self)
            else:
                return visitor.visitChildren(self)




    def dec(self):

        localctx = marzoParser.DecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_dec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(marzoParser.T__5)
            self.state = 44
            self.match(marzoParser.Var)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsigContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Var(self):
            return self.getToken(marzoParser.Var, 0)

        def Numero(self):
            return self.getToken(marzoParser.Numero, 0)

        def getRuleIndex(self):
            return marzoParser.RULE_asig

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsig" ):
                listener.enterAsig(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsig" ):
                listener.exitAsig(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsig" ):
                return visitor.visitAsig(self)
            else:
                return visitor.visitChildren(self)




    def asig(self):

        localctx = marzoParser.AsigContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_asig)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(marzoParser.Var)
            self.state = 47
            self.match(marzoParser.T__6)
            self.state = 48
            self.match(marzoParser.Numero)
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
        self._predicates[1] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




