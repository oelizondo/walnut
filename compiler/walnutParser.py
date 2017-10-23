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
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3")
        buf.write(u"\66\u01aa\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write(u"\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t")
        buf.write(u"\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22")
        buf.write(u"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4")
        buf.write(u"\30\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35")
        buf.write(u"\t\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4")
        buf.write(u"$\t$\4%\t%\4&\t&\4\'\t\'\3\2\3\2\3\2\3\2\5\2S\n\2\3\2")
        buf.write(u"\7\2V\n\2\f\2\16\2Y\13\2\3\2\7\2\\\n\2\f\2\16\2_\13\2")
        buf.write(u"\3\2\3\2\7\2c\n\2\f\2\16\2f\13\2\3\2\3\2\3\2\3\3\3\3")
        buf.write(u"\3\3\3\3\3\3\3\4\3\4\3\4\3\4\5\4t\n\4\3\4\3\4\3\4\3\4")
        buf.write(u"\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\7\7")
        buf.write(u"\u0086\n\7\f\7\16\7\u0089\13\7\3\7\3\7\3\b\3\b\3\b\3")
        buf.write(u"\b\5\b\u0091\n\b\3\b\3\b\3\b\7\b\u0096\n\b\f\b\16\b\u0099")
        buf.write(u"\13\b\3\b\3\b\3\t\3\t\3\t\3\t\5\t\u00a1\n\t\3\t\3\t\3")
        buf.write(u"\t\5\t\u00a6\n\t\3\t\3\t\7\t\u00aa\n\t\f\t\16\t\u00ad")
        buf.write(u"\13\t\3\t\3\t\3\t\3\t\5\t\u00b3\n\t\3\t\3\t\3\n\3\n\3")
        buf.write(u"\n\3\n\5\n\u00bb\n\n\3\n\3\n\3\n\5\n\u00c0\n\n\3\n\3")
        buf.write(u"\n\7\n\u00c4\n\n\f\n\16\n\u00c7\13\n\3\n\3\n\3\n\3\n")
        buf.write(u"\5\n\u00cd\n\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3")
        buf.write(u"\13\3\13\3\13\5\13\u00da\n\13\3\f\3\f\3\f\3\f\3\f\5\f")
        buf.write(u"\u00e1\n\f\3\r\3\r\5\r\u00e5\n\r\3\16\3\16\3\16\3\16")
        buf.write(u"\3\16\3\16\3\16\5\16\u00ee\n\16\3\17\3\17\3\20\3\20\3")
        buf.write(u"\20\3\20\3\20\5\20\u00f7\n\20\3\21\3\21\3\21\3\21\3\21")
        buf.write(u"\5\21\u00fe\n\21\3\22\3\22\3\22\3\22\3\22\5\22\u0105")
        buf.write(u"\n\22\3\23\3\23\3\23\3\23\3\23\5\23\u010c\n\23\3\24\3")
        buf.write(u"\24\3\24\3\24\3\24\5\24\u0113\n\24\3\25\5\25\u0116\n")
        buf.write(u"\25\3\25\3\25\3\25\3\25\3\25\5\25\u011d\n\25\3\26\3\26")
        buf.write(u"\3\26\3\26\3\26\5\26\u0124\n\26\3\27\3\27\3\30\3\30\5")
        buf.write(u"\30\u012a\n\30\3\30\3\30\6\30\u012e\n\30\r\30\16\30\u012f")
        buf.write(u"\3\31\3\31\5\31\u0134\n\31\3\32\3\32\3\32\3\32\3\32\3")
        buf.write(u"\32\3\32\3\33\3\33\3\33\3\33\3\34\3\34\5\34\u0143\n\34")
        buf.write(u"\3\35\5\35\u0146\n\35\3\35\3\35\3\35\3\35\3\35\3\35\3")
        buf.write(u"\35\3\35\3\36\5\36\u0151\n\36\3\36\3\36\3\36\3\36\3\36")
        buf.write(u"\3\37\3\37\3\37\3\37\3\37\3\37\7\37\u015e\n\37\f\37\16")
        buf.write(u"\37\u0161\13\37\3\37\3\37\3 \3 \3 \3 \7 \u0169\n \f ")
        buf.write(u"\16 \u016c\13 \3 \3 \3 \7 \u0171\n \f \16 \u0174\13 ")
        buf.write(u"\3 \3 \3!\3!\3!\3!\3!\7!\u017d\n!\f!\16!\u0180\13!\3")
        buf.write(u"!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u018c\n\"\3")
        buf.write(u"\"\3\"\3\"\3#\3#\3#\3#\3#\5#\u0196\n#\3#\3#\3$\3$\3$")
        buf.write(u"\5$\u019d\n$\3$\3$\3%\3%\3%\3%\3%\3&\3&\3\'\3\'\3\'\2")
        buf.write(u"\2(\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60")
        buf.write(u"\62\64\668:<>@BDFHJL\2\b\3\2\33\34\3\2+,\3\2)*\5\2\31")
        buf.write(u"\31\"\"$\'\3\2\6\t\4\2\17\20\36 \2\u01b2\2N\3\2\2\2\4")
        buf.write(u"j\3\2\2\2\6o\3\2\2\2\by\3\2\2\2\n|\3\2\2\2\f\u0081\3")
        buf.write(u"\2\2\2\16\u008c\3\2\2\2\20\u009c\3\2\2\2\22\u00b6\3\2")
        buf.write(u"\2\2\24\u00d9\3\2\2\2\26\u00e0\3\2\2\2\30\u00e4\3\2\2")
        buf.write(u"\2\32\u00ed\3\2\2\2\34\u00ef\3\2\2\2\36\u00f6\3\2\2\2")
        buf.write(u" \u00fd\3\2\2\2\"\u0104\3\2\2\2$\u010b\3\2\2\2&\u0112")
        buf.write(u"\3\2\2\2(\u0115\3\2\2\2*\u0123\3\2\2\2,\u0125\3\2\2\2")
        buf.write(u".\u012d\3\2\2\2\60\u0133\3\2\2\2\62\u0135\3\2\2\2\64")
        buf.write(u"\u013c\3\2\2\2\66\u0142\3\2\2\28\u0145\3\2\2\2:\u0150")
        buf.write(u"\3\2\2\2<\u0157\3\2\2\2>\u0164\3\2\2\2@\u0177\3\2\2\2")
        buf.write(u"B\u0183\3\2\2\2D\u0190\3\2\2\2F\u0199\3\2\2\2H\u01a0")
        buf.write(u"\3\2\2\2J\u01a5\3\2\2\2L\u01a7\3\2\2\2NO\7\3\2\2OP\7")
        buf.write(u"!\2\2PR\7\65\2\2QS\5\4\3\2RQ\3\2\2\2RS\3\2\2\2SW\3\2")
        buf.write(u"\2\2TV\5\6\4\2UT\3\2\2\2VY\3\2\2\2WU\3\2\2\2WX\3\2\2")
        buf.write(u"\2X]\3\2\2\2YW\3\2\2\2Z\\\5\22\n\2[Z\3\2\2\2\\_\3\2\2")
        buf.write(u"\2][\3\2\2\2]^\3\2\2\2^`\3\2\2\2_]\3\2\2\2`d\7\27\2\2")
        buf.write(u"ac\5\32\16\2ba\3\2\2\2cf\3\2\2\2db\3\2\2\2de\3\2\2\2")
        buf.write(u"eg\3\2\2\2fd\3\2\2\2gh\7\30\2\2hi\b\2\1\2i\3\3\2\2\2")
        buf.write(u"jk\7\4\2\2kl\7\62\2\2lm\5.\30\2mn\7\63\2\2n\5\3\2\2\2")
        buf.write(u"op\7\n\2\2ps\7!\2\2qr\7\13\2\2rt\7!\2\2sq\3\2\2\2st\3")
        buf.write(u"\2\2\2tu\3\2\2\2uv\7\62\2\2vw\5\b\5\2wx\7\63\2\2x\7\3")
        buf.write(u"\2\2\2yz\5\n\6\2z{\5\f\7\2{\t\3\2\2\2|}\7\21\2\2}~\7")
        buf.write(u"\62\2\2~\177\5.\30\2\177\u0080\7\63\2\2\u0080\13\3\2")
        buf.write(u"\2\2\u0081\u0082\7\22\2\2\u0082\u0083\7\62\2\2\u0083")
        buf.write(u"\u0087\5\16\b\2\u0084\u0086\5\20\t\2\u0085\u0084\3\2")
        buf.write(u"\2\2\u0086\u0089\3\2\2\2\u0087\u0085\3\2\2\2\u0087\u0088")
        buf.write(u"\3\2\2\2\u0088\u008a\3\2\2\2\u0089\u0087\3\2\2\2\u008a")
        buf.write(u"\u008b\7\63\2\2\u008b\r\3\2\2\2\u008c\u008d\7\23\2\2")
        buf.write(u"\u008d\u008e\7\24\2\2\u008e\u0090\7.\2\2\u008f\u0091")
        buf.write(u"\5\24\13\2\u0090\u008f\3\2\2\2\u0090\u0091\3\2\2\2\u0091")
        buf.write(u"\u0092\3\2\2\2\u0092\u0093\7/\2\2\u0093\u0097\7\62\2")
        buf.write(u"\2\u0094\u0096\5\32\16\2\u0095\u0094\3\2\2\2\u0096\u0099")
        buf.write(u"\3\2\2\2\u0097\u0095\3\2\2\2\u0097\u0098\3\2\2\2\u0098")
        buf.write(u"\u009a\3\2\2\2\u0099\u0097\3\2\2\2\u009a\u009b\7\63\2")
        buf.write(u"\2\u009b\17\3\2\2\2\u009c\u009d\7\23\2\2\u009d\u009e")
        buf.write(u"\7!\2\2\u009e\u00a0\7.\2\2\u009f\u00a1\5\24\13\2\u00a0")
        buf.write(u"\u009f\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a2\3\2\2")
        buf.write(u"\2\u00a2\u00a5\7/\2\2\u00a3\u00a4\7\66\2\2\u00a4\u00a6")
        buf.write(u"\5J&\2\u00a5\u00a3\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6")
        buf.write(u"\u00a7\3\2\2\2\u00a7\u00ab\7\62\2\2\u00a8\u00aa\5\32")
        buf.write(u"\16\2\u00a9\u00a8\3\2\2\2\u00aa\u00ad\3\2\2\2\u00ab\u00a9")
        buf.write(u"\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00b2\3\2\2\2\u00ad")
        buf.write(u"\u00ab\3\2\2\2\u00ae\u00af\7\5\2\2\u00af\u00b0\5\34\17")
        buf.write(u"\2\u00b0\u00b1\7\65\2\2\u00b1\u00b3\3\2\2\2\u00b2\u00ae")
        buf.write(u"\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4")
        buf.write(u"\u00b5\7\63\2\2\u00b5\21\3\2\2\2\u00b6\u00b7\7\23\2\2")
        buf.write(u"\u00b7\u00b8\7!\2\2\u00b8\u00ba\7.\2\2\u00b9\u00bb\5")
        buf.write(u"\24\13\2\u00ba\u00b9\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb")
        buf.write(u"\u00bc\3\2\2\2\u00bc\u00bf\7/\2\2\u00bd\u00be\7\66\2")
        buf.write(u"\2\u00be\u00c0\5J&\2\u00bf\u00bd\3\2\2\2\u00bf\u00c0")
        buf.write(u"\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1\u00c5\7\62\2\2\u00c2")
        buf.write(u"\u00c4\5\32\16\2\u00c3\u00c2\3\2\2\2\u00c4\u00c7\3\2")
        buf.write(u"\2\2\u00c5\u00c3\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6\u00cc")
        buf.write(u"\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c8\u00c9\7\5\2\2\u00c9")
        buf.write(u"\u00ca\5\34\17\2\u00ca\u00cb\7\65\2\2\u00cb\u00cd\3\2")
        buf.write(u"\2\2\u00cc\u00c8\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd\u00ce")
        buf.write(u"\3\2\2\2\u00ce\u00cf\7\63\2\2\u00cf\u00d0\b\n\1\2\u00d0")
        buf.write(u"\23\3\2\2\2\u00d1\u00d2\5J&\2\u00d2\u00d3\7!\2\2\u00d3")
        buf.write(u"\u00d4\7-\2\2\u00d4\u00d5\5\24\13\2\u00d5\u00da\3\2\2")
        buf.write(u"\2\u00d6\u00d7\5J&\2\u00d7\u00d8\7!\2\2\u00d8\u00da\3")
        buf.write(u"\2\2\2\u00d9\u00d1\3\2\2\2\u00d9\u00d6\3\2\2\2\u00da")
        buf.write(u"\25\3\2\2\2\u00db\u00dc\5\30\r\2\u00dc\u00dd\7-\2\2\u00dd")
        buf.write(u"\u00de\5\26\f\2\u00de\u00e1\3\2\2\2\u00df\u00e1\5\30")
        buf.write(u"\r\2\u00e0\u00db\3\2\2\2\u00e0\u00df\3\2\2\2\u00e1\27")
        buf.write(u"\3\2\2\2\u00e2\u00e5\5L\'\2\u00e3\u00e5\7!\2\2\u00e4")
        buf.write(u"\u00e2\3\2\2\2\u00e4\u00e3\3\2\2\2\u00e5\31\3\2\2\2\u00e6")
        buf.write(u"\u00e7\5\34\17\2\u00e7\u00e8\7\65\2\2\u00e8\u00ee\3\2")
        buf.write(u"\2\2\u00e9\u00ee\5.\30\2\u00ea\u00ee\5<\37\2\u00eb\u00ee")
        buf.write(u"\5> \2\u00ec\u00ee\5B\"\2\u00ed\u00e6\3\2\2\2\u00ed\u00e9")
        buf.write(u"\3\2\2\2\u00ed\u00ea\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ed")
        buf.write(u"\u00ec\3\2\2\2\u00ee\33\3\2\2\2\u00ef\u00f0\5\36\20\2")
        buf.write(u"\u00f0\35\3\2\2\2\u00f1\u00f2\5 \21\2\u00f2\u00f3\t\2")
        buf.write(u"\2\2\u00f3\u00f4\5\36\20\2\u00f4\u00f7\3\2\2\2\u00f5")
        buf.write(u"\u00f7\5 \21\2\u00f6\u00f1\3\2\2\2\u00f6\u00f5\3\2\2")
        buf.write(u"\2\u00f7\37\3\2\2\2\u00f8\u00f9\5\"\22\2\u00f9\u00fa")
        buf.write(u"\5,\27\2\u00fa\u00fb\5 \21\2\u00fb\u00fe\3\2\2\2\u00fc")
        buf.write(u"\u00fe\5\"\22\2\u00fd\u00f8\3\2\2\2\u00fd\u00fc\3\2\2")
        buf.write(u"\2\u00fe!\3\2\2\2\u00ff\u0100\5$\23\2\u0100\u0101\t\3")
        buf.write(u"\2\2\u0101\u0102\5\"\22\2\u0102\u0105\3\2\2\2\u0103\u0105")
        buf.write(u"\5$\23\2\u0104\u00ff\3\2\2\2\u0104\u0103\3\2\2\2\u0105")
        buf.write(u"#\3\2\2\2\u0106\u0107\5&\24\2\u0107\u0108\t\4\2\2\u0108")
        buf.write(u"\u0109\5$\23\2\u0109\u010c\3\2\2\2\u010a\u010c\5&\24")
        buf.write(u"\2\u010b\u0106\3\2\2\2\u010b\u010a\3\2\2\2\u010c%\3\2")
        buf.write(u"\2\2\u010d\u010e\5(\25\2\u010e\u010f\7(\2\2\u010f\u0110")
        buf.write(u"\5&\24\2\u0110\u0113\3\2\2\2\u0111\u0113\5(\25\2\u0112")
        buf.write(u"\u010d\3\2\2\2\u0112\u0111\3\2\2\2\u0113\'\3\2\2\2\u0114")
        buf.write(u"\u0116\7\32\2\2\u0115\u0114\3\2\2\2\u0115\u0116\3\2\2")
        buf.write(u"\2\u0116\u011c\3\2\2\2\u0117\u011d\5*\26\2\u0118\u0119")
        buf.write(u"\7.\2\2\u0119\u011a\5\34\17\2\u011a\u011b\7/\2\2\u011b")
        buf.write(u"\u011d\3\2\2\2\u011c\u0117\3\2\2\2\u011c\u0118\3\2\2")
        buf.write(u"\2\u011d)\3\2\2\2\u011e\u0124\7!\2\2\u011f\u0124\5L\'")
        buf.write(u"\2\u0120\u0124\5D#\2\u0121\u0124\5F$\2\u0122\u0124\5")
        buf.write(u"H%\2\u0123\u011e\3\2\2\2\u0123\u011f\3\2\2\2\u0123\u0120")
        buf.write(u"\3\2\2\2\u0123\u0121\3\2\2\2\u0123\u0122\3\2\2\2\u0124")
        buf.write(u"+\3\2\2\2\u0125\u0126\t\5\2\2\u0126-\3\2\2\2\u0127\u012a")
        buf.write(u"\5\60\31\2\u0128\u012a\5\66\34\2\u0129\u0127\3\2\2\2")
        buf.write(u"\u0129\u0128\3\2\2\2\u012a\u012b\3\2\2\2\u012b\u012c")
        buf.write(u"\7\65\2\2\u012c\u012e\3\2\2\2\u012d\u0129\3\2\2\2\u012e")
        buf.write(u"\u012f\3\2\2\2\u012f\u012d\3\2\2\2\u012f\u0130\3\2\2")
        buf.write(u"\2\u0130/\3\2\2\2\u0131\u0134\5\62\32\2\u0132\u0134\5")
        buf.write(u"\64\33\2\u0133\u0131\3\2\2\2\u0133\u0132\3\2\2\2\u0134")
        buf.write(u"\61\3\2\2\2\u0135\u0136\5J&\2\u0136\u0137\7!\2\2\u0137")
        buf.write(u"\u0138\7\60\2\2\u0138\u0139\7 \2\2\u0139\u013a\7\61\2")
        buf.write(u"\2\u013a\u013b\b\32\1\2\u013b\63\3\2\2\2\u013c\u013d")
        buf.write(u"\5J&\2\u013d\u013e\7!\2\2\u013e\u013f\b\33\1\2\u013f")
        buf.write(u"\65\3\2\2\2\u0140\u0143\58\35\2\u0141\u0143\5:\36\2\u0142")
        buf.write(u"\u0140\3\2\2\2\u0142\u0141\3\2\2\2\u0143\67\3\2\2\2\u0144")
        buf.write(u"\u0146\5J&\2\u0145\u0144\3\2\2\2\u0145\u0146\3\2\2\2")
        buf.write(u"\u0146\u0147\3\2\2\2\u0147\u0148\7!\2\2\u0148\u0149\7")
        buf.write(u"\60\2\2\u0149\u014a\7 \2\2\u014a\u014b\7\61\2\2\u014b")
        buf.write(u"\u014c\7#\2\2\u014c\u014d\5\34\17\2\u014d\u014e\b\35")
        buf.write(u"\1\2\u014e9\3\2\2\2\u014f\u0151\5J&\2\u0150\u014f\3\2")
        buf.write(u"\2\2\u0150\u0151\3\2\2\2\u0151\u0152\3\2\2\2\u0152\u0153")
        buf.write(u"\7!\2\2\u0153\u0154\7#\2\2\u0154\u0155\5\34\17\2\u0155")
        buf.write(u"\u0156\b\36\1\2\u0156;\3\2\2\2\u0157\u0158\7\25\2\2\u0158")
        buf.write(u"\u0159\7.\2\2\u0159\u015a\5\34\17\2\u015a\u015b\7/\2")
        buf.write(u"\2\u015b\u015f\7\62\2\2\u015c\u015e\5\32\16\2\u015d\u015c")
        buf.write(u"\3\2\2\2\u015e\u0161\3\2\2\2\u015f\u015d\3\2\2\2\u015f")
        buf.write(u"\u0160\3\2\2\2\u0160\u0162\3\2\2\2\u0161\u015f\3\2\2")
        buf.write(u"\2\u0162\u0163\7\63\2\2\u0163=\3\2\2\2\u0164\u0165\7")
        buf.write(u"\f\2\2\u0165\u016a\5@!\2\u0166\u0167\7\r\2\2\u0167\u0169")
        buf.write(u"\5@!\2\u0168\u0166\3\2\2\2\u0169\u016c\3\2\2\2\u016a")
        buf.write(u"\u0168\3\2\2\2\u016a\u016b\3\2\2\2\u016b\u016d\3\2\2")
        buf.write(u"\2\u016c\u016a\3\2\2\2\u016d\u016e\7\16\2\2\u016e\u0172")
        buf.write(u"\7\62\2\2\u016f\u0171\5\32\16\2\u0170\u016f\3\2\2\2\u0171")
        buf.write(u"\u0174\3\2\2\2\u0172\u0170\3\2\2\2\u0172\u0173\3\2\2")
        buf.write(u"\2\u0173\u0175\3\2\2\2\u0174\u0172\3\2\2\2\u0175\u0176")
        buf.write(u"\7\63\2\2\u0176?\3\2\2\2\u0177\u0178\7.\2\2\u0178\u0179")
        buf.write(u"\5\34\17\2\u0179\u017a\7/\2\2\u017a\u017e\7\62\2\2\u017b")
        buf.write(u"\u017d\5\32\16\2\u017c\u017b\3\2\2\2\u017d\u0180\3\2")
        buf.write(u"\2\2\u017e\u017c\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u0181")
        buf.write(u"\3\2\2\2\u0180\u017e\3\2\2\2\u0181\u0182\7\63\2\2\u0182")
        buf.write(u"A\3\2\2\2\u0183\u0184\7!\2\2\u0184\u0185\7!\2\2\u0185")
        buf.write(u"\u0186\7#\2\2\u0186\u0187\7!\2\2\u0187\u0188\7\64\2\2")
        buf.write(u"\u0188\u0189\7\26\2\2\u0189\u018b\7.\2\2\u018a\u018c")
        buf.write(u"\5\26\f\2\u018b\u018a\3\2\2\2\u018b\u018c\3\2\2\2\u018c")
        buf.write(u"\u018d\3\2\2\2\u018d\u018e\7/\2\2\u018e\u018f\7\65\2")
        buf.write(u"\2\u018fC\3\2\2\2\u0190\u0191\7!\2\2\u0191\u0192\7\64")
        buf.write(u"\2\2\u0192\u0193\7!\2\2\u0193\u0195\7.\2\2\u0194\u0196")
        buf.write(u"\5\26\f\2\u0195\u0194\3\2\2\2\u0195\u0196\3\2\2\2\u0196")
        buf.write(u"\u0197\3\2\2\2\u0197\u0198\7/\2\2\u0198E\3\2\2\2\u0199")
        buf.write(u"\u019a\7!\2\2\u019a\u019c\7.\2\2\u019b\u019d\5\26\f\2")
        buf.write(u"\u019c\u019b\3\2\2\2\u019c\u019d\3\2\2\2\u019d\u019e")
        buf.write(u"\3\2\2\2\u019e\u019f\7/\2\2\u019fG\3\2\2\2\u01a0\u01a1")
        buf.write(u"\7!\2\2\u01a1\u01a2\7\60\2\2\u01a2\u01a3\7 \2\2\u01a3")
        buf.write(u"\u01a4\7\61\2\2\u01a4I\3\2\2\2\u01a5\u01a6\t\6\2\2\u01a6")
        buf.write(u"K\3\2\2\2\u01a7\u01a8\t\7\2\2\u01a8M\3\2\2\2+RW]ds\u0087")
        buf.write(u"\u0090\u0097\u00a0\u00a5\u00ab\u00b2\u00ba\u00bf\u00c5")
        buf.write(u"\u00cc\u00d9\u00e0\u00e4\u00ed\u00f6\u00fd\u0104\u010b")
        buf.write(u"\u0112\u0115\u011c\u0123\u0129\u012f\u0133\u0142\u0145")
        buf.write(u"\u0150\u015f\u016a\u0172\u017e\u018b\u0195\u019c")
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
                     u"'initializer'", u"'while'", u"'new'", u"'run'", u"'end'", 
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
                      u"WHILE_T", u"NEW_T", u"START_T", u"FINISH_T", u"EQUAL_T", 
                      u"NOT_T", u"AND_OP_T", u"OR_OP_T", u"WS", u"CTE_STRING_T", 
                      u"CTE_FLOAT_T", u"CTE_INT_T", u"ID_T", u"NOT_EQUAL_T", 
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
    RULE_arguments = 10
    RULE_argument = 11
    RULE_blocks = 12
    RULE_expression = 13
    RULE_conditional_expression = 14
    RULE_relational_expression = 15
    RULE_math_expression = 16
    RULE_term = 17
    RULE_factor = 18
    RULE_power_of = 19
    RULE_atomic = 20
    RULE_relop_tokens = 21
    RULE_declaration_assignment = 22
    RULE_declaration = 23
    RULE_array_declaration = 24
    RULE_var_declaration = 25
    RULE_assignments = 26
    RULE_array_assignment = 27
    RULE_var_assignment = 28
    RULE_loops = 29
    RULE_conditional = 30
    RULE_if_elsif_body = 31
    RULE_object_declaration = 32
    RULE_call_object_method = 33
    RULE_call_function = 34
    RULE_call_array = 35
    RULE_var_type = 36
    RULE_constants = 37

    ruleNames =  [ u"program", u"global_variables", u"classes", u"class_body", 
                   u"class_attributes", u"class_methods", u"initializer", 
                   u"method_declaration", u"functions", u"parameters", u"arguments", 
                   u"argument", u"blocks", u"expression", u"conditional_expression", 
                   u"relational_expression", u"math_expression", u"term", 
                   u"factor", u"power_of", u"atomic", u"relop_tokens", u"declaration_assignment", 
                   u"declaration", u"array_declaration", u"var_declaration", 
                   u"assignments", u"array_assignment", u"var_assignment", 
                   u"loops", u"conditional", u"if_elsif_body", u"object_declaration", 
                   u"call_object_method", u"call_function", u"call_array", 
                   u"var_type", u"constants" ]

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
    START_T=21
    FINISH_T=22
    EQUAL_T=23
    NOT_T=24
    AND_OP_T=25
    OR_OP_T=26
    WS=27
    CTE_STRING_T=28
    CTE_FLOAT_T=29
    CTE_INT_T=30
    ID_T=31
    NOT_EQUAL_T=32
    ASSIGN_T=33
    LESS_EQ_T=34
    GREATER_EQ_T=35
    LESS_T=36
    GREATER_T=37
    POW_T=38
    DIVISION_T=39
    MULTI_T=40
    PLUS_T=41
    MINUS_T=42
    COMMA_T=43
    LP_T=44
    RP_T=45
    LB_T=46
    RB_T=47
    LCB_T=48
    RCB_T=49
    POINT_T=50
    END_OF_STM_T=51
    RETURN_TYPE_T=52

    def __init__(self, input, output=sys.stdout):
        super(walnutParser, self).__init__(input, output=output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    global program_engine
    global pp
    program_engine = Engine()
    pp = pprint.PrettyPrinter(indent=2)


    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(walnutParser.ProgramContext, self).__init__(parent, invokingState)
            self.parser = parser

        def PROGRAM_T(self):
            return self.getToken(walnutParser.PROGRAM_T, 0)

        def ID_T(self):
            return self.getToken(walnutParser.ID_T, 0)

        def END_OF_STM_T(self):
            return self.getToken(walnutParser.END_OF_STM_T, 0)

        def START_T(self):
            return self.getToken(walnutParser.START_T, 0)

        def FINISH_T(self):
            return self.getToken(walnutParser.FINISH_T, 0)

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
            self.state = 76
            self.match(walnutParser.PROGRAM_T)
            self.state = 77
            self.match(walnutParser.ID_T)
            self.state = 78
            self.match(walnutParser.END_OF_STM_T)
            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==walnutParser.GLOBALS_T:
                self.state = 79
                self.global_variables()


            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==walnutParser.CLASS_T:
                self.state = 82
                self.classes()
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==walnutParser.FUNC_T:
                self.state = 88
                self.functions()
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 94
            self.match(walnutParser.START_T)
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << walnutParser.INT_T) | (1 << walnutParser.FLOAT_T) | (1 << walnutParser.STRING_T) | (1 << walnutParser.BOOLEAN_T) | (1 << walnutParser.IF_T) | (1 << walnutParser.TRUE_T) | (1 << walnutParser.FALSE_T) | (1 << walnutParser.WHILE_T) | (1 << walnutParser.NOT_T) | (1 << walnutParser.CTE_STRING_T) | (1 << walnutParser.CTE_FLOAT_T) | (1 << walnutParser.CTE_INT_T) | (1 << walnutParser.ID_T) | (1 << walnutParser.LP_T))) != 0):
                self.state = 95
                self.blocks()
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 101
            self.match(walnutParser.FINISH_T)
            pp.pprint(program_engine.context.global_directory.globals)
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
            self.state = 104
            self.match(walnutParser.GLOBALS_T)
            self.state = 105
            self.match(walnutParser.LCB_T)
            self.state = 106
            self.declaration_assignment()
            self.state = 107
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
            self.state = 109
            self.match(walnutParser.CLASS_T)
            self.state = 110
            self.match(walnutParser.ID_T)
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==walnutParser.EXTENDS_T:
                self.state = 111
                self.match(walnutParser.EXTENDS_T)
                self.state = 112
                self.match(walnutParser.ID_T)


            self.state = 115
            self.match(walnutParser.LCB_T)
            self.state = 116
            self.class_body()
            self.state = 117
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
            self.state = 119
            self.class_attributes()
            self.state = 120
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
            self.state = 122
            self.match(walnutParser.ATTRS_T)
            self.state = 123
            self.match(walnutParser.LCB_T)
            self.state = 124
            self.declaration_assignment()
            self.state = 125
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
            self.state = 127
            self.match(walnutParser.METHODS_T)
            self.state = 128
            self.match(walnutParser.LCB_T)
            self.state = 129
            self.initializer()
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==walnutParser.FUNC_T:
                self.state = 130
                self.method_declaration()
                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 136
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
            self.state = 138
            self.match(walnutParser.FUNC_T)
            self.state = 139
            self.match(walnutParser.INIT_T)
            self.state = 140
            self.match(walnutParser.LP_T)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << walnutParser.INT_T) | (1 << walnutParser.FLOAT_T) | (1 << walnutParser.STRING_T) | (1 << walnutParser.BOOLEAN_T))) != 0):
                self.state = 141
                self.parameters()


            self.state = 144
            self.match(walnutParser.RP_T)
            self.state = 145
            self.match(walnutParser.LCB_T)
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << walnutParser.INT_T) | (1 << walnutParser.FLOAT_T) | (1 << walnutParser.STRING_T) | (1 << walnutParser.BOOLEAN_T) | (1 << walnutParser.IF_T) | (1 << walnutParser.TRUE_T) | (1 << walnutParser.FALSE_T) | (1 << walnutParser.WHILE_T) | (1 << walnutParser.NOT_T) | (1 << walnutParser.CTE_STRING_T) | (1 << walnutParser.CTE_FLOAT_T) | (1 << walnutParser.CTE_INT_T) | (1 << walnutParser.ID_T) | (1 << walnutParser.LP_T))) != 0):
                self.state = 146
                self.blocks()
                self.state = 151
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 152
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


        def END_OF_STM_T(self):
            return self.getToken(walnutParser.END_OF_STM_T, 0)

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
            self.state = 154
            self.match(walnutParser.FUNC_T)
            self.state = 155
            self.match(walnutParser.ID_T)
            self.state = 156
            self.match(walnutParser.LP_T)
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << walnutParser.INT_T) | (1 << walnutParser.FLOAT_T) | (1 << walnutParser.STRING_T) | (1 << walnutParser.BOOLEAN_T))) != 0):
                self.state = 157
                self.parameters()


            self.state = 160
            self.match(walnutParser.RP_T)
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==walnutParser.RETURN_TYPE_T:
                self.state = 161
                self.match(walnutParser.RETURN_TYPE_T)
                self.state = 162
                self.var_type()


            self.state = 165
            self.match(walnutParser.LCB_T)
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << walnutParser.INT_T) | (1 << walnutParser.FLOAT_T) | (1 << walnutParser.STRING_T) | (1 << walnutParser.BOOLEAN_T) | (1 << walnutParser.IF_T) | (1 << walnutParser.TRUE_T) | (1 << walnutParser.FALSE_T) | (1 << walnutParser.WHILE_T) | (1 << walnutParser.NOT_T) | (1 << walnutParser.CTE_STRING_T) | (1 << walnutParser.CTE_FLOAT_T) | (1 << walnutParser.CTE_INT_T) | (1 << walnutParser.ID_T) | (1 << walnutParser.LP_T))) != 0):
                self.state = 166
                self.blocks()
                self.state = 171
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==walnutParser.RETURN_T:
                self.state = 172
                self.match(walnutParser.RETURN_T)
                self.state = 173
                self.expression()
                self.state = 174
                self.match(walnutParser.END_OF_STM_T)


            self.state = 178
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
            self._ID_T = None # Token
            self._parameters = None # ParametersContext
            self._var_type = None # Var_typeContext

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


        def END_OF_STM_T(self):
            return self.getToken(walnutParser.END_OF_STM_T, 0)

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
            self.match(walnutParser.FUNC_T)
            self.state = 181
            localctx._ID_T = self.match(walnutParser.ID_T)
            self.state = 182
            self.match(walnutParser.LP_T)
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << walnutParser.INT_T) | (1 << walnutParser.FLOAT_T) | (1 << walnutParser.STRING_T) | (1 << walnutParser.BOOLEAN_T))) != 0):
                self.state = 183
                localctx._parameters = self.parameters()


            self.state = 186
            self.match(walnutParser.RP_T)
            self.state = 189
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==walnutParser.RETURN_TYPE_T:
                self.state = 187
                self.match(walnutParser.RETURN_TYPE_T)
                self.state = 188
                localctx._var_type = self.var_type()


            self.state = 191
            self.match(walnutParser.LCB_T)
            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << walnutParser.INT_T) | (1 << walnutParser.FLOAT_T) | (1 << walnutParser.STRING_T) | (1 << walnutParser.BOOLEAN_T) | (1 << walnutParser.IF_T) | (1 << walnutParser.TRUE_T) | (1 << walnutParser.FALSE_T) | (1 << walnutParser.WHILE_T) | (1 << walnutParser.NOT_T) | (1 << walnutParser.CTE_STRING_T) | (1 << walnutParser.CTE_FLOAT_T) | (1 << walnutParser.CTE_INT_T) | (1 << walnutParser.ID_T) | (1 << walnutParser.LP_T))) != 0):
                self.state = 192
                self.blocks()
                self.state = 197
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==walnutParser.RETURN_T:
                self.state = 198
                self.match(walnutParser.RETURN_T)
                self.state = 199
                self.expression()
                self.state = 200
                self.match(walnutParser.END_OF_STM_T)


            self.state = 204
            self.match(walnutParser.RCB_T)
            program_engine.register_function((None if localctx._ID_T is None else localctx._ID_T.text), (None if localctx._parameters is None else self._input.getText((localctx._parameters.start,localctx._parameters.stop))), (None if localctx._var_type is None else self._input.getText((localctx._var_type.start,localctx._var_type.stop))))
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
            self.state = 215
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 207
                self.var_type()
                self.state = 208
                self.match(walnutParser.ID_T)
                self.state = 209
                self.match(walnutParser.COMMA_T)
                self.state = 210
                self.parameters()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 212
                self.var_type()
                self.state = 213
                self.match(walnutParser.ID_T)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArgumentsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(walnutParser.ArgumentsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def argument(self):
            return self.getTypedRuleContext(walnutParser.ArgumentContext,0)


        def COMMA_T(self):
            return self.getToken(walnutParser.COMMA_T, 0)

        def arguments(self):
            return self.getTypedRuleContext(walnutParser.ArgumentsContext,0)


        def getRuleIndex(self):
            return walnutParser.RULE_arguments

        def enterRule(self, listener):
            if hasattr(listener, "enterArguments"):
                listener.enterArguments(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitArguments"):
                listener.exitArguments(self)




    def arguments(self):

        localctx = walnutParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_arguments)
        try:
            self.state = 222
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.argument()
                self.state = 218
                self.match(walnutParser.COMMA_T)
                self.state = 219
                self.arguments()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 221
                self.argument()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArgumentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(walnutParser.ArgumentContext, self).__init__(parent, invokingState)
            self.parser = parser

        def constants(self):
            return self.getTypedRuleContext(walnutParser.ConstantsContext,0)


        def ID_T(self):
            return self.getToken(walnutParser.ID_T, 0)

        def getRuleIndex(self):
            return walnutParser.RULE_argument

        def enterRule(self, listener):
            if hasattr(listener, "enterArgument"):
                listener.enterArgument(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitArgument"):
                listener.exitArgument(self)




    def argument(self):

        localctx = walnutParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [walnutParser.TRUE_T, walnutParser.FALSE_T, walnutParser.CTE_STRING_T, walnutParser.CTE_FLOAT_T, walnutParser.CTE_INT_T]:
                self.state = 224
                self.constants()
                pass
            elif token in [walnutParser.ID_T]:
                self.state = 225
                self.match(walnutParser.ID_T)
                pass
            else:
                raise NoViableAltException(self)

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


        def END_OF_STM_T(self):
            return self.getToken(walnutParser.END_OF_STM_T, 0)

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
        self.enterRule(localctx, 24, self.RULE_blocks)
        try:
            self.state = 235
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
                self.expression()
                self.state = 229
                self.match(walnutParser.END_OF_STM_T)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 231
                self.declaration_assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 232
                self.loops()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 233
                self.conditional()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 234
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
        self.enterRule(localctx, 26, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
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
        self.enterRule(localctx, 28, self.RULE_conditional_expression)
        self._la = 0 # Token type
        try:
            self.state = 244
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 239
                self.relational_expression()
                self.state = 240
                _la = self._input.LA(1)
                if not(_la==walnutParser.AND_OP_T or _la==walnutParser.OR_OP_T):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 241
                self.conditional_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 243
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
        self.enterRule(localctx, 30, self.RULE_relational_expression)
        try:
            self.state = 251
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.math_expression()
                self.state = 247
                self.relop_tokens()
                self.state = 248
                self.relational_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
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
        self.enterRule(localctx, 32, self.RULE_math_expression)
        self._la = 0 # Token type
        try:
            self.state = 258
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.term()
                self.state = 254
                _la = self._input.LA(1)
                if not(_la==walnutParser.PLUS_T or _la==walnutParser.MINUS_T):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 255
                self.math_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 257
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
        self.enterRule(localctx, 34, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.state = 265
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 260
                self.factor()
                self.state = 261
                _la = self._input.LA(1)
                if not(_la==walnutParser.DIVISION_T or _la==walnutParser.MULTI_T):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 262
                self.term()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 264
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
        self.enterRule(localctx, 36, self.RULE_factor)
        try:
            self.state = 272
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 267
                self.power_of()
                self.state = 268
                self.match(walnutParser.POW_T)
                self.state = 269
                self.factor()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 271
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

        def atomic(self):
            return self.getTypedRuleContext(walnutParser.AtomicContext,0)


        def LP_T(self):
            return self.getToken(walnutParser.LP_T, 0)

        def expression(self):
            return self.getTypedRuleContext(walnutParser.ExpressionContext,0)


        def RP_T(self):
            return self.getToken(walnutParser.RP_T, 0)

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
        self.enterRule(localctx, 38, self.RULE_power_of)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==walnutParser.NOT_T:
                self.state = 274
                self.match(walnutParser.NOT_T)


            self.state = 282
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [walnutParser.TRUE_T, walnutParser.FALSE_T, walnutParser.CTE_STRING_T, walnutParser.CTE_FLOAT_T, walnutParser.CTE_INT_T, walnutParser.ID_T]:
                self.state = 277
                self.atomic()
                pass
            elif token in [walnutParser.LP_T]:
                self.state = 278
                self.match(walnutParser.LP_T)
                self.state = 279
                self.expression()
                self.state = 280
                self.match(walnutParser.RP_T)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AtomicContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(walnutParser.AtomicContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID_T(self):
            return self.getToken(walnutParser.ID_T, 0)

        def constants(self):
            return self.getTypedRuleContext(walnutParser.ConstantsContext,0)


        def call_object_method(self):
            return self.getTypedRuleContext(walnutParser.Call_object_methodContext,0)


        def call_function(self):
            return self.getTypedRuleContext(walnutParser.Call_functionContext,0)


        def call_array(self):
            return self.getTypedRuleContext(walnutParser.Call_arrayContext,0)


        def getRuleIndex(self):
            return walnutParser.RULE_atomic

        def enterRule(self, listener):
            if hasattr(listener, "enterAtomic"):
                listener.enterAtomic(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAtomic"):
                listener.exitAtomic(self)




    def atomic(self):

        localctx = walnutParser.AtomicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_atomic)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 284
                self.match(walnutParser.ID_T)
                pass

            elif la_ == 2:
                self.state = 285
                self.constants()
                pass

            elif la_ == 3:
                self.state = 286
                self.call_object_method()
                pass

            elif la_ == 4:
                self.state = 287
                self.call_function()
                pass

            elif la_ == 5:
                self.state = 288
                self.call_array()
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
        self.enterRule(localctx, 42, self.RULE_relop_tokens)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
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

        def END_OF_STM_T(self, i=None):
            if i is None:
                return self.getTokens(walnutParser.END_OF_STM_T)
            else:
                return self.getToken(walnutParser.END_OF_STM_T, i)

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
        self.enterRule(localctx, 44, self.RULE_declaration_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 295
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                    if la_ == 1:
                        self.state = 293
                        self.declaration()
                        pass

                    elif la_ == 2:
                        self.state = 294
                        self.assignments()
                        pass


                    self.state = 297
                    self.match(walnutParser.END_OF_STM_T)

                else:
                    raise NoViableAltException(self)
                self.state = 301 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

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

        def array_declaration(self):
            return self.getTypedRuleContext(walnutParser.Array_declarationContext,0)


        def var_declaration(self):
            return self.getTypedRuleContext(walnutParser.Var_declarationContext,0)


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
        self.enterRule(localctx, 46, self.RULE_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 303
                self.array_declaration()
                pass

            elif la_ == 2:
                self.state = 304
                self.var_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Array_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(walnutParser.Array_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self._var_type = None # Var_typeContext
            self._ID_T = None # Token

        def var_type(self):
            return self.getTypedRuleContext(walnutParser.Var_typeContext,0)


        def ID_T(self):
            return self.getToken(walnutParser.ID_T, 0)

        def LB_T(self):
            return self.getToken(walnutParser.LB_T, 0)

        def CTE_INT_T(self):
            return self.getToken(walnutParser.CTE_INT_T, 0)

        def RB_T(self):
            return self.getToken(walnutParser.RB_T, 0)

        def getRuleIndex(self):
            return walnutParser.RULE_array_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterArray_declaration"):
                listener.enterArray_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitArray_declaration"):
                listener.exitArray_declaration(self)




    def array_declaration(self):

        localctx = walnutParser.Array_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_array_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            localctx._var_type = self.var_type()
            self.state = 308
            localctx._ID_T = self.match(walnutParser.ID_T)
            self.state = 309
            self.match(walnutParser.LB_T)
            self.state = 310
            self.match(walnutParser.CTE_INT_T)
            self.state = 311
            self.match(walnutParser.RB_T)
            program_engine.register_variable((None if localctx._var_type is None else self._input.getText((localctx._var_type.start,localctx._var_type.stop))), (None if localctx._ID_T is None else localctx._ID_T.text))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Var_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(walnutParser.Var_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self._var_type = None # Var_typeContext
            self._ID_T = None # Token

        def var_type(self):
            return self.getTypedRuleContext(walnutParser.Var_typeContext,0)


        def ID_T(self):
            return self.getToken(walnutParser.ID_T, 0)

        def getRuleIndex(self):
            return walnutParser.RULE_var_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterVar_declaration"):
                listener.enterVar_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitVar_declaration"):
                listener.exitVar_declaration(self)




    def var_declaration(self):

        localctx = walnutParser.Var_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_var_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            localctx._var_type = self.var_type()
            self.state = 315
            localctx._ID_T = self.match(walnutParser.ID_T)
            program_engine.register_variable((None if localctx._var_type is None else self._input.getText((localctx._var_type.start,localctx._var_type.stop))), (None if localctx._ID_T is None else localctx._ID_T.text))
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

        def array_assignment(self):
            return self.getTypedRuleContext(walnutParser.Array_assignmentContext,0)


        def var_assignment(self):
            return self.getTypedRuleContext(walnutParser.Var_assignmentContext,0)


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
        self.enterRule(localctx, 52, self.RULE_assignments)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 318
                self.array_assignment()
                pass

            elif la_ == 2:
                self.state = 319
                self.var_assignment()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Array_assignmentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(walnutParser.Array_assignmentContext, self).__init__(parent, invokingState)
            self.parser = parser
            self._var_type = None # Var_typeContext
            self._ID_T = None # Token
            self._expression = None # ExpressionContext

        def ID_T(self):
            return self.getToken(walnutParser.ID_T, 0)

        def LB_T(self):
            return self.getToken(walnutParser.LB_T, 0)

        def CTE_INT_T(self):
            return self.getToken(walnutParser.CTE_INT_T, 0)

        def RB_T(self):
            return self.getToken(walnutParser.RB_T, 0)

        def ASSIGN_T(self):
            return self.getToken(walnutParser.ASSIGN_T, 0)

        def expression(self):
            return self.getTypedRuleContext(walnutParser.ExpressionContext,0)


        def var_type(self):
            return self.getTypedRuleContext(walnutParser.Var_typeContext,0)


        def getRuleIndex(self):
            return walnutParser.RULE_array_assignment

        def enterRule(self, listener):
            if hasattr(listener, "enterArray_assignment"):
                listener.enterArray_assignment(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitArray_assignment"):
                listener.exitArray_assignment(self)




    def array_assignment(self):

        localctx = walnutParser.Array_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_array_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << walnutParser.INT_T) | (1 << walnutParser.FLOAT_T) | (1 << walnutParser.STRING_T) | (1 << walnutParser.BOOLEAN_T))) != 0):
                self.state = 322
                localctx._var_type = self.var_type()


            self.state = 325
            localctx._ID_T = self.match(walnutParser.ID_T)
            self.state = 326
            self.match(walnutParser.LB_T)
            self.state = 327
            self.match(walnutParser.CTE_INT_T)
            self.state = 328
            self.match(walnutParser.RB_T)
            self.state = 329
            self.match(walnutParser.ASSIGN_T)
            self.state = 330
            localctx._expression = self.expression()
            program_engine.register_variable((None if localctx._var_type is None else self._input.getText((localctx._var_type.start,localctx._var_type.stop))), (None if localctx._ID_T is None else localctx._ID_T.text), (None if localctx._expression is None else self._input.getText((localctx._expression.start,localctx._expression.stop))))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Var_assignmentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(walnutParser.Var_assignmentContext, self).__init__(parent, invokingState)
            self.parser = parser
            self._var_type = None # Var_typeContext
            self._ID_T = None # Token
            self._expression = None # ExpressionContext

        def ID_T(self):
            return self.getToken(walnutParser.ID_T, 0)

        def ASSIGN_T(self):
            return self.getToken(walnutParser.ASSIGN_T, 0)

        def expression(self):
            return self.getTypedRuleContext(walnutParser.ExpressionContext,0)


        def var_type(self):
            return self.getTypedRuleContext(walnutParser.Var_typeContext,0)


        def getRuleIndex(self):
            return walnutParser.RULE_var_assignment

        def enterRule(self, listener):
            if hasattr(listener, "enterVar_assignment"):
                listener.enterVar_assignment(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitVar_assignment"):
                listener.exitVar_assignment(self)




    def var_assignment(self):

        localctx = walnutParser.Var_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_var_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << walnutParser.INT_T) | (1 << walnutParser.FLOAT_T) | (1 << walnutParser.STRING_T) | (1 << walnutParser.BOOLEAN_T))) != 0):
                self.state = 333
                localctx._var_type = self.var_type()


            self.state = 336
            localctx._ID_T = self.match(walnutParser.ID_T)
            self.state = 337
            self.match(walnutParser.ASSIGN_T)
            self.state = 338
            localctx._expression = self.expression()
            program_engine.register_variable((None if localctx._var_type is None else self._input.getText((localctx._var_type.start,localctx._var_type.stop))), (None if localctx._ID_T is None else localctx._ID_T.text), (None if localctx._expression is None else self._input.getText((localctx._expression.start,localctx._expression.stop))))
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
        self.enterRule(localctx, 58, self.RULE_loops)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.match(walnutParser.WHILE_T)
            self.state = 342
            self.match(walnutParser.LP_T)
            self.state = 343
            self.expression()
            self.state = 344
            self.match(walnutParser.RP_T)
            self.state = 345
            self.match(walnutParser.LCB_T)
            self.state = 349
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << walnutParser.INT_T) | (1 << walnutParser.FLOAT_T) | (1 << walnutParser.STRING_T) | (1 << walnutParser.BOOLEAN_T) | (1 << walnutParser.IF_T) | (1 << walnutParser.TRUE_T) | (1 << walnutParser.FALSE_T) | (1 << walnutParser.WHILE_T) | (1 << walnutParser.NOT_T) | (1 << walnutParser.CTE_STRING_T) | (1 << walnutParser.CTE_FLOAT_T) | (1 << walnutParser.CTE_INT_T) | (1 << walnutParser.ID_T) | (1 << walnutParser.LP_T))) != 0):
                self.state = 346
                self.blocks()
                self.state = 351
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 352
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
        self.enterRule(localctx, 60, self.RULE_conditional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self.match(walnutParser.IF_T)
            self.state = 355
            self.if_elsif_body()
            self.state = 360
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==walnutParser.ELSEIF_T:
                self.state = 356
                self.match(walnutParser.ELSEIF_T)
                self.state = 357
                self.if_elsif_body()
                self.state = 362
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 363
            self.match(walnutParser.ELSE_T)
            self.state = 364
            self.match(walnutParser.LCB_T)
            self.state = 368
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << walnutParser.INT_T) | (1 << walnutParser.FLOAT_T) | (1 << walnutParser.STRING_T) | (1 << walnutParser.BOOLEAN_T) | (1 << walnutParser.IF_T) | (1 << walnutParser.TRUE_T) | (1 << walnutParser.FALSE_T) | (1 << walnutParser.WHILE_T) | (1 << walnutParser.NOT_T) | (1 << walnutParser.CTE_STRING_T) | (1 << walnutParser.CTE_FLOAT_T) | (1 << walnutParser.CTE_INT_T) | (1 << walnutParser.ID_T) | (1 << walnutParser.LP_T))) != 0):
                self.state = 365
                self.blocks()
                self.state = 370
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 371
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
        self.enterRule(localctx, 62, self.RULE_if_elsif_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
            self.match(walnutParser.LP_T)
            self.state = 374
            self.expression()
            self.state = 375
            self.match(walnutParser.RP_T)
            self.state = 376
            self.match(walnutParser.LCB_T)
            self.state = 380
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << walnutParser.INT_T) | (1 << walnutParser.FLOAT_T) | (1 << walnutParser.STRING_T) | (1 << walnutParser.BOOLEAN_T) | (1 << walnutParser.IF_T) | (1 << walnutParser.TRUE_T) | (1 << walnutParser.FALSE_T) | (1 << walnutParser.WHILE_T) | (1 << walnutParser.NOT_T) | (1 << walnutParser.CTE_STRING_T) | (1 << walnutParser.CTE_FLOAT_T) | (1 << walnutParser.CTE_INT_T) | (1 << walnutParser.ID_T) | (1 << walnutParser.LP_T))) != 0):
                self.state = 377
                self.blocks()
                self.state = 382
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 383
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

        def END_OF_STM_T(self):
            return self.getToken(walnutParser.END_OF_STM_T, 0)

        def arguments(self):
            return self.getTypedRuleContext(walnutParser.ArgumentsContext,0)


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
        self.enterRule(localctx, 64, self.RULE_object_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            self.match(walnutParser.ID_T)
            self.state = 386
            self.match(walnutParser.ID_T)
            self.state = 387
            self.match(walnutParser.ASSIGN_T)
            self.state = 388
            self.match(walnutParser.ID_T)
            self.state = 389
            self.match(walnutParser.POINT_T)
            self.state = 390
            self.match(walnutParser.NEW_T)
            self.state = 391
            self.match(walnutParser.LP_T)
            self.state = 393
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << walnutParser.TRUE_T) | (1 << walnutParser.FALSE_T) | (1 << walnutParser.CTE_STRING_T) | (1 << walnutParser.CTE_FLOAT_T) | (1 << walnutParser.CTE_INT_T) | (1 << walnutParser.ID_T))) != 0):
                self.state = 392
                self.arguments()


            self.state = 395
            self.match(walnutParser.RP_T)
            self.state = 396
            self.match(walnutParser.END_OF_STM_T)
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

        def RP_T(self):
            return self.getToken(walnutParser.RP_T, 0)

        def arguments(self):
            return self.getTypedRuleContext(walnutParser.ArgumentsContext,0)


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
        self.enterRule(localctx, 66, self.RULE_call_object_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self.match(walnutParser.ID_T)
            self.state = 399
            self.match(walnutParser.POINT_T)
            self.state = 400
            self.match(walnutParser.ID_T)
            self.state = 401
            self.match(walnutParser.LP_T)
            self.state = 403
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << walnutParser.TRUE_T) | (1 << walnutParser.FALSE_T) | (1 << walnutParser.CTE_STRING_T) | (1 << walnutParser.CTE_FLOAT_T) | (1 << walnutParser.CTE_INT_T) | (1 << walnutParser.ID_T))) != 0):
                self.state = 402
                self.arguments()


            self.state = 405
            self.match(walnutParser.RP_T)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Call_functionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(walnutParser.Call_functionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID_T(self):
            return self.getToken(walnutParser.ID_T, 0)

        def LP_T(self):
            return self.getToken(walnutParser.LP_T, 0)

        def RP_T(self):
            return self.getToken(walnutParser.RP_T, 0)

        def arguments(self):
            return self.getTypedRuleContext(walnutParser.ArgumentsContext,0)


        def getRuleIndex(self):
            return walnutParser.RULE_call_function

        def enterRule(self, listener):
            if hasattr(listener, "enterCall_function"):
                listener.enterCall_function(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCall_function"):
                listener.exitCall_function(self)




    def call_function(self):

        localctx = walnutParser.Call_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_call_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            self.match(walnutParser.ID_T)
            self.state = 408
            self.match(walnutParser.LP_T)
            self.state = 410
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << walnutParser.TRUE_T) | (1 << walnutParser.FALSE_T) | (1 << walnutParser.CTE_STRING_T) | (1 << walnutParser.CTE_FLOAT_T) | (1 << walnutParser.CTE_INT_T) | (1 << walnutParser.ID_T))) != 0):
                self.state = 409
                self.arguments()


            self.state = 412
            self.match(walnutParser.RP_T)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Call_arrayContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(walnutParser.Call_arrayContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID_T(self):
            return self.getToken(walnutParser.ID_T, 0)

        def LB_T(self):
            return self.getToken(walnutParser.LB_T, 0)

        def CTE_INT_T(self):
            return self.getToken(walnutParser.CTE_INT_T, 0)

        def RB_T(self):
            return self.getToken(walnutParser.RB_T, 0)

        def getRuleIndex(self):
            return walnutParser.RULE_call_array

        def enterRule(self, listener):
            if hasattr(listener, "enterCall_array"):
                listener.enterCall_array(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCall_array"):
                listener.exitCall_array(self)




    def call_array(self):

        localctx = walnutParser.Call_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_call_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
            self.match(walnutParser.ID_T)
            self.state = 415
            self.match(walnutParser.LB_T)
            self.state = 416
            self.match(walnutParser.CTE_INT_T)
            self.state = 417
            self.match(walnutParser.RB_T)
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
        self.enterRule(localctx, 72, self.RULE_var_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 419
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

        def TRUE_T(self):
            return self.getToken(walnutParser.TRUE_T, 0)

        def FALSE_T(self):
            return self.getToken(walnutParser.FALSE_T, 0)

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
        self.enterRule(localctx, 74, self.RULE_constants)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 421
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << walnutParser.TRUE_T) | (1 << walnutParser.FALSE_T) | (1 << walnutParser.CTE_STRING_T) | (1 << walnutParser.CTE_FLOAT_T) | (1 << walnutParser.CTE_INT_T))) != 0)):
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





