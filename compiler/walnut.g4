grammar walnut;

@header {
import pprint
from engine import Engine
from operation import Operation
from jump_engine import JumpEngine
}

@members {
global program_engine
global pp
global operation
global jump_eng
program_engine = Engine()
operation = Operation(program_engine)
jump_eng = JumpEngine(program_engine)
pp = pprint.PrettyPrinter(indent=2)
}

program : PROGRAM_T ID_T END_OF_STM_T global_variables? classes* {program_engine.reset_to_global()} functions* START_T {program_engine.register_run_proc()} blocks* FINISH_T {program_engine.register_program_end()} {program_engine.print_quads()} {program_engine.print_classes()} {program_engine.print_main()} ;

global_variables : GLOBALS_T LCB_T declaration_assignment RCB_T ;

classes : CLASS_T ID_T {program_engine.register_class($ID_T.text)} extends {program_engine.reset_context()}
         | CLASS_T ID_T {program_engine.register_class($ID_T.text)} LCB_T class_body RCB_T  {program_engine.reset_context()};

extends : EXTENDS_T ID_T {program_engine.context.class_directory.classes[program_engine.context.class_directory.current_class.name].register_parent_class($ID_T.text)} LCB_T class_body RCB_T;

class_body : class_attributes class_methods ;

class_attributes : ATTRS_T LCB_T (declaration END_OF_STM_T)* RCB_T ;

class_methods : METHODS_T LCB_T initializer {program_engine.register_end_proc()} (method_declaration {program_engine.register_end_proc()})* RCB_T ;

initializer : FUNC_T INIT_T {program_engine.register_function($INIT_T.text)} LP_T parameters? RP_T LCB_T blocks* RCB_T {program_engine.reset_context()} ;

method_declaration : FUNC_T ID_T {program_engine.register_function($ID_T.text)} LP_T parameters? RP_T RETURN_TYPE_T var_type {program_engine.current_context.function_directory.register_return_type($ID_T.text, $var_type.text)} function_body {program_engine.reset_context()}
                    | FUNC_T ID_T {program_engine.register_function($ID_T.text)} LP_T parameters? RP_T function_body_no_return {program_engine.reset_context()};

functions : FUNC_T ID_T {program_engine.register_function($ID_T.text)} LP_T parameters? RP_T RETURN_TYPE_T var_type {program_engine.current_context.function_directory.register_return_type($ID_T.text, $var_type.text)} function_body {program_engine.reset_context()}
            | FUNC_T ID_T {program_engine.register_function($ID_T.text)} LP_T parameters? RP_T function_body_no_return {program_engine.reset_context()};

function_body : LCB_T (blocks)* RETURN_T expression END_OF_STM_T RCB_T;
function_body_no_return : LCB_T (blocks)* RCB_T;

parameters : var_type ID_T {program_engine.current_context.function_directory.register_parameter($var_type.text, $ID_T.text)} COMMA_T parameters
             | var_type ID_T {program_engine.current_context.function_directory.register_parameter($var_type.text, $ID_T.text)};

arguments : argument COMMA_T arguments
            | argument ;

argument : (constants | ID_T) ;

blocks : expression END_OF_STM_T
         | declaration_assignment
         | loops
         | conditional
         | object_declaration
         | write ;

write : PRINT_T LP_T expression RP_T END_OF_STM_T ;

expression : conditional_expression;

conditional_expression : relational_expression {operation.compare_op()} and_or_op  {operation.operator_stack.append($and_or_op.text)} conditional_expression
                         | relational_expression {operation.compare_op()};

relational_expression : math_expression {operation.compare_relational_op()} relop_tokens {operation.operator_stack.append($relop_tokens.text)} relational_expression
                        | math_expression {operation.compare_relational_op()};

math_expression : term {operation.add_substract_op()} plus_minus_op  {operation.operator_stack.append($plus_minus_op.text)} math_expression
                  | term {operation.add_substract_op()};

term : factor {operation.multiply_divide_op()} mult_div_op  {operation.operator_stack.append($mult_div_op.text)} term
       | factor {operation.multiply_divide_op()} ;

factor : power_of {operation.power_of_op()} POW_T  {operation.operator_stack.append($POW_T.text)} factor
         | power_of  {operation.power_of_op()} ;

power_of : atomic
           | LP_T {operation.operator_stack.append('(')}  expression  RP_T {operation.operator_stack.pop()} ;

atomic : (ID_T|constants|call_object_method|call_function|call_array) {operation.add_identifier($ID_T.text, $constants.text, $call_object_method.text, $call_function.text, $call_array.text)};

relop_tokens : EQUAL_T
               | NOT_EQUAL_T
               | LESS_EQ_T
               | GREATER_EQ_T
               | LESS_T
               | GREATER_T ;

declaration_assignment : ((declaration | assignments) END_OF_STM_T)+ ;

declaration : (array_declaration | var_declaration ) ;

array_declaration : var_type ID_T LB_T CTE_INT_T RB_T {program_engine.register_variable($var_type.text, $ID_T.text)};

var_declaration : var_type ID_T {program_engine.register_variable($var_type.text, $ID_T.text)};

assignments : (array_assignment | var_assignment) ;

array_assignment : (var_type)? ID_T LB_T CTE_INT_T RB_T ASSIGN_T expression {program_engine.register_variable($var_type.text, $ID_T.text, $expression.text)};

var_assignment : (var_type)? ID_T ASSIGN_T expression {program_engine.register_variable($var_type.text, $ID_T.text, None)}{operation.assign_operation($ID_T.text)};

loops : WHILE_T LP_T {jump_eng.insert_jump()} expression {jump_eng.register_conditional()} RP_T LCB_T blocks* {jump_eng.fill_gotof()}RCB_T ;

conditional : IF_T if_body (ELSEIF_T else_if_body)* ELSE_T  LCB_T blocks* {jump_eng.fill_gotos()} RCB_T ;

if_body: LP_T expression RP_T {jump_eng.register_conditional()} LCB_T blocks* {jump_eng.register_goto()} RCB_T ;

else_if_body: LP_T expression RP_T {jump_eng.register_elseif()} LCB_T blocks* {jump_eng.register_goto()} RCB_T ;

object_declaration : ID_T ID_T ASSIGN_T ID_T POINT_T NEW_T LP_T arguments? RP_T END_OF_STM_T;

call_object_method : ID_T POINT_T ID_T LP_T arguments? RP_T;

call_function : ID_T LP_T arguments? RP_T ;

call_array : ID_T LB_T CTE_INT_T RB_T ;

var_type : INT_T|STRING_T|FLOAT_T|BOOLEAN_T ;

constants : CTE_FLOAT_T
            |CTE_INT_T
            |CTE_STRING_T
            |TRUE_T
            |FALSE_T ;
and_or_op: (OR_OP_T | AND_OP_T) ;
mult_div_op : (MULTI_T|DIVISION_T) ;
plus_minus_op : (PLUS_T | MINUS_T) ;


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
START_T : 'run' ;
FINISH_T : 'end' ;
PRINT_T : 'puts' ;

EQUAL_T : '=='|'is' ;
NOT_T : '!'|'not' ;
AND_OP_T : '&&'|'and' ;
OR_OP_T : '||'|'or' ;

WS : [ \t\r\n] -> skip ;

CTE_STRING_T : '"'.*?'"' ;
CTE_FLOAT_T : (DIGIT)+POINT_T(DIGIT)+ ;
CTE_INT_T : DIGIT+ ;

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
