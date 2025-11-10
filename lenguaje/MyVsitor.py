from GrammarVisitor import GrammarVisistor
from GrammarParser import GrammarParser

class MyVisitor(GrammarVisistor):
    def _init__(self):
        self.memory={}
    #Definimosla assignacion
    def visitAssingn(self,ctx):
        name=ctx.ID().getText()
        value=self.visit(ctx.expr())
        self.memory[name]=value
        #Definimos la assignacion
    def visitPRINT(SELF,CTX):
        value=self.visit(ctx.expr())
        print(value)