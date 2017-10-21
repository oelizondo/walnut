# Generated from walnut.g4 by ANTLR 4.7
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys


from vm import VM

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3")
        buf.write(u"\65\u014e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write(u"\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t")
        buf.write(u"\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22")
        buf.write(u"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4")
        buf.write(u"\30\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35")
        buf.write(u"\t\35\4\36\t\36\3\2\3\2\3\2\5\2@\n\2\3\2\7\2C\n\2\f\2")
        buf.write(u"\16\2F\13\2\3\2\7\2I\n\2\f\2\16\2L\13\2\3\2\7\2O\n\2")
        buf.write(u"\f\2\16\2R\13\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3")
        buf.write(u"\4\5\4^\n\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3")
        buf.write(u"\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\6\7r\n\7\r\7\16\7s\3\7")
        buf.write(u"\3\7\3\b\3\b\3\b\3\b\5\b|\n\b\3\b\3\b\3\b\7\b\u0081\n")
        buf.write(u"\b\f\b\16\b\u0084\13\b\3\b\3\b\3\t\3\t\3\t\3\t\5\t\u008c")
        buf.write(u"\n\t\3\t\3\t\3\t\5\t\u0091\n\t\3\t\3\t\7\t\u0095\n\t")
        buf.write(u"\f\t\16\t\u0098\13\t\3\t\3\t\5\t\u009c\n\t\3\t\3\t\3")
        buf.write(u"\n\3\n\3\n\3\n\5\n\u00a4\n\n\3\n\3\n\3\n\5\n\u00a9\n")
        buf.write(u"\n\3\n\3\n\7\n\u00ad\n\n\f\n\16\n\u00b0\13\n\3\n\3\n")
        buf.write(u"\5\n\u00b4\n\n\3\n\6\n\u00b7\n\n\r\n\16\n\u00b8\3\13")
        buf.write(u"\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u00c3\n\13\3")
        buf.write(u"\f\3\f\3\f\3\f\3\f\5\f\u00ca\n\f\3\r\3\r\3\16\3\16\3")
        buf.write(u"\16\3\16\3\16\5\16\u00d3\n\16\3\17\3\17\3\17\3\17\3\17")
        buf.write(u"\5\17\u00da\n\17\3\20\3\20\3\20\3\20\3\20\5\20\u00e1")
        buf.write(u"\n\20\3\21\3\21\3\21\3\21\3\21\5\21\u00e8\n\21\3\22\3")
        buf.write(u"\22\3\22\3\22\3\22\5\22\u00ef\n\22\3\23\5\23\u00f2\n")
        buf.write(u"\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u00fb\n\23")
        buf.write(u"\3\24\3\24\3\25\3\25\6\25\u0101\n\25\r\25\16\25\u0102")
        buf.write(u"\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3")
        buf.write(u"\30\3\30\3\30\7\30\u0112\n\30\f\30\16\30\u0115\13\30")
        buf.write(u"\3\30\3\30\3\31\3\31\3\31\3\31\6\31\u011d\n\31\r\31\16")
        buf.write(u"\31\u011e\3\31\3\31\3\31\7\31\u0124\n\31\f\31\16\31\u0127")
        buf.write(u"\13\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\7\32\u0130")
        buf.write(u"\n\32\f\32\16\32\u0133\13\32\3\32\3\32\3\33\3\33\3\33")
        buf.write(u"\3\33\3\33\3\33\3\33\3\33\5\33\u013f\n\33\3\33\3\33\3")
        buf.write(u"\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\36\3\36")
        buf.write(u"\3\36\2\2\37\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 ")
        buf.write(u"\"$&(*,.\60\62\64\668:\2\t\3\2\31\32\3\2*+\3\2()\4\2")
        buf.write(u"\30\30++\5\2\27\27!!#&\3\2\6\t\3\2\34\37\2\u0156\2<\3")
        buf.write(u"\2\2\2\4S\3\2\2\2\6X\3\2\2\2\be\3\2\2\2\nh\3\2\2\2\f")
        buf.write(u"m\3\2\2\2\16w\3\2\2\2\20\u0087\3\2\2\2\22\u00b6\3\2\2")
        buf.write(u"\2\24\u00c2\3\2\2\2\26\u00c9\3\2\2\2\30\u00cb\3\2\2\2")
        buf.write(u"\32\u00d2\3\2\2\2\34\u00d9\3\2\2\2\36\u00e0\3\2\2\2 ")
        buf.write(u"\u00e7\3\2\2\2\"\u00ee\3\2\2\2$\u00f1\3\2\2\2&\u00fc")
        buf.write(u"\3\2\2\2(\u0100\3\2\2\2*\u0104\3\2\2\2,\u0108\3\2\2\2")
        buf.write(u".\u010b\3\2\2\2\60\u0118\3\2\2\2\62\u012a\3\2\2\2\64")
        buf.write(u"\u0136\3\2\2\2\66\u0142\3\2\2\28\u0149\3\2\2\2:\u014b")
        buf.write(u"\3\2\2\2<=\7\3\2\2=?\7 \2\2>@\5\4\3\2?>\3\2\2\2?@\3\2")
        buf.write(u"\2\2@D\3\2\2\2AC\5\6\4\2BA\3\2\2\2CF\3\2\2\2DB\3\2\2")
        buf.write(u"\2DE\3\2\2\2EJ\3\2\2\2FD\3\2\2\2GI\5\22\n\2HG\3\2\2\2")
        buf.write(u"IL\3\2\2\2JH\3\2\2\2JK\3\2\2\2KP\3\2\2\2LJ\3\2\2\2MO")
        buf.write(u"\5\26\f\2NM\3\2\2\2OR\3\2\2\2PN\3\2\2\2PQ\3\2\2\2Q\3")
        buf.write(u"\3\2\2\2RP\3\2\2\2ST\7\4\2\2TU\7\61\2\2UV\5(\25\2VW\7")
        buf.write(u"\62\2\2W\5\3\2\2\2XY\7\n\2\2YZ\7 \2\2Z]\b\4\1\2[\\\7")
        buf.write(u"\13\2\2\\^\7 \2\2][\3\2\2\2]^\3\2\2\2^_\3\2\2\2_`\7\61")
        buf.write(u"\2\2`a\5\b\5\2ab\7\62\2\2bc\3\2\2\2cd\b\4\1\2d\7\3\2")
        buf.write(u"\2\2ef\5\n\6\2fg\5\f\7\2g\t\3\2\2\2hi\7\21\2\2ij\7\61")
        buf.write(u"\2\2jk\5(\25\2kl\7\62\2\2l\13\3\2\2\2mn\7\22\2\2no\7")
        buf.write(u"\61\2\2oq\5\16\b\2pr\5\20\t\2qp\3\2\2\2rs\3\2\2\2sq\3")
        buf.write(u"\2\2\2st\3\2\2\2tu\3\2\2\2uv\7\62\2\2v\r\3\2\2\2wx\7")
        buf.write(u"\23\2\2xy\7\24\2\2y{\7-\2\2z|\5\24\13\2{z\3\2\2\2{|\3")
        buf.write(u"\2\2\2|}\3\2\2\2}~\7.\2\2~\u0082\7\61\2\2\177\u0081\5")
        buf.write(u"\26\f\2\u0080\177\3\2\2\2\u0081\u0084\3\2\2\2\u0082\u0080")
        buf.write(u"\3\2\2\2\u0082\u0083\3\2\2\2\u0083\u0085\3\2\2\2\u0084")
        buf.write(u"\u0082\3\2\2\2\u0085\u0086\7\62\2\2\u0086\17\3\2\2\2")
        buf.write(u"\u0087\u0088\7\23\2\2\u0088\u0089\7 \2\2\u0089\u008b")
        buf.write(u"\7-\2\2\u008a\u008c\5\24\13\2\u008b\u008a\3\2\2\2\u008b")
        buf.write(u"\u008c\3\2\2\2\u008c\u008d\3\2\2\2\u008d\u0090\7.\2\2")
        buf.write(u"\u008e\u008f\7\65\2\2\u008f\u0091\58\35\2\u0090\u008e")
        buf.write(u"\3\2\2\2\u0090\u0091\3\2\2\2\u0091\u0092\3\2\2\2\u0092")
        buf.write(u"\u0096\7\61\2\2\u0093\u0095\5\26\f\2\u0094\u0093\3\2")
        buf.write(u"\2\2\u0095\u0098\3\2\2\2\u0096\u0094\3\2\2\2\u0096\u0097")
        buf.write(u"\3\2\2\2\u0097\u009b\3\2\2\2\u0098\u0096\3\2\2\2\u0099")
        buf.write(u"\u009a\7\5\2\2\u009a\u009c\5\30\r\2\u009b\u0099\3\2\2")
        buf.write(u"\2\u009b\u009c\3\2\2\2\u009c\u009d\3\2\2\2\u009d\u009e")
        buf.write(u"\7\62\2\2\u009e\21\3\2\2\2\u009f\u00a0\7\23\2\2\u00a0")
        buf.write(u"\u00a1\7 \2\2\u00a1\u00a3\7-\2\2\u00a2\u00a4\5\24\13")
        buf.write(u"\2\u00a3\u00a2\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00a5")
        buf.write(u"\3\2\2\2\u00a5\u00a8\7.\2\2\u00a6\u00a7\7\65\2\2\u00a7")
        buf.write(u"\u00a9\58\35\2\u00a8\u00a6\3\2\2\2\u00a8\u00a9\3\2\2")
        buf.write(u"\2\u00a9\u00aa\3\2\2\2\u00aa\u00ae\7\61\2\2\u00ab\u00ad")
        buf.write(u"\5\26\f\2\u00ac\u00ab\3\2\2\2\u00ad\u00b0\3\2\2\2\u00ae")
        buf.write(u"\u00ac\3\2\2\2\u00ae\u00af\3\2\2\2\u00af\u00b3\3\2\2")
        buf.write(u"\2\u00b0\u00ae\3\2\2\2\u00b1\u00b2\7\5\2\2\u00b2\u00b4")
        buf.write(u"\5\30\r\2\u00b3\u00b1\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4")
        buf.write(u"\u00b5\3\2\2\2\u00b5\u00b7\7\62\2\2\u00b6\u009f\3\2\2")
        buf.write(u"\2\u00b7\u00b8\3\2\2\2\u00b8\u00b6\3\2\2\2\u00b8\u00b9")
        buf.write(u"\3\2\2\2\u00b9\23\3\2\2\2\u00ba\u00bb\58\35\2\u00bb\u00bc")
        buf.write(u"\7 \2\2\u00bc\u00bd\7,\2\2\u00bd\u00be\5\24\13\2\u00be")
        buf.write(u"\u00c3\3\2\2\2\u00bf\u00c0\58\35\2\u00c0\u00c1\7 \2\2")
        buf.write(u"\u00c1\u00c3\3\2\2\2\u00c2\u00ba\3\2\2\2\u00c2\u00bf")
        buf.write(u"\3\2\2\2\u00c3\25\3\2\2\2\u00c4\u00ca\5\30\r\2\u00c5")
        buf.write(u"\u00ca\5(\25\2\u00c6\u00ca\5.\30\2\u00c7\u00ca\5\60\31")
        buf.write(u"\2\u00c8\u00ca\5\64\33\2\u00c9\u00c4\3\2\2\2\u00c9\u00c5")
        buf.write(u"\3\2\2\2\u00c9\u00c6\3\2\2\2\u00c9\u00c7\3\2\2\2\u00c9")
        buf.write(u"\u00c8\3\2\2\2\u00ca\27\3\2\2\2\u00cb\u00cc\5\32\16\2")
        buf.write(u"\u00cc\31\3\2\2\2\u00cd\u00ce\5\34\17\2\u00ce\u00cf\t")
        buf.write(u"\2\2\2\u00cf\u00d0\5\32\16\2\u00d0\u00d3\3\2\2\2\u00d1")
        buf.write(u"\u00d3\5\34\17\2\u00d2\u00cd\3\2\2\2\u00d2\u00d1\3\2")
        buf.write(u"\2\2\u00d3\33\3\2\2\2\u00d4\u00d5\5\36\20\2\u00d5\u00d6")
        buf.write(u"\5&\24\2\u00d6\u00d7\5\34\17\2\u00d7\u00da\3\2\2\2\u00d8")
        buf.write(u"\u00da\5\36\20\2\u00d9\u00d4\3\2\2\2\u00d9\u00d8\3\2")
        buf.write(u"\2\2\u00da\35\3\2\2\2\u00db\u00dc\5 \21\2\u00dc\u00dd")
        buf.write(u"\t\3\2\2\u00dd\u00de\5\36\20\2\u00de\u00e1\3\2\2\2\u00df")
        buf.write(u"\u00e1\5 \21\2\u00e0\u00db\3\2\2\2\u00e0\u00df\3\2\2")
        buf.write(u"\2\u00e1\37\3\2\2\2\u00e2\u00e3\5\"\22\2\u00e3\u00e4")
        buf.write(u"\t\4\2\2\u00e4\u00e5\5 \21\2\u00e5\u00e8\3\2\2\2\u00e6")
        buf.write(u"\u00e8\5\"\22\2\u00e7\u00e2\3\2\2\2\u00e7\u00e6\3\2\2")
        buf.write(u"\2\u00e8!\3\2\2\2\u00e9\u00ea\5$\23\2\u00ea\u00eb\7\'")
        buf.write(u"\2\2\u00eb\u00ec\5\"\22\2\u00ec\u00ef\3\2\2\2\u00ed\u00ef")
        buf.write(u"\5$\23\2\u00ee\u00e9\3\2\2\2\u00ee\u00ed\3\2\2\2\u00ef")
        buf.write(u"#\3\2\2\2\u00f0\u00f2\t\5\2\2\u00f1\u00f0\3\2\2\2\u00f1")
        buf.write(u"\u00f2\3\2\2\2\u00f2\u00fa\3\2\2\2\u00f3\u00fb\7 \2\2")
        buf.write(u"\u00f4\u00fb\5:\36\2\u00f5\u00fb\5\66\34\2\u00f6\u00f7")
        buf.write(u"\7-\2\2\u00f7\u00f8\5\30\r\2\u00f8\u00f9\7.\2\2\u00f9")
        buf.write(u"\u00fb\3\2\2\2\u00fa\u00f3\3\2\2\2\u00fa\u00f4\3\2\2")
        buf.write(u"\2\u00fa\u00f5\3\2\2\2\u00fa\u00f6\3\2\2\2\u00fb%\3\2")
        buf.write(u"\2\2\u00fc\u00fd\t\6\2\2\u00fd\'\3\2\2\2\u00fe\u0101")
        buf.write(u"\5,\27\2\u00ff\u0101\5*\26\2\u0100\u00fe\3\2\2\2\u0100")
        buf.write(u"\u00ff\3\2\2\2\u0101\u0102\3\2\2\2\u0102\u0100\3\2\2")
        buf.write(u"\2\u0102\u0103\3\2\2\2\u0103)\3\2\2\2\u0104\u0105\7 ")
        buf.write(u"\2\2\u0105\u0106\7\"\2\2\u0106\u0107\5\30\r\2\u0107+")
        buf.write(u"\3\2\2\2\u0108\u0109\58\35\2\u0109\u010a\7 \2\2\u010a")
        buf.write(u"-\3\2\2\2\u010b\u010c\7\25\2\2\u010c\u010d\7-\2\2\u010d")
        buf.write(u"\u010e\5\30\r\2\u010e\u010f\7.\2\2\u010f\u0113\7\61\2")
        buf.write(u"\2\u0110\u0112\5\26\f\2\u0111\u0110\3\2\2\2\u0112\u0115")
        buf.write(u"\3\2\2\2\u0113\u0111\3\2\2\2\u0113\u0114\3\2\2\2\u0114")
        buf.write(u"\u0116\3\2\2\2\u0115\u0113\3\2\2\2\u0116\u0117\7\62\2")
        buf.write(u"\2\u0117/\3\2\2\2\u0118\u0119\7\f\2\2\u0119\u011c\5\62")
        buf.write(u"\32\2\u011a\u011b\7\r\2\2\u011b\u011d\5\62\32\2\u011c")
        buf.write(u"\u011a\3\2\2\2\u011d\u011e\3\2\2\2\u011e\u011c\3\2\2")
        buf.write(u"\2\u011e\u011f\3\2\2\2\u011f\u0120\3\2\2\2\u0120\u0121")
        buf.write(u"\7\16\2\2\u0121\u0125\7\61\2\2\u0122\u0124\5\26\f\2\u0123")
        buf.write(u"\u0122\3\2\2\2\u0124\u0127\3\2\2\2\u0125\u0123\3\2\2")
        buf.write(u"\2\u0125\u0126\3\2\2\2\u0126\u0128\3\2\2\2\u0127\u0125")
        buf.write(u"\3\2\2\2\u0128\u0129\7\62\2\2\u0129\61\3\2\2\2\u012a")
        buf.write(u"\u012b\7-\2\2\u012b\u012c\5\30\r\2\u012c\u012d\7.\2\2")
        buf.write(u"\u012d\u0131\7\61\2\2\u012e\u0130\5\26\f\2\u012f\u012e")
        buf.write(u"\3\2\2\2\u0130\u0133\3\2\2\2\u0131\u012f\3\2\2\2\u0131")
        buf.write(u"\u0132\3\2\2\2\u0132\u0134\3\2\2\2\u0133\u0131\3\2\2")
        buf.write(u"\2\u0134\u0135\7\62\2\2\u0135\63\3\2\2\2\u0136\u0137")
        buf.write(u"\7 \2\2\u0137\u0138\7 \2\2\u0138\u0139\7\"\2\2\u0139")
        buf.write(u"\u013a\7 \2\2\u013a\u013b\7\63\2\2\u013b\u013c\7\26\2")
        buf.write(u"\2\u013c\u013e\7-\2\2\u013d\u013f\5\24\13\2\u013e\u013d")
        buf.write(u"\3\2\2\2\u013e\u013f\3\2\2\2\u013f\u0140\3\2\2\2\u0140")
        buf.write(u"\u0141\7.\2\2\u0141\65\3\2\2\2\u0142\u0143\7 \2\2\u0143")
        buf.write(u"\u0144\7\63\2\2\u0144\u0145\7 \2\2\u0145\u0146\7-\2\2")
        buf.write(u"\u0146\u0147\5\24\13\2\u0147\u0148\7.\2\2\u0148\67\3")
        buf.write(u"\2\2\2\u0149\u014a\t\7\2\2\u014a9\3\2\2\2\u014b\u014c")
        buf.write(u"\t\b\2\2\u014c;\3\2\2\2#?DJP]s{\u0082\u008b\u0090\u0096")
        buf.write(u"\u009b\u00a3\u00a8\u00ae\u00b3\u00b8\u00c2\u00c9\u00d2")
        buf.write(u"\u00d9\u00e0\u00e7\u00ee\u00f1\u00fa\u0100\u0102\u0113")
        buf.write(u"\u011e\u0125\u0131\u013e")
        return buf.getvalue()


class walnutParser ( Parser ):

    grammarFileName = "walnut.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'program'", u"'globals'", u"'return'", 
                     u"'int'", u"'float'", u"'string'", u"'boolean'", u"'class'", 
                     u"'extends'", u"'if'", u"'elseif'", u"'else'", u"'true'", 
                     u"'false'", u"'attributes'", u"'methods'", u"'func'", 
                     u"'initializer'", u"'while'", u"'new'", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"'!='", u"'='", u"'<='", u"'>='", u"'<'", 
                     u"'>'", u"'^'", u"'/'", u"'*'", u"'+'", u"'-'", u"','", 
                     u"'('", u"')'", u"'['", u"']'", u"'{'", u"'}'", u"'.'", 
                     u"';'", u"':'" ]

    symbolicNames = [ u"<INVALID>", u"PROGRAM_T", u"GLOBALS_T", u"RETURN_T", 
                      u"INT_T", u"FLOAT_T", u"STRING_T", u"BOOLEAN_T", u"CLASS_T", 
                      u"EXTENDS_T", u"IF_T", u"ELSEIF_T", u"ELSE_T", u"TRUE_T", 
                      u"FALSE_T", u"ATTRS_T", u"METHODS_T", u"FUNC_T", u"INIT_T", 
                      u"WHILE_T", u"NEW_T", u"EQUAL_T", u"NOT_T", u"AND_OP_T", 
                      u"OR_OP_T", u"WS", u"CTE_STRING_T", u"CTE_INT_T", 
                      u"CTE_FLOAT_T", u"CTE_BOOL_T", u"ID_T", u"NOT_EQUAL_T", 
                      u"ASSIGN_T", u"LESS_EQ_T", u"GREATER_EQ_T", u"LESS_T", 
                      u"GREATER_T", u"POW_T", u"DIVISION_T", u"MULTI_T", 
                      u"PLUS_T", u"MINUS_T", u"COMMA_T", u"LP_T", u"RP_T", 
                      u"LB_T", u"RB_T", u"LCB_T", u"RCB_T", u"POINT_T", 
                      u"END_OF_STM_T", u"RETURN_TYPE_T" ]

    RULE_program = 0
    RULE_global_variables = 1
    RULE_classes = 2
    RULE_class_body = 3
    RULE_class_attributes = 4
    RULE_class_methods = 5
    RULE_initializer = 6
    RULE_method_declaration = 7
    RULE_functions = 8
    RULE_parameters = 9
    RULE_blocks = 10
    RULE_expression = 11
    RULE_conditional_expression = 12
    RULE_relational_expression = 13
    RULE_math_expression = 14
    RULE_term = 15
    RULE_factor = 16
    RULE_power_of = 17
    RULE_relop_tokens = 18
    RULE_declaration_assignment = 19
    RULE_assignments = 20
    RULE_declaration = 21
    RULE_loops = 22
    RULE_conditional = 23
    RULE_if_elsif_body = 24
    RULE_object_declaration = 25
    RULE_call_object_method = 26
    RULE_var_type = 27
    RULE_constants = 28

    ruleNames =  [ u"program", u"global_variables", u"classes", u"class_body", 
                   u"class_attributes", u"class_methods", u"initializer", 
                   u"method_declaration", u"functions", u"parameters", u"blocks", 
                   u"expression", u"conditional_expression", u"relational_expression", 
                   u"math_expression", u"term", u"factor", u"power_of", 
                   u"relop_tokens", u"declaration_assignment", u"assignments", 
                   u"declaration", u"loops", u"conditional", u"if_elsif_body", 
                   u"object_declaration", u"call_object_method", u"var_type", 
                   u"constants" ]

    EOF = Token.EOF
    PROGRAM_T=1
    GLOBALS_T=2
    RETURN_T=3
    INT_T=4
    FLOAT_T=5
    STRING_T=6
    BOOLEAN_T=7
    CLASS_T=8
    EXTENDS_T=9
    IF_T=10
    ELSEIF_T=11
    ELSE_T=12
    TRUE_T=13
    FALSE_T=14
    ATTRS_T=15
    METHODS_T=16
    FUNC_T=17
    INIT_T=18
    WHILE_T=19
    NEW_T=20
    EQUAL_T=21
    NOT_T=22
    AND_OP_T=23
    OR_OP_T=24
    WS=25
    CTE_STRING_T=26
    CTE_INT_T=27
    CTE_FLOAT_T=28
    CTE_BOOL_T=29
    ID_T=30
    NOT_EQUAL_T=31
    ASSIGN_T=32
    LESS_EQ_T=33
    GREATER_EQ_T=34
    LESS_T=35
    GREATER_T=36
    POW_T=37
    DIVISION_T=38
    MULTI_T=39
    PLUS_T=40
    MINUS_T=41
    COMMA_T=42
    LP_T=43
    RP_T=44
    LB_T=45
    RB_T=46
    LCB_T=47
    RCB_T=48
    POINT_T=49
    END_OF_STM_T=50
    RETURN_TYPE_T=51

    def __init__(self, input, output=sys.stdout):
        super(walnutParser, self).__init__(input, output=output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    global virtual_machine
    virtual_machine = VM()


    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(walnutParser.ProgramContext, self).__init__(parent, invokingState)
            self.parser = parser

        def PROGRAM_T(self):
            return self.getToken(walnutParser.PROGRAM_T, 0)

        def ID_T(self):
            return self.getToken(walnutParser.ID_T, 0)

        def global_variables(self):
            return self.getTypedRuleContext(walnutParser.Global_variablesContext,0)


        def classes(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(walnutParser.ClassesContext)
            else:
                return self.getTypedRuleContext(walnutParser.ClassesContext,i)


        def functions(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(walnutParser.FunctionsContext)
            else:
                return self.getTypedRuleContext(walnutParser.FunctionsContext,i)


        def blocks(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(walnutParser.BlocksContext)
            else:
                return self.getTypedRuleContext(walnutParser.BlocksContext,i)


        def getRuleIndex(self):
            return walnutParser.RULE_program

        def enterRule(self, listener):
            if hasattr(listener, "enterProgram"):
                listener.enterProgram(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitProgram"):
                listener.exitProgram(self)




    def program(self):

        localctx = walnutParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(walnutParser.PROGRAM_T)
            self.state = 59
            self.match(walnutParser.ID_T)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==walnutParser.GLOBALS_T:
                self.state = 60
                self.global_variables()


            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==walnutParser.CLASS_T:
                self.state = 63
                self.classes()
                self.state = 68
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==walnutParser.FUNC_T:
                self.state = 69
                self.functions()
                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << walnutParser.INT_T) | (1 << walnutParser.FLOAT_T) | (1 << walnutParser.STRING_T) | (1 << walnutParser.BOOLEAN_T) | (1 << walnutParser.IF_T) | (1 << walnutParser.WHILE_T) | (1 << walnutParser.NOT_T) | (1 << walnutParser.CTE_STRING_T) | (1 << walnutParser.CTE_INT_T) | (1 << walnutParser.CTE_FLOAT_T) | (1 << walnutParser.CTE_BOOL_T) | (1 << walnutParser.ID_T) | (1 << walnutParser.MINUS_T) | (1 << walnutParser.LP_T))) != 0):
                self.state = 75
                self.blocks()
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Global_variablesContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(walnutParser.Global_variablesContext, self).__init__(parent, invokingState)
            self.parser = parser

        def GLOBALS_T(self):
            return self.getToken(walnutParser.GLOBALS_T, 0)

        def LCB_T(self):
            return self.getToken(walnutParser.LCB_T, 0)

        def declaration_assignment(self):
            return self.getTypedRuleContext(walnutParser.Declaration_assignmentContext,0)


        def RCB_T(self):
            return self.getToken(walnutParser.RCB_T, 0)

        def getRuleIndex(self):
            return walnutParser.RULE_global_variables

        def enterRule(self, listener):
            if hasattr(listener, "enterGlobal_variables"):
                listener.enterGlobal_variables(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitGlobal_variables"):
                listener.exitGlobal_variables(self)




    def global_variables(self):

        localctx = walnutParser.Global_variablesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_global_variables)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(walnutParser.GLOBALS_T)
            self.state = 82
            self.match(walnutParser.LCB_T)
            self.state = 83
            self.declaration_assignment()
            self.state = 84
            self.match(walnutParser.RCB_T)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ClassesContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(walnutParser.ClassesContext, self).__init__(parent, invokingState)
            self.parser = parser

        def CLASS_T(self):
            return self.getToken(walnutParser.CLASS_T, 0)

        def ID_T(self, i=None):
            if i is None:
                return self.getTokens(walnutParser.ID_T)
            else:
                return self.getToken(walnutParser.ID_T, i)

        def LCB_T(self):
            return self.getToken(walnutParser.LCB_T, 0)

        def class_body(self):
            return self.getTypedRuleContext(walnutParser.Class_bodyContext,0)


        def RCB_T(self):
            return self.getToken(walnutParser.RCB_T, 0)

        def EXTENDS_T(self):
            return self.getToken(walnutParser.EXTENDS_T, 0)

        def getRuleIndex(self):
            return walnutParser.RULE_classes

        def enterRule(self, listener):
            if hasattr(listener, "enterClasses"):
                listener.enterClasses(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitClasses"):
                listener.exitClasses(self)




    def classes(self):

        localctx = walnutParser.ClassesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_classes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(walnutParser.CLASS_T)
            self.state = 87
            self.match(walnutParser.ID_T)

            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==walnutParser.EXTENDS_T:
                self.state = 89
                self.match(walnutParser.EXTENDS_T)
                self.state = 90
                self.match(walnutParser.ID_T)


            self.state = 93
            self.match(walnutParser.LCB_T)
            self.state = 94
            self.class_body()
            self.state = 95
            self.match(walnutParser.RCB_T)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Class_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(walnutParser.Class_bodyContext, self).__init__(parent, invokingState)
            self.parser = parser

        def class_attributes(self):
            return self.getTypedRuleContext(walnutParser.Class_attributesContext,0)


        def class_methods(self):
            return self.getTypedRuleContext(walnutParser.Class_methodsContext,0)


        def getRuleIndex(self):
            return walnutParser.RULE_class_body

        def enterRule(self, listener):
            if hasattr(listener, "enterClass_body"):
                listener.enterClass_body(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitClass_body"):
                listener.exitClass_body(self)




    def class_body(self):

        localctx = walnutParser.Class_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_class_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.class_attributes()
            self.state = 100
            self.class_methods()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Class_attributesContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(walnutParser.Class_attributesContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ATTRS_T(self):
            return self.getToken(walnutParser.ATTRS_T, 0)

        def LCB_T(self):
            return self.getToken(walnutParser.LCB_T, 0)

        def declaration_assignment(self):
            return self.getTypedRuleContext(walnutParser.Declaration_assignmentContext,0)


        def RCB_T(self):
            return self.getToken(walnutParser.RCB_T, 0)

        def getRuleIndex(self):
            return walnutParser.RULE_class_attributes

        def enterRule(self, listener):
            if hasattr(listener, "enterClass_attributes"):
                listener.enterClass_attributes(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitClass_attributes"):
                listener.exitClass_attributes(self)




    def class_attributes(self):

        localctx = walnutParser.Class_attributesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_class_attributes)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(walnutParser.ATTRS_T)
            self.state = 103
            self.match(walnutParser.LCB_T)
            self.state = 104
            self.declaration_assignment()
            self.state = 105
            self.match(walnutParser.RCB_T)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Class_methodsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(walnutParser.Class_methodsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def METHODS_T(self):
            return self.getToken(walnutParser.METHODS_T, 0)

        def LCB_T(self):
            return self.getToken(walnutParser.LCB_T, 0)

        def initializer(self):
            return self.getTypedRuleContext(walnutParser.InitializerContext,0)


        def RCB_T(self):
            return self.getToken(walnutParser.RCB_T, 0)

        def method_declaration(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(walnutParser.Method_declarationContext)
            else:
                return self.getTypedRuleContext(walnutParser.Method_declarationContext,i)


        def getRuleIndex(self):
            return walnutParser.RULE_class_methods

        def enterRule(self, listener):
            if hasattr(listener, "enterClass_methods"):
                listener.enterClass_methods(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitClass_methods"):
                listener.exitClass_methods(self)




    def class_methods(self):

        localctx = walnutParser.Class_methodsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_class_methods)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(walnutParser.METHODS_T)
            self.state = 108
            self.match(walnutParser.LCB_T)
            self.state = 109
            self.initializer()
            self.state = 111 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 110
                self.method_declaration()
                self.state = 113 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==walnutParser.FUNC_T):
                    break

            self.state = 115
            self.match(walnutParser.RCB_T)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InitializerContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(walnutParser.InitializerContext, self).__init__(parent, invokingState)
            self.parser = parser

        def FUNC_T(self):
            return self.getToken(walnutParser.FUNC_T, 0)

        def INIT_T(self):
            return self.getToken(walnutParser.INIT_T, 0)

        def LP_T(self):
            return self.getToken(walnutParser.LP_T, 0)

        def RP_T(self):
            return self.getToken(walnutParser.RP_T, 0)

        def LCB_T(self):
            return self.getToken(walnutParser.LCB_T, 0)

        def RCB_T(self):
            return self.getToken(walnutParser.RCB_T, 0)

        def parameters(self):
            return self.getTypedRuleContext(walnutParser.ParametersContext,0)


        def blocks(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(walnutParser.BlocksContext)
            else:
                return self.getTypedRuleContext(walnutParser.BlocksContext,i)


        def getRuleIndex(self):
            return walnutParser.RULE_initializer

        def enterRule(self, listener):
            if hasattr(listener, "enterInitializer"):
                listener.enterInitializer(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitInitializer"):
                listener.exitInitializer(self)




    def initializer(self):

        localctx = walnutParser.InitializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_initializer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(walnutParser.FUNC_T)
            self.state = 118
            self.match(walnutParser.INIT_T)
            self.state = 119
            self.match(walnutParser.LP_T)
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << walnutParser.INT_T) | (1 << walnutParser.FLOAT_T) | (1 << walnutParser.STRING_T) | (1 << walnutParser.BOOLEAN_T))) != 0):
                self.state = 120
                self.parameters()


            self.state = 123
            self.match(walnutParser.RP_T)
            self.state = 124
            self.match(walnutParser.LCB_T)
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << walnutParser.INT_T) | (1 << walnutParser.FLOAT_T) | (1 << walnutParser.STRING_T) | (1 << walnutParser.BOOLEAN_T) | (1 << walnutParser.IF_T) | (1 << walnutParser.WHILE_T) | (1 << walnutParser.NOT_T) | (1 << walnutParser.CTE_STRING_T) | (1 << walnutParser.CTE_INT_T) | (1 << walnutParser.CTE_FLOAT_T) | (1 << walnutParser.CTE_BOOL_T) | (1 << walnutParser.ID_T) | (1 << walnutParser.MINUS_T) | (1 << walnutParser.LP_T))) != 0):
                self.state = 125
                self.blocks()
                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 131
            self.match(walnutParser.RCB_T)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(walnutParser.Method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def FUNC_T(self):
            return self.getToken(walnutParser.FUNC_T, 0)

        def ID_T(self):
            return self.getToken(walnutParser.ID_T, 0)

        def LP_T(self):
            return self.getToken(walnutParser.LP_T, 0)

        def RP_T(self):
            return self.getToken(walnutParser.RP_T, 0)

        def LCB_T(self):
            return self.getToken(walnutParser.LCB_T, 0)

        def RCB_T(self):
            return self.getToken(walnutParser.RCB_T, 0)

        def parameters(self):
            return self.getTypedRuleContext(walnutParser.ParametersContext,0)


        def RETURN_TYPE_T(self):
            return self.getToken(walnutParser.RETURN_TYPE_T, 0)

        def var_type(self):
            return self.getTypedRuleContext(walnutParser.Var_typeContext,0)


        def blocks(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(walnutParser.BlocksContext)
            else:
                return self.getTypedRuleContext(walnutParser.BlocksContext,i)


        def RETURN_T(self):
            return self.getToken(walnutParser.RETURN_T, 0)

        def expression(self):
            return self.getTypedRuleContext(walnutParser.ExpressionContext,0)


        def getRuleIndex(self):
            return walnutParser.RULE_method_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterMethod_declaration"):
                listener.enterMethod_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMethod_declaration"):
                listener.exitMethod_declaration(self)




    def method_declaration(self):

        localctx = walnutParser.Method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(walnutParser.FUNC_T)
            self.state = 134
            self.match(walnutParser.ID_T)
            self.state = 135
            self.match(walnutParser.LP_T)
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << walnutParser.INT_T) | (1 << walnutParser.FLOAT_T) | (1 << walnutParser.STRING_T) | (1 << walnutParser.BOOLEAN_T))) != 0):
                self.state = 136
                self.parameters()


            self.state = 139
            self.match(walnutParser.RP_T)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==walnutParser.RETURN_TYPE_T:
                self.state = 140
                self.match(walnutParser.RETURN_TYPE_T)
                self.state = 141
                self.var_type()


            self.state = 144
            self.match(walnutParser.LCB_T)
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << walnutParser.INT_T) | (1 << walnutParser.FLOAT_T) | (1 << walnutParser.STRING_T) | (1 << walnutParser.BOOLEAN_T) | (1 << walnutParser.IF_T) | (1 << walnutParser.WHILE_T) | (1 << walnutParser.NOT_T) | (1 << walnutParser.CTE_STRING_T) | (1 << walnutParser.CTE_INT_T) | (1 << walnutParser.CTE_FLOAT_T) | (1 << walnutParser.CTE_BOOL_T) | (1 << walnutParser.ID_T) | (1 << walnutParser.MINUS_T) | (1 << walnutParser.LP_T))) != 0):
                self.state = 145
                self.blocks()
                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==walnutParser.RETURN_T:
                self.state = 151
                self.match(walnutParser.RETURN_T)
                self.state = 152
                self.expression()


            self.state = 155
            self.match(walnutParser.RCB_T)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(walnutParser.FunctionsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def FUNC_T(self, i=None):
            if i is None:
                return self.getTokens(walnutParser.FUNC_T)
            else:
                return self.getToken(walnutParser.FUNC_T, i)

        def ID_T(self, i=None):
            if i is None:
                return self.getTokens(walnutParser.ID_T)
            else:
                return self.getToken(walnutParser.ID_T, i)

        def LP_T(self, i=None):
            if i is None:
                return self.getTokens(walnutParser.LP_T)
            else:
                return self.getToken(walnutParser.LP_T, i)

        def RP_T(self, i=None):
            if i is None:
                return self.getTokens(walnutParser.RP_T)
            else:
                return self.getToken(walnutParser.RP_T, i)

        def LCB_T(self, i=None):
            if i is None:
                return self.getTokens(walnutParser.LCB_T)
            else:
                return self.getToken(walnutParser.LCB_T, i)

        def RCB_T(self, i=None):
            if i is None:
                return self.getTokens(walnutParser.RCB_T)
            else:
                return self.getToken(walnutParser.RCB_T, i)

        def parameters(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(walnutParser.ParametersContext)
            else:
                return self.getTypedRuleContext(walnutParser.ParametersContext,i)


        def RETURN_TYPE_T(self, i=None):
            if i is None:
                return self.getTokens(walnutParser.RETURN_TYPE_T)
            else:
                return self.getToken(walnutParser.RETURN_TYPE_T, i)

        def var_type(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(walnutParser.Var_typeContext)
            else:
                return self.getTypedRuleContext(walnutParser.Var_typeContext,i)


        def blocks(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(walnutParser.BlocksContext)
            else:
                return self.getTypedRuleContext(walnutParser.BlocksContext,i)


        def RETURN_T(self, i=None):
            if i is None:
                return self.getTokens(walnutParser.RETURN_T)
            else:
                return self.getToken(walnutParser.RETURN_T, i)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(walnutParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(walnutParser.ExpressionContext,i)


        def getRuleIndex(self):
            return walnutParser.RULE_functions

        def enterRule(self, listener):
            if hasattr(listener, "enterFunctions"):
                listener.enterFunctions(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFunctions"):
                listener.exitFunctions(self)




    def functions(self):

        localctx = walnutParser.FunctionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_functions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 157
                    self.match(walnutParser.FUNC_T)
                    self.state = 158
                    self.match(walnutParser.ID_T)
                    self.state = 159
                    self.match(walnutParser.LP_T)
                    self.state = 161
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << walnutParser.INT_T) | (1 << walnutParser.FLOAT_T) | (1 << walnutParser.STRING_T) | (1 << walnutParser.BOOLEAN_T))) != 0):
                        self.state = 160
                        self.parameters()


                    self.state = 163
                    self.match(walnutParser.RP_T)
                    self.state = 166
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==walnutParser.RETURN_TYPE_T:
                        self.state = 164
                        self.match(walnutParser.RETURN_TYPE_T)
                        self.state = 165
                        self.var_type()


                    self.state = 168
                    self.match(walnutParser.LCB_T)
                    self.state = 172
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << walnutParser.INT_T) | (1 << walnutParser.FLOAT_T) | (1 << walnutParser.STRING_T) | (1 << walnutParser.BOOLEAN_T) | (1 << walnutParser.IF_T) | (1 << walnutParser.WHILE_T) | (1 << walnutParser.NOT_T) | (1 << walnutParser.CTE_STRING_T) | (1 << walnutParser.CTE_INT_T) | (1 << walnutParser.CTE_FLOAT_T) | (1 << walnutParser.CTE_BOOL_T) | (1 << walnutParser.ID_T) | (1 << walnutParser.MINUS_T) | (1 << walnutParser.LP_T))) != 0):
                        self.state = 169
                        self.blocks()
                        self.state = 174
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 177
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==walnutParser.RETURN_T:
                        self.state = 175
                        self.match(walnutParser.RETURN_T)
                        self.state = 176
                        self.expression()


                    self.state = 179
                    self.match(walnutParser.RCB_T)

                else:
                    raise NoViableAltException(self)
                self.state = 182 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParametersContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(walnutParser.ParametersContext, self).__init__(parent, invokingState)
            self.parser = parser

        def var_type(self):
            return self.getTypedRuleContext(walnutParser.Var_typeContext,0)


        def ID_T(self):
            return self.getToken(walnutParser.ID_T, 0)

        def COMMA_T(self):
            return self.getToken(walnutParser.COMMA_T, 0)

        def parameters(self):
            return self.getTypedRuleContext(walnutParser.ParametersContext,0)


        def getRuleIndex(self):
            return walnutParser.RULE_parameters

        def enterRule(self, listener):
            if hasattr(listener, "enterParameters"):
                listener.enterParameters(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitParameters"):
                listener.exitParameters(self)




    def parameters(self):

        localctx = walnutParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_parameters)
        try:
            self.state = 192
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self.var_type()
                self.state = 185
                self.match(walnutParser.ID_T)
                self.state = 186
                self.match(walnutParser.COMMA_T)
                self.state = 187
                self.parameters()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 189
                self.var_type()
                self.state = 190
                self.match(walnutParser.ID_T)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BlocksContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(walnutParser.BlocksContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(walnutParser.ExpressionContext,0)


        def declaration_assignment(self):
            return self.getTypedRuleContext(walnutParser.Declaration_assignmentContext,0)


        def loops(self):
            return self.getTypedRuleContext(walnutParser.LoopsContext,0)


        def conditional(self):
            return self.getTypedRuleContext(walnutParser.ConditionalContext,0)


        def object_declaration(self):
            return self.getTypedRuleContext(walnutParser.Object_declarationContext,0)


        def getRuleIndex(self):
            return walnutParser.RULE_blocks

        def enterRule(self, listener):
            if hasattr(listener, "enterBlocks"):
                listener.enterBlocks(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitBlocks"):
                listener.exitBlocks(self)




    def blocks(self):

        localctx = walnutParser.BlocksContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_blocks)
        try:
            self.state = 199
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 195
                self.declaration_assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 196
                self.loops()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 197
                self.conditional()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 198
                self.object_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(walnutParser.ExpressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def conditional_expression(self):
            return self.getTypedRuleContext(walnutParser.Conditional_expressionContext,0)


        def getRuleIndex(self):
            return walnutParser.RULE_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterExpression"):
                listener.enterExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitExpression"):
                listener.exitExpression(self)




    def expression(self):

        localctx = walnutParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.conditional_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Conditional_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(walnutParser.Conditional_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def relational_expression(self):
            return self.getTypedRuleContext(walnutParser.Relational_expressionContext,0)


        def conditional_expression(self):
            return self.getTypedRuleContext(walnutParser.Conditional_expressionContext,0)


        def OR_OP_T(self):
            return self.getToken(walnutParser.OR_OP_T, 0)

        def AND_OP_T(self):
            return self.getToken(walnutParser.AND_OP_T, 0)

        def getRuleIndex(self):
            return walnutParser.RULE_conditional_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterConditional_expression"):
                listener.enterConditional_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitConditional_expression"):
                listener.exitConditional_expression(self)




    def conditional_expression(self):

        localctx = walnutParser.Conditional_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_conditional_expression)
        self._la = 0 # Token type
        try:
            self.state = 208
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 203
                self.relational_expression()
                self.state = 204
                _la = self._input.LA(1)
                if not(_la==walnutParser.AND_OP_T or _la==walnutParser.OR_OP_T):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 205
                self.conditional_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 207
                self.relational_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Relational_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(walnutParser.Relational_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def math_expression(self):
            return self.getTypedRuleContext(walnutParser.Math_expressionContext,0)


        def relop_tokens(self):
            return self.getTypedRuleContext(walnutParser.Relop_tokensContext,0)


        def relational_expression(self):
            return self.getTypedRuleContext(walnutParser.Relational_expressionContext,0)


        def getRuleIndex(self):
            return walnutParser.RULE_relational_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterRelational_expression"):
                listener.enterRelational_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitRelational_expression"):
                listener.exitRelational_expression(self)




    def relational_expression(self):

        localctx = walnutParser.Relational_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_relational_expression)
        try:
            self.state = 215
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 210
                self.math_expression()
                self.state = 211
                self.relop_tokens()
                self.state = 212
                self.relational_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 214
                self.math_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Math_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(walnutParser.Math_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(walnutParser.TermContext,0)


        def math_expression(self):
            return self.getTypedRuleContext(walnutParser.Math_expressionContext,0)


        def PLUS_T(self):
            return self.getToken(walnutParser.PLUS_T, 0)

        def MINUS_T(self):
            return self.getToken(walnutParser.MINUS_T, 0)

        def getRuleIndex(self):
            return walnutParser.RULE_math_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterMath_expression"):
                listener.enterMath_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMath_expression"):
                listener.exitMath_expression(self)




    def math_expression(self):

        localctx = walnutParser.Math_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_math_expression)
        self._la = 0 # Token type
        try:
            self.state = 222
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.term()
                self.state = 218
                _la = self._input.LA(1)
                if not(_la==walnutParser.PLUS_T or _la==walnutParser.MINUS_T):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 219
                self.math_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 221
                self.term()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TermContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(walnutParser.TermContext, self).__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(walnutParser.FactorContext,0)


        def term(self):
            return self.getTypedRuleContext(walnutParser.TermContext,0)


        def MULTI_T(self):
            return self.getToken(walnutParser.MULTI_T, 0)

        def DIVISION_T(self):
            return self.getToken(walnutParser.DIVISION_T, 0)

        def getRuleIndex(self):
            return walnutParser.RULE_term

        def enterRule(self, listener):
            if hasattr(listener, "enterTerm"):
                listener.enterTerm(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTerm"):
                listener.exitTerm(self)




    def term(self):

        localctx = walnutParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.state = 229
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 224
                self.factor()
                self.state = 225
                _la = self._input.LA(1)
                if not(_la==walnutParser.DIVISION_T or _la==walnutParser.MULTI_T):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 226
                self.term()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 228
                self.factor()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FactorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(walnutParser.FactorContext, self).__init__(parent, invokingState)
            self.parser = parser

        def power_of(self):
            return self.getTypedRuleContext(walnutParser.Power_ofContext,0)


        def POW_T(self):
            return self.getToken(walnutParser.POW_T, 0)

        def factor(self):
            return self.getTypedRuleContext(walnutParser.FactorContext,0)


        def getRuleIndex(self):
            return walnutParser.RULE_factor

        def enterRule(self, listener):
            if hasattr(listener, "enterFactor"):
                listener.enterFactor(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFactor"):
                listener.exitFactor(self)




    def factor(self):

        localctx = walnutParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_factor)
        try:
            self.state = 236
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.power_of()
                self.state = 232
                self.match(walnutParser.POW_T)
                self.state = 233
                self.factor()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 235
                self.power_of()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Power_ofContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(walnutParser.Power_ofContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID_T(self):
            return self.getToken(walnutParser.ID_T, 0)

        def constants(self):
            return self.getTypedRuleContext(walnutParser.ConstantsContext,0)


        def call_object_method(self):
            return self.getTypedRuleContext(walnutParser.Call_object_methodContext,0)


        def LP_T(self):
            return self.getToken(walnutParser.LP_T, 0)

        def expression(self):
            return self.getTypedRuleContext(walnutParser.ExpressionContext,0)


        def RP_T(self):
            return self.getToken(walnutParser.RP_T, 0)

        def MINUS_T(self):
            return self.getToken(walnutParser.MINUS_T, 0)

        def NOT_T(self):
            return self.getToken(walnutParser.NOT_T, 0)

        def getRuleIndex(self):
            return walnutParser.RULE_power_of

        def enterRule(self, listener):
            if hasattr(listener, "enterPower_of"):
                listener.enterPower_of(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPower_of"):
                listener.exitPower_of(self)




    def power_of(self):

        localctx = walnutParser.Power_ofContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_power_of)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==walnutParser.NOT_T or _la==walnutParser.MINUS_T:
                self.state = 238
                _la = self._input.LA(1)
                if not(_la==walnutParser.NOT_T or _la==walnutParser.MINUS_T):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 248
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 241
                self.match(walnutParser.ID_T)
                pass

            elif la_ == 2:
                self.state = 242
                self.constants()
                pass

            elif la_ == 3:
                self.state = 243
                self.call_object_method()
                pass

            elif la_ == 4:
                self.state = 244
                self.match(walnutParser.LP_T)
                self.state = 245
                self.expression()
                self.state = 246
                self.match(walnutParser.RP_T)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Relop_tokensContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(walnutParser.Relop_tokensContext, self).__init__(parent, invokingState)
            self.parser = parser

        def EQUAL_T(self):
            return self.getToken(walnutParser.EQUAL_T, 0)

        def NOT_EQUAL_T(self):
            return self.getToken(walnutParser.NOT_EQUAL_T, 0)

        def LESS_EQ_T(self):
            return self.getToken(walnutParser.LESS_EQ_T, 0)

        def GREATER_EQ_T(self):
            return self.getToken(walnutParser.GREATER_EQ_T, 0)

        def LESS_T(self):
            return self.getToken(walnutParser.LESS_T, 0)

        def GREATER_T(self):
            return self.getToken(walnutParser.GREATER_T, 0)

        def getRuleIndex(self):
            return walnutParser.RULE_relop_tokens

        def enterRule(self, listener):
            if hasattr(listener, "enterRelop_tokens"):
                listener.enterRelop_tokens(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitRelop_tokens"):
                listener.exitRelop_tokens(self)




    def relop_tokens(self):

        localctx = walnutParser.Relop_tokensContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_relop_tokens)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << walnutParser.EQUAL_T) | (1 << walnutParser.NOT_EQUAL_T) | (1 << walnutParser.LESS_EQ_T) | (1 << walnutParser.GREATER_EQ_T) | (1 << walnutParser.LESS_T) | (1 << walnutParser.GREATER_T))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Declaration_assignmentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(walnutParser.Declaration_assignmentContext, self).__init__(parent, invokingState)
            self.parser = parser

        def declaration(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(walnutParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(walnutParser.DeclarationContext,i)


        def assignments(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(walnutParser.AssignmentsContext)
            else:
                return self.getTypedRuleContext(walnutParser.AssignmentsContext,i)


        def getRuleIndex(self):
            return walnutParser.RULE_declaration_assignment

        def enterRule(self, listener):
            if hasattr(listener, "enterDeclaration_assignment"):
                listener.enterDeclaration_assignment(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDeclaration_assignment"):
                listener.exitDeclaration_assignment(self)




    def declaration_assignment(self):

        localctx = walnutParser.Declaration_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_declaration_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 254
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [walnutParser.INT_T, walnutParser.FLOAT_T, walnutParser.STRING_T, walnutParser.BOOLEAN_T]:
                        self.state = 252
                        self.declaration()
                        pass
                    elif token in [walnutParser.ID_T]:
                        self.state = 253
                        self.assignments()
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 256 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignmentsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(walnutParser.AssignmentsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID_T(self):
            return self.getToken(walnutParser.ID_T, 0)

        def ASSIGN_T(self):
            return self.getToken(walnutParser.ASSIGN_T, 0)

        def expression(self):
            return self.getTypedRuleContext(walnutParser.ExpressionContext,0)


        def getRuleIndex(self):
            return walnutParser.RULE_assignments

        def enterRule(self, listener):
            if hasattr(listener, "enterAssignments"):
                listener.enterAssignments(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAssignments"):
                listener.exitAssignments(self)




    def assignments(self):

        localctx = walnutParser.AssignmentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_assignments)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(walnutParser.ID_T)
            self.state = 259
            self.match(walnutParser.ASSIGN_T)
            self.state = 260
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(walnutParser.DeclarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def var_type(self):
            return self.getTypedRuleContext(walnutParser.Var_typeContext,0)


        def ID_T(self):
            return self.getToken(walnutParser.ID_T, 0)

        def getRuleIndex(self):
            return walnutParser.RULE_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterDeclaration"):
                listener.enterDeclaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDeclaration"):
                listener.exitDeclaration(self)




    def declaration(self):

        localctx = walnutParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.var_type()
            self.state = 263
            self.match(walnutParser.ID_T)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LoopsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(walnutParser.LoopsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def WHILE_T(self):
            return self.getToken(walnutParser.WHILE_T, 0)

        def LP_T(self):
            return self.getToken(walnutParser.LP_T, 0)

        def expression(self):
            return self.getTypedRuleContext(walnutParser.ExpressionContext,0)


        def RP_T(self):
            return self.getToken(walnutParser.RP_T, 0)

        def LCB_T(self):
            return self.getToken(walnutParser.LCB_T, 0)

        def RCB_T(self):
            return self.getToken(walnutParser.RCB_T, 0)

        def blocks(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(walnutParser.BlocksContext)
            else:
                return self.getTypedRuleContext(walnutParser.BlocksContext,i)


        def getRuleIndex(self):
            return walnutParser.RULE_loops

        def enterRule(self, listener):
            if hasattr(listener, "enterLoops"):
                listener.enterLoops(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLoops"):
                listener.exitLoops(self)




    def loops(self):

        localctx = walnutParser.LoopsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_loops)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.match(walnutParser.WHILE_T)
            self.state = 266
            self.match(walnutParser.LP_T)
            self.state = 267
            self.expression()
            self.state = 268
            self.match(walnutParser.RP_T)
            self.state = 269
            self.match(walnutParser.LCB_T)
            self.state = 273
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << walnutParser.INT_T) | (1 << walnutParser.FLOAT_T) | (1 << walnutParser.STRING_T) | (1 << walnutParser.BOOLEAN_T) | (1 << walnutParser.IF_T) | (1 << walnutParser.WHILE_T) | (1 << walnutParser.NOT_T) | (1 << walnutParser.CTE_STRING_T) | (1 << walnutParser.CTE_INT_T) | (1 << walnutParser.CTE_FLOAT_T) | (1 << walnutParser.CTE_BOOL_T) | (1 << walnutParser.ID_T) | (1 << walnutParser.MINUS_T) | (1 << walnutParser.LP_T))) != 0):
                self.state = 270
                self.blocks()
                self.state = 275
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 276
            self.match(walnutParser.RCB_T)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConditionalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(walnutParser.ConditionalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def IF_T(self):
            return self.getToken(walnutParser.IF_T, 0)

        def if_elsif_body(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(walnutParser.If_elsif_bodyContext)
            else:
                return self.getTypedRuleContext(walnutParser.If_elsif_bodyContext,i)


        def ELSE_T(self):
            return self.getToken(walnutParser.ELSE_T, 0)

        def LCB_T(self):
            return self.getToken(walnutParser.LCB_T, 0)

        def RCB_T(self):
            return self.getToken(walnutParser.RCB_T, 0)

        def ELSEIF_T(self, i=None):
            if i is None:
                return self.getTokens(walnutParser.ELSEIF_T)
            else:
                return self.getToken(walnutParser.ELSEIF_T, i)

        def blocks(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(walnutParser.BlocksContext)
            else:
                return self.getTypedRuleContext(walnutParser.BlocksContext,i)


        def getRuleIndex(self):
            return walnutParser.RULE_conditional

        def enterRule(self, listener):
            if hasattr(listener, "enterConditional"):
                listener.enterConditional(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitConditional"):
                listener.exitConditional(self)




    def conditional(self):

        localctx = walnutParser.ConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_conditional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(walnutParser.IF_T)
            self.state = 279
            self.if_elsif_body()
            self.state = 282 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 280
                self.match(walnutParser.ELSEIF_T)
                self.state = 281
                self.if_elsif_body()
                self.state = 284 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==walnutParser.ELSEIF_T):
                    break

            self.state = 286
            self.match(walnutParser.ELSE_T)
            self.state = 287
            self.match(walnutParser.LCB_T)
            self.state = 291
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << walnutParser.INT_T) | (1 << walnutParser.FLOAT_T) | (1 << walnutParser.STRING_T) | (1 << walnutParser.BOOLEAN_T) | (1 << walnutParser.IF_T) | (1 << walnutParser.WHILE_T) | (1 << walnutParser.NOT_T) | (1 << walnutParser.CTE_STRING_T) | (1 << walnutParser.CTE_INT_T) | (1 << walnutParser.CTE_FLOAT_T) | (1 << walnutParser.CTE_BOOL_T) | (1 << walnutParser.ID_T) | (1 << walnutParser.MINUS_T) | (1 << walnutParser.LP_T))) != 0):
                self.state = 288
                self.blocks()
                self.state = 293
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 294
            self.match(walnutParser.RCB_T)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class If_elsif_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(walnutParser.If_elsif_bodyContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LP_T(self):
            return self.getToken(walnutParser.LP_T, 0)

        def expression(self):
            return self.getTypedRuleContext(walnutParser.ExpressionContext,0)


        def RP_T(self):
            return self.getToken(walnutParser.RP_T, 0)

        def LCB_T(self):
            return self.getToken(walnutParser.LCB_T, 0)

        def RCB_T(self):
            return self.getToken(walnutParser.RCB_T, 0)

        def blocks(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(walnutParser.BlocksContext)
            else:
                return self.getTypedRuleContext(walnutParser.BlocksContext,i)


        def getRuleIndex(self):
            return walnutParser.RULE_if_elsif_body

        def enterRule(self, listener):
            if hasattr(listener, "enterIf_elsif_body"):
                listener.enterIf_elsif_body(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIf_elsif_body"):
                listener.exitIf_elsif_body(self)




    def if_elsif_body(self):

        localctx = walnutParser.If_elsif_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_if_elsif_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.match(walnutParser.LP_T)
            self.state = 297
            self.expression()
            self.state = 298
            self.match(walnutParser.RP_T)
            self.state = 299
            self.match(walnutParser.LCB_T)
            self.state = 303
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << walnutParser.INT_T) | (1 << walnutParser.FLOAT_T) | (1 << walnutParser.STRING_T) | (1 << walnutParser.BOOLEAN_T) | (1 << walnutParser.IF_T) | (1 << walnutParser.WHILE_T) | (1 << walnutParser.NOT_T) | (1 << walnutParser.CTE_STRING_T) | (1 << walnutParser.CTE_INT_T) | (1 << walnutParser.CTE_FLOAT_T) | (1 << walnutParser.CTE_BOOL_T) | (1 << walnutParser.ID_T) | (1 << walnutParser.MINUS_T) | (1 << walnutParser.LP_T))) != 0):
                self.state = 300
                self.blocks()
                self.state = 305
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 306
            self.match(walnutParser.RCB_T)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Object_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(walnutParser.Object_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID_T(self, i=None):
            if i is None:
                return self.getTokens(walnutParser.ID_T)
            else:
                return self.getToken(walnutParser.ID_T, i)

        def ASSIGN_T(self):
            return self.getToken(walnutParser.ASSIGN_T, 0)

        def POINT_T(self):
            return self.getToken(walnutParser.POINT_T, 0)

        def NEW_T(self):
            return self.getToken(walnutParser.NEW_T, 0)

        def LP_T(self):
            return self.getToken(walnutParser.LP_T, 0)

        def RP_T(self):
            return self.getToken(walnutParser.RP_T, 0)

        def parameters(self):
            return self.getTypedRuleContext(walnutParser.ParametersContext,0)


        def getRuleIndex(self):
            return walnutParser.RULE_object_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterObject_declaration"):
                listener.enterObject_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitObject_declaration"):
                listener.exitObject_declaration(self)




    def object_declaration(self):

        localctx = walnutParser.Object_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_object_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.match(walnutParser.ID_T)
            self.state = 309
            self.match(walnutParser.ID_T)
            self.state = 310
            self.match(walnutParser.ASSIGN_T)
            self.state = 311
            self.match(walnutParser.ID_T)
            self.state = 312
            self.match(walnutParser.POINT_T)
            self.state = 313
            self.match(walnutParser.NEW_T)
            self.state = 314
            self.match(walnutParser.LP_T)
            self.state = 316
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << walnutParser.INT_T) | (1 << walnutParser.FLOAT_T) | (1 << walnutParser.STRING_T) | (1 << walnutParser.BOOLEAN_T))) != 0):
                self.state = 315
                self.parameters()


            self.state = 318
            self.match(walnutParser.RP_T)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Call_object_methodContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(walnutParser.Call_object_methodContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID_T(self, i=None):
            if i is None:
                return self.getTokens(walnutParser.ID_T)
            else:
                return self.getToken(walnutParser.ID_T, i)

        def POINT_T(self):
            return self.getToken(walnutParser.POINT_T, 0)

        def LP_T(self):
            return self.getToken(walnutParser.LP_T, 0)

        def parameters(self):
            return self.getTypedRuleContext(walnutParser.ParametersContext,0)


        def RP_T(self):
            return self.getToken(walnutParser.RP_T, 0)

        def getRuleIndex(self):
            return walnutParser.RULE_call_object_method

        def enterRule(self, listener):
            if hasattr(listener, "enterCall_object_method"):
                listener.enterCall_object_method(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCall_object_method"):
                listener.exitCall_object_method(self)




    def call_object_method(self):

        localctx = walnutParser.Call_object_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_call_object_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.match(walnutParser.ID_T)
            self.state = 321
            self.match(walnutParser.POINT_T)
            self.state = 322
            self.match(walnutParser.ID_T)
            self.state = 323
            self.match(walnutParser.LP_T)
            self.state = 324
            self.parameters()
            self.state = 325
            self.match(walnutParser.RP_T)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Var_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(walnutParser.Var_typeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def INT_T(self):
            return self.getToken(walnutParser.INT_T, 0)

        def STRING_T(self):
            return self.getToken(walnutParser.STRING_T, 0)

        def FLOAT_T(self):
            return self.getToken(walnutParser.FLOAT_T, 0)

        def BOOLEAN_T(self):
            return self.getToken(walnutParser.BOOLEAN_T, 0)

        def getRuleIndex(self):
            return walnutParser.RULE_var_type

        def enterRule(self, listener):
            if hasattr(listener, "enterVar_type"):
                listener.enterVar_type(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitVar_type"):
                listener.exitVar_type(self)




    def var_type(self):

        localctx = walnutParser.Var_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_var_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << walnutParser.INT_T) | (1 << walnutParser.FLOAT_T) | (1 << walnutParser.STRING_T) | (1 << walnutParser.BOOLEAN_T))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConstantsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(walnutParser.ConstantsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def CTE_FLOAT_T(self):
            return self.getToken(walnutParser.CTE_FLOAT_T, 0)

        def CTE_INT_T(self):
            return self.getToken(walnutParser.CTE_INT_T, 0)

        def CTE_STRING_T(self):
            return self.getToken(walnutParser.CTE_STRING_T, 0)

        def CTE_BOOL_T(self):
            return self.getToken(walnutParser.CTE_BOOL_T, 0)

        def getRuleIndex(self):
            return walnutParser.RULE_constants

        def enterRule(self, listener):
            if hasattr(listener, "enterConstants"):
                listener.enterConstants(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitConstants"):
                listener.exitConstants(self)




    def constants(self):

        localctx = walnutParser.ConstantsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_constants)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << walnutParser.CTE_STRING_T) | (1 << walnutParser.CTE_INT_T) | (1 << walnutParser.CTE_FLOAT_T) | (1 << walnutParser.CTE_BOOL_T))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





