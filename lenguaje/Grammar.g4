grammar Grammar;

program:(if_statement NEWLINE)*EOF;

statement: assing | print | if_statement | for_staement;

/*Definimos la asignacion*/ 
assing:ID'='expr;

/*Definimos print*/ 
print:'print''('expr')';

/*Definimos if*/ 
if_statement:'if''('expr')'block;

/*Definimos for*/ 
for_staement:'for''('assing';'expr';'assing')'block;

/*Definimos block*/ 

block:'{'(statement NEWLINE)*']';

/*Definimos expr*/
expr:expr op=('*'|'/')expr
   | expr op=('+'|'-')expr
   | expr op=('>'|'<'|'>='|'=<')expr
   | expr op=('=='|'!=')expr
   | ID
   |'('expr')'
   ;

/*Definimos de elementos finales*/

ID:[a-zA-Z][a-zA-Z_0-9]*;
NEWLINE:[\r\n];
WS:[\t]->skip;
SEMI:';';



