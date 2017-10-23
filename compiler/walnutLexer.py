# Generated from walnut.g4 by ANTLR 4.7
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys


import pprint
from engine import Engine


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2")
        buf.write(u"\66\u0173\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6")
        buf.write(u"\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4")
        buf.write(u"\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t")
        buf.write(u"\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27")
        buf.write(u"\4\30\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4")
        buf.write(u"\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t")
        buf.write(u"#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4")
        buf.write(u",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62")
        buf.write(u"\4\63\t\63\4\64\t\64\4\65\t\65\4\66\t\66\4\67\t\67\3")
        buf.write(u"\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3")
        buf.write(u"\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write(u"\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3")
        buf.write(u"\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write(u"\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write(u"\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write(u"\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write(u"\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3")
        buf.write(u"\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write(u"\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3")
        buf.write(u"\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write(u"\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3")
        buf.write(u"\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write(u"\3\32\5\32\u0106\n\32\3\33\3\33\3\33\3\33\5\33\u010c")
        buf.write(u"\n\33\3\34\3\34\3\34\3\34\3\34\5\34\u0113\n\34\3\35\3")
        buf.write(u"\35\3\35\3\35\5\35\u0119\n\35\3\36\3\36\3\36\3\36\3\37")
        buf.write(u"\3\37\7\37\u0121\n\37\f\37\16\37\u0124\13\37\3\37\3\37")
        buf.write(u"\3 \5 \u0129\n \3 \6 \u012c\n \r \16 \u012d\3 \3 \6 ")
        buf.write(u"\u0132\n \r \16 \u0133\3!\5!\u0137\n!\3!\6!\u013a\n!")
        buf.write(u"\r!\16!\u013b\3\"\3\"\3\"\3\"\7\"\u0142\n\"\f\"\16\"")
        buf.write(u"\u0145\13\"\3#\3#\3#\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'")
        buf.write(u"\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60")
        buf.write(u"\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3")
        buf.write(u"\65\3\66\3\66\3\67\3\67\3\u0122\28\3\2\5\2\7\3\t\4\13")
        buf.write(u"\5\r\6\17\7\21\b\23\t\25\n\27\13\31\f\33\r\35\16\37\17")
        buf.write(u"!\20#\21%\22\'\23)\24+\25-\26/\27\61\30\63\31\65\32\67")
        buf.write(u"\339\34;\35=\36?\37A C!E\"G#I$K%M&O\'Q(S)U*W+Y,[-]._")
        buf.write(u"/a\60c\61e\62g\63i\64k\65m\66\3\2\5\3\2\62;\4\2C\\c|")
        buf.write(u"\5\2\13\f\17\17\"\"\2\u017d\2\7\3\2\2\2\2\t\3\2\2\2\2")
        buf.write(u"\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23")
        buf.write(u"\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33")
        buf.write(u"\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2")
        buf.write(u"\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-")
        buf.write(u"\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3")
        buf.write(u"\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write(u"\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write(u"\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write(u"\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write(u"\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2")
        buf.write(u"e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2")
        buf.write(u"\3o\3\2\2\2\5q\3\2\2\2\7s\3\2\2\2\t{\3\2\2\2\13\u0083")
        buf.write(u"\3\2\2\2\r\u008a\3\2\2\2\17\u008e\3\2\2\2\21\u0094\3")
        buf.write(u"\2\2\2\23\u009b\3\2\2\2\25\u00a3\3\2\2\2\27\u00a9\3\2")
        buf.write(u"\2\2\31\u00b1\3\2\2\2\33\u00b4\3\2\2\2\35\u00bb\3\2\2")
        buf.write(u"\2\37\u00c0\3\2\2\2!\u00c5\3\2\2\2#\u00cb\3\2\2\2%\u00d6")
        buf.write(u"\3\2\2\2\'\u00de\3\2\2\2)\u00e3\3\2\2\2+\u00ef\3\2\2")
        buf.write(u"\2-\u00f5\3\2\2\2/\u00f9\3\2\2\2\61\u00fd\3\2\2\2\63")
        buf.write(u"\u0105\3\2\2\2\65\u010b\3\2\2\2\67\u0112\3\2\2\29\u0118")
        buf.write(u"\3\2\2\2;\u011a\3\2\2\2=\u011e\3\2\2\2?\u0128\3\2\2\2")
        buf.write(u"A\u0136\3\2\2\2C\u013d\3\2\2\2E\u0146\3\2\2\2G\u0149")
        buf.write(u"\3\2\2\2I\u014b\3\2\2\2K\u014e\3\2\2\2M\u0151\3\2\2\2")
        buf.write(u"O\u0153\3\2\2\2Q\u0155\3\2\2\2S\u0157\3\2\2\2U\u0159")
        buf.write(u"\3\2\2\2W\u015b\3\2\2\2Y\u015d\3\2\2\2[\u015f\3\2\2\2")
        buf.write(u"]\u0161\3\2\2\2_\u0163\3\2\2\2a\u0165\3\2\2\2c\u0167")
        buf.write(u"\3\2\2\2e\u0169\3\2\2\2g\u016b\3\2\2\2i\u016d\3\2\2\2")
        buf.write(u"k\u016f\3\2\2\2m\u0171\3\2\2\2op\t\2\2\2p\4\3\2\2\2q")
        buf.write(u"r\t\3\2\2r\6\3\2\2\2st\7r\2\2tu\7t\2\2uv\7q\2\2vw\7i")
        buf.write(u"\2\2wx\7t\2\2xy\7c\2\2yz\7o\2\2z\b\3\2\2\2{|\7i\2\2|")
        buf.write(u"}\7n\2\2}~\7q\2\2~\177\7d\2\2\177\u0080\7c\2\2\u0080")
        buf.write(u"\u0081\7n\2\2\u0081\u0082\7u\2\2\u0082\n\3\2\2\2\u0083")
        buf.write(u"\u0084\7t\2\2\u0084\u0085\7g\2\2\u0085\u0086\7v\2\2\u0086")
        buf.write(u"\u0087\7w\2\2\u0087\u0088\7t\2\2\u0088\u0089\7p\2\2\u0089")
        buf.write(u"\f\3\2\2\2\u008a\u008b\7k\2\2\u008b\u008c\7p\2\2\u008c")
        buf.write(u"\u008d\7v\2\2\u008d\16\3\2\2\2\u008e\u008f\7h\2\2\u008f")
        buf.write(u"\u0090\7n\2\2\u0090\u0091\7q\2\2\u0091\u0092\7c\2\2\u0092")
        buf.write(u"\u0093\7v\2\2\u0093\20\3\2\2\2\u0094\u0095\7u\2\2\u0095")
        buf.write(u"\u0096\7v\2\2\u0096\u0097\7t\2\2\u0097\u0098\7k\2\2\u0098")
        buf.write(u"\u0099\7p\2\2\u0099\u009a\7i\2\2\u009a\22\3\2\2\2\u009b")
        buf.write(u"\u009c\7d\2\2\u009c\u009d\7q\2\2\u009d\u009e\7q\2\2\u009e")
        buf.write(u"\u009f\7n\2\2\u009f\u00a0\7g\2\2\u00a0\u00a1\7c\2\2\u00a1")
        buf.write(u"\u00a2\7p\2\2\u00a2\24\3\2\2\2\u00a3\u00a4\7e\2\2\u00a4")
        buf.write(u"\u00a5\7n\2\2\u00a5\u00a6\7c\2\2\u00a6\u00a7\7u\2\2\u00a7")
        buf.write(u"\u00a8\7u\2\2\u00a8\26\3\2\2\2\u00a9\u00aa\7g\2\2\u00aa")
        buf.write(u"\u00ab\7z\2\2\u00ab\u00ac\7v\2\2\u00ac\u00ad\7g\2\2\u00ad")
        buf.write(u"\u00ae\7p\2\2\u00ae\u00af\7f\2\2\u00af\u00b0\7u\2\2\u00b0")
        buf.write(u"\30\3\2\2\2\u00b1\u00b2\7k\2\2\u00b2\u00b3\7h\2\2\u00b3")
        buf.write(u"\32\3\2\2\2\u00b4\u00b5\7g\2\2\u00b5\u00b6\7n\2\2\u00b6")
        buf.write(u"\u00b7\7u\2\2\u00b7\u00b8\7g\2\2\u00b8\u00b9\7k\2\2\u00b9")
        buf.write(u"\u00ba\7h\2\2\u00ba\34\3\2\2\2\u00bb\u00bc\7g\2\2\u00bc")
        buf.write(u"\u00bd\7n\2\2\u00bd\u00be\7u\2\2\u00be\u00bf\7g\2\2\u00bf")
        buf.write(u"\36\3\2\2\2\u00c0\u00c1\7v\2\2\u00c1\u00c2\7t\2\2\u00c2")
        buf.write(u"\u00c3\7w\2\2\u00c3\u00c4\7g\2\2\u00c4 \3\2\2\2\u00c5")
        buf.write(u"\u00c6\7h\2\2\u00c6\u00c7\7c\2\2\u00c7\u00c8\7n\2\2\u00c8")
        buf.write(u"\u00c9\7u\2\2\u00c9\u00ca\7g\2\2\u00ca\"\3\2\2\2\u00cb")
        buf.write(u"\u00cc\7c\2\2\u00cc\u00cd\7v\2\2\u00cd\u00ce\7v\2\2\u00ce")
        buf.write(u"\u00cf\7t\2\2\u00cf\u00d0\7k\2\2\u00d0\u00d1\7d\2\2\u00d1")
        buf.write(u"\u00d2\7w\2\2\u00d2\u00d3\7v\2\2\u00d3\u00d4\7g\2\2\u00d4")
        buf.write(u"\u00d5\7u\2\2\u00d5$\3\2\2\2\u00d6\u00d7\7o\2\2\u00d7")
        buf.write(u"\u00d8\7g\2\2\u00d8\u00d9\7v\2\2\u00d9\u00da\7j\2\2\u00da")
        buf.write(u"\u00db\7q\2\2\u00db\u00dc\7f\2\2\u00dc\u00dd\7u\2\2\u00dd")
        buf.write(u"&\3\2\2\2\u00de\u00df\7h\2\2\u00df\u00e0\7w\2\2\u00e0")
        buf.write(u"\u00e1\7p\2\2\u00e1\u00e2\7e\2\2\u00e2(\3\2\2\2\u00e3")
        buf.write(u"\u00e4\7k\2\2\u00e4\u00e5\7p\2\2\u00e5\u00e6\7k\2\2\u00e6")
        buf.write(u"\u00e7\7v\2\2\u00e7\u00e8\7k\2\2\u00e8\u00e9\7c\2\2\u00e9")
        buf.write(u"\u00ea\7n\2\2\u00ea\u00eb\7k\2\2\u00eb\u00ec\7|\2\2\u00ec")
        buf.write(u"\u00ed\7g\2\2\u00ed\u00ee\7t\2\2\u00ee*\3\2\2\2\u00ef")
        buf.write(u"\u00f0\7y\2\2\u00f0\u00f1\7j\2\2\u00f1\u00f2\7k\2\2\u00f2")
        buf.write(u"\u00f3\7n\2\2\u00f3\u00f4\7g\2\2\u00f4,\3\2\2\2\u00f5")
        buf.write(u"\u00f6\7p\2\2\u00f6\u00f7\7g\2\2\u00f7\u00f8\7y\2\2\u00f8")
        buf.write(u".\3\2\2\2\u00f9\u00fa\7t\2\2\u00fa\u00fb\7w\2\2\u00fb")
        buf.write(u"\u00fc\7p\2\2\u00fc\60\3\2\2\2\u00fd\u00fe\7g\2\2\u00fe")
        buf.write(u"\u00ff\7p\2\2\u00ff\u0100\7f\2\2\u0100\62\3\2\2\2\u0101")
        buf.write(u"\u0102\7?\2\2\u0102\u0106\7?\2\2\u0103\u0104\7k\2\2\u0104")
        buf.write(u"\u0106\7u\2\2\u0105\u0101\3\2\2\2\u0105\u0103\3\2\2\2")
        buf.write(u"\u0106\64\3\2\2\2\u0107\u010c\7#\2\2\u0108\u0109\7p\2")
        buf.write(u"\2\u0109\u010a\7q\2\2\u010a\u010c\7v\2\2\u010b\u0107")
        buf.write(u"\3\2\2\2\u010b\u0108\3\2\2\2\u010c\66\3\2\2\2\u010d\u010e")
        buf.write(u"\7(\2\2\u010e\u0113\7(\2\2\u010f\u0110\7c\2\2\u0110\u0111")
        buf.write(u"\7p\2\2\u0111\u0113\7f\2\2\u0112\u010d\3\2\2\2\u0112")
        buf.write(u"\u010f\3\2\2\2\u01138\3\2\2\2\u0114\u0115\7~\2\2\u0115")
        buf.write(u"\u0119\7~\2\2\u0116\u0117\7q\2\2\u0117\u0119\7t\2\2\u0118")
        buf.write(u"\u0114\3\2\2\2\u0118\u0116\3\2\2\2\u0119:\3\2\2\2\u011a")
        buf.write(u"\u011b\t\4\2\2\u011b\u011c\3\2\2\2\u011c\u011d\b\36\2")
        buf.write(u"\2\u011d<\3\2\2\2\u011e\u0122\7$\2\2\u011f\u0121\13\2")
        buf.write(u"\2\2\u0120\u011f\3\2\2\2\u0121\u0124\3\2\2\2\u0122\u0123")
        buf.write(u"\3\2\2\2\u0122\u0120\3\2\2\2\u0123\u0125\3\2\2\2\u0124")
        buf.write(u"\u0122\3\2\2\2\u0125\u0126\7$\2\2\u0126>\3\2\2\2\u0127")
        buf.write(u"\u0129\7/\2\2\u0128\u0127\3\2\2\2\u0128\u0129\3\2\2\2")
        buf.write(u"\u0129\u012b\3\2\2\2\u012a\u012c\5\3\2\2\u012b\u012a")
        buf.write(u"\3\2\2\2\u012c\u012d\3\2\2\2\u012d\u012b\3\2\2\2\u012d")
        buf.write(u"\u012e\3\2\2\2\u012e\u012f\3\2\2\2\u012f\u0131\5i\65")
        buf.write(u"\2\u0130\u0132\5\3\2\2\u0131\u0130\3\2\2\2\u0132\u0133")
        buf.write(u"\3\2\2\2\u0133\u0131\3\2\2\2\u0133\u0134\3\2\2\2\u0134")
        buf.write(u"@\3\2\2\2\u0135\u0137\7/\2\2\u0136\u0135\3\2\2\2\u0136")
        buf.write(u"\u0137\3\2\2\2\u0137\u0139\3\2\2\2\u0138\u013a\5\3\2")
        buf.write(u"\2\u0139\u0138\3\2\2\2\u013a\u013b\3\2\2\2\u013b\u0139")
        buf.write(u"\3\2\2\2\u013b\u013c\3\2\2\2\u013cB\3\2\2\2\u013d\u0143")
        buf.write(u"\5\5\3\2\u013e\u0142\5\5\3\2\u013f\u0142\7a\2\2\u0140")
        buf.write(u"\u0142\5\3\2\2\u0141\u013e\3\2\2\2\u0141\u013f\3\2\2")
        buf.write(u"\2\u0141\u0140\3\2\2\2\u0142\u0145\3\2\2\2\u0143\u0141")
        buf.write(u"\3\2\2\2\u0143\u0144\3\2\2\2\u0144D\3\2\2\2\u0145\u0143")
        buf.write(u"\3\2\2\2\u0146\u0147\7#\2\2\u0147\u0148\7?\2\2\u0148")
        buf.write(u"F\3\2\2\2\u0149\u014a\7?\2\2\u014aH\3\2\2\2\u014b\u014c")
        buf.write(u"\7>\2\2\u014c\u014d\7?\2\2\u014dJ\3\2\2\2\u014e\u014f")
        buf.write(u"\7@\2\2\u014f\u0150\7?\2\2\u0150L\3\2\2\2\u0151\u0152")
        buf.write(u"\7>\2\2\u0152N\3\2\2\2\u0153\u0154\7@\2\2\u0154P\3\2")
        buf.write(u"\2\2\u0155\u0156\7`\2\2\u0156R\3\2\2\2\u0157\u0158\7")
        buf.write(u"\61\2\2\u0158T\3\2\2\2\u0159\u015a\7,\2\2\u015aV\3\2")
        buf.write(u"\2\2\u015b\u015c\7-\2\2\u015cX\3\2\2\2\u015d\u015e\7")
        buf.write(u"/\2\2\u015eZ\3\2\2\2\u015f\u0160\7.\2\2\u0160\\\3\2\2")
        buf.write(u"\2\u0161\u0162\7*\2\2\u0162^\3\2\2\2\u0163\u0164\7+\2")
        buf.write(u"\2\u0164`\3\2\2\2\u0165\u0166\7]\2\2\u0166b\3\2\2\2\u0167")
        buf.write(u"\u0168\7_\2\2\u0168d\3\2\2\2\u0169\u016a\7}\2\2\u016a")
        buf.write(u"f\3\2\2\2\u016b\u016c\7\177\2\2\u016ch\3\2\2\2\u016d")
        buf.write(u"\u016e\7\60\2\2\u016ej\3\2\2\2\u016f\u0170\7=\2\2\u0170")
        buf.write(u"l\3\2\2\2\u0171\u0172\7<\2\2\u0172n\3\2\2\2\17\2\u0105")
        buf.write(u"\u010b\u0112\u0118\u0122\u0128\u012d\u0133\u0136\u013b")
        buf.write(u"\u0141\u0143\3\b\2\2")
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
    START_T = 21
    FINISH_T = 22
    EQUAL_T = 23
    NOT_T = 24
    AND_OP_T = 25
    OR_OP_T = 26
    WS = 27
    CTE_STRING_T = 28
    CTE_FLOAT_T = 29
    CTE_INT_T = 30
    ID_T = 31
    NOT_EQUAL_T = 32
    ASSIGN_T = 33
    LESS_EQ_T = 34
    GREATER_EQ_T = 35
    LESS_T = 36
    GREATER_T = 37
    POW_T = 38
    DIVISION_T = 39
    MULTI_T = 40
    PLUS_T = 41
    MINUS_T = 42
    COMMA_T = 43
    LP_T = 44
    RP_T = 45
    LB_T = 46
    RB_T = 47
    LCB_T = 48
    RCB_T = 49
    POINT_T = 50
    END_OF_STM_T = 51
    RETURN_TYPE_T = 52

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"'program'", u"'globals'", u"'return'", u"'int'", u"'float'", 
            u"'string'", u"'boolean'", u"'class'", u"'extends'", u"'if'", 
            u"'elseif'", u"'else'", u"'true'", u"'false'", u"'attributes'", 
            u"'methods'", u"'func'", u"'initializer'", u"'while'", u"'new'", 
            u"'run'", u"'end'", u"'!='", u"'='", u"'<='", u"'>='", u"'<'", 
            u"'>'", u"'^'", u"'/'", u"'*'", u"'+'", u"'-'", u"','", u"'('", 
            u"')'", u"'['", u"']'", u"'{'", u"'}'", u"'.'", u"';'", u"':'" ]

    symbolicNames = [ u"<INVALID>",
            u"PROGRAM_T", u"GLOBALS_T", u"RETURN_T", u"INT_T", u"FLOAT_T", 
            u"STRING_T", u"BOOLEAN_T", u"CLASS_T", u"EXTENDS_T", u"IF_T", 
            u"ELSEIF_T", u"ELSE_T", u"TRUE_T", u"FALSE_T", u"ATTRS_T", u"METHODS_T", 
            u"FUNC_T", u"INIT_T", u"WHILE_T", u"NEW_T", u"START_T", u"FINISH_T", 
            u"EQUAL_T", u"NOT_T", u"AND_OP_T", u"OR_OP_T", u"WS", u"CTE_STRING_T", 
            u"CTE_FLOAT_T", u"CTE_INT_T", u"ID_T", u"NOT_EQUAL_T", u"ASSIGN_T", 
            u"LESS_EQ_T", u"GREATER_EQ_T", u"LESS_T", u"GREATER_T", u"POW_T", 
            u"DIVISION_T", u"MULTI_T", u"PLUS_T", u"MINUS_T", u"COMMA_T", 
            u"LP_T", u"RP_T", u"LB_T", u"RB_T", u"LCB_T", u"RCB_T", u"POINT_T", 
            u"END_OF_STM_T", u"RETURN_TYPE_T" ]

    ruleNames = [ u"DIGIT", u"LETTER", u"PROGRAM_T", u"GLOBALS_T", u"RETURN_T", 
                  u"INT_T", u"FLOAT_T", u"STRING_T", u"BOOLEAN_T", u"CLASS_T", 
                  u"EXTENDS_T", u"IF_T", u"ELSEIF_T", u"ELSE_T", u"TRUE_T", 
                  u"FALSE_T", u"ATTRS_T", u"METHODS_T", u"FUNC_T", u"INIT_T", 
                  u"WHILE_T", u"NEW_T", u"START_T", u"FINISH_T", u"EQUAL_T", 
                  u"NOT_T", u"AND_OP_T", u"OR_OP_T", u"WS", u"CTE_STRING_T", 
                  u"CTE_FLOAT_T", u"CTE_INT_T", u"ID_T", u"NOT_EQUAL_T", 
                  u"ASSIGN_T", u"LESS_EQ_T", u"GREATER_EQ_T", u"LESS_T", 
                  u"GREATER_T", u"POW_T", u"DIVISION_T", u"MULTI_T", u"PLUS_T", 
                  u"MINUS_T", u"COMMA_T", u"LP_T", u"RP_T", u"LB_T", u"RB_T", 
                  u"LCB_T", u"RCB_T", u"POINT_T", u"END_OF_STM_T", u"RETURN_TYPE_T" ]

    grammarFileName = u"walnut.g4"

    def __init__(self, input=None, output=sys.stdout):
        super(walnutLexer, self).__init__(input, output=output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    global program_engine
    global pp
    program_engine = Engine()
    pp = pprint.PrettyPrinter(indent=2)


