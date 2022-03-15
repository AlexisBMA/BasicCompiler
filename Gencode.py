from operator import truediv
import marzoListener

from collections import deque
vars = {}

if __name__ is not None and "." in __name__:
    from .marzoParser import marzoParser
else:
    from marzoParser import marzoParser

listener = marzoListener.marzoListener
numbers = deque

class ReadNumber(listener):
    def enterPrimaria(self, ctx:marzoParser.PrimariaContext):
        numbers.append(ctx.Numero().getText())
    
class Asignacion(listener):
    def exitAsignacion(self, ctx:marzoParser.AsignacionContext):
        vars.append(ctx.Var().getText(), int(ctx.Numero().getText()))

class Declaracion(listener):
    def exitDeclaracion(self, ctx: marzoParser.DeclaracionContext):
        if ctx.Var().getText() in vars:
            vars[ctx.Var().getText()] = ctx.Number().getText()

class Suma(listener):
    def exitSuma(self, ctx: marzoParser.SumaContext):
        return (numbers.pop() + numbers.pop())

class CompareBiggerThan(listener):
    def exitMayor(self, ctx: marzoParser.MayorContext):
        if numbers.pop() > numbers.pop():
            return True
        else:
            return False

class Print(listener):
    def exitPrint(self, ctx: marzoParser.PrintContext):
        if ctx.Var().getText() != None:
            print(vars[ctx.Var().getText()])
        else: 
            print("Error")


