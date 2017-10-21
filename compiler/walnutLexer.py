# Generated from walnut.g4 by ANTLR 4.7
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys


from vm import VM


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2")
        buf.write(u"\65\u0160\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6")
        buf.write(u"\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4")
        buf.write(u"\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t")
        buf.write(u"\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27")
        buf.write(u"\4\30\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4")
        buf.write(u"\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t")
        buf.write(u"#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4")
        buf.write(u",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62")
        buf.write(u"\4\63\t\63\4\64\t\64\4\65\t\65\4\66\t\66\3\2\3\2\3\3")
        buf.write(u"\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5")
        buf.write(u"\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7")
        buf.write(u"\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t")
        buf.write(u"\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3")
        buf.write(u"\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write(u"\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3")
        buf.write(u"\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write(u"\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3")
        buf.write(u"\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write(u"\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3")
        buf.write(u"\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write(u"\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30\3")
        buf.write(u"\30\3\30\5\30\u00fc\n\30\3\31\3\31\3\31\3\31\5\31\u0102")
        buf.write(u"\n\31\3\32\3\32\3\32\3\32\3\32\5\32\u0109\n\32\3\33\3")
        buf.write(u"\33\3\33\3\33\5\33\u010f\n\33\3\34\3\34\3\34\3\34\3\35")
        buf.write(u"\3\35\7\35\u0117\n\35\f\35\16\35\u011a\13\35\3\35\3\35")
        buf.write(u"\3\36\6\36\u011f\n\36\r\36\16\36\u0120\3\37\3\37\3\37")
        buf.write(u"\3\37\3 \3 \5 \u0129\n \3!\3!\3!\3!\7!\u012f\n!\f!\16")
        buf.write(u"!\u0132\13!\3\"\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3%\3&\3")
        buf.write(u"&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3")
        buf.write(u"/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64")
        buf.write(u"\3\65\3\65\3\66\3\66\3\u0118\2\67\3\2\5\2\7\3\t\4\13")
        buf.write(u"\5\r\6\17\7\21\b\23\t\25\n\27\13\31\f\33\r\35\16\37\17")
        buf.write(u"!\20#\21%\22\'\23)\24+\25-\26/\27\61\30\63\31\65\32\67")
        buf.write(u"\339\34;\35=\36?\37A C!E\"G#I$K%M&O\'Q(S)U*W+Y,[-]._")
        buf.write(u"/a\60c\61e\62g\63i\64k\65\3\2\5\3\2\62;\4\2C\\c|\5\2")
        buf.write(u"\13\f\17\17\"\"\2\u0167\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write(u"\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write(u"\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3")
        buf.write(u"\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2")
        buf.write(u"\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3")
        buf.write(u"\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2")
        buf.write(u"\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2")
        buf.write(u"?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2")
        buf.write(u"\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2")
        buf.write(u"\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2")
        buf.write(u"\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3")
        buf.write(u"\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\3m\3\2\2\2\5")
        buf.write(u"o\3\2\2\2\7q\3\2\2\2\ty\3\2\2\2\13\u0081\3\2\2\2\r\u0088")
        buf.write(u"\3\2\2\2\17\u008c\3\2\2\2\21\u0092\3\2\2\2\23\u0099\3")
        buf.write(u"\2\2\2\25\u00a1\3\2\2\2\27\u00a7\3\2\2\2\31\u00af\3\2")
        buf.write(u"\2\2\33\u00b2\3\2\2\2\35\u00b9\3\2\2\2\37\u00be\3\2\2")
        buf.write(u"\2!\u00c3\3\2\2\2#\u00c9\3\2\2\2%\u00d4\3\2\2\2\'\u00dc")
        buf.write(u"\3\2\2\2)\u00e1\3\2\2\2+\u00ed\3\2\2\2-\u00f3\3\2\2\2")
        buf.write(u"/\u00fb\3\2\2\2\61\u0101\3\2\2\2\63\u0108\3\2\2\2\65")
        buf.write(u"\u010e\3\2\2\2\67\u0110\3\2\2\29\u0114\3\2\2\2;\u011e")
        buf.write(u"\3\2\2\2=\u0122\3\2\2\2?\u0128\3\2\2\2A\u012a\3\2\2\2")
        buf.write(u"C\u0133\3\2\2\2E\u0136\3\2\2\2G\u0138\3\2\2\2I\u013b")
        buf.write(u"\3\2\2\2K\u013e\3\2\2\2M\u0140\3\2\2\2O\u0142\3\2\2\2")
        buf.write(u"Q\u0144\3\2\2\2S\u0146\3\2\2\2U\u0148\3\2\2\2W\u014a")
        buf.write(u"\3\2\2\2Y\u014c\3\2\2\2[\u014e\3\2\2\2]\u0150\3\2\2\2")
        buf.write(u"_\u0152\3\2\2\2a\u0154\3\2\2\2c\u0156\3\2\2\2e\u0158")
        buf.write(u"\3\2\2\2g\u015a\3\2\2\2i\u015c\3\2\2\2k\u015e\3\2\2\2")
        buf.write(u"mn\t\2\2\2n\4\3\2\2\2op\t\3\2\2p\6\3\2\2\2qr\7r\2\2r")
        buf.write(u"s\7t\2\2st\7q\2\2tu\7i\2\2uv\7t\2\2vw\7c\2\2wx\7o\2\2")
        buf.write(u"x\b\3\2\2\2yz\7i\2\2z{\7n\2\2{|\7q\2\2|}\7d\2\2}~\7c")
        buf.write(u"\2\2~\177\7n\2\2\177\u0080\7u\2\2\u0080\n\3\2\2\2\u0081")
        buf.write(u"\u0082\7t\2\2\u0082\u0083\7g\2\2\u0083\u0084\7v\2\2\u0084")
        buf.write(u"\u0085\7w\2\2\u0085\u0086\7t\2\2\u0086\u0087\7p\2\2\u0087")
        buf.write(u"\f\3\2\2\2\u0088\u0089\7k\2\2\u0089\u008a\7p\2\2\u008a")
        buf.write(u"\u008b\7v\2\2\u008b\16\3\2\2\2\u008c\u008d\7h\2\2\u008d")
        buf.write(u"\u008e\7n\2\2\u008e\u008f\7q\2\2\u008f\u0090\7c\2\2\u0090")
        buf.write(u"\u0091\7v\2\2\u0091\20\3\2\2\2\u0092\u0093\7u\2\2\u0093")
        buf.write(u"\u0094\7v\2\2\u0094\u0095\7t\2\2\u0095\u0096\7k\2\2\u0096")
        buf.write(u"\u0097\7p\2\2\u0097\u0098\7i\2\2\u0098\22\3\2\2\2\u0099")
        buf.write(u"\u009a\7d\2\2\u009a\u009b\7q\2\2\u009b\u009c\7q\2\2\u009c")
        buf.write(u"\u009d\7n\2\2\u009d\u009e\7g\2\2\u009e\u009f\7c\2\2\u009f")
        buf.write(u"\u00a0\7p\2\2\u00a0\24\3\2\2\2\u00a1\u00a2\7e\2\2\u00a2")
        buf.write(u"\u00a3\7n\2\2\u00a3\u00a4\7c\2\2\u00a4\u00a5\7u\2\2\u00a5")
        buf.write(u"\u00a6\7u\2\2\u00a6\26\3\2\2\2\u00a7\u00a8\7g\2\2\u00a8")
        buf.write(u"\u00a9\7z\2\2\u00a9\u00aa\7v\2\2\u00aa\u00ab\7g\2\2\u00ab")
        buf.write(u"\u00ac\7p\2\2\u00ac\u00ad\7f\2\2\u00ad\u00ae\7u\2\2\u00ae")
        buf.write(u"\30\3\2\2\2\u00af\u00b0\7k\2\2\u00b0\u00b1\7h\2\2\u00b1")
        buf.write(u"\32\3\2\2\2\u00b2\u00b3\7g\2\2\u00b3\u00b4\7n\2\2\u00b4")
        buf.write(u"\u00b5\7u\2\2\u00b5\u00b6\7g\2\2\u00b6\u00b7\7k\2\2\u00b7")
        buf.write(u"\u00b8\7h\2\2\u00b8\34\3\2\2\2\u00b9\u00ba\7g\2\2\u00ba")
        buf.write(u"\u00bb\7n\2\2\u00bb\u00bc\7u\2\2\u00bc\u00bd\7g\2\2\u00bd")
        buf.write(u"\36\3\2\2\2\u00be\u00bf\7v\2\2\u00bf\u00c0\7t\2\2\u00c0")
        buf.write(u"\u00c1\7w\2\2\u00c1\u00c2\7g\2\2\u00c2 \3\2\2\2\u00c3")
        buf.write(u"\u00c4\7h\2\2\u00c4\u00c5\7c\2\2\u00c5\u00c6\7n\2\2\u00c6")
        buf.write(u"\u00c7\7u\2\2\u00c7\u00c8\7g\2\2\u00c8\"\3\2\2\2\u00c9")
        buf.write(u"\u00ca\7c\2\2\u00ca\u00cb\7v\2\2\u00cb\u00cc\7v\2\2\u00cc")
        buf.write(u"\u00cd\7t\2\2\u00cd\u00ce\7k\2\2\u00ce\u00cf\7d\2\2\u00cf")
        buf.write(u"\u00d0\7w\2\2\u00d0\u00d1\7v\2\2\u00d1\u00d2\7g\2\2\u00d2")
        buf.write(u"\u00d3\7u\2\2\u00d3$\3\2\2\2\u00d4\u00d5\7o\2\2\u00d5")
        buf.write(u"\u00d6\7g\2\2\u00d6\u00d7\7v\2\2\u00d7\u00d8\7j\2\2\u00d8")
        buf.write(u"\u00d9\7q\2\2\u00d9\u00da\7f\2\2\u00da\u00db\7u\2\2\u00db")
        buf.write(u"&\3\2\2\2\u00dc\u00dd\7h\2\2\u00dd\u00de\7w\2\2\u00de")
        buf.write(u"\u00df\7p\2\2\u00df\u00e0\7e\2\2\u00e0(\3\2\2\2\u00e1")
        buf.write(u"\u00e2\7k\2\2\u00e2\u00e3\7p\2\2\u00e3\u00e4\7k\2\2\u00e4")
        buf.write(u"\u00e5\7v\2\2\u00e5\u00e6\7k\2\2\u00e6\u00e7\7c\2\2\u00e7")
        buf.write(u"\u00e8\7n\2\2\u00e8\u00e9\7k\2\2\u00e9\u00ea\7|\2\2\u00ea")
        buf.write(u"\u00eb\7g\2\2\u00eb\u00ec\7t\2\2\u00ec*\3\2\2\2\u00ed")
        buf.write(u"\u00ee\7y\2\2\u00ee\u00ef\7j\2\2\u00ef\u00f0\7k\2\2\u00f0")
        buf.write(u"\u00f1\7n\2\2\u00f1\u00f2\7g\2\2\u00f2,\3\2\2\2\u00f3")
        buf.write(u"\u00f4\7p\2\2\u00f4\u00f5\7g\2\2\u00f5\u00f6\7y\2\2\u00f6")
        buf.write(u".\3\2\2\2\u00f7\u00f8\7?\2\2\u00f8\u00fc\7?\2\2\u00f9")
        buf.write(u"\u00fa\7k\2\2\u00fa\u00fc\7u\2\2\u00fb\u00f7\3\2\2\2")
        buf.write(u"\u00fb\u00f9\3\2\2\2\u00fc\60\3\2\2\2\u00fd\u0102\7#")
        buf.write(u"\2\2\u00fe\u00ff\7p\2\2\u00ff\u0100\7q\2\2\u0100\u0102")
        buf.write(u"\7v\2\2\u0101\u00fd\3\2\2\2\u0101\u00fe\3\2\2\2\u0102")
        buf.write(u"\62\3\2\2\2\u0103\u0104\7(\2\2\u0104\u0109\7(\2\2\u0105")
        buf.write(u"\u0106\7c\2\2\u0106\u0107\7p\2\2\u0107\u0109\7f\2\2\u0108")
        buf.write(u"\u0103\3\2\2\2\u0108\u0105\3\2\2\2\u0109\64\3\2\2\2\u010a")
        buf.write(u"\u010b\7~\2\2\u010b\u010f\7~\2\2\u010c\u010d\7q\2\2\u010d")
        buf.write(u"\u010f\7t\2\2\u010e\u010a\3\2\2\2\u010e\u010c\3\2\2\2")
        buf.write(u"\u010f\66\3\2\2\2\u0110\u0111\t\4\2\2\u0111\u0112\3\2")
        buf.write(u"\2\2\u0112\u0113\b\34\2\2\u01138\3\2\2\2\u0114\u0118")
        buf.write(u"\7$\2\2\u0115\u0117\13\2\2\2\u0116\u0115\3\2\2\2\u0117")
        buf.write(u"\u011a\3\2\2\2\u0118\u0119\3\2\2\2\u0118\u0116\3\2\2")
        buf.write(u"\2\u0119\u011b\3\2\2\2\u011a\u0118\3\2\2\2\u011b\u011c")
        buf.write(u"\7$\2\2\u011c:\3\2\2\2\u011d\u011f\5\3\2\2\u011e\u011d")
        buf.write(u"\3\2\2\2\u011f\u0120\3\2\2\2\u0120\u011e\3\2\2\2\u0120")
        buf.write(u"\u0121\3\2\2\2\u0121<\3\2\2\2\u0122\u0123\5\3\2\2\u0123")
        buf.write(u"\u0124\13\2\2\2\u0124\u0125\5\3\2\2\u0125>\3\2\2\2\u0126")
        buf.write(u"\u0129\5\37\20\2\u0127\u0129\5!\21\2\u0128\u0126\3\2")
        buf.write(u"\2\2\u0128\u0127\3\2\2\2\u0129@\3\2\2\2\u012a\u0130\5")
        buf.write(u"\5\3\2\u012b\u012f\5\5\3\2\u012c\u012f\7a\2\2\u012d\u012f")
        buf.write(u"\5\3\2\2\u012e\u012b\3\2\2\2\u012e\u012c\3\2\2\2\u012e")
        buf.write(u"\u012d\3\2\2\2\u012f\u0132\3\2\2\2\u0130\u012e\3\2\2")
        buf.write(u"\2\u0130\u0131\3\2\2\2\u0131B\3\2\2\2\u0132\u0130\3\2")
        buf.write(u"\2\2\u0133\u0134\7#\2\2\u0134\u0135\7?\2\2\u0135D\3\2")
        buf.write(u"\2\2\u0136\u0137\7?\2\2\u0137F\3\2\2\2\u0138\u0139\7")
        buf.write(u">\2\2\u0139\u013a\7?\2\2\u013aH\3\2\2\2\u013b\u013c\7")
        buf.write(u"@\2\2\u013c\u013d\7?\2\2\u013dJ\3\2\2\2\u013e\u013f\7")
        buf.write(u">\2\2\u013fL\3\2\2\2\u0140\u0141\7@\2\2\u0141N\3\2\2")
        buf.write(u"\2\u0142\u0143\7`\2\2\u0143P\3\2\2\2\u0144\u0145\7\61")
        buf.write(u"\2\2\u0145R\3\2\2\2\u0146\u0147\7,\2\2\u0147T\3\2\2\2")
        buf.write(u"\u0148\u0149\7-\2\2\u0149V\3\2\2\2\u014a\u014b\7/\2\2")
        buf.write(u"\u014bX\3\2\2\2\u014c\u014d\7.\2\2\u014dZ\3\2\2\2\u014e")
        buf.write(u"\u014f\7*\2\2\u014f\\\3\2\2\2\u0150\u0151\7+\2\2\u0151")
        buf.write(u"^\3\2\2\2\u0152\u0153\7]\2\2\u0153`\3\2\2\2\u0154\u0155")
        buf.write(u"\7_\2\2\u0155b\3\2\2\2\u0156\u0157\7}\2\2\u0157d\3\2")
        buf.write(u"\2\2\u0158\u0159\7\177\2\2\u0159f\3\2\2\2\u015a\u015b")
        buf.write(u"\7\60\2\2\u015bh\3\2\2\2\u015c\u015d\7=\2\2\u015dj\3")
        buf.write(u"\2\2\2\u015e\u015f\7<\2\2\u015fl\3\2\2\2\f\2\u00fb\u0101")
        buf.write(u"\u0108\u010e\u0118\u0120\u0128\u012e\u0130\3\b\2\2")
        return buf.getvalue()


class walnutLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PROGRAM_T = 1
    GLOBALS_T = 2
    RETURN_T = 3
    INT_T = 4
    FLOAT_T = 5
    STRING_T = 6
    BOOLEAN_T = 7
    CLASS_T = 8
    EXTENDS_T = 9
    IF_T = 10
    ELSEIF_T = 11
    ELSE_T = 12
    TRUE_T = 13
    FALSE_T = 14
    ATTRS_T = 15
    METHODS_T = 16
    FUNC_T = 17
    INIT_T = 18
    WHILE_T = 19
    NEW_T = 20
    EQUAL_T = 21
    NOT_T = 22
    AND_OP_T = 23
    OR_OP_T = 24
    WS = 25
    CTE_STRING_T = 26
    CTE_INT_T = 27
    CTE_FLOAT_T = 28
    CTE_BOOL_T = 29
    ID_T = 30
    NOT_EQUAL_T = 31
    ASSIGN_T = 32
    LESS_EQ_T = 33
    GREATER_EQ_T = 34
    LESS_T = 35
    GREATER_T = 36
    POW_T = 37
    DIVISION_T = 38
    MULTI_T = 39
    PLUS_T = 40
    MINUS_T = 41
    COMMA_T = 42
    LP_T = 43
    RP_T = 44
    LB_T = 45
    RB_T = 46
    LCB_T = 47
    RCB_T = 48
    POINT_T = 49
    END_OF_STM_T = 50
    RETURN_TYPE_T = 51

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"'program'", u"'globals'", u"'return'", u"'int'", u"'float'", 
            u"'string'", u"'boolean'", u"'class'", u"'extends'", u"'if'", 
            u"'elseif'", u"'else'", u"'true'", u"'false'", u"'attributes'", 
            u"'methods'", u"'func'", u"'initializer'", u"'while'", u"'new'", 
            u"'!='", u"'='", u"'<='", u"'>='", u"'<'", u"'>'", u"'^'", u"'/'", 
            u"'*'", u"'+'", u"'-'", u"','", u"'('", u"')'", u"'['", u"']'", 
            u"'{'", u"'}'", u"'.'", u"';'", u"':'" ]

    symbolicNames = [ u"<INVALID>",
            u"PROGRAM_T", u"GLOBALS_T", u"RETURN_T", u"INT_T", u"FLOAT_T", 
            u"STRING_T", u"BOOLEAN_T", u"CLASS_T", u"EXTENDS_T", u"IF_T", 
            u"ELSEIF_T", u"ELSE_T", u"TRUE_T", u"FALSE_T", u"ATTRS_T", u"METHODS_T", 
            u"FUNC_T", u"INIT_T", u"WHILE_T", u"NEW_T", u"EQUAL_T", u"NOT_T", 
            u"AND_OP_T", u"OR_OP_T", u"WS", u"CTE_STRING_T", u"CTE_INT_T", 
            u"CTE_FLOAT_T", u"CTE_BOOL_T", u"ID_T", u"NOT_EQUAL_T", u"ASSIGN_T", 
            u"LESS_EQ_T", u"GREATER_EQ_T", u"LESS_T", u"GREATER_T", u"POW_T", 
            u"DIVISION_T", u"MULTI_T", u"PLUS_T", u"MINUS_T", u"COMMA_T", 
            u"LP_T", u"RP_T", u"LB_T", u"RB_T", u"LCB_T", u"RCB_T", u"POINT_T", 
            u"END_OF_STM_T", u"RETURN_TYPE_T" ]

    ruleNames = [ u"DIGIT", u"LETTER", u"PROGRAM_T", u"GLOBALS_T", u"RETURN_T", 
                  u"INT_T", u"FLOAT_T", u"STRING_T", u"BOOLEAN_T", u"CLASS_T", 
                  u"EXTENDS_T", u"IF_T", u"ELSEIF_T", u"ELSE_T", u"TRUE_T", 
                  u"FALSE_T", u"ATTRS_T", u"METHODS_T", u"FUNC_T", u"INIT_T", 
                  u"WHILE_T", u"NEW_T", u"EQUAL_T", u"NOT_T", u"AND_OP_T", 
                  u"OR_OP_T", u"WS", u"CTE_STRING_T", u"CTE_INT_T", u"CTE_FLOAT_T", 
                  u"CTE_BOOL_T", u"ID_T", u"NOT_EQUAL_T", u"ASSIGN_T", u"LESS_EQ_T", 
                  u"GREATER_EQ_T", u"LESS_T", u"GREATER_T", u"POW_T", u"DIVISION_T", 
                  u"MULTI_T", u"PLUS_T", u"MINUS_T", u"COMMA_T", u"LP_T", 
                  u"RP_T", u"LB_T", u"RB_T", u"LCB_T", u"RCB_T", u"POINT_T", 
                  u"END_OF_STM_T", u"RETURN_TYPE_T" ]

    grammarFileName = u"walnut.g4"

    def __init__(self, input=None, output=sys.stdout):
        super(walnutLexer, self).__init__(input, output=output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    global virtual_machine
    virtual_machine = VM()


