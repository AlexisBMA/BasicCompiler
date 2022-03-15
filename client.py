from antlr import *
import sys

def GenCode(marzoListener):
    def enterProgram(self, ctx:marzoParser.ProgramContext):
        print(".text")

    def exitPrimaria(self, ctx:marzoParser.PrimariaContext):
        print("load $1, " + ctx.Numero)

    def exitSuma(self, ctx:marzoParser.SumaContext):
        print("load $1, " + ctx.Numero)

def main(): 
    parser = marzoParser(CommonTokenStream(marzoLexer(FileStream("input.txt"))))
    tree = parser.program()
    declarations = DeclareListener()


    gencode = GenCode()
    walker = ParseTreeWalker()
    walker.walk(declarations, tree)

if __name__ == '__main__':
    main()