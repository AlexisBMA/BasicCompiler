grammar marzo;

program : expression+ ;

expression: 
    expression '+' expression   #suma
    | Numero                    #primaria
    ; 


statement: 
    'if' expression 'then' statement ('else' statement) ?   #if
    | asig                                                  #asignacion
    | dec                                                   #declaracion
    | expression '>' expression                             #mayor
    | Print                                                 #print
    ; 

dec : 'int' Var; 
asig : Var '=' Numero;
Var : [a-z]+;
Numero : [0-9]+;
Print: 'print' Var;

WS: [ \t\n\r] + -> skip;