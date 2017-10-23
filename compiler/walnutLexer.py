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
        buf.write(u"\67\u0174\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6")
        buf.write(u"\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4")
        buf.write(u"\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t")
        buf.write(u"\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27")
        buf.write(u"\4\30\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4")
        buf.write(u"\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t")
        buf.write(u"#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4")
        buf.write(u",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62")
        buf.write(u"\4\63\t\63\4\64\t\64\4\65\t\65\4\66\t\66\4\67\t\67\4")
        buf.write(u"8\t8\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write(u"\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6")
        buf.write(u"\3\6\3\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t")
        buf.write(u"\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write(u"\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3")
        buf.write(u"\f\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3")
        buf.write(u"\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write(u"\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3")
        buf.write(u"\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write(u"\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3")
        buf.write(u"\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write(u"\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3")
        buf.write(u"\27\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write(u"\3\32\3\32\3\32\3\33\3\33\3\33\3\33\5\33\u010d\n\33\3")
        buf.write(u"\34\3\34\3\34\3\34\5\34\u0113\n\34\3\35\3\35\3\35\3\35")
        buf.write(u"\3\35\5\35\u011a\n\35\3\36\3\36\3\36\3\36\5\36\u0120")
        buf.write(u"\n\36\3\37\3\37\3\37\3\37\3 \3 \7 \u0128\n \f \16 \u012b")
        buf.write(u"\13 \3 \3 \3!\6!\u0130\n!\r!\16!\u0131\3!\3!\6!\u0136")
        buf.write(u"\n!\r!\16!\u0137\3\"\6\"\u013b\n\"\r\"\16\"\u013c\3#")
        buf.write(u"\3#\3#\3#\7#\u0143\n#\f#\16#\u0146\13#\3$\3$\3$\3%\3")
        buf.write(u"%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,")
        buf.write(u"\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63")
        buf.write(u"\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\3")
        buf.write(u"\u0129\29\3\2\5\2\7\3\t\4\13\5\r\6\17\7\21\b\23\t\25")
        buf.write(u"\n\27\13\31\f\33\r\35\16\37\17!\20#\21%\22\'\23)\24+")
        buf.write(u"\25-\26/\27\61\30\63\31\65\32\67\339\34;\35=\36?\37A")
        buf.write(u" C!E\"G#I$K%M&O\'Q(S)U*W+Y,[-]._/a\60c\61e\62g\63i\64")
        buf.write(u"k\65m\66o\67\3\2\5\3\2\62;\4\2C\\c|\5\2\13\f\17\17\"")
        buf.write(u"\"\2\u017c\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write(u"\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3")
        buf.write(u"\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write(u"\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2")
        buf.write(u"\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2")
        buf.write(u"\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2")
        buf.write(u"\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3")
        buf.write(u"\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2")
        buf.write(u"K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2")
        buf.write(u"\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2")
        buf.write(u"\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2")
        buf.write(u"\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\3q\3")
        buf.write(u"\2\2\2\5s\3\2\2\2\7u\3\2\2\2\t}\3\2\2\2\13\u0085\3\2")
        buf.write(u"\2\2\r\u008c\3\2\2\2\17\u0090\3\2\2\2\21\u0096\3\2\2")
        buf.write(u"\2\23\u009d\3\2\2\2\25\u00a5\3\2\2\2\27\u00ab\3\2\2\2")
        buf.write(u"\31\u00b3\3\2\2\2\33\u00b6\3\2\2\2\35\u00bd\3\2\2\2\37")
        buf.write(u"\u00c2\3\2\2\2!\u00c7\3\2\2\2#\u00cd\3\2\2\2%\u00d8\3")
        buf.write(u"\2\2\2\'\u00e0\3\2\2\2)\u00e5\3\2\2\2+\u00f1\3\2\2\2")
        buf.write(u"-\u00f7\3\2\2\2/\u00fb\3\2\2\2\61\u00ff\3\2\2\2\63\u0103")
        buf.write(u"\3\2\2\2\65\u010c\3\2\2\2\67\u0112\3\2\2\29\u0119\3\2")
        buf.write(u"\2\2;\u011f\3\2\2\2=\u0121\3\2\2\2?\u0125\3\2\2\2A\u012f")
        buf.write(u"\3\2\2\2C\u013a\3\2\2\2E\u013e\3\2\2\2G\u0147\3\2\2\2")
        buf.write(u"I\u014a\3\2\2\2K\u014c\3\2\2\2M\u014f\3\2\2\2O\u0152")
        buf.write(u"\3\2\2\2Q\u0154\3\2\2\2S\u0156\3\2\2\2U\u0158\3\2\2\2")
        buf.write(u"W\u015a\3\2\2\2Y\u015c\3\2\2\2[\u015e\3\2\2\2]\u0160")
        buf.write(u"\3\2\2\2_\u0162\3\2\2\2a\u0164\3\2\2\2c\u0166\3\2\2\2")
        buf.write(u"e\u0168\3\2\2\2g\u016a\3\2\2\2i\u016c\3\2\2\2k\u016e")
        buf.write(u"\3\2\2\2m\u0170\3\2\2\2o\u0172\3\2\2\2qr\t\2\2\2r\4\3")
        buf.write(u"\2\2\2st\t\3\2\2t\6\3\2\2\2uv\7r\2\2vw\7t\2\2wx\7q\2")
        buf.write(u"\2xy\7i\2\2yz\7t\2\2z{\7c\2\2{|\7o\2\2|\b\3\2\2\2}~\7")
        buf.write(u"i\2\2~\177\7n\2\2\177\u0080\7q\2\2\u0080\u0081\7d\2\2")
        buf.write(u"\u0081\u0082\7c\2\2\u0082\u0083\7n\2\2\u0083\u0084\7")
        buf.write(u"u\2\2\u0084\n\3\2\2\2\u0085\u0086\7t\2\2\u0086\u0087")
        buf.write(u"\7g\2\2\u0087\u0088\7v\2\2\u0088\u0089\7w\2\2\u0089\u008a")
        buf.write(u"\7t\2\2\u008a\u008b\7p\2\2\u008b\f\3\2\2\2\u008c\u008d")
        buf.write(u"\7k\2\2\u008d\u008e\7p\2\2\u008e\u008f\7v\2\2\u008f\16")
        buf.write(u"\3\2\2\2\u0090\u0091\7h\2\2\u0091\u0092\7n\2\2\u0092")
        buf.write(u"\u0093\7q\2\2\u0093\u0094\7c\2\2\u0094\u0095\7v\2\2\u0095")
        buf.write(u"\20\3\2\2\2\u0096\u0097\7u\2\2\u0097\u0098\7v\2\2\u0098")
        buf.write(u"\u0099\7t\2\2\u0099\u009a\7k\2\2\u009a\u009b\7p\2\2\u009b")
        buf.write(u"\u009c\7i\2\2\u009c\22\3\2\2\2\u009d\u009e\7d\2\2\u009e")
        buf.write(u"\u009f\7q\2\2\u009f\u00a0\7q\2\2\u00a0\u00a1\7n\2\2\u00a1")
        buf.write(u"\u00a2\7g\2\2\u00a2\u00a3\7c\2\2\u00a3\u00a4\7p\2\2\u00a4")
        buf.write(u"\24\3\2\2\2\u00a5\u00a6\7e\2\2\u00a6\u00a7\7n\2\2\u00a7")
        buf.write(u"\u00a8\7c\2\2\u00a8\u00a9\7u\2\2\u00a9\u00aa\7u\2\2\u00aa")
        buf.write(u"\26\3\2\2\2\u00ab\u00ac\7g\2\2\u00ac\u00ad\7z\2\2\u00ad")
        buf.write(u"\u00ae\7v\2\2\u00ae\u00af\7g\2\2\u00af\u00b0\7p\2\2\u00b0")
        buf.write(u"\u00b1\7f\2\2\u00b1\u00b2\7u\2\2\u00b2\30\3\2\2\2\u00b3")
        buf.write(u"\u00b4\7k\2\2\u00b4\u00b5\7h\2\2\u00b5\32\3\2\2\2\u00b6")
        buf.write(u"\u00b7\7g\2\2\u00b7\u00b8\7n\2\2\u00b8\u00b9\7u\2\2\u00b9")
        buf.write(u"\u00ba\7g\2\2\u00ba\u00bb\7k\2\2\u00bb\u00bc\7h\2\2\u00bc")
        buf.write(u"\34\3\2\2\2\u00bd\u00be\7g\2\2\u00be\u00bf\7n\2\2\u00bf")
        buf.write(u"\u00c0\7u\2\2\u00c0\u00c1\7g\2\2\u00c1\36\3\2\2\2\u00c2")
        buf.write(u"\u00c3\7v\2\2\u00c3\u00c4\7t\2\2\u00c4\u00c5\7w\2\2\u00c5")
        buf.write(u"\u00c6\7g\2\2\u00c6 \3\2\2\2\u00c7\u00c8\7h\2\2\u00c8")
        buf.write(u"\u00c9\7c\2\2\u00c9\u00ca\7n\2\2\u00ca\u00cb\7u\2\2\u00cb")
        buf.write(u"\u00cc\7g\2\2\u00cc\"\3\2\2\2\u00cd\u00ce\7c\2\2\u00ce")
        buf.write(u"\u00cf\7v\2\2\u00cf\u00d0\7v\2\2\u00d0\u00d1\7t\2\2\u00d1")
        buf.write(u"\u00d2\7k\2\2\u00d2\u00d3\7d\2\2\u00d3\u00d4\7w\2\2\u00d4")
        buf.write(u"\u00d5\7v\2\2\u00d5\u00d6\7g\2\2\u00d6\u00d7\7u\2\2\u00d7")
        buf.write(u"$\3\2\2\2\u00d8\u00d9\7o\2\2\u00d9\u00da\7g\2\2\u00da")
        buf.write(u"\u00db\7v\2\2\u00db\u00dc\7j\2\2\u00dc\u00dd\7q\2\2\u00dd")
        buf.write(u"\u00de\7f\2\2\u00de\u00df\7u\2\2\u00df&\3\2\2\2\u00e0")
        buf.write(u"\u00e1\7h\2\2\u00e1\u00e2\7w\2\2\u00e2\u00e3\7p\2\2\u00e3")
        buf.write(u"\u00e4\7e\2\2\u00e4(\3\2\2\2\u00e5\u00e6\7k\2\2\u00e6")
        buf.write(u"\u00e7\7p\2\2\u00e7\u00e8\7k\2\2\u00e8\u00e9\7v\2\2\u00e9")
        buf.write(u"\u00ea\7k\2\2\u00ea\u00eb\7c\2\2\u00eb\u00ec\7n\2\2\u00ec")
        buf.write(u"\u00ed\7k\2\2\u00ed\u00ee\7|\2\2\u00ee\u00ef\7g\2\2\u00ef")
        buf.write(u"\u00f0\7t\2\2\u00f0*\3\2\2\2\u00f1\u00f2\7y\2\2\u00f2")
        buf.write(u"\u00f3\7j\2\2\u00f3\u00f4\7k\2\2\u00f4\u00f5\7n\2\2\u00f5")
        buf.write(u"\u00f6\7g\2\2\u00f6,\3\2\2\2\u00f7\u00f8\7p\2\2\u00f8")
        buf.write(u"\u00f9\7g\2\2\u00f9\u00fa\7y\2\2\u00fa.\3\2\2\2\u00fb")
        buf.write(u"\u00fc\7t\2\2\u00fc\u00fd\7w\2\2\u00fd\u00fe\7p\2\2\u00fe")
        buf.write(u"\60\3\2\2\2\u00ff\u0100\7g\2\2\u0100\u0101\7p\2\2\u0101")
        buf.write(u"\u0102\7f\2\2\u0102\62\3\2\2\2\u0103\u0104\7r\2\2\u0104")
        buf.write(u"\u0105\7w\2\2\u0105\u0106\7v\2\2\u0106\u0107\7u\2\2\u0107")
        buf.write(u"\64\3\2\2\2\u0108\u0109\7?\2\2\u0109\u010d\7?\2\2\u010a")
        buf.write(u"\u010b\7k\2\2\u010b\u010d\7u\2\2\u010c\u0108\3\2\2\2")
        buf.write(u"\u010c\u010a\3\2\2\2\u010d\66\3\2\2\2\u010e\u0113\7#")
        buf.write(u"\2\2\u010f\u0110\7p\2\2\u0110\u0111\7q\2\2\u0111\u0113")
        buf.write(u"\7v\2\2\u0112\u010e\3\2\2\2\u0112\u010f\3\2\2\2\u0113")
        buf.write(u"8\3\2\2\2\u0114\u0115\7(\2\2\u0115\u011a\7(\2\2\u0116")
        buf.write(u"\u0117\7c\2\2\u0117\u0118\7p\2\2\u0118\u011a\7f\2\2\u0119")
        buf.write(u"\u0114\3\2\2\2\u0119\u0116\3\2\2\2\u011a:\3\2\2\2\u011b")
        buf.write(u"\u011c\7~\2\2\u011c\u0120\7~\2\2\u011d\u011e\7q\2\2\u011e")
        buf.write(u"\u0120\7t\2\2\u011f\u011b\3\2\2\2\u011f\u011d\3\2\2\2")
        buf.write(u"\u0120<\3\2\2\2\u0121\u0122\t\4\2\2\u0122\u0123\3\2\2")
        buf.write(u"\2\u0123\u0124\b\37\2\2\u0124>\3\2\2\2\u0125\u0129\7")
        buf.write(u"$\2\2\u0126\u0128\13\2\2\2\u0127\u0126\3\2\2\2\u0128")
        buf.write(u"\u012b\3\2\2\2\u0129\u012a\3\2\2\2\u0129\u0127\3\2\2")
        buf.write(u"\2\u012a\u012c\3\2\2\2\u012b\u0129\3\2\2\2\u012c\u012d")
        buf.write(u"\7$\2\2\u012d@\3\2\2\2\u012e\u0130\5\3\2\2\u012f\u012e")
        buf.write(u"\3\2\2\2\u0130\u0131\3\2\2\2\u0131\u012f\3\2\2\2\u0131")
        buf.write(u"\u0132\3\2\2\2\u0132\u0133\3\2\2\2\u0133\u0135\5k\66")
        buf.write(u"\2\u0134\u0136\5\3\2\2\u0135\u0134\3\2\2\2\u0136\u0137")
        buf.write(u"\3\2\2\2\u0137\u0135\3\2\2\2\u0137\u0138\3\2\2\2\u0138")
        buf.write(u"B\3\2\2\2\u0139\u013b\5\3\2\2\u013a\u0139\3\2\2\2\u013b")
        buf.write(u"\u013c\3\2\2\2\u013c\u013a\3\2\2\2\u013c\u013d\3\2\2")
        buf.write(u"\2\u013dD\3\2\2\2\u013e\u0144\5\5\3\2\u013f\u0143\5\5")
        buf.write(u"\3\2\u0140\u0143\7a\2\2\u0141\u0143\5\3\2\2\u0142\u013f")
        buf.write(u"\3\2\2\2\u0142\u0140\3\2\2\2\u0142\u0141\3\2\2\2\u0143")
        buf.write(u"\u0146\3\2\2\2\u0144\u0142\3\2\2\2\u0144\u0145\3\2\2")
        buf.write(u"\2\u0145F\3\2\2\2\u0146\u0144\3\2\2\2\u0147\u0148\7#")
        buf.write(u"\2\2\u0148\u0149\7?\2\2\u0149H\3\2\2\2\u014a\u014b\7")
        buf.write(u"?\2\2\u014bJ\3\2\2\2\u014c\u014d\7>\2\2\u014d\u014e\7")
        buf.write(u"?\2\2\u014eL\3\2\2\2\u014f\u0150\7@\2\2\u0150\u0151\7")
        buf.write(u"?\2\2\u0151N\3\2\2\2\u0152\u0153\7>\2\2\u0153P\3\2\2")
        buf.write(u"\2\u0154\u0155\7@\2\2\u0155R\3\2\2\2\u0156\u0157\7`\2")
        buf.write(u"\2\u0157T\3\2\2\2\u0158\u0159\7\61\2\2\u0159V\3\2\2\2")
        buf.write(u"\u015a\u015b\7,\2\2\u015bX\3\2\2\2\u015c\u015d\7-\2\2")
        buf.write(u"\u015dZ\3\2\2\2\u015e\u015f\7/\2\2\u015f\\\3\2\2\2\u0160")
        buf.write(u"\u0161\7.\2\2\u0161^\3\2\2\2\u0162\u0163\7*\2\2\u0163")
        buf.write(u"`\3\2\2\2\u0164\u0165\7+\2\2\u0165b\3\2\2\2\u0166\u0167")
        buf.write(u"\7]\2\2\u0167d\3\2\2\2\u0168\u0169\7_\2\2\u0169f\3\2")
        buf.write(u"\2\2\u016a\u016b\7}\2\2\u016bh\3\2\2\2\u016c\u016d\7")
        buf.write(u"\177\2\2\u016dj\3\2\2\2\u016e\u016f\7\60\2\2\u016fl\3")
        buf.write(u"\2\2\2\u0170\u0171\7=\2\2\u0171n\3\2\2\2\u0172\u0173")
        buf.write(u"\7<\2\2\u0173p\3\2\2\2\r\2\u010c\u0112\u0119\u011f\u0129")
        buf.write(u"\u0131\u0137\u013c\u0142\u0144\3\b\2\2")
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
    PRINT_T = 23
    EQUAL_T = 24
    NOT_T = 25
    AND_OP_T = 26
    OR_OP_T = 27
    WS = 28
    CTE_STRING_T = 29
    CTE_FLOAT_T = 30
    CTE_INT_T = 31
    ID_T = 32
    NOT_EQUAL_T = 33
    ASSIGN_T = 34
    LESS_EQ_T = 35
    GREATER_EQ_T = 36
    LESS_T = 37
    GREATER_T = 38
    POW_T = 39
    DIVISION_T = 40
    MULTI_T = 41
    PLUS_T = 42
    MINUS_T = 43
    COMMA_T = 44
    LP_T = 45
    RP_T = 46
    LB_T = 47
    RB_T = 48
    LCB_T = 49
    RCB_T = 50
    POINT_T = 51
    END_OF_STM_T = 52
    RETURN_TYPE_T = 53

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"'program'", u"'globals'", u"'return'", u"'int'", u"'float'", 
            u"'string'", u"'boolean'", u"'class'", u"'extends'", u"'if'", 
            u"'elseif'", u"'else'", u"'true'", u"'false'", u"'attributes'", 
            u"'methods'", u"'func'", u"'initializer'", u"'while'", u"'new'", 
            u"'run'", u"'end'", u"'puts'", u"'!='", u"'='", u"'<='", u"'>='", 
            u"'<'", u"'>'", u"'^'", u"'/'", u"'*'", u"'+'", u"'-'", u"','", 
            u"'('", u"')'", u"'['", u"']'", u"'{'", u"'}'", u"'.'", u"';'", 
            u"':'" ]

    symbolicNames = [ u"<INVALID>",
            u"PROGRAM_T", u"GLOBALS_T", u"RETURN_T", u"INT_T", u"FLOAT_T", 
            u"STRING_T", u"BOOLEAN_T", u"CLASS_T", u"EXTENDS_T", u"IF_T", 
            u"ELSEIF_T", u"ELSE_T", u"TRUE_T", u"FALSE_T", u"ATTRS_T", u"METHODS_T", 
            u"FUNC_T", u"INIT_T", u"WHILE_T", u"NEW_T", u"START_T", u"FINISH_T", 
            u"PRINT_T", u"EQUAL_T", u"NOT_T", u"AND_OP_T", u"OR_OP_T", u"WS", 
            u"CTE_STRING_T", u"CTE_FLOAT_T", u"CTE_INT_T", u"ID_T", u"NOT_EQUAL_T", 
            u"ASSIGN_T", u"LESS_EQ_T", u"GREATER_EQ_T", u"LESS_T", u"GREATER_T", 
            u"POW_T", u"DIVISION_T", u"MULTI_T", u"PLUS_T", u"MINUS_T", 
            u"COMMA_T", u"LP_T", u"RP_T", u"LB_T", u"RB_T", u"LCB_T", u"RCB_T", 
            u"POINT_T", u"END_OF_STM_T", u"RETURN_TYPE_T" ]

    ruleNames = [ u"DIGIT", u"LETTER", u"PROGRAM_T", u"GLOBALS_T", u"RETURN_T", 
                  u"INT_T", u"FLOAT_T", u"STRING_T", u"BOOLEAN_T", u"CLASS_T", 
                  u"EXTENDS_T", u"IF_T", u"ELSEIF_T", u"ELSE_T", u"TRUE_T", 
                  u"FALSE_T", u"ATTRS_T", u"METHODS_T", u"FUNC_T", u"INIT_T", 
                  u"WHILE_T", u"NEW_T", u"START_T", u"FINISH_T", u"PRINT_T", 
                  u"EQUAL_T", u"NOT_T", u"AND_OP_T", u"OR_OP_T", u"WS", 
                  u"CTE_STRING_T", u"CTE_FLOAT_T", u"CTE_INT_T", u"ID_T", 
                  u"NOT_EQUAL_T", u"ASSIGN_T", u"LESS_EQ_T", u"GREATER_EQ_T", 
                  u"LESS_T", u"GREATER_T", u"POW_T", u"DIVISION_T", u"MULTI_T", 
                  u"PLUS_T", u"MINUS_T", u"COMMA_T", u"LP_T", u"RP_T", u"LB_T", 
                  u"RB_T", u"LCB_T", u"RCB_T", u"POINT_T", u"END_OF_STM_T", 
                  u"RETURN_TYPE_T" ]

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


