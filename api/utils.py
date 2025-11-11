from antlr4 import*
from lenguaje.GrammarLexer import GrammarLexer
from lenguaje.GrammarParser import GrammarParser
from lenguaje.MyVisitor import MyVisitor

import io
import sys
import json

#Definimos nuesto metodo para ejecutar las insytrucciones 
def run_code(code:str):
    input_stream=InputStream(code)
    lexer=GrammarLexer(input_stream)
    stream=CommonTokenStream(lexer)
    parser=GrammarParser(stream)
    tree=parser.program()
    
    #Captura la salida
    old_stdout=sys.stdout()
    buf=io.StringIO()
    sys=stdout=buf
    
    #Creamos un odjecto a nuestro visitor
    visitor=MyVisitor()
    #Visitamos el arbol con nuestro visitor
    visitor.visitor(tree)
    #Capturamos la salida
    output=buf.getvalue()
    
    return output