grammar walnut;
/*
* Lexer Rules
*/

fragment DIGIT : [0-9] ;
fragment LETTER : [a-zA-Z] ;

WS : (' ' | '\t' | '\n' | '\r')* ;

RETURN_T : return ;
INT_T : int ;
FLOAT_T : float ;
STRING_T : string ;
CHAR_T : char ;
BOOLEAN_T : boolean ;
CLASS_T : class ;
IF_T : if ;
ELSEIF_T : elseif ;
ELSE_T : else ;
TRUE_T : true;
FALSE_T : false;
NOT_T : not;

CTE_STRING_T : '"'.*'"' ;
CTE_INT_T : DIGIT+ ;
CTE_FLOAT_T : DIGIT.DIGIT ;
CTE_CHAR_T : '.' ;

ID_T : LETTER(LETTER | '_' | DIGIT)* ;

EQUAL_T : '==' ;
NOT_EQUAL_T : '!=' ;
ASSIGN_T : '=' ;
LESS_EQ_T : '<=' ;
GREATER_EQ_T : '>=' ;
LESS_T : '<' ;
GREATER_T : '>' ;
POW_T : '^' ;
DIVISION_T : '/' ;
MULTI_T : '*' ;
PLUS_T : '+' ;
MINUS_T : '-' ;
AND_OP_T : '&&' ;
OR_OP_T : '||' ;
COMMA_T : ',' ;
NOT_T : '!' ;
LP_T : '(' ;
RP_T : ')' ;
LB_T : '[' ;
RB_T : ']' ;
POINT_T : '.' ;
END_OF_STM_T : ';' ;
