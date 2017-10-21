grammar walnut;

program : PROGRAM_T ID_T global_variables? classes* functions* blocks*;

global_variables : GLOBALS_T LCB_T declaration_assignment RCB_T ;

classes : (CLASS_T ID_T (EXTENDS_T ID_T)? LCB_T class_body RCB_T) ;

class_body : class_attributes class_methods ;

class_attributes : ATTRS_T LCB_T declaration_assignment RCB_T ;

class_methods : METHODS_T LCB_T initializer method_declaration+ RCB_T ;

initializer : FUNC_T INIT_T LP_T parameters? RP_T LCB_T blocks* RCB_T ;

method_declaration : FUNC_T ID_T LP_T parameters? RP_T (RETURN_TYPE_T var_type)? LCB_T blocks* (RETURN_T expression)? RCB_T;

functions : (FUNC_T ID_T LP_T parameters? RP_T (RETURN_TYPE_T var_type)? LCB_T blocks* (RETURN_T expression)? RCB_T)+ ;

parameters : var_type ID_T COMMA_T parameters
             | var_type ID_T ;

blocks : expression | declaration_assignment | loops | conditional | object_declaration;

expression : conditional_expression ;

conditional_expression : relational_expression (OR_OP_T | AND_OP_T) conditional_expression
                        | relational_expression ;

relational_expression : math_expression relop_tokens relational_expression
                        | math_expression ;

math_expression : term (PLUS_T | MINUS_T) math_expression | term;

term : factor (MULTI_T|DIVISION_T) term | factor;

factor : power_of POW_T factor | power_of ;

power_of : (MINUS_T|NOT_T)? (ID_T|constants|call_object_method|LP_T expression RP_T) ;

relop_tokens : EQUAL_T | NOT_EQUAL_T | LESS_EQ_T | GREATER_EQ_T | LESS_T | GREATER_T ;

declaration_assignment : (declaration|assignments)+;

assignments : ID_T ASSIGN_T expression ;

declaration : var_type ID_T ;

loops : WHILE_T LP_T expression RP_T LCB_T blocks* RCB_T ;

conditional : IF_T if_elsif_body (ELSEIF_T if_elsif_body)+ ELSE_T LCB_T blocks* RCB_T ;

if_elsif_body : LP_T expression RP_T LCB_T blocks* RCB_T ;

object_declaration : ID_T ID_T ASSIGN_T ID_T POINT_T NEW_T LP_T parameters? RP_T ;

call_object_method : ID_T POINT_T ID_T LP_T parameters RP_T ;

var_type : INT_T|STRING_T|FLOAT_T|BOOLEAN_T ;

constants : CTE_FLOAT_T|CTE_INT_T|CTE_STRING_T|CTE_BOOL_T ;

/*
* Lexer Rules
*/

fragment DIGIT : [0-9] ;
fragment LETTER : [a-zA-Z] ;

PROGRAM_T : 'program';
GLOBALS_T : 'globals';
RETURN_T : 'return' ;
INT_T : 'int' ;
FLOAT_T : 'float' ;
STRING_T : 'string' ;
BOOLEAN_T : 'boolean' ;
CLASS_T : 'class' ;
EXTENDS_T : 'extends' ;
IF_T : 'if' ;
ELSEIF_T : 'elseif' ;
ELSE_T : 'else' ;
TRUE_T : 'true' ;
FALSE_T : 'false' ;
ATTRS_T : 'attributes' ;
METHODS_T : 'methods' ;
FUNC_T : 'func' ;
INIT_T : 'initializer' ;
WHILE_T : 'while';
NEW_T : 'new';

EQUAL_T : '=='|'is' ;
NOT_T : '!'|'not' ;
AND_OP_T : '&&'|'and' ;
OR_OP_T : '||'|'or' ;

WS : [ \t\r\n] -> skip ;

CTE_STRING_T : '"'.*?'"' ;
CTE_INT_T : DIGIT+ ;
CTE_FLOAT_T : DIGIT.DIGIT ;
CTE_BOOL_T : TRUE_T|FALSE_T ;

ID_T : LETTER(LETTER | '_' | DIGIT)* ;

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
COMMA_T : ',' ;
LP_T : '(' ;
RP_T : ')' ;
LB_T : '[' ;
RB_T : ']' ;
LCB_T : '{' ;
RCB_T : '}' ;
POINT_T : '.' ;
END_OF_STM_T : ';' ;
RETURN_TYPE_T : ':' ;
