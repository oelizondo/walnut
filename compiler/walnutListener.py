# Generated from compiler/walnut.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .walnutParser import walnutParser
else:
    from walnutParser import walnutParser

# This class defines a complete listener for a parse tree produced by walnutParser.
class walnutListener(ParseTreeListener):

    # Enter a parse tree produced by walnutParser#program.
    def enterProgram(self, ctx:walnutParser.ProgramContext):
        pass

    # Exit a parse tree produced by walnutParser#program.
    def exitProgram(self, ctx:walnutParser.ProgramContext):
        pass


    # Enter a parse tree produced by walnutParser#global_variables.
    def enterGlobal_variables(self, ctx:walnutParser.Global_variablesContext):
        pass

    # Exit a parse tree produced by walnutParser#global_variables.
    def exitGlobal_variables(self, ctx:walnutParser.Global_variablesContext):
        pass


    # Enter a parse tree produced by walnutParser#classes.
    def enterClasses(self, ctx:walnutParser.ClassesContext):
        pass

    # Exit a parse tree produced by walnutParser#classes.
    def exitClasses(self, ctx:walnutParser.ClassesContext):
        pass


    # Enter a parse tree produced by walnutParser#class_body.
    def enterClass_body(self, ctx:walnutParser.Class_bodyContext):
        pass

    # Exit a parse tree produced by walnutParser#class_body.
    def exitClass_body(self, ctx:walnutParser.Class_bodyContext):
        pass


    # Enter a parse tree produced by walnutParser#class_attributes.
    def enterClass_attributes(self, ctx:walnutParser.Class_attributesContext):
        pass

    # Exit a parse tree produced by walnutParser#class_attributes.
    def exitClass_attributes(self, ctx:walnutParser.Class_attributesContext):
        pass


    # Enter a parse tree produced by walnutParser#class_methods.
    def enterClass_methods(self, ctx:walnutParser.Class_methodsContext):
        pass

    # Exit a parse tree produced by walnutParser#class_methods.
    def exitClass_methods(self, ctx:walnutParser.Class_methodsContext):
        pass


    # Enter a parse tree produced by walnutParser#initializer.
    def enterInitializer(self, ctx:walnutParser.InitializerContext):
        pass

    # Exit a parse tree produced by walnutParser#initializer.
    def exitInitializer(self, ctx:walnutParser.InitializerContext):
        pass


    # Enter a parse tree produced by walnutParser#method_declaration.
    def enterMethod_declaration(self, ctx:walnutParser.Method_declarationContext):
        pass

    # Exit a parse tree produced by walnutParser#method_declaration.
    def exitMethod_declaration(self, ctx:walnutParser.Method_declarationContext):
        pass


    # Enter a parse tree produced by walnutParser#functions.
    def enterFunctions(self, ctx:walnutParser.FunctionsContext):
        pass

    # Exit a parse tree produced by walnutParser#functions.
    def exitFunctions(self, ctx:walnutParser.FunctionsContext):
        pass


    # Enter a parse tree produced by walnutParser#parameters.
    def enterParameters(self, ctx:walnutParser.ParametersContext):
        pass

    # Exit a parse tree produced by walnutParser#parameters.
    def exitParameters(self, ctx:walnutParser.ParametersContext):
        pass


    # Enter a parse tree produced by walnutParser#blocks.
    def enterBlocks(self, ctx:walnutParser.BlocksContext):
        pass

    # Exit a parse tree produced by walnutParser#blocks.
    def exitBlocks(self, ctx:walnutParser.BlocksContext):
        pass


    # Enter a parse tree produced by walnutParser#expression.
    def enterExpression(self, ctx:walnutParser.ExpressionContext):
        pass

    # Exit a parse tree produced by walnutParser#expression.
    def exitExpression(self, ctx:walnutParser.ExpressionContext):
        pass


    # Enter a parse tree produced by walnutParser#conditional_expression.
    def enterConditional_expression(self, ctx:walnutParser.Conditional_expressionContext):
        pass

    # Exit a parse tree produced by walnutParser#conditional_expression.
    def exitConditional_expression(self, ctx:walnutParser.Conditional_expressionContext):
        pass


    # Enter a parse tree produced by walnutParser#relational_expression.
    def enterRelational_expression(self, ctx:walnutParser.Relational_expressionContext):
        pass

    # Exit a parse tree produced by walnutParser#relational_expression.
    def exitRelational_expression(self, ctx:walnutParser.Relational_expressionContext):
        pass


    # Enter a parse tree produced by walnutParser#math_expression.
    def enterMath_expression(self, ctx:walnutParser.Math_expressionContext):
        pass

    # Exit a parse tree produced by walnutParser#math_expression.
    def exitMath_expression(self, ctx:walnutParser.Math_expressionContext):
        pass


    # Enter a parse tree produced by walnutParser#term.
    def enterTerm(self, ctx:walnutParser.TermContext):
        pass

    # Exit a parse tree produced by walnutParser#term.
    def exitTerm(self, ctx:walnutParser.TermContext):
        pass


    # Enter a parse tree produced by walnutParser#factor.
    def enterFactor(self, ctx:walnutParser.FactorContext):
        pass

    # Exit a parse tree produced by walnutParser#factor.
    def exitFactor(self, ctx:walnutParser.FactorContext):
        pass


    # Enter a parse tree produced by walnutParser#power_of.
    def enterPower_of(self, ctx:walnutParser.Power_ofContext):
        pass

    # Exit a parse tree produced by walnutParser#power_of.
    def exitPower_of(self, ctx:walnutParser.Power_ofContext):
        pass


    # Enter a parse tree produced by walnutParser#relop_tokens.
    def enterRelop_tokens(self, ctx:walnutParser.Relop_tokensContext):
        pass

    # Exit a parse tree produced by walnutParser#relop_tokens.
    def exitRelop_tokens(self, ctx:walnutParser.Relop_tokensContext):
        pass


    # Enter a parse tree produced by walnutParser#assignments.
    def enterAssignments(self, ctx:walnutParser.AssignmentsContext):
        pass

    # Exit a parse tree produced by walnutParser#assignments.
    def exitAssignments(self, ctx:walnutParser.AssignmentsContext):
        pass


    # Enter a parse tree produced by walnutParser#declaration.
    def enterDeclaration(self, ctx:walnutParser.DeclarationContext):
        pass

    # Exit a parse tree produced by walnutParser#declaration.
    def exitDeclaration(self, ctx:walnutParser.DeclarationContext):
        pass


    # Enter a parse tree produced by walnutParser#loops.
    def enterLoops(self, ctx:walnutParser.LoopsContext):
        pass

    # Exit a parse tree produced by walnutParser#loops.
    def exitLoops(self, ctx:walnutParser.LoopsContext):
        pass


    # Enter a parse tree produced by walnutParser#conditional.
    def enterConditional(self, ctx:walnutParser.ConditionalContext):
        pass

    # Exit a parse tree produced by walnutParser#conditional.
    def exitConditional(self, ctx:walnutParser.ConditionalContext):
        pass


    # Enter a parse tree produced by walnutParser#if_elsif_body.
    def enterIf_elsif_body(self, ctx:walnutParser.If_elsif_bodyContext):
        pass

    # Exit a parse tree produced by walnutParser#if_elsif_body.
    def exitIf_elsif_body(self, ctx:walnutParser.If_elsif_bodyContext):
        pass


    # Enter a parse tree produced by walnutParser#object_declaration.
    def enterObject_declaration(self, ctx:walnutParser.Object_declarationContext):
        pass

    # Exit a parse tree produced by walnutParser#object_declaration.
    def exitObject_declaration(self, ctx:walnutParser.Object_declarationContext):
        pass


    # Enter a parse tree produced by walnutParser#call_object_method.
    def enterCall_object_method(self, ctx:walnutParser.Call_object_methodContext):
        pass

    # Exit a parse tree produced by walnutParser#call_object_method.
    def exitCall_object_method(self, ctx:walnutParser.Call_object_methodContext):
        pass


    # Enter a parse tree produced by walnutParser#var_type.
    def enterVar_type(self, ctx:walnutParser.Var_typeContext):
        pass

    # Exit a parse tree produced by walnutParser#var_type.
    def exitVar_type(self, ctx:walnutParser.Var_typeContext):
        pass


