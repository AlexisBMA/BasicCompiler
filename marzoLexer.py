# Generated from c:\Users\bryan\Documents\Semestre Feb-Jun 2022\Compiladores\Parcial 1\Ejercicios\antlr\marzo.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\r")
        buf.write("I\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3")
        buf.write("\6\3\7\3\7\3\7\3\7\3\b\3\b\3\t\6\t\62\n\t\r\t\16\t\63")
        buf.write("\3\n\6\n\67\n\n\r\n\16\n8\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\f\6\fD\n\f\r\f\16\fE\3\f\3\f\2\2\r\3\3\5")
        buf.write("\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\3\2\5\3")
        buf.write("\2c|\3\2\62;\5\2\13\f\17\17\"\"\2K\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2")
        buf.write("\27\3\2\2\2\3\31\3\2\2\2\5\33\3\2\2\2\7\36\3\2\2\2\t#")
        buf.write("\3\2\2\2\13(\3\2\2\2\r*\3\2\2\2\17.\3\2\2\2\21\61\3\2")
        buf.write("\2\2\23\66\3\2\2\2\25:\3\2\2\2\27C\3\2\2\2\31\32\7-\2")
        buf.write("\2\32\4\3\2\2\2\33\34\7k\2\2\34\35\7h\2\2\35\6\3\2\2\2")
        buf.write("\36\37\7v\2\2\37 \7j\2\2 !\7g\2\2!\"\7p\2\2\"\b\3\2\2")
        buf.write("\2#$\7g\2\2$%\7n\2\2%&\7u\2\2&\'\7g\2\2\'\n\3\2\2\2()")
        buf.write("\7@\2\2)\f\3\2\2\2*+\7k\2\2+,\7p\2\2,-\7v\2\2-\16\3\2")
        buf.write("\2\2./\7?\2\2/\20\3\2\2\2\60\62\t\2\2\2\61\60\3\2\2\2")
        buf.write("\62\63\3\2\2\2\63\61\3\2\2\2\63\64\3\2\2\2\64\22\3\2\2")
        buf.write("\2\65\67\t\3\2\2\66\65\3\2\2\2\678\3\2\2\28\66\3\2\2\2")
        buf.write("89\3\2\2\29\24\3\2\2\2:;\7r\2\2;<\7t\2\2<=\7k\2\2=>\7")
        buf.write("p\2\2>?\7v\2\2?@\3\2\2\2@A\5\21\t\2A\26\3\2\2\2BD\t\4")
        buf.write("\2\2CB\3\2\2\2DE\3\2\2\2EC\3\2\2\2EF\3\2\2\2FG\3\2\2\2")
        buf.write("GH\b\f\2\2H\30\3\2\2\2\6\2\638E\3\b\2\2")
        return buf.getvalue()


class marzoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    Var = 8
    Numero = 9
    Print = 10
    WS = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'if'", "'then'", "'else'", "'>'", "'int'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "Var", "Numero", "Print", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "Var", "Numero", "Print", "WS" ]

    grammarFileName = "marzo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


