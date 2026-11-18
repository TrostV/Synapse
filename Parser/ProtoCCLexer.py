# $ANTLR 3.5.3 ProtoCC.g 2026-11-18 17:36:24

import sys
from antlr3 import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EOF=-1
T__111=111
T__112=112
T__113=113
T__114=114
T__115=115
T__116=116
T__117=117
T__118=118
T__119=119
T__120=120
T__121=121
T__122=122
T__123=123
T__124=124
T__125=125
T__126=126
T__127=127
T__128=128
T__129=129
T__130=130
T__131=131
T__132=132
T__133=133
T__134=134
T__135=135
T__136=136
T__137=137
T__138=138
T__139=139
T__140=140
T__141=141
T__142=142
T__143=143
T__144=144
T__145=145
T__146=146
T__147=147
T__148=148
ACCESS=4
ACCESS_=5
ARCH=6
ARCH_=7
ARRAY=8
ARRAY_=9
ASSIGN_=10
AWAIT=11
AWAIT_=12
BCAST_=13
BOOL=14
BOOLID=15
BOOL_=16
BREAK=17
BREAK_=18
CACHE=19
CACHE_=20
CBRACE=21
CCBRACE=22
CEBRACE=23
COMMA=24
COMMENT=25
COND_=26
CONSTANT=27
CONSTANT_=28
DATA=29
DATA_=30
DATA_RULE_=31
DDOT=32
DIR=33
DIR_=34
DOT=35
ELEMENT_=36
ELSE=37
ENDIFELSE_=38
ENDIF_=39
ENDPROC_=40
ENDWHEN_=41
EQUALSIGN=42
EVENT_=43
EVENT_ACK_=44
EVICT=45
FIFO=46
FIFO_=47
FUNCTION_CALL_=48
GUARD_=49
ID=50
ID_=51
IF=52
IFELSE_=53
IF_=54
INITSTATE_=55
INITVAL_=56
INT=57
INTID=58
INT_=59
LABEL_MESSAGE_=60
LABEL_STATE_=61
LINE_COMMENT=62
LOCAL_RULE_=63
MACHN_=64
MCAST_=65
MEM=66
MEM_=67
MINUS=68
MSG=69
MSGCSTR_=70
MSG_=71
MULT=72
NCOND_=73
NEG=74
NETWORK=75
NETWORK_=76
NEXT=77
NEXT_=78
NID=79
OBJSET_=80
OBRACE=81
OCBRACE=82
OEBRACE=83
PLUS=84
POLICY_=85
POLICY_ACTION_=86
POLICY_COH_=87
POLICY_DATA_=88
POLICY_OP_=89
POL_FILE_=90
PROC=91
PROC_=92
RANGE_=93
RULE_=94
SEMICOLON=95
SEND_=96
SET=97
SETFUNC_=98
SET_=99
STABLE=100
STABLE_=101
STALL=102
STALL_=103
STATE=104
TRANS_=105
UNDEF=106
UNDEF_=107
WHEN=108
WHEN_=109
WS=110

# token names
tokenNamesMap = {
    0: "<invalid>", 1: "<EOR>", 2: "<DOWN>", 3: "<UP>",
    -1: "EOF", 111: "T__111", 112: "T__112", 113: "T__113", 114: "T__114", 
    115: "T__115", 116: "T__116", 117: "T__117", 118: "T__118", 119: "T__119", 
    120: "T__120", 121: "T__121", 122: "T__122", 123: "T__123", 124: "T__124", 
    125: "T__125", 126: "T__126", 127: "T__127", 128: "T__128", 129: "T__129", 
    130: "T__130", 131: "T__131", 132: "T__132", 133: "T__133", 134: "T__134", 
    135: "T__135", 136: "T__136", 137: "T__137", 138: "T__138", 139: "T__139", 
    140: "T__140", 141: "T__141", 142: "T__142", 143: "T__143", 144: "T__144", 
    145: "T__145", 146: "T__146", 147: "T__147", 148: "T__148", 4: "ACCESS", 
    5: "ACCESS_", 6: "ARCH", 7: "ARCH_", 8: "ARRAY", 9: "ARRAY_", 10: "ASSIGN_", 
    11: "AWAIT", 12: "AWAIT_", 13: "BCAST_", 14: "BOOL", 15: "BOOLID", 16: "BOOL_", 
    17: "BREAK", 18: "BREAK_", 19: "CACHE", 20: "CACHE_", 21: "CBRACE", 
    22: "CCBRACE", 23: "CEBRACE", 24: "COMMA", 25: "COMMENT", 26: "COND_", 
    27: "CONSTANT", 28: "CONSTANT_", 29: "DATA", 30: "DATA_", 31: "DATA_RULE_", 
    32: "DDOT", 33: "DIR", 34: "DIR_", 35: "DOT", 36: "ELEMENT_", 37: "ELSE", 
    38: "ENDIFELSE_", 39: "ENDIF_", 40: "ENDPROC_", 41: "ENDWHEN_", 42: "EQUALSIGN", 
    43: "EVENT_", 44: "EVENT_ACK_", 45: "EVICT", 46: "FIFO", 47: "FIFO_", 
    48: "FUNCTION_CALL_", 49: "GUARD_", 50: "ID", 51: "ID_", 52: "IF", 53: "IFELSE_", 
    54: "IF_", 55: "INITSTATE_", 56: "INITVAL_", 57: "INT", 58: "INTID", 
    59: "INT_", 60: "LABEL_MESSAGE_", 61: "LABEL_STATE_", 62: "LINE_COMMENT", 
    63: "LOCAL_RULE_", 64: "MACHN_", 65: "MCAST_", 66: "MEM", 67: "MEM_", 
    68: "MINUS", 69: "MSG", 70: "MSGCSTR_", 71: "MSG_", 72: "MULT", 73: "NCOND_", 
    74: "NEG", 75: "NETWORK", 76: "NETWORK_", 77: "NEXT", 78: "NEXT_", 79: "NID", 
    80: "OBJSET_", 81: "OBRACE", 82: "OCBRACE", 83: "OEBRACE", 84: "PLUS", 
    85: "POLICY_", 86: "POLICY_ACTION_", 87: "POLICY_COH_", 88: "POLICY_DATA_", 
    89: "POLICY_OP_", 90: "POL_FILE_", 91: "PROC", 92: "PROC_", 93: "RANGE_", 
    94: "RULE_", 95: "SEMICOLON", 96: "SEND_", 97: "SET", 98: "SETFUNC_", 
    99: "SET_", 100: "STABLE", 101: "STABLE_", 102: "STALL", 103: "STALL_", 
    104: "STATE", 105: "TRANS_", 106: "UNDEF", 107: "UNDEF_", 108: "WHEN", 
    109: "WHEN_", 110: "WS"
}
Token.registerTokenNamesMap(tokenNamesMap)

class ProtoCCLexer(Lexer):

    grammarFileName = "ProtoCC.g"
    api_version = 1

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super().__init__(input, state)

        self.delegates = []

        self.dfa8 = self.DFA8(
            self, 8,
            eot = self.DFA8_eot,
            eof = self.DFA8_eof,
            min = self.DFA8_min,
            max = self.DFA8_max,
            accept = self.DFA8_accept,
            special = self.DFA8_special,
            transition = self.DFA8_transition
            )






    # $ANTLR start "ARCH"
    def mARCH(self, ):
        try:
            _type = ARCH
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:7:6: ( 'Architecture' )
            # ProtoCC.g:7:8: 'Architecture'
            pass 
            self.match("Architecture")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ARCH"



    # $ANTLR start "ARRAY"
    def mARRAY(self, ):
        try:
            _type = ARRAY
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:8:7: ( 'array' )
            # ProtoCC.g:8:9: 'array'
            pass 
            self.match("array")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ARRAY"



    # $ANTLR start "AWAIT"
    def mAWAIT(self, ):
        try:
            _type = AWAIT
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:9:7: ( 'await' )
            # ProtoCC.g:9:9: 'await'
            pass 
            self.match("await")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "AWAIT"



    # $ANTLR start "BOOLID"
    def mBOOLID(self, ):
        try:
            _type = BOOLID
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:10:8: ( 'bool' )
            # ProtoCC.g:10:10: 'bool'
            pass 
            self.match("bool")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "BOOLID"



    # $ANTLR start "BREAK"
    def mBREAK(self, ):
        try:
            _type = BREAK
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:11:7: ( 'break' )
            # ProtoCC.g:11:9: 'break'
            pass 
            self.match("break")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "BREAK"



    # $ANTLR start "CACHE"
    def mCACHE(self, ):
        try:
            _type = CACHE
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:12:7: ( 'Cache' )
            # ProtoCC.g:12:9: 'Cache'
            pass 
            self.match("Cache")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "CACHE"



    # $ANTLR start "CBRACE"
    def mCBRACE(self, ):
        try:
            _type = CBRACE
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:13:8: ( ')' )
            # ProtoCC.g:13:10: ')'
            pass 
            self.match(41)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "CBRACE"



    # $ANTLR start "CCBRACE"
    def mCCBRACE(self, ):
        try:
            _type = CCBRACE
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:14:9: ( '}' )
            # ProtoCC.g:14:11: '}'
            pass 
            self.match(125)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "CCBRACE"



    # $ANTLR start "CEBRACE"
    def mCEBRACE(self, ):
        try:
            _type = CEBRACE
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:15:9: ( ']' )
            # ProtoCC.g:15:11: ']'
            pass 
            self.match(93)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "CEBRACE"



    # $ANTLR start "COMMA"
    def mCOMMA(self, ):
        try:
            _type = COMMA
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:16:7: ( ',' )
            # ProtoCC.g:16:9: ','
            pass 
            self.match(44)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "COMMA"



    # $ANTLR start "CONSTANT"
    def mCONSTANT(self, ):
        try:
            _type = CONSTANT
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:17:10: ( '#' )
            # ProtoCC.g:17:12: '#'
            pass 
            self.match(35)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "CONSTANT"



    # $ANTLR start "DATA"
    def mDATA(self, ):
        try:
            _type = DATA
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:18:6: ( 'Data' )
            # ProtoCC.g:18:8: 'Data'
            pass 
            self.match("Data")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "DATA"



    # $ANTLR start "DDOT"
    def mDDOT(self, ):
        try:
            _type = DDOT
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:19:6: ( ':' )
            # ProtoCC.g:19:8: ':'
            pass 
            self.match(58)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "DDOT"



    # $ANTLR start "DIR"
    def mDIR(self, ):
        try:
            _type = DIR
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:20:5: ( 'Directory' )
            # ProtoCC.g:20:7: 'Directory'
            pass 
            self.match("Directory")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "DIR"



    # $ANTLR start "DOT"
    def mDOT(self, ):
        try:
            _type = DOT
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:21:5: ( '.' )
            # ProtoCC.g:21:7: '.'
            pass 
            self.match(46)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "DOT"



    # $ANTLR start "ELSE"
    def mELSE(self, ):
        try:
            _type = ELSE
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:22:6: ( 'else' )
            # ProtoCC.g:22:8: 'else'
            pass 
            self.match("else")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ELSE"



    # $ANTLR start "EQUALSIGN"
    def mEQUALSIGN(self, ):
        try:
            _type = EQUALSIGN
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:23:11: ( '=' )
            # ProtoCC.g:23:13: '='
            pass 
            self.match(61)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "EQUALSIGN"



    # $ANTLR start "FIFO"
    def mFIFO(self, ):
        try:
            _type = FIFO
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:24:6: ( 'FIFO' )
            # ProtoCC.g:24:8: 'FIFO'
            pass 
            self.match("FIFO")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "FIFO"



    # $ANTLR start "IF"
    def mIF(self, ):
        try:
            _type = IF
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:25:4: ( 'if' )
            # ProtoCC.g:25:6: 'if'
            pass 
            self.match("if")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "IF"



    # $ANTLR start "INTID"
    def mINTID(self, ):
        try:
            _type = INTID
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:26:7: ( 'int' )
            # ProtoCC.g:26:9: 'int'
            pass 
            self.match("int")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "INTID"



    # $ANTLR start "MEM"
    def mMEM(self, ):
        try:
            _type = MEM
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:27:5: ( 'Memory' )
            # ProtoCC.g:27:7: 'Memory'
            pass 
            self.match("Memory")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "MEM"



    # $ANTLR start "MINUS"
    def mMINUS(self, ):
        try:
            _type = MINUS
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:28:7: ( '-' )
            # ProtoCC.g:28:9: '-'
            pass 
            self.match(45)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "MINUS"



    # $ANTLR start "MSG"
    def mMSG(self, ):
        try:
            _type = MSG
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:29:5: ( 'Message' )
            # ProtoCC.g:29:7: 'Message'
            pass 
            self.match("Message")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "MSG"



    # $ANTLR start "MULT"
    def mMULT(self, ):
        try:
            _type = MULT
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:30:6: ( '*' )
            # ProtoCC.g:30:8: '*'
            pass 
            self.match(42)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "MULT"



    # $ANTLR start "NEG"
    def mNEG(self, ):
        try:
            _type = NEG
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:31:5: ( '!' )
            # ProtoCC.g:31:7: '!'
            pass 
            self.match(33)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "NEG"



    # $ANTLR start "NETWORK"
    def mNETWORK(self, ):
        try:
            _type = NETWORK
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:32:9: ( 'Network' )
            # ProtoCC.g:32:11: 'Network'
            pass 
            self.match("Network")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "NETWORK"



    # $ANTLR start "NEXT"
    def mNEXT(self, ):
        try:
            _type = NEXT
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:33:6: ( 'next' )
            # ProtoCC.g:33:8: 'next'
            pass 
            self.match("next")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "NEXT"



    # $ANTLR start "NID"
    def mNID(self, ):
        try:
            _type = NID
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:34:5: ( 'ID' )
            # ProtoCC.g:34:7: 'ID'
            pass 
            self.match("ID")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "NID"



    # $ANTLR start "OBRACE"
    def mOBRACE(self, ):
        try:
            _type = OBRACE
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:35:8: ( '(' )
            # ProtoCC.g:35:10: '('
            pass 
            self.match(40)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "OBRACE"



    # $ANTLR start "OCBRACE"
    def mOCBRACE(self, ):
        try:
            _type = OCBRACE
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:36:9: ( '{' )
            # ProtoCC.g:36:11: '{'
            pass 
            self.match(123)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "OCBRACE"



    # $ANTLR start "OEBRACE"
    def mOEBRACE(self, ):
        try:
            _type = OEBRACE
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:37:9: ( '[' )
            # ProtoCC.g:37:11: '['
            pass 
            self.match(91)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "OEBRACE"



    # $ANTLR start "PLUS"
    def mPLUS(self, ):
        try:
            _type = PLUS
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:38:6: ( '+' )
            # ProtoCC.g:38:8: '+'
            pass 
            self.match(43)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "PLUS"



    # $ANTLR start "PROC"
    def mPROC(self, ):
        try:
            _type = PROC
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:39:6: ( 'Process' )
            # ProtoCC.g:39:8: 'Process'
            pass 
            self.match("Process")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "PROC"



    # $ANTLR start "SEMICOLON"
    def mSEMICOLON(self, ):
        try:
            _type = SEMICOLON
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:40:11: ( ';' )
            # ProtoCC.g:40:13: ';'
            pass 
            self.match(59)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "SEMICOLON"



    # $ANTLR start "SET"
    def mSET(self, ):
        try:
            _type = SET
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:41:5: ( 'set' )
            # ProtoCC.g:41:7: 'set'
            pass 
            self.match("set")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "SET"



    # $ANTLR start "STABLE"
    def mSTABLE(self, ):
        try:
            _type = STABLE
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:42:8: ( 'Stable' )
            # ProtoCC.g:42:10: 'Stable'
            pass 
            self.match("Stable")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "STABLE"



    # $ANTLR start "STALL"
    def mSTALL(self, ):
        try:
            _type = STALL
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:43:7: ( 'stall' )
            # ProtoCC.g:43:9: 'stall'
            pass 
            self.match("stall")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "STALL"



    # $ANTLR start "STATE"
    def mSTATE(self, ):
        try:
            _type = STATE
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:44:7: ( 'State' )
            # ProtoCC.g:44:9: 'State'
            pass 
            self.match("State")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "STATE"



    # $ANTLR start "UNDEF"
    def mUNDEF(self, ):
        try:
            _type = UNDEF
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:45:7: ( 'undefine' )
            # ProtoCC.g:45:9: 'undefine'
            pass 
            self.match("undefine")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "UNDEF"



    # $ANTLR start "WHEN"
    def mWHEN(self, ):
        try:
            _type = WHEN
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:46:6: ( 'when' )
            # ProtoCC.g:46:8: 'when'
            pass 
            self.match("when")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "WHEN"



    # $ANTLR start "T__111"
    def mT__111(self, ):
        try:
            _type = T__111
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:47:8: ( '!=' )
            # ProtoCC.g:47:10: '!='
            pass 
            self.match("!=")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__111"



    # $ANTLR start "T__112"
    def mT__112(self, ):
        try:
            _type = T__112
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:48:8: ( '&' )
            # ProtoCC.g:48:10: '&'
            pass 
            self.match(38)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__112"



    # $ANTLR start "T__113"
    def mT__113(self, ):
        try:
            _type = T__113
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:49:8: ( '<' )
            # ProtoCC.g:49:10: '<'
            pass 
            self.match(60)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__113"



    # $ANTLR start "T__114"
    def mT__114(self, ):
        try:
            _type = T__114
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:50:8: ( '<=' )
            # ProtoCC.g:50:10: '<='
            pass 
            self.match("<=")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__114"



    # $ANTLR start "T__115"
    def mT__115(self, ):
        try:
            _type = T__115
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:51:8: ( '==' )
            # ProtoCC.g:51:10: '=='
            pass 
            self.match("==")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__115"



    # $ANTLR start "T__116"
    def mT__116(self, ):
        try:
            _type = T__116
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:52:8: ( '>' )
            # ProtoCC.g:52:10: '>'
            pass 
            self.match(62)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__116"



    # $ANTLR start "T__117"
    def mT__117(self, ):
        try:
            _type = T__117
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:53:8: ( '>=' )
            # ProtoCC.g:53:10: '>='
            pass 
            self.match(">=")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__117"



    # $ANTLR start "T__118"
    def mT__118(self, ):
        try:
            _type = T__118
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:54:8: ( 'Bcast' )
            # ProtoCC.g:54:10: 'Bcast'
            pass 
            self.match("Bcast")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__118"



    # $ANTLR start "T__119"
    def mT__119(self, ):
        try:
            _type = T__119
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:55:8: ( 'Clean' )
            # ProtoCC.g:55:10: 'Clean'
            pass 
            self.match("Clean")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__119"



    # $ANTLR start "T__120"
    def mT__120(self, ):
        try:
            _type = T__120
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:56:8: ( 'Dirty' )
            # ProtoCC.g:56:10: 'Dirty'
            pass 
            self.match("Dirty")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__120"



    # $ANTLR start "T__121"
    def mT__121(self, ):
        try:
            _type = T__121
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:57:8: ( 'Event' )
            # ProtoCC.g:57:10: 'Event'
            pass 
            self.match("Event")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__121"



    # $ANTLR start "T__122"
    def mT__122(self, ):
        try:
            _type = T__122
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:58:8: ( 'Local' )
            # ProtoCC.g:58:10: 'Local'
            pass 
            self.match("Local")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__122"



    # $ANTLR start "T__123"
    def mT__123(self, ):
        try:
            _type = T__123
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:59:8: ( 'Mcast' )
            # ProtoCC.g:59:10: 'Mcast'
            pass 
            self.match("Mcast")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__123"



    # $ANTLR start "T__124"
    def mT__124(self, ):
        try:
            _type = T__124
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:60:8: ( 'NP' )
            # ProtoCC.g:60:10: 'NP'
            pass 
            self.match("NP")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__124"



    # $ANTLR start "T__125"
    def mT__125(self, ):
        try:
            _type = T__125
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:61:8: ( 'None' )
            # ProtoCC.g:61:10: 'None'
            pass 
            self.match("None")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__125"



    # $ANTLR start "T__126"
    def mT__126(self, ):
        try:
            _type = T__126
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:62:8: ( 'Ordered' )
            # ProtoCC.g:62:10: 'Ordered'
            pass 
            self.match("Ordered")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__126"



    # $ANTLR start "T__127"
    def mT__127(self, ):
        try:
            _type = T__127
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:63:8: ( 'P' )
            # ProtoCC.g:63:10: 'P'
            pass 
            self.match(80)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__127"



    # $ANTLR start "T__128"
    def mT__128(self, ):
        try:
            _type = T__128
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:64:8: ( 'Policy' )
            # ProtoCC.g:64:10: 'Policy'
            pass 
            self.match("Policy")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__128"



    # $ANTLR start "T__129"
    def mT__129(self, ):
        try:
            _type = T__129
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:65:8: ( 'Rd' )
            # ProtoCC.g:65:10: 'Rd'
            pass 
            self.match("Rd")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__129"



    # $ANTLR start "T__130"
    def mT__130(self, ):
        try:
            _type = T__130
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:66:8: ( 'RdWr' )
            # ProtoCC.g:66:10: 'RdWr'
            pass 
            self.match("RdWr")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__130"



    # $ANTLR start "T__131"
    def mT__131(self, ):
        try:
            _type = T__131
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:67:8: ( 'Rule' )
            # ProtoCC.g:67:10: 'Rule'
            pass 
            self.match("Rule")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__131"



    # $ANTLR start "T__132"
    def mT__132(self, ):
        try:
            _type = T__132
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:68:8: ( 'Send' )
            # ProtoCC.g:68:10: 'Send'
            pass 
            self.match("Send")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__132"



    # $ANTLR start "T__133"
    def mT__133(self, ):
        try:
            _type = T__133
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:69:8: ( 'Unordered' )
            # ProtoCC.g:69:10: 'Unordered'
            pass 
            self.match("Unordered")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__133"



    # $ANTLR start "T__134"
    def mT__134(self, ):
        try:
            _type = T__134
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:70:8: ( 'Wr' )
            # ProtoCC.g:70:10: 'Wr'
            pass 
            self.match("Wr")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__134"



    # $ANTLR start "T__135"
    def mT__135(self, ):
        try:
            _type = T__135
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:71:8: ( '_' )
            # ProtoCC.g:71:10: '_'
            pass 
            self.match(95)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__135"



    # $ANTLR start "T__136"
    def mT__136(self, ):
        try:
            _type = T__136
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:72:8: ( 'action' )
            # ProtoCC.g:72:10: 'action'
            pass 
            self.match("action")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__136"



    # $ANTLR start "T__137"
    def mT__137(self, ):
        try:
            _type = T__137
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:73:8: ( 'add' )
            # ProtoCC.g:73:10: 'add'
            pass 
            self.match("add")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__137"



    # $ANTLR start "T__138"
    def mT__138(self, ):
        try:
            _type = T__138
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:74:8: ( 'bcast' )
            # ProtoCC.g:74:10: 'bcast'
            pass 
            self.match("bcast")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__138"



    # $ANTLR start "T__139"
    def mT__139(self, ):
        try:
            _type = T__139
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:75:8: ( 'clear' )
            # ProtoCC.g:75:10: 'clear'
            pass 
            self.match("clear")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__139"



    # $ANTLR start "T__140"
    def mT__140(self, ):
        try:
            _type = T__140
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:76:8: ( 'coh' )
            # ProtoCC.g:76:10: 'coh'
            pass 
            self.match("coh")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__140"



    # $ANTLR start "T__141"
    def mT__141(self, ):
        try:
            _type = T__141
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:77:8: ( 'contains' )
            # ProtoCC.g:77:10: 'contains'
            pass 
            self.match("contains")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__141"



    # $ANTLR start "T__142"
    def mT__142(self, ):
        try:
            _type = T__142
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:78:8: ( 'count' )
            # ProtoCC.g:78:10: 'count'
            pass 
            self.match("count")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__142"



    # $ANTLR start "T__143"
    def mT__143(self, ):
        try:
            _type = T__143
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:79:8: ( 'del' )
            # ProtoCC.g:79:10: 'del'
            pass 
            self.match("del")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__143"



    # $ANTLR start "T__144"
    def mT__144(self, ):
        try:
            _type = T__144
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:80:8: ( 'mcast' )
            # ProtoCC.g:80:10: 'mcast'
            pass 
            self.match("mcast")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__144"



    # $ANTLR start "T__145"
    def mT__145(self, ):
        try:
            _type = T__145
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:81:8: ( 'nco' )
            # ProtoCC.g:81:10: 'nco'
            pass 
            self.match("nco")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__145"



    # $ANTLR start "T__146"
    def mT__146(self, ):
        try:
            _type = T__146
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:82:8: ( 'send' )
            # ProtoCC.g:82:10: 'send'
            pass 
            self.match("send")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__146"



    # $ANTLR start "T__147"
    def mT__147(self, ):
        try:
            _type = T__147
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:83:8: ( 'smallest' )
            # ProtoCC.g:83:10: 'smallest'
            pass 
            self.match("smallest")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__147"



    # $ANTLR start "T__148"
    def mT__148(self, ):
        try:
            _type = T__148
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:84:8: ( '|' )
            # ProtoCC.g:84:10: '|'
            pass 
            self.match(124)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__148"



    # $ANTLR start "WS"
    def mWS(self, ):
        try:
            _type = WS
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:184:5: ( ( ' ' | '\\t' | '\\r' | '\\n' ) )
            # ProtoCC.g:184:9: ( ' ' | '\\t' | '\\r' | '\\n' )
            pass 
            if self.input.LA(1) in {9, 10, 13, 32}:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            #action start
            _channel=HIDDEN;
            #action end




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "WS"



    # $ANTLR start "COMMENT"
    def mCOMMENT(self, ):
        try:
            _type = COMMENT
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:192:5: ( '/*' ( options {greedy=false; } : . )* '*/' )
            # ProtoCC.g:192:9: '/*' ( options {greedy=false; } : . )* '*/'
            pass 
            self.match("/*")


            # ProtoCC.g:192:14: ( options {greedy=false; } : . )*
            while True: #loop1
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if (LA1_0 == 42) :
                    LA1_1 = self.input.LA(2)

                    if (LA1_1 == 47) :
                        alt1 = 2
                    elif ((0 <= LA1_1 <= 46) or (48 <= LA1_1 <= 65535) or LA1_1 in {}) :
                        alt1 = 1


                elif ((0 <= LA1_0 <= 41) or (43 <= LA1_0 <= 65535) or LA1_0 in {}) :
                    alt1 = 1


                if alt1 == 1:
                    # ProtoCC.g:192:42: .
                    pass 
                    self.matchAny()


                else:
                    break #loop1


            self.match("*/")


            #action start
            _channel=HIDDEN;
            #action end




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "COMMENT"



    # $ANTLR start "LINE_COMMENT"
    def mLINE_COMMENT(self, ):
        try:
            _type = LINE_COMMENT
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:196:5: ( '//' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n' )
            # ProtoCC.g:196:7: '//' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n'
            pass 
            self.match("//")


            # ProtoCC.g:196:12: (~ ( '\\n' | '\\r' ) )*
            while True: #loop2
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if ((0 <= LA2_0 <= 9) or (14 <= LA2_0 <= 65535) or LA2_0 in {11, 12}) :
                    alt2 = 1


                if alt2 == 1:
                    # ProtoCC.g:
                    pass 
                    if (0 <= self.input.LA(1) <= 9) or (14 <= self.input.LA(1) <= 65535) or self.input.LA(1) in {11, 12}:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop2


            # ProtoCC.g:196:26: ( '\\r' )?
            alt3 = 2
            LA3_0 = self.input.LA(1)

            if (LA3_0 == 13) :
                alt3 = 1
            if alt3 == 1:
                # ProtoCC.g:196:26: '\\r'
                pass 
                self.match(13)




            self.match(10)

            #action start
            _channel=HIDDEN;
            #action end




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LINE_COMMENT"



    # $ANTLR start "BOOL"
    def mBOOL(self, ):
        try:
            _type = BOOL
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:201:5: ( 'true' | 'false' )
            alt4 = 2
            LA4_0 = self.input.LA(1)

            if (LA4_0 == 116) :
                alt4 = 1
            elif (LA4_0 == 102) :
                alt4 = 2
            else:
                nvae = NoViableAltException("", 4, 0, self.input)

                raise nvae


            if alt4 == 1:
                # ProtoCC.g:201:9: 'true'
                pass 
                self.match("true")



            elif alt4 == 2:
                # ProtoCC.g:201:18: 'false'
                pass 
                self.match("false")



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "BOOL"



    # $ANTLR start "INT"
    def mINT(self, ):
        try:
            _type = INT
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:202:5: ( ( '0' .. '9' )+ )
            # ProtoCC.g:202:7: ( '0' .. '9' )+
            pass 
            # ProtoCC.g:202:7: ( '0' .. '9' )+
            cnt5 = 0
            while True: #loop5
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if ((48 <= LA5_0 <= 57) or LA5_0 in {}) :
                    alt5 = 1


                if alt5 == 1:
                    # ProtoCC.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57) or self.input.LA(1) in {}:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    if cnt5 >= 1:
                        break #loop5

                    eee = EarlyExitException(5, self.input)
                    raise eee

                cnt5 += 1




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "INT"



    # $ANTLR start "ACCESS"
    def mACCESS(self, ):
        try:
            _type = ACCESS
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:204:7: ( 'load' | 'store' )
            alt6 = 2
            LA6_0 = self.input.LA(1)

            if (LA6_0 == 108) :
                alt6 = 1
            elif (LA6_0 == 115) :
                alt6 = 2
            else:
                nvae = NoViableAltException("", 6, 0, self.input)

                raise nvae


            if alt6 == 1:
                # ProtoCC.g:204:9: 'load'
                pass 
                self.match("load")



            elif alt6 == 2:
                # ProtoCC.g:204:18: 'store'
                pass 
                self.match("store")



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ACCESS"



    # $ANTLR start "EVICT"
    def mEVICT(self, ):
        try:
            _type = EVICT
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:205:6: ( 'evict' )
            # ProtoCC.g:205:8: 'evict'
            pass 
            self.match("evict")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "EVICT"



    # $ANTLR start "ID"
    def mID(self, ):
        try:
            _type = ID
            _channel = DEFAULT_CHANNEL

            # ProtoCC.g:207:5: ( ( 'a' .. 'z' | 'A' .. 'Z' | '_' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' )* )
            # ProtoCC.g:207:7: ( 'a' .. 'z' | 'A' .. 'Z' | '_' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' )*
            pass 
            if (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122) or self.input.LA(1) in {95}:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            # ProtoCC.g:207:31: ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' )*
            while True: #loop7
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if ((48 <= LA7_0 <= 57) or (65 <= LA7_0 <= 90) or (97 <= LA7_0 <= 122) or LA7_0 in {95}) :
                    alt7 = 1


                if alt7 == 1:
                    # ProtoCC.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122) or self.input.LA(1) in {95}:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop7




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ID"



    def mTokens(self):
        # ProtoCC.g:1:8: ( ARCH | ARRAY | AWAIT | BOOLID | BREAK | CACHE | CBRACE | CCBRACE | CEBRACE | COMMA | CONSTANT | DATA | DDOT | DIR | DOT | ELSE | EQUALSIGN | FIFO | IF | INTID | MEM | MINUS | MSG | MULT | NEG | NETWORK | NEXT | NID | OBRACE | OCBRACE | OEBRACE | PLUS | PROC | SEMICOLON | SET | STABLE | STALL | STATE | UNDEF | WHEN | T__111 | T__112 | T__113 | T__114 | T__115 | T__116 | T__117 | T__118 | T__119 | T__120 | T__121 | T__122 | T__123 | T__124 | T__125 | T__126 | T__127 | T__128 | T__129 | T__130 | T__131 | T__132 | T__133 | T__134 | T__135 | T__136 | T__137 | T__138 | T__139 | T__140 | T__141 | T__142 | T__143 | T__144 | T__145 | T__146 | T__147 | T__148 | WS | COMMENT | LINE_COMMENT | BOOL | INT | ACCESS | EVICT | ID )
        alt8 = 86
        alt8 = self.dfa8.predict(self.input)
        if alt8 == 1:
            # ProtoCC.g:1:10: ARCH
            pass 
            self.mARCH()



        elif alt8 == 2:
            # ProtoCC.g:1:15: ARRAY
            pass 
            self.mARRAY()



        elif alt8 == 3:
            # ProtoCC.g:1:21: AWAIT
            pass 
            self.mAWAIT()



        elif alt8 == 4:
            # ProtoCC.g:1:27: BOOLID
            pass 
            self.mBOOLID()



        elif alt8 == 5:
            # ProtoCC.g:1:34: BREAK
            pass 
            self.mBREAK()



        elif alt8 == 6:
            # ProtoCC.g:1:40: CACHE
            pass 
            self.mCACHE()



        elif alt8 == 7:
            # ProtoCC.g:1:46: CBRACE
            pass 
            self.mCBRACE()



        elif alt8 == 8:
            # ProtoCC.g:1:53: CCBRACE
            pass 
            self.mCCBRACE()



        elif alt8 == 9:
            # ProtoCC.g:1:61: CEBRACE
            pass 
            self.mCEBRACE()



        elif alt8 == 10:
            # ProtoCC.g:1:69: COMMA
            pass 
            self.mCOMMA()



        elif alt8 == 11:
            # ProtoCC.g:1:75: CONSTANT
            pass 
            self.mCONSTANT()



        elif alt8 == 12:
            # ProtoCC.g:1:84: DATA
            pass 
            self.mDATA()



        elif alt8 == 13:
            # ProtoCC.g:1:89: DDOT
            pass 
            self.mDDOT()



        elif alt8 == 14:
            # ProtoCC.g:1:94: DIR
            pass 
            self.mDIR()



        elif alt8 == 15:
            # ProtoCC.g:1:98: DOT
            pass 
            self.mDOT()



        elif alt8 == 16:
            # ProtoCC.g:1:102: ELSE
            pass 
            self.mELSE()



        elif alt8 == 17:
            # ProtoCC.g:1:107: EQUALSIGN
            pass 
            self.mEQUALSIGN()



        elif alt8 == 18:
            # ProtoCC.g:1:117: FIFO
            pass 
            self.mFIFO()



        elif alt8 == 19:
            # ProtoCC.g:1:122: IF
            pass 
            self.mIF()



        elif alt8 == 20:
            # ProtoCC.g:1:125: INTID
            pass 
            self.mINTID()



        elif alt8 == 21:
            # ProtoCC.g:1:131: MEM
            pass 
            self.mMEM()



        elif alt8 == 22:
            # ProtoCC.g:1:135: MINUS
            pass 
            self.mMINUS()



        elif alt8 == 23:
            # ProtoCC.g:1:141: MSG
            pass 
            self.mMSG()



        elif alt8 == 24:
            # ProtoCC.g:1:145: MULT
            pass 
            self.mMULT()



        elif alt8 == 25:
            # ProtoCC.g:1:150: NEG
            pass 
            self.mNEG()



        elif alt8 == 26:
            # ProtoCC.g:1:154: NETWORK
            pass 
            self.mNETWORK()



        elif alt8 == 27:
            # ProtoCC.g:1:162: NEXT
            pass 
            self.mNEXT()



        elif alt8 == 28:
            # ProtoCC.g:1:167: NID
            pass 
            self.mNID()



        elif alt8 == 29:
            # ProtoCC.g:1:171: OBRACE
            pass 
            self.mOBRACE()



        elif alt8 == 30:
            # ProtoCC.g:1:178: OCBRACE
            pass 
            self.mOCBRACE()



        elif alt8 == 31:
            # ProtoCC.g:1:186: OEBRACE
            pass 
            self.mOEBRACE()



        elif alt8 == 32:
            # ProtoCC.g:1:194: PLUS
            pass 
            self.mPLUS()



        elif alt8 == 33:
            # ProtoCC.g:1:199: PROC
            pass 
            self.mPROC()



        elif alt8 == 34:
            # ProtoCC.g:1:204: SEMICOLON
            pass 
            self.mSEMICOLON()



        elif alt8 == 35:
            # ProtoCC.g:1:214: SET
            pass 
            self.mSET()



        elif alt8 == 36:
            # ProtoCC.g:1:218: STABLE
            pass 
            self.mSTABLE()



        elif alt8 == 37:
            # ProtoCC.g:1:225: STALL
            pass 
            self.mSTALL()



        elif alt8 == 38:
            # ProtoCC.g:1:231: STATE
            pass 
            self.mSTATE()



        elif alt8 == 39:
            # ProtoCC.g:1:237: UNDEF
            pass 
            self.mUNDEF()



        elif alt8 == 40:
            # ProtoCC.g:1:243: WHEN
            pass 
            self.mWHEN()



        elif alt8 == 41:
            # ProtoCC.g:1:248: T__111
            pass 
            self.mT__111()



        elif alt8 == 42:
            # ProtoCC.g:1:255: T__112
            pass 
            self.mT__112()



        elif alt8 == 43:
            # ProtoCC.g:1:262: T__113
            pass 
            self.mT__113()



        elif alt8 == 44:
            # ProtoCC.g:1:269: T__114
            pass 
            self.mT__114()



        elif alt8 == 45:
            # ProtoCC.g:1:276: T__115
            pass 
            self.mT__115()



        elif alt8 == 46:
            # ProtoCC.g:1:283: T__116
            pass 
            self.mT__116()



        elif alt8 == 47:
            # ProtoCC.g:1:290: T__117
            pass 
            self.mT__117()



        elif alt8 == 48:
            # ProtoCC.g:1:297: T__118
            pass 
            self.mT__118()



        elif alt8 == 49:
            # ProtoCC.g:1:304: T__119
            pass 
            self.mT__119()



        elif alt8 == 50:
            # ProtoCC.g:1:311: T__120
            pass 
            self.mT__120()



        elif alt8 == 51:
            # ProtoCC.g:1:318: T__121
            pass 
            self.mT__121()



        elif alt8 == 52:
            # ProtoCC.g:1:325: T__122
            pass 
            self.mT__122()



        elif alt8 == 53:
            # ProtoCC.g:1:332: T__123
            pass 
            self.mT__123()



        elif alt8 == 54:
            # ProtoCC.g:1:339: T__124
            pass 
            self.mT__124()



        elif alt8 == 55:
            # ProtoCC.g:1:346: T__125
            pass 
            self.mT__125()



        elif alt8 == 56:
            # ProtoCC.g:1:353: T__126
            pass 
            self.mT__126()



        elif alt8 == 57:
            # ProtoCC.g:1:360: T__127
            pass 
            self.mT__127()



        elif alt8 == 58:
            # ProtoCC.g:1:367: T__128
            pass 
            self.mT__128()



        elif alt8 == 59:
            # ProtoCC.g:1:374: T__129
            pass 
            self.mT__129()



        elif alt8 == 60:
            # ProtoCC.g:1:381: T__130
            pass 
            self.mT__130()



        elif alt8 == 61:
            # ProtoCC.g:1:388: T__131
            pass 
            self.mT__131()



        elif alt8 == 62:
            # ProtoCC.g:1:395: T__132
            pass 
            self.mT__132()



        elif alt8 == 63:
            # ProtoCC.g:1:402: T__133
            pass 
            self.mT__133()



        elif alt8 == 64:
            # ProtoCC.g:1:409: T__134
            pass 
            self.mT__134()



        elif alt8 == 65:
            # ProtoCC.g:1:416: T__135
            pass 
            self.mT__135()



        elif alt8 == 66:
            # ProtoCC.g:1:423: T__136
            pass 
            self.mT__136()



        elif alt8 == 67:
            # ProtoCC.g:1:430: T__137
            pass 
            self.mT__137()



        elif alt8 == 68:
            # ProtoCC.g:1:437: T__138
            pass 
            self.mT__138()



        elif alt8 == 69:
            # ProtoCC.g:1:444: T__139
            pass 
            self.mT__139()



        elif alt8 == 70:
            # ProtoCC.g:1:451: T__140
            pass 
            self.mT__140()



        elif alt8 == 71:
            # ProtoCC.g:1:458: T__141
            pass 
            self.mT__141()



        elif alt8 == 72:
            # ProtoCC.g:1:465: T__142
            pass 
            self.mT__142()



        elif alt8 == 73:
            # ProtoCC.g:1:472: T__143
            pass 
            self.mT__143()



        elif alt8 == 74:
            # ProtoCC.g:1:479: T__144
            pass 
            self.mT__144()



        elif alt8 == 75:
            # ProtoCC.g:1:486: T__145
            pass 
            self.mT__145()



        elif alt8 == 76:
            # ProtoCC.g:1:493: T__146
            pass 
            self.mT__146()



        elif alt8 == 77:
            # ProtoCC.g:1:500: T__147
            pass 
            self.mT__147()



        elif alt8 == 78:
            # ProtoCC.g:1:507: T__148
            pass 
            self.mT__148()



        elif alt8 == 79:
            # ProtoCC.g:1:514: WS
            pass 
            self.mWS()



        elif alt8 == 80:
            # ProtoCC.g:1:517: COMMENT
            pass 
            self.mCOMMENT()



        elif alt8 == 81:
            # ProtoCC.g:1:525: LINE_COMMENT
            pass 
            self.mLINE_COMMENT()



        elif alt8 == 82:
            # ProtoCC.g:1:538: BOOL
            pass 
            self.mBOOL()



        elif alt8 == 83:
            # ProtoCC.g:1:543: INT
            pass 
            self.mINT()



        elif alt8 == 84:
            # ProtoCC.g:1:547: ACCESS
            pass 
            self.mACCESS()



        elif alt8 == 85:
            # ProtoCC.g:1:554: EVICT
            pass 
            self.mEVICT()



        elif alt8 == 86:
            # ProtoCC.g:1:560: ID
            pass 
            self.mID()








    # lookup tables for DFA #8

    DFA8_eot = DFA.unpack(
        "\1\uffff\4\67\5\uffff\1\67\2\uffff\1\67\1\107\3\67\2\uffff\1\116"
        "\3\67\4\uffff\1\127\1\uffff\4\67\1\uffff\1\140\1\142\7\67\1\153"
        "\3\67\3\uffff\2\67\1\uffff\1\67\1\uffff\16\67\2\uffff\1\67\1\u0084"
        "\3\67\2\uffff\1\67\1\u008a\3\67\1\u008e\2\67\1\uffff\7\67\4\uffff"
        "\4\67\1\u009f\2\67\1\u00a2\1\uffff\4\67\2\uffff\7\67\1\u00b0\12"
        "\67\1\uffff\1\u00bc\4\67\1\uffff\2\67\1\u00c3\1\uffff\2\67\1\u00c6"
        "\15\67\1\uffff\2\67\1\uffff\1\67\1\u00d8\2\67\1\u00db\10\67\1\uffff"
        "\1\u00e4\4\67\1\u00e9\2\67\1\u00ec\1\67\1\u00ee\1\uffff\4\67\1\u00f3"
        "\1\u00f4\1\uffff\2\67\1\uffff\1\u00f7\5\67\1\u00fd\1\67\1\u00ff"
        "\4\67\1\u0104\1\u0105\2\67\1\uffff\2\67\1\uffff\1\67\1\u010b\1\67"
        "\1\u010d\1\67\1\u010f\1\u0110\1\67\1\uffff\1\u0112\1\u0113\1\u0114"
        "\1\u0115\1\uffff\1\67\1\u0117\1\uffff\1\u0118\1\uffff\2\67\1\u011b"
        "\1\67\2\uffff\2\67\1\uffff\1\u011f\1\u010d\2\67\1\u0122\1\uffff"
        "\1\67\1\uffff\1\u0124\1\u0125\1\u0126\1\67\2\uffff\1\67\1\u0129"
        "\1\67\1\u012b\1\u012c\1\uffff\1\u010b\1\uffff\1\67\2\uffff\1\u012e"
        "\4\uffff\1\67\2\uffff\1\u0130\1\67\1\uffff\2\67\1\u0134\1\uffff"
        "\1\67\1\u0136\1\uffff\1\67\3\uffff\2\67\1\uffff\1\67\2\uffff\1\67"
        "\1\uffff\1\67\1\uffff\1\u013d\1\u013e\1\u013f\1\uffff\1\67\1\uffff"
        "\1\67\1\u0142\4\67\3\uffff\1\u0147\1\u0148\1\uffff\1\67\1\u014a"
        "\1\67\1\u014c\2\uffff\1\u014d\1\uffff\1\67\2\uffff\1\67\1\u0150"
        "\1\uffff"
        )

    DFA8_eof = DFA.unpack(
        "\u0151\uffff"
        )

    DFA8_min = DFA.unpack(
        "\1\11\1\162\2\143\1\141\5\uffff\1\141\2\uffff\1\154\1\75\1\111\1"
        "\146\1\143\2\uffff\1\75\1\120\1\143\1\104\4\uffff\1\60\1\uffff\2"
        "\145\1\156\1\150\1\uffff\2\75\1\143\1\166\1\157\1\162\1\144\1\156"
        "\1\162\1\60\1\154\1\145\1\143\2\uffff\1\52\1\162\1\141\1\uffff\1"
        "\157\1\uffff\1\143\1\162\1\141\1\164\1\144\1\157\1\145\1\141\1\143"
        "\1\145\1\164\1\162\1\163\1\151\2\uffff\1\106\1\60\1\164\1\155\1"
        "\141\2\uffff\1\164\1\60\1\156\1\170\1\157\1\60\1\157\1\154\1\uffff"
        "\1\156\3\141\1\156\1\144\1\145\4\uffff\1\141\1\145\1\143\1\144\1"
        "\60\1\154\1\157\1\60\1\uffff\1\145\1\150\1\154\1\141\2\uffff\1\165"
        "\1\154\1\141\1\150\1\141\2\151\1\60\1\154\1\141\1\163\1\150\2\141"
        "\2\145\1\143\1\117\1\uffff\1\60\1\157\2\163\1\167\1\uffff\1\145"
        "\1\164\1\60\1\uffff\1\143\1\151\1\60\1\144\1\154\1\162\1\154\1\142"
        "\1\144\1\145\1\156\1\163\1\156\1\141\1\145\1\162\1\uffff\1\145\1"
        "\162\1\uffff\1\141\1\60\1\164\1\156\1\60\1\163\1\145\1\163\1\144"
        "\1\151\1\171\1\164\1\157\1\uffff\1\60\1\153\1\164\1\145\1\156\1"
        "\60\1\143\1\171\1\60\1\164\1\60\1\uffff\1\162\1\141\1\164\1\157"
        "\2\60\1\uffff\1\145\1\143\1\uffff\1\60\1\154\1\145\2\154\1\145\1"
        "\60\1\146\1\60\2\164\1\154\1\162\2\60\1\144\1\162\1\uffff\1\141"
        "\1\164\1\uffff\1\164\1\60\1\145\1\60\1\164\2\60\1\156\1\uffff\4"
        "\60\1\uffff\1\164\1\60\1\uffff\1\60\1\uffff\1\171\1\147\1\60\1\162"
        "\2\uffff\1\163\1\171\1\uffff\2\60\2\145\1\60\1\uffff\1\151\1\uffff"
        "\3\60\1\145\2\uffff\1\145\1\60\1\151\2\60\1\uffff\1\60\1\uffff\1"
        "\145\2\uffff\1\60\4\uffff\1\157\2\uffff\1\60\1\145\1\uffff\1\153"
        "\1\163\1\60\1\uffff\1\163\1\60\1\uffff\1\156\3\uffff\1\144\1\162"
        "\1\uffff\1\156\2\uffff\1\143\1\uffff\1\162\1\uffff\3\60\1\uffff"
        "\1\164\1\uffff\1\145\1\60\1\145\1\163\1\164\1\171\3\uffff\2\60\1"
        "\uffff\1\144\1\60\1\165\1\60\2\uffff\1\60\1\uffff\1\162\2\uffff"
        "\1\145\1\60\1\uffff"
        )

    DFA8_max = DFA.unpack(
        "\1\175\1\162\1\167\1\162\1\154\5\uffff\1\151\2\uffff\1\166\1\75"
        "\1\111\1\156\1\145\2\uffff\1\75\1\157\1\145\1\104\4\uffff\1\172"
        "\1\uffff\2\164\1\156\1\150\1\uffff\2\75\1\143\1\166\1\157\1\162"
        "\1\165\1\156\1\162\1\172\1\157\1\145\1\143\2\uffff\1\57\1\162\1"
        "\141\1\uffff\1\157\1\uffff\1\143\1\162\1\141\1\164\1\144\1\157\1"
        "\145\1\141\1\143\1\145\1\164\1\162\1\163\1\151\2\uffff\1\106\1\172"
        "\1\164\1\163\1\141\2\uffff\1\164\1\172\1\156\1\170\1\157\1\172\1"
        "\157\1\154\1\uffff\1\164\1\157\2\141\1\156\1\144\1\145\4\uffff\1"
        "\141\1\145\1\143\1\144\1\172\1\154\1\157\1\172\1\uffff\1\145\1\165"
        "\1\154\1\141\2\uffff\1\165\1\154\1\141\1\150\1\141\2\151\1\172\1"
        "\154\1\141\1\163\1\150\2\141\1\164\1\145\1\143\1\117\1\uffff\1\172"
        "\1\157\2\163\1\167\1\uffff\1\145\1\164\1\172\1\uffff\1\143\1\151"
        "\1\172\1\144\1\154\1\162\1\154\1\164\1\144\1\145\1\156\1\163\1\156"
        "\1\141\1\145\1\162\1\uffff\1\145\1\162\1\uffff\1\141\1\172\1\164"
        "\1\156\1\172\1\163\1\145\1\163\1\144\1\151\1\171\1\164\1\157\1\uffff"
        "\1\172\1\153\1\164\1\145\1\156\1\172\1\143\1\171\1\172\1\164\1\172"
        "\1\uffff\1\162\1\141\1\164\1\157\2\172\1\uffff\1\145\1\143\1\uffff"
        "\1\172\1\154\1\145\2\154\1\145\1\172\1\146\1\172\2\164\1\154\1\162"
        "\2\172\1\144\1\162\1\uffff\1\141\1\164\1\uffff\1\164\1\172\1\145"
        "\1\172\1\164\2\172\1\156\1\uffff\4\172\1\uffff\1\164\1\172\1\uffff"
        "\1\172\1\uffff\1\171\1\147\1\172\1\162\2\uffff\1\163\1\171\1\uffff"
        "\2\172\2\145\1\172\1\uffff\1\151\1\uffff\3\172\1\145\2\uffff\1\145"
        "\1\172\1\151\2\172\1\uffff\1\172\1\uffff\1\145\2\uffff\1\172\4\uffff"
        "\1\157\2\uffff\1\172\1\145\1\uffff\1\153\1\163\1\172\1\uffff\1\163"
        "\1\172\1\uffff\1\156\3\uffff\1\144\1\162\1\uffff\1\156\2\uffff\1"
        "\143\1\uffff\1\162\1\uffff\3\172\1\uffff\1\164\1\uffff\1\145\1\172"
        "\1\145\1\163\1\164\1\171\3\uffff\2\172\1\uffff\1\144\1\172\1\165"
        "\1\172\2\uffff\1\172\1\uffff\1\162\2\uffff\1\145\1\172\1\uffff"
        )

    DFA8_accept = DFA.unpack(
        "\5\uffff\1\7\1\10\1\11\1\12\1\13\1\uffff\1\15\1\17\5\uffff\1\26"
        "\1\30\4\uffff\1\35\1\36\1\37\1\40\1\uffff\1\42\4\uffff\1\52\15\uffff"
        "\1\116\1\117\3\uffff\1\123\1\uffff\1\126\16\uffff\1\55\1\21\5\uffff"
        "\1\51\1\31\10\uffff\1\71\7\uffff\1\54\1\53\1\57\1\56\10\uffff\1"
        "\101\4\uffff\1\120\1\121\22\uffff\1\23\5\uffff\1\66\3\uffff\1\34"
        "\20\uffff\1\73\2\uffff\1\100\15\uffff\1\103\13\uffff\1\24\6\uffff"
        "\1\113\2\uffff\1\43\21\uffff\1\106\2\uffff\1\111\10\uffff\1\4\4"
        "\uffff\1\14\2\uffff\1\20\1\uffff\1\22\4\uffff\1\67\1\33\2\uffff"
        "\1\114\5\uffff\1\76\1\uffff\1\50\4\uffff\1\74\1\75\5\uffff\1\122"
        "\1\uffff\1\124\1\uffff\1\2\1\3\1\uffff\1\5\1\104\1\6\1\61\1\uffff"
        "\1\62\1\125\2\uffff\1\65\3\uffff\1\45\2\uffff\1\46\1\uffff\1\60"
        "\1\63\1\64\2\uffff\1\105\1\uffff\1\110\1\112\1\uffff\1\102\1\uffff"
        "\1\25\3\uffff\1\72\1\uffff\1\44\6\uffff\1\27\1\32\1\41\2\uffff\1"
        "\70\4\uffff\1\115\1\47\1\uffff\1\107\1\uffff\1\16\1\77\2\uffff\1"
        "\1"
        )

    DFA8_special = DFA.unpack(
        "\u0151\uffff"
        )


    DFA8_transition = [
        DFA.unpack("\2\61\2\uffff\1\61\22\uffff\1\61\1\24\1\uffff\1\11\2"
        "\uffff\1\42\1\uffff\1\30\1\5\1\23\1\33\1\10\1\22\1\14\1\62\12\65"
        "\1\13\1\35\1\43\1\16\1\44\2\uffff\1\1\1\45\1\4\1\12\1\46\1\17\2"
        "\67\1\27\2\67\1\47\1\21\1\25\1\50\1\34\1\67\1\51\1\37\1\67\1\52"
        "\1\67\1\53\3\67\1\32\1\uffff\1\7\1\uffff\1\54\1\uffff\1\2\1\3\1"
        "\55\1\56\1\15\1\64\2\67\1\20\2\67\1\66\1\57\1\26\4\67\1\36\1\63"
        "\1\40\1\67\1\41\3\67\1\31\1\60\1\6"),
        DFA.unpack("\1\70"),
        DFA.unpack("\1\73\1\74\15\uffff\1\71\4\uffff\1\72"),
        DFA.unpack("\1\77\13\uffff\1\75\2\uffff\1\76"),
        DFA.unpack("\1\100\12\uffff\1\101"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\102\7\uffff\1\103"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\104\11\uffff\1\105"),
        DFA.unpack("\1\106"),
        DFA.unpack("\1\110"),
        DFA.unpack("\1\111\7\uffff\1\112"),
        DFA.unpack("\1\114\1\uffff\1\113"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\115"),
        DFA.unpack("\1\120\24\uffff\1\117\11\uffff\1\121"),
        DFA.unpack("\1\123\1\uffff\1\122"),
        DFA.unpack("\1\124"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\16\67\1\126"
        "\2\67\1\125\10\67"),
        DFA.unpack(""),
        DFA.unpack("\1\130\7\uffff\1\132\6\uffff\1\131"),
        DFA.unpack("\1\134\16\uffff\1\133"),
        DFA.unpack("\1\135"),
        DFA.unpack("\1\136"),
        DFA.unpack(""),
        DFA.unpack("\1\137"),
        DFA.unpack("\1\141"),
        DFA.unpack("\1\143"),
        DFA.unpack("\1\144"),
        DFA.unpack("\1\145"),
        DFA.unpack("\1\146"),
        DFA.unpack("\1\147\20\uffff\1\150"),
        DFA.unpack("\1\151"),
        DFA.unpack("\1\152"),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack("\1\154\2\uffff\1\155"),
        DFA.unpack("\1\156"),
        DFA.unpack("\1\157"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\160\4\uffff\1\161"),
        DFA.unpack("\1\162"),
        DFA.unpack("\1\163"),
        DFA.unpack(""),
        DFA.unpack("\1\164"),
        DFA.unpack(""),
        DFA.unpack("\1\165"),
        DFA.unpack("\1\166"),
        DFA.unpack("\1\167"),
        DFA.unpack("\1\170"),
        DFA.unpack("\1\171"),
        DFA.unpack("\1\172"),
        DFA.unpack("\1\173"),
        DFA.unpack("\1\174"),
        DFA.unpack("\1\175"),
        DFA.unpack("\1\176"),
        DFA.unpack("\1\177"),
        DFA.unpack("\1\u0080"),
        DFA.unpack("\1\u0081"),
        DFA.unpack("\1\u0082"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u0083"),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack("\1\u0085"),
        DFA.unpack("\1\u0086\5\uffff\1\u0087"),
        DFA.unpack("\1\u0088"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u0089"),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack("\1\u008b"),
        DFA.unpack("\1\u008c"),
        DFA.unpack("\1\u008d"),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack("\1\u008f"),
        DFA.unpack("\1\u0090"),
        DFA.unpack(""),
        DFA.unpack("\1\u0092\5\uffff\1\u0091"),
        DFA.unpack("\1\u0093\15\uffff\1\u0094"),
        DFA.unpack("\1\u0095"),
        DFA.unpack("\1\u0096"),
        DFA.unpack("\1\u0097"),
        DFA.unpack("\1\u0098"),
        DFA.unpack("\1\u0099"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u009a"),
        DFA.unpack("\1\u009b"),
        DFA.unpack("\1\u009c"),
        DFA.unpack("\1\u009d"),
        DFA.unpack("\12\67\7\uffff\26\67\1\u009e\3\67\4\uffff\1\67\1\uffff"
        "\32\67"),
        DFA.unpack("\1\u00a0"),
        DFA.unpack("\1\u00a1"),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack(""),
        DFA.unpack("\1\u00a3"),
        DFA.unpack("\1\u00a4\5\uffff\1\u00a5\6\uffff\1\u00a6"),
        DFA.unpack("\1\u00a7"),
        DFA.unpack("\1\u00a8"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u00a9"),
        DFA.unpack("\1\u00aa"),
        DFA.unpack("\1\u00ab"),
        DFA.unpack("\1\u00ac"),
        DFA.unpack("\1\u00ad"),
        DFA.unpack("\1\u00ae"),
        DFA.unpack("\1\u00af"),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack("\1\u00b1"),
        DFA.unpack("\1\u00b2"),
        DFA.unpack("\1\u00b3"),
        DFA.unpack("\1\u00b4"),
        DFA.unpack("\1\u00b5"),
        DFA.unpack("\1\u00b6"),
        DFA.unpack("\1\u00b7\16\uffff\1\u00b8"),
        DFA.unpack("\1\u00b9"),
        DFA.unpack("\1\u00ba"),
        DFA.unpack("\1\u00bb"),
        DFA.unpack(""),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack("\1\u00bd"),
        DFA.unpack("\1\u00be"),
        DFA.unpack("\1\u00bf"),
        DFA.unpack("\1\u00c0"),
        DFA.unpack(""),
        DFA.unpack("\1\u00c1"),
        DFA.unpack("\1\u00c2"),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack(""),
        DFA.unpack("\1\u00c4"),
        DFA.unpack("\1\u00c5"),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack("\1\u00c7"),
        DFA.unpack("\1\u00c8"),
        DFA.unpack("\1\u00c9"),
        DFA.unpack("\1\u00ca"),
        DFA.unpack("\1\u00cb\21\uffff\1\u00cc"),
        DFA.unpack("\1\u00cd"),
        DFA.unpack("\1\u00ce"),
        DFA.unpack("\1\u00cf"),
        DFA.unpack("\1\u00d0"),
        DFA.unpack("\1\u00d1"),
        DFA.unpack("\1\u00d2"),
        DFA.unpack("\1\u00d3"),
        DFA.unpack("\1\u00d4"),
        DFA.unpack(""),
        DFA.unpack("\1\u00d5"),
        DFA.unpack("\1\u00d6"),
        DFA.unpack(""),
        DFA.unpack("\1\u00d7"),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack("\1\u00d9"),
        DFA.unpack("\1\u00da"),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack("\1\u00dc"),
        DFA.unpack("\1\u00dd"),
        DFA.unpack("\1\u00de"),
        DFA.unpack("\1\u00df"),
        DFA.unpack("\1\u00e0"),
        DFA.unpack("\1\u00e1"),
        DFA.unpack("\1\u00e2"),
        DFA.unpack("\1\u00e3"),
        DFA.unpack(""),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack("\1\u00e5"),
        DFA.unpack("\1\u00e6"),
        DFA.unpack("\1\u00e7"),
        DFA.unpack("\1\u00e8"),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack("\1\u00ea"),
        DFA.unpack("\1\u00eb"),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack("\1\u00ed"),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack(""),
        DFA.unpack("\1\u00ef"),
        DFA.unpack("\1\u00f0"),
        DFA.unpack("\1\u00f1"),
        DFA.unpack("\1\u00f2"),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack(""),
        DFA.unpack("\1\u00f5"),
        DFA.unpack("\1\u00f6"),
        DFA.unpack(""),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack("\1\u00f8"),
        DFA.unpack("\1\u00f9"),
        DFA.unpack("\1\u00fa"),
        DFA.unpack("\1\u00fb"),
        DFA.unpack("\1\u00fc"),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack("\1\u00fe"),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack("\1\u0100"),
        DFA.unpack("\1\u0101"),
        DFA.unpack("\1\u0102"),
        DFA.unpack("\1\u0103"),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack("\1\u0106"),
        DFA.unpack("\1\u0107"),
        DFA.unpack(""),
        DFA.unpack("\1\u0108"),
        DFA.unpack("\1\u0109"),
        DFA.unpack(""),
        DFA.unpack("\1\u010a"),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack("\1\u010c"),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack("\1\u010e"),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack("\1\u0111"),
        DFA.unpack(""),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack(""),
        DFA.unpack("\1\u0116"),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack(""),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack(""),
        DFA.unpack("\1\u0119"),
        DFA.unpack("\1\u011a"),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack("\1\u011c"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u011d"),
        DFA.unpack("\1\u011e"),
        DFA.unpack(""),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack("\1\u0120"),
        DFA.unpack("\1\u0121"),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack(""),
        DFA.unpack("\1\u0123"),
        DFA.unpack(""),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack("\1\u0127"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u0128"),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack("\1\u012a"),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack(""),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack(""),
        DFA.unpack("\1\u012d"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u012f"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack("\1\u0131"),
        DFA.unpack(""),
        DFA.unpack("\1\u0132"),
        DFA.unpack("\1\u0133"),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack(""),
        DFA.unpack("\1\u0135"),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack(""),
        DFA.unpack("\1\u0137"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u0138"),
        DFA.unpack("\1\u0139"),
        DFA.unpack(""),
        DFA.unpack("\1\u013a"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u013b"),
        DFA.unpack(""),
        DFA.unpack("\1\u013c"),
        DFA.unpack(""),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack(""),
        DFA.unpack("\1\u0140"),
        DFA.unpack(""),
        DFA.unpack("\1\u0141"),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack("\1\u0143"),
        DFA.unpack("\1\u0144"),
        DFA.unpack("\1\u0145"),
        DFA.unpack("\1\u0146"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack(""),
        DFA.unpack("\1\u0149"),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack("\1\u014b"),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack(""),
        DFA.unpack("\1\u014e"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u014f"),
        DFA.unpack("\12\67\7\uffff\32\67\4\uffff\1\67\1\uffff\32\67"),
        DFA.unpack("")
    ]

    # class definition for DFA #8

    class DFA8(DFA):
        pass


 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(ProtoCCLexer)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
