from GrammarVisitor import GrammarVisistor
from GrammarParser import GrammarParser

class MyVisitor(GrammarVisistor):
    #Definimos la memomoria o el entorno
    def _init__(self):
        self.memory={}
        
        
    #Definimosla assignacion
    def visitAssingn(self,ctx):
        #se ostiene el id o el nombre de la variable
        name=ctx.ID().getText()
         #se obtiene el valo, ya sea un valor numerico o una expresion
        value=self.visit(ctx.expr())
        #se almacena en memomoria a aprtir del nombre y el valor 
        self.memory[name]=value
        
    #Definimos la imprecion
    def visitPrint(self,ctx):
        #Defiimos la exprecion que se desea mostrar
        value=self.visit(ctx.expr())
        print(value)
        
    #Definimos las expresiones     
    def visitExpr(self,ctx):
        #Busca si existen IDs
        if ctx.ID():
            #Odtiene del contexto el nombre de la variable
            name=ctx.ID().getText()
            #Si el nombre de la variable no esta , lanza un error
            if name not in self.memory:
                raise NameError(f"Variable'{name}'no definida")
            #Si existee el nombre retorna la varable
            return self.memory[name]
        #Busca el operador 
        elif ctx.op:
            #Visita y odtiene lado izquierda 
            left=self.visit(ctx.expr(0))
            #Visita y odtiene lado derecho
            right=self.visit(ctx.expr(1))
            #Evalua la operacion a realizar
            if ctx.op.text=="+":
                return left + right
            if ctx.op.text=="-":
                return left - right
            if ctx.op.text=="*":
                return left * right
            if ctx.op.text=="/":
                #Verifca la divicion de cero
                if right==0:
                    raise ValueError("Divicion por cero")
                return left / right