# Generated from c:\Users\bryan\Documents\Semestre Feb-Jun 2022\Compiladores\Parcial 1\Ejercicios\antlr\marzo.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .marzoParser import marzoParser
else:
    from marzoParser import marzoParser

# This class defines a complete listener for a parse tree produced by marzoParser.
class marzoListener(ParseTreeListener):

    # Enter a parse tree produced by marzoParser#program.
    def enterProgram(self, ctx:marzoParser.ProgramContext):
        pass

    # Exit a parse tree produced by marzoParser#program.
    def exitProgram(self, ctx:marzoParser.ProgramContext):
        pass


    # Enter a parse tree produced by marzoParser#suma.
    def enterSuma(self, ctx:marzoParser.SumaContext):
        pass

    # Exit a parse tree produced by marzoParser#suma.
    def exitSuma(self, ctx:marzoParser.SumaContext):
        pass


    # Enter a parse tree produced by marzoParser#primaria.
    def enterPrimaria(self, ctx:marzoParser.PrimariaContext):
        pass

    # Exit a parse tree produced by marzoParser#primaria.
    def exitPrimaria(self, ctx:marzoParser.PrimariaContext):
        pass


    # Enter a parse tree produced by marzoParser#if.
    def enterIf(self, ctx:marzoParser.IfContext):
        pass

    # Exit a parse tree produced by marzoParser#if.
    def exitIf(self, ctx:marzoParser.IfContext):
        pass


    # Enter a parse tree produced by marzoParser#asignacion.
    def enterAsignacion(self, ctx:marzoParser.AsignacionContext):
        pass

    # Exit a parse tree produced by marzoParser#asignacion.
    def exitAsignacion(self, ctx:marzoParser.AsignacionContext):
        pass


    # Enter a parse tree produced by marzoParser#declaracion.
    def enterDeclaracion(self, ctx:marzoParser.DeclaracionContext):
        pass

    # Exit a parse tree produced by marzoParser#declaracion.
    def exitDeclaracion(self, ctx:marzoParser.DeclaracionContext):
        pass


    # Enter a parse tree produced by marzoParser#mayor.
    def enterMayor(self, ctx:marzoParser.MayorContext):
        pass

    # Exit a parse tree produced by marzoParser#mayor.
    def exitMayor(self, ctx:marzoParser.MayorContext):
        pass


    # Enter a parse tree produced by marzoParser#print.
    def enterPrint(self, ctx:marzoParser.PrintContext):
        pass

    # Exit a parse tree produced by marzoParser#print.
    def exitPrint(self, ctx:marzoParser.PrintContext):
        pass


    # Enter a parse tree produced by marzoParser#dec.
    def enterDec(self, ctx:marzoParser.DecContext):
        pass

    # Exit a parse tree produced by marzoParser#dec.
    def exitDec(self, ctx:marzoParser.DecContext):
        pass


    # Enter a parse tree produced by marzoParser#asig.
    def enterAsig(self, ctx:marzoParser.AsigContext):
        pass

    # Exit a parse tree produced by marzoParser#asig.
    def exitAsig(self, ctx:marzoParser.AsigContext):
        pass



del marzoParser