grammar walnut;

@header {
import pprint
import sys
from engine import Engine
from operation import Operation
from jump_engine import JumpEngine
from structures_engine import StructuresEngine
}

@members {
global program_engine
global pp
global operation
global jump_eng
global structures_engine
program_engine = Engine()
operation = Operation(program_engine)
jump_eng = JumpEngine(program_engine,operation)
structures_engine = StructuresEngine(program_engine)
pp = pprint.PrettyPrinter(indent=2)

}

program : PROGRAM_T ID_T END_OF_STM_T {program_engine.insert_first_cuad()} classes* {program_engine.reset_to_global()} global_variables? (functions {program_engine.register_end_proc()})* START_T {program_engine.register_run_proc()} blocks* FINISH_T {program_engine.register_program_end()} {program_engine.write_quads()};
finally {exit}

global_variables : GLOBALS_T LCB_T {program_engine.set_global_environment()} declaration_assignment RCB_T {program_engine.remove_global_enviroment()};

classes : CLASS_T ID_T {program_engine.register_class($ID_T.text)} extends {program_engine.reset_context()}
         | CLASS_T ID_T {program_engine.register_class($ID_T.text)} LCB_T class_body RCB_T  {program_engine.reset_context()};

extends : EXTENDS_T ID_T {program_engine.context.class_directory.classes[program_engine.context.class_directory.current_class.name].register_parent_class($ID_T.text)} LCB_T class_body RCB_T;

class_body : class_attributes class_methods ;

class_attributes : ATTRS_T LCB_T (declaration END_OF_STM_T)* RCB_T ;

class_methods : METHODS_T LCB_T initializer {program_engine.register_end_proc()} (method_declaration {program_engine.register_end_proc()})* RCB_T ;

initializer : FUNC_T INIT_T {program_engine.register_function($INIT_T.text)} LP_T parameters? {operation.reset_parameter_counter()} RP_T LCB_T blocks* RCB_T {program_engine.reset_context()} ;

method_declaration : FUNC_T ID_T {program_engine.register_function($ID_T.text)} LP_T parameters? RP_T {operation.reset_parameter_counter()} RETURN_TYPE_T var_type {program_engine.register_function_return_type($ID_T.text, $var_type.text)} function_body {program_engine.register_return($ID_T.text,operation.identifier_stack[-1],operation.type_stack[-1])} {program_engine.reset_context()}
                    | FUNC_T ID_T {program_engine.register_function($ID_T.text)} LP_T parameters? RP_T {operation.reset_parameter_counter()} function_body_no_return {program_engine.reset_context()};

functions : FUNC_T ID_T {program_engine.register_function($ID_T.text)} LP_T parameters? RP_T {operation.reset_parameter_counter()} RETURN_TYPE_T var_type {program_engine.register_function_return_type($ID_T.text, $var_type.text)} function_body {program_engine.register_return($ID_T.text,operation.identifier_stack[-1],operation.type_stack[-1])} {program_engine.reset_context()}
            | FUNC_T ID_T {program_engine.register_function($ID_T.text)} LP_T parameters? RP_T {operation.reset_parameter_counter()} function_body_no_return {program_engine.reset_context()};

function_body : LCB_T (blocks)* RETURN_T expression END_OF_STM_T RCB_T;
function_body_no_return : LCB_T (blocks)* RCB_T;

parameters : var_type ID_T {operation.register_parameter($var_type.text, $ID_T.text)} COMMA_T parameters
             | var_type ID_T {operation.register_parameter($var_type.text, $ID_T.text)};

arguments : argument {operation.function_argument_validation()} COMMA_T arguments
            | argument {operation.function_argument_validation()};

obj_arguments : argument {operation.method_argument_validation()} COMMA_T obj_arguments
                | argument {operation.method_argument_validation()} ;

argument : expression ;

blocks : expression END_OF_STM_T
         | declaration_assignment
         | loops
         | conditional
         | object_declaration END_OF_STM_T
         | write
         | read ;

conditional_blocks: expression END_OF_STM_T
                   | (assignments END_OF_STM_T)+
                   | loops
                   | conditional
                   | write
                   | read ;

write : PRINT_T LP_T write_aux RP_T END_OF_STM_T;

write_aux: expression {operation.register_print()} COMMA_T write_aux
          | expression {operation.register_print()};

read: READ_T LP_T read_aux RP_T END_OF_STM_T;

read_aux: CTE_STRING_T COMMA_T ID_T {operation.register_read($CTE_STRING_T.text, $ID_T.text)};

loops : WHILE_T LP_T {jump_eng.insert_jump()} expression {operation.verify_boolean()} {jump_eng.register_conditional()} RP_T LCB_T conditional_blocks* RCB_T {jump_eng.fill_gotof()} ;

conditional : IF_T if_body (ELSEIF_T else_if_body)* ELSE_T LCB_T conditional_blocks* {jump_eng.fill_gotos()} RCB_T ;

if_body: LP_T expression {operation.verify_boolean()} RP_T {jump_eng.register_conditional()} LCB_T conditional_blocks* {jump_eng.register_goto()} RCB_T ;

else_if_body: LP_T expression {operation.verify_boolean()} RP_T {jump_eng.register_conditional()} LCB_T conditional_blocks* {jump_eng.register_goto()} RCB_T ;

object_declaration : ID_T {program_engine.register_new_object($ID_T.text)} object_declaration_aux ;
object_declaration_aux: ID_T {program_engine.current_context.object_directory.assign_object($ID_T.text)} {operation.set_current_object(str($ID_T.text))} ASSIGN_T {program_engine.register_method_era("initializer")} object_initialization ;
object_initialization: ID_T {program_engine.current_context.object_directory.validate_class_name($ID_T.text)} POINT_T NEW_T {operation.current_function = "initializer"} LP_T {operation.operator_stack.append('(')} obj_arguments? {operation.operator_stack.pop()} {operation.method_argument_number_validation()} RP_T {operation.method_call(operation.current_function)};

call_object_method : ID_T {operation.save_status()} {operation.set_current_object(str($ID_T.text))} object_method;
object_method : POINT_T ID_T {operation.current_function = $ID_T.text} {program_engine.register_method_era($ID_T.text)} LP_T {operation.operator_stack.append('(')} obj_arguments? {operation.operator_stack.pop()} {operation.method_argument_number_validation()} RP_T {operation.method_call(operation.current_function)} {operation.function_return_save()} {operation.reset_status()} ;

call_function : ID_T {operation.save_status()} {operation.current_function = $ID_T.text} {program_engine.register_function_era($ID_T.text)} LP_T {operation.operator_stack.append('(')} (arguments)? {operation.operator_stack.pop()} {operation.argument_number_validation()} RP_T {operation.function_call($ID_T.text)} {operation.function_return_save()} {operation.reset_status()} ;

call_collection : ID_T {operation.add_identifier(None,None,$ID_T.text)} LB_T {operation.verify_dimensions($ID_T.text)} expression {operation.generate_access_cuad(0)} RB_T ({operation.update_dimension()} call_matrix)? {operation.verify_array()} {operation.finish_collection_access()};

call_matrix: LB_T {operation.verify_matrix()} expression {operation.generate_access_cuad(1)} RB_T ;

declaration_assignment : ((declaration | assignments) END_OF_STM_T)+ ;

declaration : (array_declaration {structures_engine.set_next_memory_avail()}| var_declaration | object_declaration) ;

array_declaration : var_type ID_T LB_T CTE_INT_T  {program_engine.register_variable($var_type.text, $ID_T.text, [], $CTE_INT_T.text)} {structures_engine.set_current_collection($ID_T.text)} {structures_engine.inject_cell($CTE_INT_T.text)} RB_T (matrix)? {structures_engine.fill_k()} ;

matrix: LB_T CTE_INT_T {structures_engine.inject_cell($CTE_INT_T.text)} RB_T ;

var_declaration : var_type ID_T {program_engine.register_variable($var_type.text, $ID_T.text)};

assignments : (collection_assignment | var_assignment) ;

collection_assignment : call_collection ASSIGN_T expression {operation.collection_assignment()};

var_assignment : var_type ID_T ASSIGN_T expression {program_engine.register_variable($var_type.text, $ID_T.text)}{operation.assign_operation($ID_T.text)}
                | ID_T ASSIGN_T expression {operation.assign_operation($ID_T.text)};

var_type : INT_T|STRING_T|FLOAT_T|BOOLEAN_T ;

constants : CTE_FLOAT_T
            |CTE_INT_T
            |CTE_STRING_T
            |TRUE_T
            |FALSE_T ;
and_or_op: (OR_OP_T | AND_OP_T) ;
mult_div_op : (MULTI_T|DIVISION_T) ;
plus_minus_op : (PLUS_T | MINUS_T) ;

expression : conditional_expression;

conditional_expression : relational_expression {operation.compare_op()} and_or_op {operation.operator_stack.append($and_or_op.text)} conditional_expression
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

atomic : ID_T {operation.add_identifier($ID_T.text, None, None)}
        |constants {operation.add_identifier(None, $constants.text, None)}
        |call_object_method
        |call_function
        |call_collection;

relop_tokens : EQUAL_T
               | NOT_EQUAL_T
               | LESS_EQ_T
               | GREATER_EQ_T
               | LESS_T
               | GREATER_T ;

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
READ_T : 'read' ;


EQUAL_T : '=='|'is' ;
NOT_T : '!'|'not' ;
AND_OP_T : '&&'|'and' ;
OR_OP_T : '||'|'or' ;

WS : [ \t\r\n] -> skip ;

CTE_STRING_T : '"'.*?'"' ;
CTE_FLOAT_T : (DIGIT)+POINT_T(DIGIT)+ ;
CTE_INT_T : DIGIT+ ;

ID_T : LETTER(LETTER | '_' | DIGIT)* ;
CLASS_ID_T : LETTER(LETTER | '_' | DIGIT)*;

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
