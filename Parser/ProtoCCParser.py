# $ANTLR 3.5.3 ProtoCC.g 2026-11-16 17:02:38

import sys
from antlr3 import *

from antlr3.tree import *




# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EOF=-1
T__109=109
T__110=110
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
GUARD_=48
ID=49
ID_=50
IF=51
IFELSE_=52
IF_=53
INITSTATE_=54
INITVAL_=55
INT=56
INTID=57
INT_=58
LABEL_MESSAGE_=59
LABEL_STATE_=60
LINE_COMMENT=61
LOCAL_RULE_=62
MACHN_=63
MCAST_=64
MEM=65
MEM_=66
MINUS=67
MSG=68
MSGCSTR_=69
MSG_=70
MULT=71
NCOND_=72
NEG=73
NETWORK=74
NETWORK_=75
NEXT=76
NEXT_=77
NID=78
OBJSET_=79
OBRACE=80
OCBRACE=81
OEBRACE=82
PLUS=83
POLICY_=84
POLICY_COH_=85
POLICY_DATA_=86
POLICY_OP_=87
POL_FILE_=88
PROC=89
PROC_=90
RANGE_=91
RULE_=92
SEMICOLON=93
SEND_=94
SET=95
SETFUNC_=96
SET_=97
STABLE=98
STABLE_=99
STALL=100
STALL_=101
STATE=102
TRANS_=103
UNDEF=104
UNDEF_=105
WHEN=106
WHEN_=107
WS=108

# token names
tokenNamesMap = {
    0: "<invalid>", 1: "<EOR>", 2: "<DOWN>", 3: "<UP>",
    -1: "EOF", 109: "T__109", 110: "T__110", 111: "T__111", 112: "T__112", 
    113: "T__113", 114: "T__114", 115: "T__115", 116: "T__116", 117: "T__117", 
    118: "T__118", 119: "T__119", 120: "T__120", 121: "T__121", 122: "T__122", 
    123: "T__123", 124: "T__124", 125: "T__125", 126: "T__126", 127: "T__127", 
    128: "T__128", 129: "T__129", 130: "T__130", 131: "T__131", 132: "T__132", 
    133: "T__133", 134: "T__134", 135: "T__135", 136: "T__136", 137: "T__137", 
    138: "T__138", 139: "T__139", 140: "T__140", 141: "T__141", 142: "T__142", 
    143: "T__143", 144: "T__144", 145: "T__145", 4: "ACCESS", 5: "ACCESS_", 
    6: "ARCH", 7: "ARCH_", 8: "ARRAY", 9: "ARRAY_", 10: "ASSIGN_", 11: "AWAIT", 
    12: "AWAIT_", 13: "BCAST_", 14: "BOOL", 15: "BOOLID", 16: "BOOL_", 17: "BREAK", 
    18: "BREAK_", 19: "CACHE", 20: "CACHE_", 21: "CBRACE", 22: "CCBRACE", 
    23: "CEBRACE", 24: "COMMA", 25: "COMMENT", 26: "COND_", 27: "CONSTANT", 
    28: "CONSTANT_", 29: "DATA", 30: "DATA_", 31: "DATA_RULE_", 32: "DDOT", 
    33: "DIR", 34: "DIR_", 35: "DOT", 36: "ELEMENT_", 37: "ELSE", 38: "ENDIFELSE_", 
    39: "ENDIF_", 40: "ENDPROC_", 41: "ENDWHEN_", 42: "EQUALSIGN", 43: "EVENT_", 
    44: "EVENT_ACK_", 45: "EVICT", 46: "FIFO", 47: "FIFO_", 48: "GUARD_", 
    49: "ID", 50: "ID_", 51: "IF", 52: "IFELSE_", 53: "IF_", 54: "INITSTATE_", 
    55: "INITVAL_", 56: "INT", 57: "INTID", 58: "INT_", 59: "LABEL_MESSAGE_", 
    60: "LABEL_STATE_", 61: "LINE_COMMENT", 62: "LOCAL_RULE_", 63: "MACHN_", 
    64: "MCAST_", 65: "MEM", 66: "MEM_", 67: "MINUS", 68: "MSG", 69: "MSGCSTR_", 
    70: "MSG_", 71: "MULT", 72: "NCOND_", 73: "NEG", 74: "NETWORK", 75: "NETWORK_", 
    76: "NEXT", 77: "NEXT_", 78: "NID", 79: "OBJSET_", 80: "OBRACE", 81: "OCBRACE", 
    82: "OEBRACE", 83: "PLUS", 84: "POLICY_", 85: "POLICY_COH_", 86: "POLICY_DATA_", 
    87: "POLICY_OP_", 88: "POL_FILE_", 89: "PROC", 90: "PROC_", 91: "RANGE_", 
    92: "RULE_", 93: "SEMICOLON", 94: "SEND_", 95: "SET", 96: "SETFUNC_", 
    97: "SET_", 98: "STABLE", 99: "STABLE_", 100: "STALL", 101: "STALL_", 
    102: "STATE", 103: "TRANS_", 104: "UNDEF", 105: "UNDEF_", 106: "WHEN", 
    107: "WHEN_", 108: "WS"
}
Token.registerTokenNamesMap(tokenNamesMap)

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ACCESS", "ACCESS_", "ARCH", "ARCH_", "ARRAY", "ARRAY_", "ASSIGN_", 
    "AWAIT", "AWAIT_", "BCAST_", "BOOL", "BOOLID", "BOOL_", "BREAK", "BREAK_", 
    "CACHE", "CACHE_", "CBRACE", "CCBRACE", "CEBRACE", "COMMA", "COMMENT", 
    "COND_", "CONSTANT", "CONSTANT_", "DATA", "DATA_", "DATA_RULE_", "DDOT", 
    "DIR", "DIR_", "DOT", "ELEMENT_", "ELSE", "ENDIFELSE_", "ENDIF_", "ENDPROC_", 
    "ENDWHEN_", "EQUALSIGN", "EVENT_", "EVENT_ACK_", "EVICT", "FIFO", "FIFO_", 
    "GUARD_", "ID", "ID_", "IF", "IFELSE_", "IF_", "INITSTATE_", "INITVAL_", 
    "INT", "INTID", "INT_", "LABEL_MESSAGE_", "LABEL_STATE_", "LINE_COMMENT", 
    "LOCAL_RULE_", "MACHN_", "MCAST_", "MEM", "MEM_", "MINUS", "MSG", "MSGCSTR_", 
    "MSG_", "MULT", "NCOND_", "NEG", "NETWORK", "NETWORK_", "NEXT", "NEXT_", 
    "NID", "OBJSET_", "OBRACE", "OCBRACE", "OEBRACE", "PLUS", "POLICY_", 
    "POLICY_COH_", "POLICY_DATA_", "POLICY_OP_", "POL_FILE_", "PROC", "PROC_", 
    "RANGE_", "RULE_", "SEMICOLON", "SEND_", "SET", "SETFUNC_", "SET_", 
    "STABLE", "STABLE_", "STALL", "STALL_", "STATE", "TRANS_", "UNDEF", 
    "UNDEF_", "WHEN", "WHEN_", "WS", "'!='", "'&'", "'<'", "'<='", "'=='", 
    "'>'", "'>='", "'Bcast'", "'Clean'", "'Dirty'", "'Event'", "'Local'", 
    "'Mcast'", "'NP'", "'None'", "'Ordered'", "'P'", "'Policy'", "'Rd'", 
    "'RdWr'", "'Rule'", "'Send'", "'Unordered'", "'Wr'", "'_'", "'add'", 
    "'bcast'", "'clear'", "'coh'", "'contains'", "'count'", "'del'", "'mcast'", 
    "'nco'", "'send'", "'smallest'", "'|'"
]



class ProtoCCParser(Parser):
    grammarFileName = "ProtoCC.g"
    api_version = 1
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super().__init__(input, state, *args, **kwargs)




        self.delegates = []

        self._adaptor = None
        self.adaptor = CommonTreeAdaptor()



    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)


    class send_function_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "send_function"
    # ProtoCC.g:141:1: send_function : ( 'send' | 'Send' );
    def send_function(self, ):
        retval = self.send_function_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set1 = None

        set1_tree = None

        try:
            try:
                # ProtoCC.g:142:2: ( 'send' | 'Send' )
                # ProtoCC.g:
                pass 
                root_0 = self._adaptor.nil()


                set1 = self.input.LT(1)

                if self.input.LA(1) in {130, 143}:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set1))

                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "send_function"


    class mcast_function_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "mcast_function"
    # ProtoCC.g:146:1: mcast_function : ( 'mcast' | 'Mcast' );
    def mcast_function(self, ):
        retval = self.mcast_function_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set2 = None

        set2_tree = None

        try:
            try:
                # ProtoCC.g:147:2: ( 'mcast' | 'Mcast' )
                # ProtoCC.g:
                pass 
                root_0 = self._adaptor.nil()


                set2 = self.input.LT(1)

                if self.input.LA(1) in {121, 141}:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set2))

                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "mcast_function"


    class bcast_function_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "bcast_function"
    # ProtoCC.g:151:1: bcast_function : ( 'bcast' | 'Bcast' );
    def bcast_function(self, ):
        retval = self.bcast_function_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set3 = None

        set3_tree = None

        try:
            try:
                # ProtoCC.g:152:2: ( 'bcast' | 'Bcast' )
                # ProtoCC.g:
                pass 
                root_0 = self._adaptor.nil()


                set3 = self.input.LT(1)

                if self.input.LA(1) in {116, 135}:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set3))

                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "bcast_function"


    class internal_event_function_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "internal_event_function"
    # ProtoCC.g:156:1: internal_event_function : 'Event' ;
    def internal_event_function(self, ):
        retval = self.internal_event_function_return()
        retval.start = self.input.LT(1)


        root_0 = None

        string_literal4 = None

        string_literal4_tree = None

        try:
            try:
                # ProtoCC.g:157:2: ( 'Event' )
                # ProtoCC.g:157:4: 'Event'
                pass 
                root_0 = self._adaptor.nil()


                string_literal4 = self.match(self.input, 119, self.FOLLOW_119_in_internal_event_function750)
                string_literal4_tree = self._adaptor.createWithPayload(string_literal4)
                self._adaptor.addChild(root_0, string_literal4_tree)





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "internal_event_function"


    class set_function_types_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "set_function_types"
    # ProtoCC.g:160:1: set_function_types : ( 'add' | 'count' | 'contains' | 'del' | 'clear' | 'smallest' );
    def set_function_types(self, ):
        retval = self.set_function_types_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set5 = None

        set5_tree = None

        try:
            try:
                # ProtoCC.g:161:2: ( 'add' | 'count' | 'contains' | 'del' | 'clear' | 'smallest' )
                # ProtoCC.g:
                pass 
                root_0 = self._adaptor.nil()


                set5 = self.input.LT(1)

                if self.input.LA(1) in {134, 136, 138, 139, 140, 144}:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set5))

                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "set_function_types"


    class relational_operator_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "relational_operator"
    # ProtoCC.g:169:1: relational_operator : ( '==' | '!=' | '<=' | '>=' | '<' | '>' );
    def relational_operator(self, ):
        retval = self.relational_operator_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set6 = None

        set6_tree = None

        try:
            try:
                # ProtoCC.g:170:2: ( '==' | '!=' | '<=' | '>=' | '<' | '>' )
                # ProtoCC.g:
                pass 
                root_0 = self._adaptor.nil()


                set6 = self.input.LT(1)

                if (111 <= self.input.LA(1) <= 115) or self.input.LA(1) in {109}:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set6))

                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "relational_operator"


    class combinatorial_operator_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "combinatorial_operator"
    # ProtoCC.g:178:1: combinatorial_operator : ( '&' | '|' );
    def combinatorial_operator(self, ):
        retval = self.combinatorial_operator_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set7 = None

        set7_tree = None

        try:
            try:
                # ProtoCC.g:179:5: ( '&' | '|' )
                # ProtoCC.g:
                pass 
                root_0 = self._adaptor.nil()


                set7 = self.input.LT(1)

                if self.input.LA(1) in {110, 145}:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set7))

                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "combinatorial_operator"


    class document_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "document"
    # ProtoCC.g:209:1: document : ( ( const_decl | init_hw | arch_block | expressions )* | policy_file );
    def document(self, ):
        retval = self.document_return()
        retval.start = self.input.LT(1)


        root_0 = None

        const_decl8 = None
        init_hw9 = None
        arch_block10 = None
        expressions11 = None
        policy_file12 = None


        try:
            try:
                # ProtoCC.g:210:2: ( ( const_decl | init_hw | arch_block | expressions )* | policy_file )
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if (LA2_0 in {EOF, ACCESS, ARCH, CACHE, CONSTANT, DIR, ID, IF, MEM, MSG, NETWORK, STALL, STATE, UNDEF, 119}) :
                    alt2 = 1
                elif (LA2_0 == 126) :
                    alt2 = 2
                else:
                    nvae = NoViableAltException("", 2, 0, self.input)

                    raise nvae


                if alt2 == 1:
                    # ProtoCC.g:210:4: ( const_decl | init_hw | arch_block | expressions )*
                    pass 
                    root_0 = self._adaptor.nil()


                    # ProtoCC.g:210:4: ( const_decl | init_hw | arch_block | expressions )*
                    while True: #loop1
                        alt1 = 5
                        LA1 = self.input.LA(1)
                        if LA1 in {CONSTANT}:
                            alt1 = 1
                        elif LA1 in {CACHE, DIR, MEM, MSG, NETWORK}:
                            alt1 = 2
                        elif LA1 in {ARCH}:
                            alt1 = 3
                        elif LA1 in {ACCESS, ID, IF, STALL, STATE, UNDEF, 119}:
                            alt1 = 4

                        if alt1 == 1:
                            # ProtoCC.g:210:5: const_decl
                            pass 
                            self._state.following.append(self.FOLLOW_const_decl_in_document1078)
                            const_decl8 = self.const_decl()

                            self._state.following.pop()
                            self._adaptor.addChild(root_0, const_decl8.tree)



                        elif alt1 == 2:
                            # ProtoCC.g:210:18: init_hw
                            pass 
                            self._state.following.append(self.FOLLOW_init_hw_in_document1082)
                            init_hw9 = self.init_hw()

                            self._state.following.pop()
                            self._adaptor.addChild(root_0, init_hw9.tree)



                        elif alt1 == 3:
                            # ProtoCC.g:210:28: arch_block
                            pass 
                            self._state.following.append(self.FOLLOW_arch_block_in_document1086)
                            arch_block10 = self.arch_block()

                            self._state.following.pop()
                            self._adaptor.addChild(root_0, arch_block10.tree)



                        elif alt1 == 4:
                            # ProtoCC.g:210:41: expressions
                            pass 
                            self._state.following.append(self.FOLLOW_expressions_in_document1090)
                            expressions11 = self.expressions()

                            self._state.following.pop()
                            self._adaptor.addChild(root_0, expressions11.tree)



                        else:
                            break #loop1



                elif alt2 == 2:
                    # ProtoCC.g:211:4: policy_file
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_policy_file_in_document1098)
                    policy_file12 = self.policy_file()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, policy_file12.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "document"


    class declarations_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "declarations"
    # ProtoCC.g:215:1: declarations : ( int_decl | bool_decl | state_decl | data_decl | id_decl );
    def declarations(self, ):
        retval = self.declarations_return()
        retval.start = self.input.LT(1)


        root_0 = None

        int_decl13 = None
        bool_decl14 = None
        state_decl15 = None
        data_decl16 = None
        id_decl17 = None


        try:
            try:
                # ProtoCC.g:215:14: ( int_decl | bool_decl | state_decl | data_decl | id_decl )
                alt3 = 5
                LA3 = self.input.LA(1)
                if LA3 in {INTID}:
                    alt3 = 1
                elif LA3 in {BOOLID}:
                    alt3 = 2
                elif LA3 in {STATE}:
                    alt3 = 3
                elif LA3 in {DATA}:
                    alt3 = 4
                elif LA3 in {NID, SET}:
                    alt3 = 5
                else:
                    nvae = NoViableAltException("", 3, 0, self.input)

                    raise nvae


                if alt3 == 1:
                    # ProtoCC.g:215:16: int_decl
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_int_decl_in_declarations1109)
                    int_decl13 = self.int_decl()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, int_decl13.tree)



                elif alt3 == 2:
                    # ProtoCC.g:215:27: bool_decl
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_bool_decl_in_declarations1113)
                    bool_decl14 = self.bool_decl()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, bool_decl14.tree)



                elif alt3 == 3:
                    # ProtoCC.g:215:39: state_decl
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_state_decl_in_declarations1117)
                    state_decl15 = self.state_decl()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, state_decl15.tree)



                elif alt3 == 4:
                    # ProtoCC.g:215:52: data_decl
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_data_decl_in_declarations1121)
                    data_decl16 = self.data_decl()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, data_decl16.tree)



                elif alt3 == 5:
                    # ProtoCC.g:215:64: id_decl
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_id_decl_in_declarations1125)
                    id_decl17 = self.id_decl()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, id_decl17.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "declarations"


    class const_decl_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "const_decl"
    # ProtoCC.g:217:5: const_decl : CONSTANT ID INT -> ^( CONSTANT_ ID INT ) ;
    def const_decl(self, ):
        retval = self.const_decl_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CONSTANT18 = None
        ID19 = None
        INT20 = None

        CONSTANT18_tree = None
        ID19_tree = None
        INT20_tree = None
        stream_CONSTANT = RewriteRuleTokenStream(self._adaptor, "token CONSTANT")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INT = RewriteRuleTokenStream(self._adaptor, "token INT")

        try:
            try:
                # ProtoCC.g:217:16: ( CONSTANT ID INT -> ^( CONSTANT_ ID INT ) )
                # ProtoCC.g:217:18: CONSTANT ID INT
                pass 
                CONSTANT18 = self.match(self.input, CONSTANT, self.FOLLOW_CONSTANT_in_const_decl1137) 
                stream_CONSTANT.add(CONSTANT18)


                ID19 = self.match(self.input, ID, self.FOLLOW_ID_in_const_decl1139) 
                stream_ID.add(ID19)


                INT20 = self.match(self.input, INT, self.FOLLOW_INT_in_const_decl1141) 
                stream_INT.add(INT20)


                # AST Rewrite
                # elements: ID, INT
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 217:34: -> ^( CONSTANT_ ID INT )
                # ProtoCC.g:217:37: ^( CONSTANT_ ID INT )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(CONSTANT_, "CONSTANT_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_1, 
                stream_INT.nextNode()
                )

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "const_decl"


    class int_decl_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "int_decl"
    # ProtoCC.g:219:5: int_decl : INTID range ID ( EQUALSIGN INT )* SEMICOLON -> ^( INT_ ID range ( ^( INITVAL_ INT ) )* ) ;
    def int_decl(self, ):
        retval = self.int_decl_return()
        retval.start = self.input.LT(1)


        root_0 = None

        INTID21 = None
        ID23 = None
        EQUALSIGN24 = None
        INT25 = None
        SEMICOLON26 = None
        range22 = None

        INTID21_tree = None
        ID23_tree = None
        EQUALSIGN24_tree = None
        INT25_tree = None
        SEMICOLON26_tree = None
        stream_EQUALSIGN = RewriteRuleTokenStream(self._adaptor, "token EQUALSIGN")
        stream_INTID = RewriteRuleTokenStream(self._adaptor, "token INTID")
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INT = RewriteRuleTokenStream(self._adaptor, "token INT")
        stream_range = RewriteRuleSubtreeStream(self._adaptor, "rule range")
        try:
            try:
                # ProtoCC.g:219:14: ( INTID range ID ( EQUALSIGN INT )* SEMICOLON -> ^( INT_ ID range ( ^( INITVAL_ INT ) )* ) )
                # ProtoCC.g:219:16: INTID range ID ( EQUALSIGN INT )* SEMICOLON
                pass 
                INTID21 = self.match(self.input, INTID, self.FOLLOW_INTID_in_int_decl1163) 
                stream_INTID.add(INTID21)


                self._state.following.append(self.FOLLOW_range_in_int_decl1165)
                range22 = self.range()

                self._state.following.pop()
                stream_range.add(range22.tree)


                ID23 = self.match(self.input, ID, self.FOLLOW_ID_in_int_decl1167) 
                stream_ID.add(ID23)


                # ProtoCC.g:219:31: ( EQUALSIGN INT )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == EQUALSIGN) :
                        alt4 = 1


                    if alt4 == 1:
                        # ProtoCC.g:219:32: EQUALSIGN INT
                        pass 
                        EQUALSIGN24 = self.match(self.input, EQUALSIGN, self.FOLLOW_EQUALSIGN_in_int_decl1170) 
                        stream_EQUALSIGN.add(EQUALSIGN24)


                        INT25 = self.match(self.input, INT, self.FOLLOW_INT_in_int_decl1172) 
                        stream_INT.add(INT25)



                    else:
                        break #loop4


                SEMICOLON26 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_int_decl1176) 
                stream_SEMICOLON.add(SEMICOLON26)


                # AST Rewrite
                # elements: ID, range, INT
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 219:58: -> ^( INT_ ID range ( ^( INITVAL_ INT ) )* )
                # ProtoCC.g:219:61: ^( INT_ ID range ( ^( INITVAL_ INT ) )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(INT_, "INT_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_1, stream_range.nextTree())

                # ProtoCC.g:219:77: ( ^( INITVAL_ INT ) )*
                while stream_INT.hasNext():
                    # ProtoCC.g:219:77: ^( INITVAL_ INT )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(INITVAL_, "INITVAL_")
                    , root_2)

                    self._adaptor.addChild(root_2, 
                    stream_INT.nextNode()
                    )

                    self._adaptor.addChild(root_1, root_2)


                stream_INT.reset();

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "int_decl"


    class bool_decl_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "bool_decl"
    # ProtoCC.g:220:5: bool_decl : BOOLID ID ( EQUALSIGN BOOL )* SEMICOLON -> ^( BOOL_ ID ( ^( INITVAL_ BOOL ) )* ) ;
    def bool_decl(self, ):
        retval = self.bool_decl_return()
        retval.start = self.input.LT(1)


        root_0 = None

        BOOLID27 = None
        ID28 = None
        EQUALSIGN29 = None
        BOOL30 = None
        SEMICOLON31 = None

        BOOLID27_tree = None
        ID28_tree = None
        EQUALSIGN29_tree = None
        BOOL30_tree = None
        SEMICOLON31_tree = None
        stream_EQUALSIGN = RewriteRuleTokenStream(self._adaptor, "token EQUALSIGN")
        stream_BOOL = RewriteRuleTokenStream(self._adaptor, "token BOOL")
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_BOOLID = RewriteRuleTokenStream(self._adaptor, "token BOOLID")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # ProtoCC.g:220:15: ( BOOLID ID ( EQUALSIGN BOOL )* SEMICOLON -> ^( BOOL_ ID ( ^( INITVAL_ BOOL ) )* ) )
                # ProtoCC.g:220:17: BOOLID ID ( EQUALSIGN BOOL )* SEMICOLON
                pass 
                BOOLID27 = self.match(self.input, BOOLID, self.FOLLOW_BOOLID_in_bool_decl1204) 
                stream_BOOLID.add(BOOLID27)


                ID28 = self.match(self.input, ID, self.FOLLOW_ID_in_bool_decl1206) 
                stream_ID.add(ID28)


                # ProtoCC.g:220:27: ( EQUALSIGN BOOL )*
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == EQUALSIGN) :
                        alt5 = 1


                    if alt5 == 1:
                        # ProtoCC.g:220:28: EQUALSIGN BOOL
                        pass 
                        EQUALSIGN29 = self.match(self.input, EQUALSIGN, self.FOLLOW_EQUALSIGN_in_bool_decl1209) 
                        stream_EQUALSIGN.add(EQUALSIGN29)


                        BOOL30 = self.match(self.input, BOOL, self.FOLLOW_BOOL_in_bool_decl1211) 
                        stream_BOOL.add(BOOL30)



                    else:
                        break #loop5


                SEMICOLON31 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_bool_decl1215) 
                stream_SEMICOLON.add(SEMICOLON31)


                # AST Rewrite
                # elements: ID, BOOL
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 220:55: -> ^( BOOL_ ID ( ^( INITVAL_ BOOL ) )* )
                # ProtoCC.g:220:58: ^( BOOL_ ID ( ^( INITVAL_ BOOL ) )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(BOOL_, "BOOL_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # ProtoCC.g:220:69: ( ^( INITVAL_ BOOL ) )*
                while stream_BOOL.hasNext():
                    # ProtoCC.g:220:69: ^( INITVAL_ BOOL )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(INITVAL_, "INITVAL_")
                    , root_2)

                    self._adaptor.addChild(root_2, 
                    stream_BOOL.nextNode()
                    )

                    self._adaptor.addChild(root_1, root_2)


                stream_BOOL.reset();

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "bool_decl"


    class state_decl_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "state_decl"
    # ProtoCC.g:222:5: state_decl : STATE ID SEMICOLON -> ^( INITSTATE_ ID ) ;
    def state_decl(self, ):
        retval = self.state_decl_return()
        retval.start = self.input.LT(1)


        root_0 = None

        STATE32 = None
        ID33 = None
        SEMICOLON34 = None

        STATE32_tree = None
        ID33_tree = None
        SEMICOLON34_tree = None
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_STATE = RewriteRuleTokenStream(self._adaptor, "token STATE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # ProtoCC.g:222:16: ( STATE ID SEMICOLON -> ^( INITSTATE_ ID ) )
                # ProtoCC.g:222:18: STATE ID SEMICOLON
                pass 
                STATE32 = self.match(self.input, STATE, self.FOLLOW_STATE_in_state_decl1242) 
                stream_STATE.add(STATE32)


                ID33 = self.match(self.input, ID, self.FOLLOW_ID_in_state_decl1244) 
                stream_ID.add(ID33)


                SEMICOLON34 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_state_decl1246) 
                stream_SEMICOLON.add(SEMICOLON34)


                # AST Rewrite
                # elements: ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 222:37: -> ^( INITSTATE_ ID )
                # ProtoCC.g:222:40: ^( INITSTATE_ ID )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(INITSTATE_, "INITSTATE_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "state_decl"


    class data_decl_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "data_decl"
    # ProtoCC.g:223:5: data_decl : DATA ID SEMICOLON -> ^( DATA_ ID ) ;
    def data_decl(self, ):
        retval = self.data_decl_return()
        retval.start = self.input.LT(1)


        root_0 = None

        DATA35 = None
        ID36 = None
        SEMICOLON37 = None

        DATA35_tree = None
        ID36_tree = None
        SEMICOLON37_tree = None
        stream_DATA = RewriteRuleTokenStream(self._adaptor, "token DATA")
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # ProtoCC.g:223:15: ( DATA ID SEMICOLON -> ^( DATA_ ID ) )
                # ProtoCC.g:223:17: DATA ID SEMICOLON
                pass 
                DATA35 = self.match(self.input, DATA, self.FOLLOW_DATA_in_data_decl1265) 
                stream_DATA.add(DATA35)


                ID36 = self.match(self.input, ID, self.FOLLOW_ID_in_data_decl1267) 
                stream_ID.add(ID36)


                SEMICOLON37 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_data_decl1269) 
                stream_SEMICOLON.add(SEMICOLON37)


                # AST Rewrite
                # elements: ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 223:35: -> ^( DATA_ ID )
                # ProtoCC.g:223:38: ^( DATA_ ID )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(DATA_, "DATA_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "data_decl"


    class id_decl_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "id_decl"
    # ProtoCC.g:224:5: id_decl : ( set_decl )* NID ID ( EQUALSIGN ( set_decl )* ID )* SEMICOLON -> ^( ID_ ID ( set_decl )* ( ^( INITVAL_ ( set_decl )* ID ) )* ) ;
    def id_decl(self, ):
        retval = self.id_decl_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NID39 = None
        ID40 = None
        EQUALSIGN41 = None
        ID43 = None
        SEMICOLON44 = None
        set_decl38 = None
        set_decl42 = None

        NID39_tree = None
        ID40_tree = None
        EQUALSIGN41_tree = None
        ID43_tree = None
        SEMICOLON44_tree = None
        stream_EQUALSIGN = RewriteRuleTokenStream(self._adaptor, "token EQUALSIGN")
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_NID = RewriteRuleTokenStream(self._adaptor, "token NID")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_set_decl = RewriteRuleSubtreeStream(self._adaptor, "rule set_decl")
        try:
            try:
                # ProtoCC.g:224:13: ( ( set_decl )* NID ID ( EQUALSIGN ( set_decl )* ID )* SEMICOLON -> ^( ID_ ID ( set_decl )* ( ^( INITVAL_ ( set_decl )* ID ) )* ) )
                # ProtoCC.g:224:15: ( set_decl )* NID ID ( EQUALSIGN ( set_decl )* ID )* SEMICOLON
                pass 
                # ProtoCC.g:224:15: ( set_decl )*
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == SET) :
                        alt6 = 1


                    if alt6 == 1:
                        # ProtoCC.g:224:15: set_decl
                        pass 
                        self._state.following.append(self.FOLLOW_set_decl_in_id_decl1288)
                        set_decl38 = self.set_decl()

                        self._state.following.pop()
                        stream_set_decl.add(set_decl38.tree)



                    else:
                        break #loop6


                NID39 = self.match(self.input, NID, self.FOLLOW_NID_in_id_decl1291) 
                stream_NID.add(NID39)


                ID40 = self.match(self.input, ID, self.FOLLOW_ID_in_id_decl1293) 
                stream_ID.add(ID40)


                # ProtoCC.g:224:32: ( EQUALSIGN ( set_decl )* ID )*
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == EQUALSIGN) :
                        alt8 = 1


                    if alt8 == 1:
                        # ProtoCC.g:224:33: EQUALSIGN ( set_decl )* ID
                        pass 
                        EQUALSIGN41 = self.match(self.input, EQUALSIGN, self.FOLLOW_EQUALSIGN_in_id_decl1296) 
                        stream_EQUALSIGN.add(EQUALSIGN41)


                        # ProtoCC.g:224:43: ( set_decl )*
                        while True: #loop7
                            alt7 = 2
                            LA7_0 = self.input.LA(1)

                            if (LA7_0 == SET) :
                                alt7 = 1


                            if alt7 == 1:
                                # ProtoCC.g:224:43: set_decl
                                pass 
                                self._state.following.append(self.FOLLOW_set_decl_in_id_decl1298)
                                set_decl42 = self.set_decl()

                                self._state.following.pop()
                                stream_set_decl.add(set_decl42.tree)



                            else:
                                break #loop7


                        ID43 = self.match(self.input, ID, self.FOLLOW_ID_in_id_decl1301) 
                        stream_ID.add(ID43)



                    else:
                        break #loop8


                SEMICOLON44 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_id_decl1305) 
                stream_SEMICOLON.add(SEMICOLON44)


                # AST Rewrite
                # elements: set_decl, set_decl, ID, ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 224:68: -> ^( ID_ ID ( set_decl )* ( ^( INITVAL_ ( set_decl )* ID ) )* )
                # ProtoCC.g:224:71: ^( ID_ ID ( set_decl )* ( ^( INITVAL_ ( set_decl )* ID ) )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(ID_, "ID_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # ProtoCC.g:224:80: ( set_decl )*
                while stream_set_decl.hasNext():
                    self._adaptor.addChild(root_1, stream_set_decl.nextTree())


                stream_set_decl.reset();

                # ProtoCC.g:224:90: ( ^( INITVAL_ ( set_decl )* ID ) )*
                while stream_ID.hasNext():
                    # ProtoCC.g:224:90: ^( INITVAL_ ( set_decl )* ID )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(INITVAL_, "INITVAL_")
                    , root_2)

                    # ProtoCC.g:224:101: ( set_decl )*
                    while stream_set_decl.hasNext():
                        self._adaptor.addChild(root_2, stream_set_decl.nextTree())


                    stream_set_decl.reset();

                    self._adaptor.addChild(root_2, 
                    stream_ID.nextNode()
                    )

                    self._adaptor.addChild(root_1, root_2)


                stream_ID.reset();

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "id_decl"


    class set_decl_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "set_decl"
    # ProtoCC.g:226:9: set_decl : SET OEBRACE val_range CEBRACE -> ^( SET_ val_range ) ;
    def set_decl(self, ):
        retval = self.set_decl_return()
        retval.start = self.input.LT(1)


        root_0 = None

        SET45 = None
        OEBRACE46 = None
        CEBRACE48 = None
        val_range47 = None

        SET45_tree = None
        OEBRACE46_tree = None
        CEBRACE48_tree = None
        stream_SET = RewriteRuleTokenStream(self._adaptor, "token SET")
        stream_CEBRACE = RewriteRuleTokenStream(self._adaptor, "token CEBRACE")
        stream_OEBRACE = RewriteRuleTokenStream(self._adaptor, "token OEBRACE")
        stream_val_range = RewriteRuleSubtreeStream(self._adaptor, "rule val_range")
        try:
            try:
                # ProtoCC.g:226:18: ( SET OEBRACE val_range CEBRACE -> ^( SET_ val_range ) )
                # ProtoCC.g:226:20: SET OEBRACE val_range CEBRACE
                pass 
                SET45 = self.match(self.input, SET, self.FOLLOW_SET_in_set_decl1342) 
                stream_SET.add(SET45)


                OEBRACE46 = self.match(self.input, OEBRACE, self.FOLLOW_OEBRACE_in_set_decl1344) 
                stream_OEBRACE.add(OEBRACE46)


                self._state.following.append(self.FOLLOW_val_range_in_set_decl1346)
                val_range47 = self.val_range()

                self._state.following.pop()
                stream_val_range.add(val_range47.tree)


                CEBRACE48 = self.match(self.input, CEBRACE, self.FOLLOW_CEBRACE_in_set_decl1348) 
                stream_CEBRACE.add(CEBRACE48)


                # AST Rewrite
                # elements: val_range
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 226:50: -> ^( SET_ val_range )
                # ProtoCC.g:226:53: ^( SET_ val_range )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(SET_, "SET_")
                , root_1)

                self._adaptor.addChild(root_1, stream_val_range.nextTree())

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "set_decl"


    class range_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "range"
    # ProtoCC.g:227:9: range : OEBRACE val_range DOT DOT val_range CEBRACE -> ^( RANGE_ OEBRACE val_range DOT DOT val_range CEBRACE ) ;
    def range(self, ):
        retval = self.range_return()
        retval.start = self.input.LT(1)


        root_0 = None

        OEBRACE49 = None
        DOT51 = None
        DOT52 = None
        CEBRACE54 = None
        val_range50 = None
        val_range53 = None

        OEBRACE49_tree = None
        DOT51_tree = None
        DOT52_tree = None
        CEBRACE54_tree = None
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")
        stream_CEBRACE = RewriteRuleTokenStream(self._adaptor, "token CEBRACE")
        stream_OEBRACE = RewriteRuleTokenStream(self._adaptor, "token OEBRACE")
        stream_val_range = RewriteRuleSubtreeStream(self._adaptor, "rule val_range")
        try:
            try:
                # ProtoCC.g:227:15: ( OEBRACE val_range DOT DOT val_range CEBRACE -> ^( RANGE_ OEBRACE val_range DOT DOT val_range CEBRACE ) )
                # ProtoCC.g:227:17: OEBRACE val_range DOT DOT val_range CEBRACE
                pass 
                OEBRACE49 = self.match(self.input, OEBRACE, self.FOLLOW_OEBRACE_in_range1371) 
                stream_OEBRACE.add(OEBRACE49)


                self._state.following.append(self.FOLLOW_val_range_in_range1373)
                val_range50 = self.val_range()

                self._state.following.pop()
                stream_val_range.add(val_range50.tree)


                DOT51 = self.match(self.input, DOT, self.FOLLOW_DOT_in_range1375) 
                stream_DOT.add(DOT51)


                DOT52 = self.match(self.input, DOT, self.FOLLOW_DOT_in_range1377) 
                stream_DOT.add(DOT52)


                self._state.following.append(self.FOLLOW_val_range_in_range1379)
                val_range53 = self.val_range()

                self._state.following.pop()
                stream_val_range.add(val_range53.tree)


                CEBRACE54 = self.match(self.input, CEBRACE, self.FOLLOW_CEBRACE_in_range1381) 
                stream_CEBRACE.add(CEBRACE54)


                # AST Rewrite
                # elements: OEBRACE, DOT, val_range, val_range, DOT, CEBRACE
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 227:61: -> ^( RANGE_ OEBRACE val_range DOT DOT val_range CEBRACE )
                # ProtoCC.g:227:64: ^( RANGE_ OEBRACE val_range DOT DOT val_range CEBRACE )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(RANGE_, "RANGE_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_OEBRACE.nextNode()
                )

                self._adaptor.addChild(root_1, stream_val_range.nextTree())

                self._adaptor.addChild(root_1, 
                stream_DOT.nextNode()
                )

                self._adaptor.addChild(root_1, 
                stream_DOT.nextNode()
                )

                self._adaptor.addChild(root_1, stream_val_range.nextTree())

                self._adaptor.addChild(root_1, 
                stream_CEBRACE.nextNode()
                )

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "range"


    class val_range_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "val_range"
    # ProtoCC.g:228:9: val_range : ( INT | ID );
    def val_range(self, ):
        retval = self.val_range_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set55 = None

        set55_tree = None

        try:
            try:
                # ProtoCC.g:228:19: ( INT | ID )
                # ProtoCC.g:
                pass 
                root_0 = self._adaptor.nil()


                set55 = self.input.LT(1)

                if self.input.LA(1) in {ID, INT}:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set55))

                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "val_range"


    class array_decl_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "array_decl"
    # ProtoCC.g:230:5: array_decl : ARRAY range ;
    def array_decl(self, ):
        retval = self.array_decl_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ARRAY56 = None
        range57 = None

        ARRAY56_tree = None

        try:
            try:
                # ProtoCC.g:230:16: ( ARRAY range )
                # ProtoCC.g:230:18: ARRAY range
                pass 
                root_0 = self._adaptor.nil()


                ARRAY56 = self.match(self.input, ARRAY, self.FOLLOW_ARRAY_in_array_decl1430)
                ARRAY56_tree = self._adaptor.createWithPayload(ARRAY56)
                self._adaptor.addChild(root_0, ARRAY56_tree)



                self._state.following.append(self.FOLLOW_range_in_array_decl1432)
                range57 = self.range()

                self._state.following.pop()
                self._adaptor.addChild(root_0, range57.tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "array_decl"


    class fifo_decl_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "fifo_decl"
    # ProtoCC.g:231:5: fifo_decl : FIFO range ;
    def fifo_decl(self, ):
        retval = self.fifo_decl_return()
        retval.start = self.input.LT(1)


        root_0 = None

        FIFO58 = None
        range59 = None

        FIFO58_tree = None

        try:
            try:
                # ProtoCC.g:231:14: ( FIFO range )
                # ProtoCC.g:231:16: FIFO range
                pass 
                root_0 = self._adaptor.nil()


                FIFO58 = self.match(self.input, FIFO, self.FOLLOW_FIFO_in_fifo_decl1442)
                FIFO58_tree = self._adaptor.createWithPayload(FIFO58)
                self._adaptor.addChild(root_0, FIFO58_tree)



                self._state.following.append(self.FOLLOW_range_in_fifo_decl1444)
                range59 = self.range()

                self._state.following.pop()
                self._adaptor.addChild(root_0, range59.tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "fifo_decl"


    class init_hw_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "init_hw"
    # ProtoCC.g:234:1: init_hw : ( network_block | machines | message_block );
    def init_hw(self, ):
        retval = self.init_hw_return()
        retval.start = self.input.LT(1)


        root_0 = None

        network_block60 = None
        machines61 = None
        message_block62 = None


        try:
            try:
                # ProtoCC.g:234:9: ( network_block | machines | message_block )
                alt9 = 3
                LA9 = self.input.LA(1)
                if LA9 in {NETWORK}:
                    alt9 = 1
                elif LA9 in {CACHE, DIR, MEM}:
                    alt9 = 2
                elif LA9 in {MSG}:
                    alt9 = 3
                else:
                    nvae = NoViableAltException("", 9, 0, self.input)

                    raise nvae


                if alt9 == 1:
                    # ProtoCC.g:234:11: network_block
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_network_block_in_init_hw1454)
                    network_block60 = self.network_block()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, network_block60.tree)



                elif alt9 == 2:
                    # ProtoCC.g:234:27: machines
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_machines_in_init_hw1458)
                    machines61 = self.machines()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, machines61.tree)



                elif alt9 == 3:
                    # ProtoCC.g:234:38: message_block
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_message_block_in_init_hw1462)
                    message_block62 = self.message_block()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, message_block62.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "init_hw"


    class object_block_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "object_block"
    # ProtoCC.g:235:5: object_block : object_expr SEMICOLON -> object_expr ;
    def object_block(self, ):
        retval = self.object_block_return()
        retval.start = self.input.LT(1)


        root_0 = None

        SEMICOLON64 = None
        object_expr63 = None

        SEMICOLON64_tree = None
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_object_expr = RewriteRuleSubtreeStream(self._adaptor, "rule object_expr")
        try:
            try:
                # ProtoCC.g:235:18: ( object_expr SEMICOLON -> object_expr )
                # ProtoCC.g:235:20: object_expr SEMICOLON
                pass 
                self._state.following.append(self.FOLLOW_object_expr_in_object_block1473)
                object_expr63 = self.object_expr()

                self._state.following.pop()
                stream_object_expr.add(object_expr63.tree)


                SEMICOLON64 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_object_block1475) 
                stream_SEMICOLON.add(SEMICOLON64)


                # AST Rewrite
                # elements: object_expr
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 235:42: -> object_expr
                self._adaptor.addChild(root_0, stream_object_expr.nextTree())




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "object_block"


    class object_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "object_expr"
    # ProtoCC.g:236:5: object_expr : ( object_id | object_func );
    def object_expr(self, ):
        retval = self.object_expr_return()
        retval.start = self.input.LT(1)


        root_0 = None

        object_id65 = None
        object_func66 = None


        try:
            try:
                # ProtoCC.g:236:17: ( object_id | object_func )
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (LA10_0 == ID) :
                    LA10_1 = self.input.LA(2)

                    if (LA10_1 == DOT) :
                        alt10 = 2
                    elif ((109 <= LA10_1 <= 115) or LA10_1 in {BOOL, CBRACE, COMMA, ID, INT, MINUS, MULT, NID, OCBRACE, PLUS, SEMICOLON, 145}) :
                        alt10 = 1
                    else:
                        nvae = NoViableAltException("", 10, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 10, 0, self.input)

                    raise nvae


                if alt10 == 1:
                    # ProtoCC.g:236:19: object_id
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_object_id_in_object_expr1490)
                    object_id65 = self.object_id()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, object_id65.tree)



                elif alt10 == 2:
                    # ProtoCC.g:236:31: object_func
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_object_func_in_object_expr1494)
                    object_func66 = self.object_func()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, object_func66.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "object_expr"


    class object_id_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "object_id"
    # ProtoCC.g:237:5: object_id : ID -> ^( ID ) ;
    def object_id(self, ):
        retval = self.object_id_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID67 = None

        ID67_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # ProtoCC.g:237:14: ( ID -> ^( ID ) )
                # ProtoCC.g:237:17: ID
                pass 
                ID67 = self.match(self.input, ID, self.FOLLOW_ID_in_object_id1505) 
                stream_ID.add(ID67)


                # AST Rewrite
                # elements: ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 237:20: -> ^( ID )
                # ProtoCC.g:237:23: ^( ID )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                stream_ID.nextNode()
                , root_1)

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "object_id"


    class object_func_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "object_func"
    # ProtoCC.g:238:5: object_func : ID DOT object_idres ( OBRACE ( object_expr )* ( COMMA object_expr )* CBRACE )* -> ^( ID DOT object_idres ( OBRACE ( object_expr )* ( COMMA object_expr )* CBRACE )* ) ;
    def object_func(self, ):
        retval = self.object_func_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID68 = None
        DOT69 = None
        OBRACE71 = None
        COMMA73 = None
        CBRACE75 = None
        object_idres70 = None
        object_expr72 = None
        object_expr74 = None

        ID68_tree = None
        DOT69_tree = None
        OBRACE71_tree = None
        COMMA73_tree = None
        CBRACE75_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_OBRACE = RewriteRuleTokenStream(self._adaptor, "token OBRACE")
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CBRACE = RewriteRuleTokenStream(self._adaptor, "token CBRACE")
        stream_object_idres = RewriteRuleSubtreeStream(self._adaptor, "rule object_idres")
        stream_object_expr = RewriteRuleSubtreeStream(self._adaptor, "rule object_expr")
        try:
            try:
                # ProtoCC.g:238:17: ( ID DOT object_idres ( OBRACE ( object_expr )* ( COMMA object_expr )* CBRACE )* -> ^( ID DOT object_idres ( OBRACE ( object_expr )* ( COMMA object_expr )* CBRACE )* ) )
                # ProtoCC.g:238:19: ID DOT object_idres ( OBRACE ( object_expr )* ( COMMA object_expr )* CBRACE )*
                pass 
                ID68 = self.match(self.input, ID, self.FOLLOW_ID_in_object_func1522) 
                stream_ID.add(ID68)


                DOT69 = self.match(self.input, DOT, self.FOLLOW_DOT_in_object_func1524) 
                stream_DOT.add(DOT69)


                self._state.following.append(self.FOLLOW_object_idres_in_object_func1526)
                object_idres70 = self.object_idres()

                self._state.following.pop()
                stream_object_idres.add(object_idres70.tree)


                # ProtoCC.g:238:39: ( OBRACE ( object_expr )* ( COMMA object_expr )* CBRACE )*
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == OBRACE) :
                        alt13 = 1


                    if alt13 == 1:
                        # ProtoCC.g:238:40: OBRACE ( object_expr )* ( COMMA object_expr )* CBRACE
                        pass 
                        OBRACE71 = self.match(self.input, OBRACE, self.FOLLOW_OBRACE_in_object_func1529) 
                        stream_OBRACE.add(OBRACE71)


                        # ProtoCC.g:238:47: ( object_expr )*
                        while True: #loop11
                            alt11 = 2
                            LA11_0 = self.input.LA(1)

                            if (LA11_0 == ID) :
                                alt11 = 1


                            if alt11 == 1:
                                # ProtoCC.g:238:47: object_expr
                                pass 
                                self._state.following.append(self.FOLLOW_object_expr_in_object_func1531)
                                object_expr72 = self.object_expr()

                                self._state.following.pop()
                                stream_object_expr.add(object_expr72.tree)



                            else:
                                break #loop11


                        # ProtoCC.g:238:60: ( COMMA object_expr )*
                        while True: #loop12
                            alt12 = 2
                            LA12_0 = self.input.LA(1)

                            if (LA12_0 == COMMA) :
                                alt12 = 1


                            if alt12 == 1:
                                # ProtoCC.g:238:61: COMMA object_expr
                                pass 
                                COMMA73 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_object_func1535) 
                                stream_COMMA.add(COMMA73)


                                self._state.following.append(self.FOLLOW_object_expr_in_object_func1537)
                                object_expr74 = self.object_expr()

                                self._state.following.pop()
                                stream_object_expr.add(object_expr74.tree)



                            else:
                                break #loop12


                        CBRACE75 = self.match(self.input, CBRACE, self.FOLLOW_CBRACE_in_object_func1541) 
                        stream_CBRACE.add(CBRACE75)



                    else:
                        break #loop13


                # AST Rewrite
                # elements: ID, object_expr, object_expr, DOT, OBRACE, COMMA, object_idres, CBRACE
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 238:90: -> ^( ID DOT object_idres ( OBRACE ( object_expr )* ( COMMA object_expr )* CBRACE )* )
                # ProtoCC.g:239:9: ^( ID DOT object_idres ( OBRACE ( object_expr )* ( COMMA object_expr )* CBRACE )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                stream_ID.nextNode()
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_DOT.nextNode()
                )

                self._adaptor.addChild(root_1, stream_object_idres.nextTree())

                # ProtoCC.g:239:31: ( OBRACE ( object_expr )* ( COMMA object_expr )* CBRACE )*
                while stream_OBRACE.hasNext() or stream_CBRACE.hasNext():
                    self._adaptor.addChild(root_1, 
                    stream_OBRACE.nextNode()
                    )

                    # ProtoCC.g:239:39: ( object_expr )*
                    while stream_object_expr.hasNext():
                        self._adaptor.addChild(root_1, stream_object_expr.nextTree())


                    stream_object_expr.reset();

                    # ProtoCC.g:239:52: ( COMMA object_expr )*
                    while stream_object_expr.hasNext() or stream_COMMA.hasNext():
                        self._adaptor.addChild(root_1, 
                        stream_COMMA.nextNode()
                        )

                        self._adaptor.addChild(root_1, stream_object_expr.nextTree())


                    stream_object_expr.reset();
                    stream_COMMA.reset();

                    self._adaptor.addChild(root_1, 
                    stream_CBRACE.nextNode()
                    )


                stream_OBRACE.reset();
                stream_CBRACE.reset();

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "object_func"


    class object_idres_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "object_idres"
    # ProtoCC.g:240:5: object_idres : ( ID | NID );
    def object_idres(self, ):
        retval = self.object_idres_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set76 = None

        set76_tree = None

        try:
            try:
                # ProtoCC.g:240:17: ( ID | NID )
                # ProtoCC.g:
                pass 
                root_0 = self._adaptor.nil()


                set76 = self.input.LT(1)

                if self.input.LA(1) in {ID, NID}:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set76))

                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "object_idres"


    class machines_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "machines"
    # ProtoCC.g:243:5: machines : ( cache_block | dir_block | mem_block );
    def machines(self, ):
        retval = self.machines_return()
        retval.start = self.input.LT(1)


        root_0 = None

        cache_block77 = None
        dir_block78 = None
        mem_block79 = None


        try:
            try:
                # ProtoCC.g:243:14: ( cache_block | dir_block | mem_block )
                alt14 = 3
                LA14 = self.input.LA(1)
                if LA14 in {CACHE}:
                    alt14 = 1
                elif LA14 in {DIR}:
                    alt14 = 2
                elif LA14 in {MEM}:
                    alt14 = 3
                else:
                    nvae = NoViableAltException("", 14, 0, self.input)

                    raise nvae


                if alt14 == 1:
                    # ProtoCC.g:243:16: cache_block
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_cache_block_in_machines1610)
                    cache_block77 = self.cache_block()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, cache_block77.tree)



                elif alt14 == 2:
                    # ProtoCC.g:243:30: dir_block
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_dir_block_in_machines1614)
                    dir_block78 = self.dir_block()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, dir_block78.tree)



                elif alt14 == 3:
                    # ProtoCC.g:243:42: mem_block
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_mem_block_in_machines1618)
                    mem_block79 = self.mem_block()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, mem_block79.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "machines"


    class cache_block_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "cache_block"
    # ProtoCC.g:244:9: cache_block : CACHE OCBRACE ( declarations )* CCBRACE ( objset_decl )* ID SEMICOLON -> ^( CACHE_ ID ( objset_decl )* ( declarations )* ) ;
    def cache_block(self, ):
        retval = self.cache_block_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CACHE80 = None
        OCBRACE81 = None
        CCBRACE83 = None
        ID85 = None
        SEMICOLON86 = None
        declarations82 = None
        objset_decl84 = None

        CACHE80_tree = None
        OCBRACE81_tree = None
        CCBRACE83_tree = None
        ID85_tree = None
        SEMICOLON86_tree = None
        stream_OCBRACE = RewriteRuleTokenStream(self._adaptor, "token OCBRACE")
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CACHE = RewriteRuleTokenStream(self._adaptor, "token CACHE")
        stream_CCBRACE = RewriteRuleTokenStream(self._adaptor, "token CCBRACE")
        stream_objset_decl = RewriteRuleSubtreeStream(self._adaptor, "rule objset_decl")
        stream_declarations = RewriteRuleSubtreeStream(self._adaptor, "rule declarations")
        try:
            try:
                # ProtoCC.g:244:21: ( CACHE OCBRACE ( declarations )* CCBRACE ( objset_decl )* ID SEMICOLON -> ^( CACHE_ ID ( objset_decl )* ( declarations )* ) )
                # ProtoCC.g:244:23: CACHE OCBRACE ( declarations )* CCBRACE ( objset_decl )* ID SEMICOLON
                pass 
                CACHE80 = self.match(self.input, CACHE, self.FOLLOW_CACHE_in_cache_block1633) 
                stream_CACHE.add(CACHE80)


                OCBRACE81 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_cache_block1635) 
                stream_OCBRACE.add(OCBRACE81)


                # ProtoCC.g:244:37: ( declarations )*
                while True: #loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if (LA15_0 in {BOOLID, DATA, INTID, NID, SET, STATE}) :
                        alt15 = 1


                    if alt15 == 1:
                        # ProtoCC.g:244:37: declarations
                        pass 
                        self._state.following.append(self.FOLLOW_declarations_in_cache_block1637)
                        declarations82 = self.declarations()

                        self._state.following.pop()
                        stream_declarations.add(declarations82.tree)



                    else:
                        break #loop15


                CCBRACE83 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_cache_block1640) 
                stream_CCBRACE.add(CCBRACE83)


                # ProtoCC.g:244:59: ( objset_decl )*
                while True: #loop16
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if (LA16_0 == SET) :
                        alt16 = 1


                    if alt16 == 1:
                        # ProtoCC.g:244:59: objset_decl
                        pass 
                        self._state.following.append(self.FOLLOW_objset_decl_in_cache_block1642)
                        objset_decl84 = self.objset_decl()

                        self._state.following.pop()
                        stream_objset_decl.add(objset_decl84.tree)



                    else:
                        break #loop16


                ID85 = self.match(self.input, ID, self.FOLLOW_ID_in_cache_block1645) 
                stream_ID.add(ID85)


                SEMICOLON86 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_cache_block1647) 
                stream_SEMICOLON.add(SEMICOLON86)


                # AST Rewrite
                # elements: ID, objset_decl, declarations
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 244:85: -> ^( CACHE_ ID ( objset_decl )* ( declarations )* )
                # ProtoCC.g:245:13: ^( CACHE_ ID ( objset_decl )* ( declarations )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(CACHE_, "CACHE_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # ProtoCC.g:245:25: ( objset_decl )*
                while stream_objset_decl.hasNext():
                    self._adaptor.addChild(root_1, stream_objset_decl.nextTree())


                stream_objset_decl.reset();

                # ProtoCC.g:245:38: ( declarations )*
                while stream_declarations.hasNext():
                    self._adaptor.addChild(root_1, stream_declarations.nextTree())


                stream_declarations.reset();

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "cache_block"


    class dir_block_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "dir_block"
    # ProtoCC.g:246:9: dir_block : DIR OCBRACE ( declarations )* CCBRACE ( objset_decl )* ID SEMICOLON -> ^( DIR_ ID ( objset_decl )* ( declarations )* ) ;
    def dir_block(self, ):
        retval = self.dir_block_return()
        retval.start = self.input.LT(1)


        root_0 = None

        DIR87 = None
        OCBRACE88 = None
        CCBRACE90 = None
        ID92 = None
        SEMICOLON93 = None
        declarations89 = None
        objset_decl91 = None

        DIR87_tree = None
        OCBRACE88_tree = None
        CCBRACE90_tree = None
        ID92_tree = None
        SEMICOLON93_tree = None
        stream_OCBRACE = RewriteRuleTokenStream(self._adaptor, "token OCBRACE")
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_DIR = RewriteRuleTokenStream(self._adaptor, "token DIR")
        stream_CCBRACE = RewriteRuleTokenStream(self._adaptor, "token CCBRACE")
        stream_objset_decl = RewriteRuleSubtreeStream(self._adaptor, "rule objset_decl")
        stream_declarations = RewriteRuleSubtreeStream(self._adaptor, "rule declarations")
        try:
            try:
                # ProtoCC.g:246:19: ( DIR OCBRACE ( declarations )* CCBRACE ( objset_decl )* ID SEMICOLON -> ^( DIR_ ID ( objset_decl )* ( declarations )* ) )
                # ProtoCC.g:246:21: DIR OCBRACE ( declarations )* CCBRACE ( objset_decl )* ID SEMICOLON
                pass 
                DIR87 = self.match(self.input, DIR, self.FOLLOW_DIR_in_dir_block1688) 
                stream_DIR.add(DIR87)


                OCBRACE88 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_dir_block1690) 
                stream_OCBRACE.add(OCBRACE88)


                # ProtoCC.g:246:33: ( declarations )*
                while True: #loop17
                    alt17 = 2
                    LA17_0 = self.input.LA(1)

                    if (LA17_0 in {BOOLID, DATA, INTID, NID, SET, STATE}) :
                        alt17 = 1


                    if alt17 == 1:
                        # ProtoCC.g:246:33: declarations
                        pass 
                        self._state.following.append(self.FOLLOW_declarations_in_dir_block1692)
                        declarations89 = self.declarations()

                        self._state.following.pop()
                        stream_declarations.add(declarations89.tree)



                    else:
                        break #loop17


                CCBRACE90 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_dir_block1695) 
                stream_CCBRACE.add(CCBRACE90)


                # ProtoCC.g:246:55: ( objset_decl )*
                while True: #loop18
                    alt18 = 2
                    LA18_0 = self.input.LA(1)

                    if (LA18_0 == SET) :
                        alt18 = 1


                    if alt18 == 1:
                        # ProtoCC.g:246:55: objset_decl
                        pass 
                        self._state.following.append(self.FOLLOW_objset_decl_in_dir_block1697)
                        objset_decl91 = self.objset_decl()

                        self._state.following.pop()
                        stream_objset_decl.add(objset_decl91.tree)



                    else:
                        break #loop18


                ID92 = self.match(self.input, ID, self.FOLLOW_ID_in_dir_block1700) 
                stream_ID.add(ID92)


                SEMICOLON93 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_dir_block1702) 
                stream_SEMICOLON.add(SEMICOLON93)


                # AST Rewrite
                # elements: objset_decl, declarations, ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 246:81: -> ^( DIR_ ID ( objset_decl )* ( declarations )* )
                # ProtoCC.g:247:13: ^( DIR_ ID ( objset_decl )* ( declarations )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(DIR_, "DIR_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # ProtoCC.g:247:23: ( objset_decl )*
                while stream_objset_decl.hasNext():
                    self._adaptor.addChild(root_1, stream_objset_decl.nextTree())


                stream_objset_decl.reset();

                # ProtoCC.g:247:36: ( declarations )*
                while stream_declarations.hasNext():
                    self._adaptor.addChild(root_1, stream_declarations.nextTree())


                stream_declarations.reset();

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "dir_block"


    class mem_block_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "mem_block"
    # ProtoCC.g:248:9: mem_block : MEM OCBRACE ( declarations )* CCBRACE ( objset_decl )* ID SEMICOLON -> ^( MEM_ ID ( objset_decl )* ( declarations )* ) ;
    def mem_block(self, ):
        retval = self.mem_block_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MEM94 = None
        OCBRACE95 = None
        CCBRACE97 = None
        ID99 = None
        SEMICOLON100 = None
        declarations96 = None
        objset_decl98 = None

        MEM94_tree = None
        OCBRACE95_tree = None
        CCBRACE97_tree = None
        ID99_tree = None
        SEMICOLON100_tree = None
        stream_MEM = RewriteRuleTokenStream(self._adaptor, "token MEM")
        stream_OCBRACE = RewriteRuleTokenStream(self._adaptor, "token OCBRACE")
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CCBRACE = RewriteRuleTokenStream(self._adaptor, "token CCBRACE")
        stream_objset_decl = RewriteRuleSubtreeStream(self._adaptor, "rule objset_decl")
        stream_declarations = RewriteRuleSubtreeStream(self._adaptor, "rule declarations")
        try:
            try:
                # ProtoCC.g:248:19: ( MEM OCBRACE ( declarations )* CCBRACE ( objset_decl )* ID SEMICOLON -> ^( MEM_ ID ( objset_decl )* ( declarations )* ) )
                # ProtoCC.g:248:21: MEM OCBRACE ( declarations )* CCBRACE ( objset_decl )* ID SEMICOLON
                pass 
                MEM94 = self.match(self.input, MEM, self.FOLLOW_MEM_in_mem_block1743) 
                stream_MEM.add(MEM94)


                OCBRACE95 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_mem_block1745) 
                stream_OCBRACE.add(OCBRACE95)


                # ProtoCC.g:248:33: ( declarations )*
                while True: #loop19
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if (LA19_0 in {BOOLID, DATA, INTID, NID, SET, STATE}) :
                        alt19 = 1


                    if alt19 == 1:
                        # ProtoCC.g:248:33: declarations
                        pass 
                        self._state.following.append(self.FOLLOW_declarations_in_mem_block1747)
                        declarations96 = self.declarations()

                        self._state.following.pop()
                        stream_declarations.add(declarations96.tree)



                    else:
                        break #loop19


                CCBRACE97 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_mem_block1750) 
                stream_CCBRACE.add(CCBRACE97)


                # ProtoCC.g:248:55: ( objset_decl )*
                while True: #loop20
                    alt20 = 2
                    LA20_0 = self.input.LA(1)

                    if (LA20_0 == SET) :
                        alt20 = 1


                    if alt20 == 1:
                        # ProtoCC.g:248:55: objset_decl
                        pass 
                        self._state.following.append(self.FOLLOW_objset_decl_in_mem_block1752)
                        objset_decl98 = self.objset_decl()

                        self._state.following.pop()
                        stream_objset_decl.add(objset_decl98.tree)



                    else:
                        break #loop20


                ID99 = self.match(self.input, ID, self.FOLLOW_ID_in_mem_block1755) 
                stream_ID.add(ID99)


                SEMICOLON100 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_mem_block1757) 
                stream_SEMICOLON.add(SEMICOLON100)


                # AST Rewrite
                # elements: declarations, objset_decl, ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 248:81: -> ^( MEM_ ID ( objset_decl )* ( declarations )* )
                # ProtoCC.g:249:13: ^( MEM_ ID ( objset_decl )* ( declarations )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(MEM_, "MEM_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # ProtoCC.g:249:23: ( objset_decl )*
                while stream_objset_decl.hasNext():
                    self._adaptor.addChild(root_1, stream_objset_decl.nextTree())


                stream_objset_decl.reset();

                # ProtoCC.g:249:36: ( declarations )*
                while stream_declarations.hasNext():
                    self._adaptor.addChild(root_1, stream_declarations.nextTree())


                stream_declarations.reset();

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "mem_block"


    class objset_decl_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "objset_decl"
    # ProtoCC.g:251:9: objset_decl : SET OEBRACE val_range CEBRACE -> ^( OBJSET_ val_range ) ;
    def objset_decl(self, ):
        retval = self.objset_decl_return()
        retval.start = self.input.LT(1)


        root_0 = None

        SET101 = None
        OEBRACE102 = None
        CEBRACE104 = None
        val_range103 = None

        SET101_tree = None
        OEBRACE102_tree = None
        CEBRACE104_tree = None
        stream_SET = RewriteRuleTokenStream(self._adaptor, "token SET")
        stream_CEBRACE = RewriteRuleTokenStream(self._adaptor, "token CEBRACE")
        stream_OEBRACE = RewriteRuleTokenStream(self._adaptor, "token OEBRACE")
        stream_val_range = RewriteRuleSubtreeStream(self._adaptor, "rule val_range")
        try:
            try:
                # ProtoCC.g:251:21: ( SET OEBRACE val_range CEBRACE -> ^( OBJSET_ val_range ) )
                # ProtoCC.g:251:23: SET OEBRACE val_range CEBRACE
                pass 
                SET101 = self.match(self.input, SET, self.FOLLOW_SET_in_objset_decl1799) 
                stream_SET.add(SET101)


                OEBRACE102 = self.match(self.input, OEBRACE, self.FOLLOW_OEBRACE_in_objset_decl1801) 
                stream_OEBRACE.add(OEBRACE102)


                self._state.following.append(self.FOLLOW_val_range_in_objset_decl1803)
                val_range103 = self.val_range()

                self._state.following.pop()
                stream_val_range.add(val_range103.tree)


                CEBRACE104 = self.match(self.input, CEBRACE, self.FOLLOW_CEBRACE_in_objset_decl1805) 
                stream_CEBRACE.add(CEBRACE104)


                # AST Rewrite
                # elements: val_range
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 251:53: -> ^( OBJSET_ val_range )
                # ProtoCC.g:251:56: ^( OBJSET_ val_range )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(OBJSET_, "OBJSET_")
                , root_1)

                self._adaptor.addChild(root_1, stream_val_range.nextTree())

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "objset_decl"


    class network_block_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "network_block"
    # ProtoCC.g:254:5: network_block : NETWORK OCBRACE ( network_element )* CCBRACE SEMICOLON -> ^( NETWORK_ ( network_element )* ) ;
    def network_block(self, ):
        retval = self.network_block_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NETWORK105 = None
        OCBRACE106 = None
        CCBRACE108 = None
        SEMICOLON109 = None
        network_element107 = None

        NETWORK105_tree = None
        OCBRACE106_tree = None
        CCBRACE108_tree = None
        SEMICOLON109_tree = None
        stream_NETWORK = RewriteRuleTokenStream(self._adaptor, "token NETWORK")
        stream_OCBRACE = RewriteRuleTokenStream(self._adaptor, "token OCBRACE")
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_CCBRACE = RewriteRuleTokenStream(self._adaptor, "token CCBRACE")
        stream_network_element = RewriteRuleSubtreeStream(self._adaptor, "rule network_element")
        try:
            try:
                # ProtoCC.g:254:19: ( NETWORK OCBRACE ( network_element )* CCBRACE SEMICOLON -> ^( NETWORK_ ( network_element )* ) )
                # ProtoCC.g:254:21: NETWORK OCBRACE ( network_element )* CCBRACE SEMICOLON
                pass 
                NETWORK105 = self.match(self.input, NETWORK, self.FOLLOW_NETWORK_in_network_block1831) 
                stream_NETWORK.add(NETWORK105)


                OCBRACE106 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_network_block1833) 
                stream_OCBRACE.add(OCBRACE106)


                # ProtoCC.g:254:37: ( network_element )*
                while True: #loop21
                    alt21 = 2
                    LA21_0 = self.input.LA(1)

                    if (LA21_0 in {124, 131}) :
                        alt21 = 1


                    if alt21 == 1:
                        # ProtoCC.g:254:37: network_element
                        pass 
                        self._state.following.append(self.FOLLOW_network_element_in_network_block1835)
                        network_element107 = self.network_element()

                        self._state.following.pop()
                        stream_network_element.add(network_element107.tree)



                    else:
                        break #loop21


                CCBRACE108 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_network_block1838) 
                stream_CCBRACE.add(CCBRACE108)


                SEMICOLON109 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_network_block1840) 
                stream_SEMICOLON.add(SEMICOLON109)


                # AST Rewrite
                # elements: network_element
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 254:72: -> ^( NETWORK_ ( network_element )* )
                # ProtoCC.g:254:75: ^( NETWORK_ ( network_element )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(NETWORK_, "NETWORK_")
                , root_1)

                # ProtoCC.g:254:86: ( network_element )*
                while stream_network_element.hasNext():
                    self._adaptor.addChild(root_1, stream_network_element.nextTree())


                stream_network_element.reset();

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "network_block"


    class element_type_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "element_type"
    # ProtoCC.g:255:9: element_type : ( 'Ordered' | 'Unordered' );
    def element_type(self, ):
        retval = self.element_type_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set110 = None

        set110_tree = None

        try:
            try:
                # ProtoCC.g:255:22: ( 'Ordered' | 'Unordered' )
                # ProtoCC.g:
                pass 
                root_0 = self._adaptor.nil()


                set110 = self.input.LT(1)

                if self.input.LA(1) in {124, 131}:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set110))

                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "element_type"


    class network_element_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "network_element"
    # ProtoCC.g:256:9: network_element : element_type ID SEMICOLON -> ^( ELEMENT_ element_type ID ) ;
    def network_element(self, ):
        retval = self.network_element_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID112 = None
        SEMICOLON113 = None
        element_type111 = None

        ID112_tree = None
        SEMICOLON113_tree = None
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_element_type = RewriteRuleSubtreeStream(self._adaptor, "rule element_type")
        try:
            try:
                # ProtoCC.g:256:25: ( element_type ID SEMICOLON -> ^( ELEMENT_ element_type ID ) )
                # ProtoCC.g:256:27: element_type ID SEMICOLON
                pass 
                self._state.following.append(self.FOLLOW_element_type_in_network_element1883)
                element_type111 = self.element_type()

                self._state.following.pop()
                stream_element_type.add(element_type111.tree)


                ID112 = self.match(self.input, ID, self.FOLLOW_ID_in_network_element1885) 
                stream_ID.add(ID112)


                SEMICOLON113 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_network_element1887) 
                stream_SEMICOLON.add(SEMICOLON113)


                # AST Rewrite
                # elements: element_type, ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 256:53: -> ^( ELEMENT_ element_type ID )
                # ProtoCC.g:256:56: ^( ELEMENT_ element_type ID )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(ELEMENT_, "ELEMENT_")
                , root_1)

                self._adaptor.addChild(root_1, stream_element_type.nextTree())

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "network_element"


    class network_send_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "network_send"
    # ProtoCC.g:257:5: network_send : ID DOT send_function OBRACE ID CBRACE SEMICOLON -> ^( SEND_ ID ID ) ;
    def network_send(self, ):
        retval = self.network_send_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID114 = None
        DOT115 = None
        OBRACE117 = None
        ID118 = None
        CBRACE119 = None
        SEMICOLON120 = None
        send_function116 = None

        ID114_tree = None
        DOT115_tree = None
        OBRACE117_tree = None
        ID118_tree = None
        CBRACE119_tree = None
        SEMICOLON120_tree = None
        stream_OBRACE = RewriteRuleTokenStream(self._adaptor, "token OBRACE")
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CBRACE = RewriteRuleTokenStream(self._adaptor, "token CBRACE")
        stream_send_function = RewriteRuleSubtreeStream(self._adaptor, "rule send_function")
        try:
            try:
                # ProtoCC.g:257:18: ( ID DOT send_function OBRACE ID CBRACE SEMICOLON -> ^( SEND_ ID ID ) )
                # ProtoCC.g:257:20: ID DOT send_function OBRACE ID CBRACE SEMICOLON
                pass 
                ID114 = self.match(self.input, ID, self.FOLLOW_ID_in_network_send1908) 
                stream_ID.add(ID114)


                DOT115 = self.match(self.input, DOT, self.FOLLOW_DOT_in_network_send1910) 
                stream_DOT.add(DOT115)


                self._state.following.append(self.FOLLOW_send_function_in_network_send1912)
                send_function116 = self.send_function()

                self._state.following.pop()
                stream_send_function.add(send_function116.tree)


                OBRACE117 = self.match(self.input, OBRACE, self.FOLLOW_OBRACE_in_network_send1914) 
                stream_OBRACE.add(OBRACE117)


                ID118 = self.match(self.input, ID, self.FOLLOW_ID_in_network_send1916) 
                stream_ID.add(ID118)


                CBRACE119 = self.match(self.input, CBRACE, self.FOLLOW_CBRACE_in_network_send1918) 
                stream_CBRACE.add(CBRACE119)


                SEMICOLON120 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_network_send1920) 
                stream_SEMICOLON.add(SEMICOLON120)


                # AST Rewrite
                # elements: ID, ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 257:68: -> ^( SEND_ ID ID )
                # ProtoCC.g:257:71: ^( SEND_ ID ID )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(SEND_, "SEND_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "network_send"


    class network_bcast_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "network_bcast"
    # ProtoCC.g:258:5: network_bcast : ID DOT bcast_function OBRACE ID CBRACE SEMICOLON -> ^( BCAST_ ID ID ) ;
    def network_bcast(self, ):
        retval = self.network_bcast_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID121 = None
        DOT122 = None
        OBRACE124 = None
        ID125 = None
        CBRACE126 = None
        SEMICOLON127 = None
        bcast_function123 = None

        ID121_tree = None
        DOT122_tree = None
        OBRACE124_tree = None
        ID125_tree = None
        CBRACE126_tree = None
        SEMICOLON127_tree = None
        stream_OBRACE = RewriteRuleTokenStream(self._adaptor, "token OBRACE")
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CBRACE = RewriteRuleTokenStream(self._adaptor, "token CBRACE")
        stream_bcast_function = RewriteRuleSubtreeStream(self._adaptor, "rule bcast_function")
        try:
            try:
                # ProtoCC.g:258:18: ( ID DOT bcast_function OBRACE ID CBRACE SEMICOLON -> ^( BCAST_ ID ID ) )
                # ProtoCC.g:258:20: ID DOT bcast_function OBRACE ID CBRACE SEMICOLON
                pass 
                ID121 = self.match(self.input, ID, self.FOLLOW_ID_in_network_bcast1940) 
                stream_ID.add(ID121)


                DOT122 = self.match(self.input, DOT, self.FOLLOW_DOT_in_network_bcast1942) 
                stream_DOT.add(DOT122)


                self._state.following.append(self.FOLLOW_bcast_function_in_network_bcast1944)
                bcast_function123 = self.bcast_function()

                self._state.following.pop()
                stream_bcast_function.add(bcast_function123.tree)


                OBRACE124 = self.match(self.input, OBRACE, self.FOLLOW_OBRACE_in_network_bcast1946) 
                stream_OBRACE.add(OBRACE124)


                ID125 = self.match(self.input, ID, self.FOLLOW_ID_in_network_bcast1948) 
                stream_ID.add(ID125)


                CBRACE126 = self.match(self.input, CBRACE, self.FOLLOW_CBRACE_in_network_bcast1950) 
                stream_CBRACE.add(CBRACE126)


                SEMICOLON127 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_network_bcast1952) 
                stream_SEMICOLON.add(SEMICOLON127)


                # AST Rewrite
                # elements: ID, ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 258:69: -> ^( BCAST_ ID ID )
                # ProtoCC.g:258:72: ^( BCAST_ ID ID )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(BCAST_, "BCAST_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "network_bcast"


    class network_mcast_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "network_mcast"
    # ProtoCC.g:259:5: network_mcast : ID DOT mcast_function OBRACE ID COMMA ID CBRACE SEMICOLON -> ^( MCAST_ ID ID ID ) ;
    def network_mcast(self, ):
        retval = self.network_mcast_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID128 = None
        DOT129 = None
        OBRACE131 = None
        ID132 = None
        COMMA133 = None
        ID134 = None
        CBRACE135 = None
        SEMICOLON136 = None
        mcast_function130 = None

        ID128_tree = None
        DOT129_tree = None
        OBRACE131_tree = None
        ID132_tree = None
        COMMA133_tree = None
        ID134_tree = None
        CBRACE135_tree = None
        SEMICOLON136_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_OBRACE = RewriteRuleTokenStream(self._adaptor, "token OBRACE")
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CBRACE = RewriteRuleTokenStream(self._adaptor, "token CBRACE")
        stream_mcast_function = RewriteRuleSubtreeStream(self._adaptor, "rule mcast_function")
        try:
            try:
                # ProtoCC.g:259:18: ( ID DOT mcast_function OBRACE ID COMMA ID CBRACE SEMICOLON -> ^( MCAST_ ID ID ID ) )
                # ProtoCC.g:259:20: ID DOT mcast_function OBRACE ID COMMA ID CBRACE SEMICOLON
                pass 
                ID128 = self.match(self.input, ID, self.FOLLOW_ID_in_network_mcast1972) 
                stream_ID.add(ID128)


                DOT129 = self.match(self.input, DOT, self.FOLLOW_DOT_in_network_mcast1974) 
                stream_DOT.add(DOT129)


                self._state.following.append(self.FOLLOW_mcast_function_in_network_mcast1976)
                mcast_function130 = self.mcast_function()

                self._state.following.pop()
                stream_mcast_function.add(mcast_function130.tree)


                OBRACE131 = self.match(self.input, OBRACE, self.FOLLOW_OBRACE_in_network_mcast1978) 
                stream_OBRACE.add(OBRACE131)


                ID132 = self.match(self.input, ID, self.FOLLOW_ID_in_network_mcast1980) 
                stream_ID.add(ID132)


                COMMA133 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_network_mcast1982) 
                stream_COMMA.add(COMMA133)


                ID134 = self.match(self.input, ID, self.FOLLOW_ID_in_network_mcast1984) 
                stream_ID.add(ID134)


                CBRACE135 = self.match(self.input, CBRACE, self.FOLLOW_CBRACE_in_network_mcast1986) 
                stream_CBRACE.add(CBRACE135)


                SEMICOLON136 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_network_mcast1988) 
                stream_SEMICOLON.add(SEMICOLON136)


                # AST Rewrite
                # elements: ID, ID, ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 259:78: -> ^( MCAST_ ID ID ID )
                # ProtoCC.g:259:81: ^( MCAST_ ID ID ID )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(MCAST_, "MCAST_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "network_mcast"


    class message_block_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "message_block"
    # ProtoCC.g:262:5: message_block : MSG ID OCBRACE ( declarations )* CCBRACE SEMICOLON -> ^( MSG_ ID ( declarations )* ) ;
    def message_block(self, ):
        retval = self.message_block_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MSG137 = None
        ID138 = None
        OCBRACE139 = None
        CCBRACE141 = None
        SEMICOLON142 = None
        declarations140 = None

        MSG137_tree = None
        ID138_tree = None
        OCBRACE139_tree = None
        CCBRACE141_tree = None
        SEMICOLON142_tree = None
        stream_MSG = RewriteRuleTokenStream(self._adaptor, "token MSG")
        stream_OCBRACE = RewriteRuleTokenStream(self._adaptor, "token OCBRACE")
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CCBRACE = RewriteRuleTokenStream(self._adaptor, "token CCBRACE")
        stream_declarations = RewriteRuleSubtreeStream(self._adaptor, "rule declarations")
        try:
            try:
                # ProtoCC.g:262:19: ( MSG ID OCBRACE ( declarations )* CCBRACE SEMICOLON -> ^( MSG_ ID ( declarations )* ) )
                # ProtoCC.g:262:21: MSG ID OCBRACE ( declarations )* CCBRACE SEMICOLON
                pass 
                MSG137 = self.match(self.input, MSG, self.FOLLOW_MSG_in_message_block2018) 
                stream_MSG.add(MSG137)


                ID138 = self.match(self.input, ID, self.FOLLOW_ID_in_message_block2020) 
                stream_ID.add(ID138)


                OCBRACE139 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_message_block2022) 
                stream_OCBRACE.add(OCBRACE139)


                # ProtoCC.g:262:36: ( declarations )*
                while True: #loop22
                    alt22 = 2
                    LA22_0 = self.input.LA(1)

                    if (LA22_0 in {BOOLID, DATA, INTID, NID, SET, STATE}) :
                        alt22 = 1


                    if alt22 == 1:
                        # ProtoCC.g:262:36: declarations
                        pass 
                        self._state.following.append(self.FOLLOW_declarations_in_message_block2024)
                        declarations140 = self.declarations()

                        self._state.following.pop()
                        stream_declarations.add(declarations140.tree)



                    else:
                        break #loop22


                CCBRACE141 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_message_block2027) 
                stream_CCBRACE.add(CCBRACE141)


                SEMICOLON142 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_message_block2029) 
                stream_SEMICOLON.add(SEMICOLON142)


                # AST Rewrite
                # elements: declarations, ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 262:68: -> ^( MSG_ ID ( declarations )* )
                # ProtoCC.g:262:71: ^( MSG_ ID ( declarations )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(MSG_, "MSG_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # ProtoCC.g:262:81: ( declarations )*
                while stream_declarations.hasNext():
                    self._adaptor.addChild(root_1, stream_declarations.nextTree())


                stream_declarations.reset();

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "message_block"


    class message_constr_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "message_constr"
    # ProtoCC.g:263:5: message_constr : ID OBRACE ( message_expr )* ( COMMA message_expr )* CBRACE -> ^( MSGCSTR_ ID ( message_expr )* ) ;
    def message_constr(self, ):
        retval = self.message_constr_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID143 = None
        OBRACE144 = None
        COMMA146 = None
        CBRACE148 = None
        message_expr145 = None
        message_expr147 = None

        ID143_tree = None
        OBRACE144_tree = None
        COMMA146_tree = None
        CBRACE148_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_OBRACE = RewriteRuleTokenStream(self._adaptor, "token OBRACE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CBRACE = RewriteRuleTokenStream(self._adaptor, "token CBRACE")
        stream_message_expr = RewriteRuleSubtreeStream(self._adaptor, "rule message_expr")
        try:
            try:
                # ProtoCC.g:263:20: ( ID OBRACE ( message_expr )* ( COMMA message_expr )* CBRACE -> ^( MSGCSTR_ ID ( message_expr )* ) )
                # ProtoCC.g:263:22: ID OBRACE ( message_expr )* ( COMMA message_expr )* CBRACE
                pass 
                ID143 = self.match(self.input, ID, self.FOLLOW_ID_in_message_constr2051) 
                stream_ID.add(ID143)


                OBRACE144 = self.match(self.input, OBRACE, self.FOLLOW_OBRACE_in_message_constr2053) 
                stream_OBRACE.add(OBRACE144)


                # ProtoCC.g:263:32: ( message_expr )*
                while True: #loop23
                    alt23 = 2
                    LA23_0 = self.input.LA(1)

                    if (LA23_0 in {BOOL, ID, INT, NID}) :
                        alt23 = 1


                    if alt23 == 1:
                        # ProtoCC.g:263:32: message_expr
                        pass 
                        self._state.following.append(self.FOLLOW_message_expr_in_message_constr2055)
                        message_expr145 = self.message_expr()

                        self._state.following.pop()
                        stream_message_expr.add(message_expr145.tree)



                    else:
                        break #loop23


                # ProtoCC.g:263:46: ( COMMA message_expr )*
                while True: #loop24
                    alt24 = 2
                    LA24_0 = self.input.LA(1)

                    if (LA24_0 == COMMA) :
                        alt24 = 1


                    if alt24 == 1:
                        # ProtoCC.g:263:47: COMMA message_expr
                        pass 
                        COMMA146 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_message_constr2059) 
                        stream_COMMA.add(COMMA146)


                        self._state.following.append(self.FOLLOW_message_expr_in_message_constr2061)
                        message_expr147 = self.message_expr()

                        self._state.following.pop()
                        stream_message_expr.add(message_expr147.tree)



                    else:
                        break #loop24


                CBRACE148 = self.match(self.input, CBRACE, self.FOLLOW_CBRACE_in_message_constr2065) 
                stream_CBRACE.add(CBRACE148)


                # AST Rewrite
                # elements: message_expr, ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 263:75: -> ^( MSGCSTR_ ID ( message_expr )* )
                # ProtoCC.g:263:78: ^( MSGCSTR_ ID ( message_expr )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(MSGCSTR_, "MSGCSTR_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # ProtoCC.g:263:92: ( message_expr )*
                while stream_message_expr.hasNext():
                    self._adaptor.addChild(root_1, stream_message_expr.nextTree())


                stream_message_expr.reset();

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "message_constr"


    class message_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "message_expr"
    # ProtoCC.g:264:5: message_expr : ( object_expr | set_func | INT | BOOL | NID );
    def message_expr(self, ):
        retval = self.message_expr_return()
        retval.start = self.input.LT(1)


        root_0 = None

        INT151 = None
        BOOL152 = None
        NID153 = None
        object_expr149 = None
        set_func150 = None

        INT151_tree = None
        BOOL152_tree = None
        NID153_tree = None

        try:
            try:
                # ProtoCC.g:264:18: ( object_expr | set_func | INT | BOOL | NID )
                alt25 = 5
                LA25 = self.input.LA(1)
                if LA25 in {ID}:
                    LA25_1 = self.input.LA(2)

                    if (LA25_1 == DOT) :
                        LA25_5 = self.input.LA(3)

                        if (LA25_5 in {ID, NID}) :
                            alt25 = 1
                        elif (LA25_5 in {134, 136, 138, 139, 140, 144}) :
                            alt25 = 2
                        else:
                            nvae = NoViableAltException("", 25, 5, self.input)

                            raise nvae


                    elif (LA25_1 in {BOOL, CBRACE, COMMA, ID, INT, NID}) :
                        alt25 = 1
                    else:
                        nvae = NoViableAltException("", 25, 1, self.input)

                        raise nvae


                elif LA25 in {INT}:
                    alt25 = 3
                elif LA25 in {BOOL}:
                    alt25 = 4
                elif LA25 in {NID}:
                    alt25 = 5
                else:
                    nvae = NoViableAltException("", 25, 0, self.input)

                    raise nvae


                if alt25 == 1:
                    # ProtoCC.g:264:20: object_expr
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_object_expr_in_message_expr2087)
                    object_expr149 = self.object_expr()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, object_expr149.tree)



                elif alt25 == 2:
                    # ProtoCC.g:264:34: set_func
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_set_func_in_message_expr2091)
                    set_func150 = self.set_func()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, set_func150.tree)



                elif alt25 == 3:
                    # ProtoCC.g:264:45: INT
                    pass 
                    root_0 = self._adaptor.nil()


                    INT151 = self.match(self.input, INT, self.FOLLOW_INT_in_message_expr2095)
                    INT151_tree = self._adaptor.createWithPayload(INT151)
                    self._adaptor.addChild(root_0, INT151_tree)




                elif alt25 == 4:
                    # ProtoCC.g:264:51: BOOL
                    pass 
                    root_0 = self._adaptor.nil()


                    BOOL152 = self.match(self.input, BOOL, self.FOLLOW_BOOL_in_message_expr2099)
                    BOOL152_tree = self._adaptor.createWithPayload(BOOL152)
                    self._adaptor.addChild(root_0, BOOL152_tree)




                elif alt25 == 5:
                    # ProtoCC.g:264:58: NID
                    pass 
                    root_0 = self._adaptor.nil()


                    NID153 = self.match(self.input, NID, self.FOLLOW_NID_in_message_expr2103)
                    NID153_tree = self._adaptor.createWithPayload(NID153)
                    self._adaptor.addChild(root_0, NID153_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "message_expr"


    class set_block_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "set_block"
    # ProtoCC.g:267:5: set_block : set_func SEMICOLON -> set_func ;
    def set_block(self, ):
        retval = self.set_block_return()
        retval.start = self.input.LT(1)


        root_0 = None

        SEMICOLON155 = None
        set_func154 = None

        SEMICOLON155_tree = None
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_set_func = RewriteRuleSubtreeStream(self._adaptor, "rule set_func")
        try:
            try:
                # ProtoCC.g:267:15: ( set_func SEMICOLON -> set_func )
                # ProtoCC.g:267:17: set_func SEMICOLON
                pass 
                self._state.following.append(self.FOLLOW_set_func_in_set_block2121)
                set_func154 = self.set_func()

                self._state.following.pop()
                stream_set_func.add(set_func154.tree)


                SEMICOLON155 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_set_block2123) 
                stream_SEMICOLON.add(SEMICOLON155)


                # AST Rewrite
                # elements: set_func
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 267:36: -> set_func
                self._adaptor.addChild(root_0, stream_set_func.nextTree())




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "set_block"


    class set_func_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "set_func"
    # ProtoCC.g:268:5: set_func : ID DOT set_function_types OBRACE ( set_nest )* CBRACE -> ^( SETFUNC_ ID DOT set_function_types OBRACE ( set_nest )* CBRACE ) ;
    def set_func(self, ):
        retval = self.set_func_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID156 = None
        DOT157 = None
        OBRACE159 = None
        CBRACE161 = None
        set_function_types158 = None
        set_nest160 = None

        ID156_tree = None
        DOT157_tree = None
        OBRACE159_tree = None
        CBRACE161_tree = None
        stream_OBRACE = RewriteRuleTokenStream(self._adaptor, "token OBRACE")
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CBRACE = RewriteRuleTokenStream(self._adaptor, "token CBRACE")
        stream_set_function_types = RewriteRuleSubtreeStream(self._adaptor, "rule set_function_types")
        stream_set_nest = RewriteRuleSubtreeStream(self._adaptor, "rule set_nest")
        try:
            try:
                # ProtoCC.g:268:14: ( ID DOT set_function_types OBRACE ( set_nest )* CBRACE -> ^( SETFUNC_ ID DOT set_function_types OBRACE ( set_nest )* CBRACE ) )
                # ProtoCC.g:268:16: ID DOT set_function_types OBRACE ( set_nest )* CBRACE
                pass 
                ID156 = self.match(self.input, ID, self.FOLLOW_ID_in_set_func2138) 
                stream_ID.add(ID156)


                DOT157 = self.match(self.input, DOT, self.FOLLOW_DOT_in_set_func2140) 
                stream_DOT.add(DOT157)


                self._state.following.append(self.FOLLOW_set_function_types_in_set_func2142)
                set_function_types158 = self.set_function_types()

                self._state.following.pop()
                stream_set_function_types.add(set_function_types158.tree)


                OBRACE159 = self.match(self.input, OBRACE, self.FOLLOW_OBRACE_in_set_func2144) 
                stream_OBRACE.add(OBRACE159)


                # ProtoCC.g:268:49: ( set_nest )*
                while True: #loop26
                    alt26 = 2
                    LA26_0 = self.input.LA(1)

                    if (LA26_0 == ID) :
                        alt26 = 1


                    if alt26 == 1:
                        # ProtoCC.g:268:49: set_nest
                        pass 
                        self._state.following.append(self.FOLLOW_set_nest_in_set_func2146)
                        set_nest160 = self.set_nest()

                        self._state.following.pop()
                        stream_set_nest.add(set_nest160.tree)



                    else:
                        break #loop26


                CBRACE161 = self.match(self.input, CBRACE, self.FOLLOW_CBRACE_in_set_func2149) 
                stream_CBRACE.add(CBRACE161)


                # AST Rewrite
                # elements: set_nest, OBRACE, CBRACE, ID, DOT, set_function_types
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 268:66: -> ^( SETFUNC_ ID DOT set_function_types OBRACE ( set_nest )* CBRACE )
                # ProtoCC.g:269:9: ^( SETFUNC_ ID DOT set_function_types OBRACE ( set_nest )* CBRACE )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(SETFUNC_, "SETFUNC_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_1, 
                stream_DOT.nextNode()
                )

                self._adaptor.addChild(root_1, stream_set_function_types.nextTree())

                self._adaptor.addChild(root_1, 
                stream_OBRACE.nextNode()
                )

                # ProtoCC.g:269:53: ( set_nest )*
                while stream_set_nest.hasNext():
                    self._adaptor.addChild(root_1, stream_set_nest.nextTree())


                stream_set_nest.reset();

                self._adaptor.addChild(root_1, 
                stream_CBRACE.nextNode()
                )

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "set_func"


    class set_nest_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "set_nest"
    # ProtoCC.g:270:5: set_nest : ( set_func | object_expr );
    def set_nest(self, ):
        retval = self.set_nest_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set_func162 = None
        object_expr163 = None


        try:
            try:
                # ProtoCC.g:270:14: ( set_func | object_expr )
                alt27 = 2
                LA27_0 = self.input.LA(1)

                if (LA27_0 == ID) :
                    LA27_1 = self.input.LA(2)

                    if (LA27_1 == DOT) :
                        LA27_2 = self.input.LA(3)

                        if (LA27_2 in {134, 136, 138, 139, 140, 144}) :
                            alt27 = 1
                        elif (LA27_2 in {ID, NID}) :
                            alt27 = 2
                        else:
                            nvae = NoViableAltException("", 27, 2, self.input)

                            raise nvae


                    elif (LA27_1 in {CBRACE, ID}) :
                        alt27 = 2
                    else:
                        nvae = NoViableAltException("", 27, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 27, 0, self.input)

                    raise nvae


                if alt27 == 1:
                    # ProtoCC.g:270:16: set_func
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_set_func_in_set_nest2187)
                    set_func162 = self.set_func()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, set_func162.tree)



                elif alt27 == 2:
                    # ProtoCC.g:270:27: object_expr
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_object_expr_in_set_nest2191)
                    object_expr163 = self.object_expr()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, object_expr163.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "set_nest"


    class internal_event_block_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "internal_event_block"
    # ProtoCC.g:274:5: internal_event_block : internal_event_func SEMICOLON -> internal_event_func ;
    def internal_event_block(self, ):
        retval = self.internal_event_block_return()
        retval.start = self.input.LT(1)


        root_0 = None

        SEMICOLON165 = None
        internal_event_func164 = None

        SEMICOLON165_tree = None
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_internal_event_func = RewriteRuleSubtreeStream(self._adaptor, "rule internal_event_func")
        try:
            try:
                # ProtoCC.g:274:25: ( internal_event_func SEMICOLON -> internal_event_func )
                # ProtoCC.g:274:27: internal_event_func SEMICOLON
                pass 
                self._state.following.append(self.FOLLOW_internal_event_func_in_internal_event_block2209)
                internal_event_func164 = self.internal_event_func()

                self._state.following.pop()
                stream_internal_event_func.add(internal_event_func164.tree)


                SEMICOLON165 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_internal_event_block2211) 
                stream_SEMICOLON.add(SEMICOLON165)


                # AST Rewrite
                # elements: internal_event_func
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 274:57: -> internal_event_func
                self._adaptor.addChild(root_0, stream_internal_event_func.nextTree())




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "internal_event_block"


    class internal_event_func_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "internal_event_func"
    # ProtoCC.g:275:5: internal_event_func : internal_event_function OBRACE ID CBRACE -> ^( EVENT_ ID ) ^( EVENT_ACK_ ID ) ;
    def internal_event_func(self, ):
        retval = self.internal_event_func_return()
        retval.start = self.input.LT(1)


        root_0 = None

        OBRACE167 = None
        ID168 = None
        CBRACE169 = None
        internal_event_function166 = None

        OBRACE167_tree = None
        ID168_tree = None
        CBRACE169_tree = None
        stream_OBRACE = RewriteRuleTokenStream(self._adaptor, "token OBRACE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CBRACE = RewriteRuleTokenStream(self._adaptor, "token CBRACE")
        stream_internal_event_function = RewriteRuleSubtreeStream(self._adaptor, "rule internal_event_function")
        try:
            try:
                # ProtoCC.g:275:24: ( internal_event_function OBRACE ID CBRACE -> ^( EVENT_ ID ) ^( EVENT_ACK_ ID ) )
                # ProtoCC.g:275:26: internal_event_function OBRACE ID CBRACE
                pass 
                self._state.following.append(self.FOLLOW_internal_event_function_in_internal_event_func2225)
                internal_event_function166 = self.internal_event_function()

                self._state.following.pop()
                stream_internal_event_function.add(internal_event_function166.tree)


                OBRACE167 = self.match(self.input, OBRACE, self.FOLLOW_OBRACE_in_internal_event_func2227) 
                stream_OBRACE.add(OBRACE167)


                ID168 = self.match(self.input, ID, self.FOLLOW_ID_in_internal_event_func2229) 
                stream_ID.add(ID168)


                CBRACE169 = self.match(self.input, CBRACE, self.FOLLOW_CBRACE_in_internal_event_func2231) 
                stream_CBRACE.add(CBRACE169)


                # AST Rewrite
                # elements: ID, ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 275:67: -> ^( EVENT_ ID ) ^( EVENT_ACK_ ID )
                # ProtoCC.g:275:70: ^( EVENT_ ID )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(EVENT_, "EVENT_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_0, root_1)

                # ProtoCC.g:275:83: ^( EVENT_ACK_ ID )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(EVENT_ACK_, "EVENT_ACK_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "internal_event_func"


    class arch_block_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "arch_block"
    # ProtoCC.g:278:1: arch_block : ARCH ID OCBRACE arch_body CCBRACE -> ^( ARCH_ ^( MACHN_ ID ) arch_body ) ;
    def arch_block(self, ):
        retval = self.arch_block_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ARCH170 = None
        ID171 = None
        OCBRACE172 = None
        CCBRACE174 = None
        arch_body173 = None

        ARCH170_tree = None
        ID171_tree = None
        OCBRACE172_tree = None
        CCBRACE174_tree = None
        stream_OCBRACE = RewriteRuleTokenStream(self._adaptor, "token OCBRACE")
        stream_ARCH = RewriteRuleTokenStream(self._adaptor, "token ARCH")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CCBRACE = RewriteRuleTokenStream(self._adaptor, "token CCBRACE")
        stream_arch_body = RewriteRuleSubtreeStream(self._adaptor, "rule arch_body")
        try:
            try:
                # ProtoCC.g:278:12: ( ARCH ID OCBRACE arch_body CCBRACE -> ^( ARCH_ ^( MACHN_ ID ) arch_body ) )
                # ProtoCC.g:278:14: ARCH ID OCBRACE arch_body CCBRACE
                pass 
                ARCH170 = self.match(self.input, ARCH, self.FOLLOW_ARCH_in_arch_block2255) 
                stream_ARCH.add(ARCH170)


                ID171 = self.match(self.input, ID, self.FOLLOW_ID_in_arch_block2257) 
                stream_ID.add(ID171)


                OCBRACE172 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_arch_block2259) 
                stream_OCBRACE.add(OCBRACE172)


                self._state.following.append(self.FOLLOW_arch_body_in_arch_block2261)
                arch_body173 = self.arch_body()

                self._state.following.pop()
                stream_arch_body.add(arch_body173.tree)


                CCBRACE174 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_arch_block2263) 
                stream_CCBRACE.add(CCBRACE174)


                # AST Rewrite
                # elements: ID, arch_body
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 278:48: -> ^( ARCH_ ^( MACHN_ ID ) arch_body )
                # ProtoCC.g:278:51: ^( ARCH_ ^( MACHN_ ID ) arch_body )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(ARCH_, "ARCH_")
                , root_1)

                # ProtoCC.g:278:59: ^( MACHN_ ID )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(MACHN_, "MACHN_")
                , root_2)

                self._adaptor.addChild(root_2, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_1, root_2)

                self._adaptor.addChild(root_1, stream_arch_body.nextTree())

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "arch_block"


    class arch_body_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "arch_body"
    # ProtoCC.g:280:1: arch_body : ( stable_def | process_block )* ;
    def arch_body(self, ):
        retval = self.arch_body_return()
        retval.start = self.input.LT(1)


        root_0 = None

        stable_def175 = None
        process_block176 = None


        try:
            try:
                # ProtoCC.g:280:10: ( ( stable_def | process_block )* )
                # ProtoCC.g:280:12: ( stable_def | process_block )*
                pass 
                root_0 = self._adaptor.nil()


                # ProtoCC.g:280:12: ( stable_def | process_block )*
                while True: #loop28
                    alt28 = 3
                    LA28_0 = self.input.LA(1)

                    if (LA28_0 == STABLE) :
                        alt28 = 1
                    elif (LA28_0 == PROC) :
                        alt28 = 2


                    if alt28 == 1:
                        # ProtoCC.g:280:13: stable_def
                        pass 
                        self._state.following.append(self.FOLLOW_stable_def_in_arch_body2285)
                        stable_def175 = self.stable_def()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, stable_def175.tree)



                    elif alt28 == 2:
                        # ProtoCC.g:280:26: process_block
                        pass 
                        self._state.following.append(self.FOLLOW_process_block_in_arch_body2289)
                        process_block176 = self.process_block()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, process_block176.tree)



                    else:
                        break #loop28




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "arch_body"


    class stable_def_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "stable_def"
    # ProtoCC.g:282:1: stable_def : STABLE OCBRACE ID ( COMMA ID )* CCBRACE -> ^( STABLE_ ID ( ID )* ) ;
    def stable_def(self, ):
        retval = self.stable_def_return()
        retval.start = self.input.LT(1)


        root_0 = None

        STABLE177 = None
        OCBRACE178 = None
        ID179 = None
        COMMA180 = None
        ID181 = None
        CCBRACE182 = None

        STABLE177_tree = None
        OCBRACE178_tree = None
        ID179_tree = None
        COMMA180_tree = None
        ID181_tree = None
        CCBRACE182_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_OCBRACE = RewriteRuleTokenStream(self._adaptor, "token OCBRACE")
        stream_STABLE = RewriteRuleTokenStream(self._adaptor, "token STABLE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CCBRACE = RewriteRuleTokenStream(self._adaptor, "token CCBRACE")

        try:
            try:
                # ProtoCC.g:282:12: ( STABLE OCBRACE ID ( COMMA ID )* CCBRACE -> ^( STABLE_ ID ( ID )* ) )
                # ProtoCC.g:282:14: STABLE OCBRACE ID ( COMMA ID )* CCBRACE
                pass 
                STABLE177 = self.match(self.input, STABLE, self.FOLLOW_STABLE_in_stable_def2299) 
                stream_STABLE.add(STABLE177)


                OCBRACE178 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_stable_def2301) 
                stream_OCBRACE.add(OCBRACE178)


                ID179 = self.match(self.input, ID, self.FOLLOW_ID_in_stable_def2303) 
                stream_ID.add(ID179)


                # ProtoCC.g:282:32: ( COMMA ID )*
                while True: #loop29
                    alt29 = 2
                    LA29_0 = self.input.LA(1)

                    if (LA29_0 == COMMA) :
                        alt29 = 1


                    if alt29 == 1:
                        # ProtoCC.g:282:33: COMMA ID
                        pass 
                        COMMA180 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_stable_def2306) 
                        stream_COMMA.add(COMMA180)


                        ID181 = self.match(self.input, ID, self.FOLLOW_ID_in_stable_def2308) 
                        stream_ID.add(ID181)



                    else:
                        break #loop29


                CCBRACE182 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_stable_def2312) 
                stream_CCBRACE.add(CCBRACE182)


                # AST Rewrite
                # elements: ID, ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 282:52: -> ^( STABLE_ ID ( ID )* )
                # ProtoCC.g:282:55: ^( STABLE_ ID ( ID )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(STABLE_, "STABLE_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # ProtoCC.g:282:68: ( ID )*
                while stream_ID.hasNext():
                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )


                stream_ID.reset();

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "stable_def"


    class process_block_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "process_block"
    # ProtoCC.g:284:1: process_block : PROC process_trans OCBRACE ( process_expr )* CCBRACE -> ^( PROC_ process_trans ( process_expr )* ^( ENDPROC_ ) ) ;
    def process_block(self, ):
        retval = self.process_block_return()
        retval.start = self.input.LT(1)


        root_0 = None

        PROC183 = None
        OCBRACE185 = None
        CCBRACE187 = None
        process_trans184 = None
        process_expr186 = None

        PROC183_tree = None
        OCBRACE185_tree = None
        CCBRACE187_tree = None
        stream_PROC = RewriteRuleTokenStream(self._adaptor, "token PROC")
        stream_OCBRACE = RewriteRuleTokenStream(self._adaptor, "token OCBRACE")
        stream_CCBRACE = RewriteRuleTokenStream(self._adaptor, "token CCBRACE")
        stream_process_trans = RewriteRuleSubtreeStream(self._adaptor, "rule process_trans")
        stream_process_expr = RewriteRuleSubtreeStream(self._adaptor, "rule process_expr")
        try:
            try:
                # ProtoCC.g:284:15: ( PROC process_trans OCBRACE ( process_expr )* CCBRACE -> ^( PROC_ process_trans ( process_expr )* ^( ENDPROC_ ) ) )
                # ProtoCC.g:284:17: PROC process_trans OCBRACE ( process_expr )* CCBRACE
                pass 
                PROC183 = self.match(self.input, PROC, self.FOLLOW_PROC_in_process_block2331) 
                stream_PROC.add(PROC183)


                self._state.following.append(self.FOLLOW_process_trans_in_process_block2333)
                process_trans184 = self.process_trans()

                self._state.following.pop()
                stream_process_trans.add(process_trans184.tree)


                OCBRACE185 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_process_block2335) 
                stream_OCBRACE.add(OCBRACE185)


                # ProtoCC.g:284:44: ( process_expr )*
                while True: #loop30
                    alt30 = 2
                    LA30_0 = self.input.LA(1)

                    if (LA30_0 in {ACCESS, AWAIT, ID, IF, STALL, STATE, UNDEF, 119}) :
                        alt30 = 1


                    if alt30 == 1:
                        # ProtoCC.g:284:44: process_expr
                        pass 
                        self._state.following.append(self.FOLLOW_process_expr_in_process_block2337)
                        process_expr186 = self.process_expr()

                        self._state.following.pop()
                        stream_process_expr.add(process_expr186.tree)



                    else:
                        break #loop30


                CCBRACE187 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_process_block2340) 
                stream_CCBRACE.add(CCBRACE187)


                # AST Rewrite
                # elements: process_expr, process_trans
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 284:66: -> ^( PROC_ process_trans ( process_expr )* ^( ENDPROC_ ) )
                # ProtoCC.g:284:69: ^( PROC_ process_trans ( process_expr )* ^( ENDPROC_ ) )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(PROC_, "PROC_")
                , root_1)

                self._adaptor.addChild(root_1, stream_process_trans.nextTree())

                # ProtoCC.g:284:91: ( process_expr )*
                while stream_process_expr.hasNext():
                    self._adaptor.addChild(root_1, stream_process_expr.nextTree())


                stream_process_expr.reset();

                # ProtoCC.g:284:105: ^( ENDPROC_ )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(ENDPROC_, "ENDPROC_")
                , root_2)

                self._adaptor.addChild(root_1, root_2)

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "process_block"


    class process_trans_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "process_trans"
    # ProtoCC.g:285:5: process_trans : OBRACE ID COMMA process_events ( process_finalstate )* CBRACE -> ^( TRANS_ ID process_events ( process_finalstate )* ) ;
    def process_trans(self, ):
        retval = self.process_trans_return()
        retval.start = self.input.LT(1)


        root_0 = None

        OBRACE188 = None
        ID189 = None
        COMMA190 = None
        CBRACE193 = None
        process_events191 = None
        process_finalstate192 = None

        OBRACE188_tree = None
        ID189_tree = None
        COMMA190_tree = None
        CBRACE193_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_OBRACE = RewriteRuleTokenStream(self._adaptor, "token OBRACE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CBRACE = RewriteRuleTokenStream(self._adaptor, "token CBRACE")
        stream_process_events = RewriteRuleSubtreeStream(self._adaptor, "rule process_events")
        stream_process_finalstate = RewriteRuleSubtreeStream(self._adaptor, "rule process_finalstate")
        try:
            try:
                # ProtoCC.g:285:19: ( OBRACE ID COMMA process_events ( process_finalstate )* CBRACE -> ^( TRANS_ ID process_events ( process_finalstate )* ) )
                # ProtoCC.g:285:21: OBRACE ID COMMA process_events ( process_finalstate )* CBRACE
                pass 
                OBRACE188 = self.match(self.input, OBRACE, self.FOLLOW_OBRACE_in_process_trans2366) 
                stream_OBRACE.add(OBRACE188)


                ID189 = self.match(self.input, ID, self.FOLLOW_ID_in_process_trans2368) 
                stream_ID.add(ID189)


                COMMA190 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_process_trans2370) 
                stream_COMMA.add(COMMA190)


                self._state.following.append(self.FOLLOW_process_events_in_process_trans2372)
                process_events191 = self.process_events()

                self._state.following.pop()
                stream_process_events.add(process_events191.tree)


                # ProtoCC.g:285:52: ( process_finalstate )*
                while True: #loop31
                    alt31 = 2
                    LA31_0 = self.input.LA(1)

                    if (LA31_0 == COMMA) :
                        alt31 = 1


                    if alt31 == 1:
                        # ProtoCC.g:285:52: process_finalstate
                        pass 
                        self._state.following.append(self.FOLLOW_process_finalstate_in_process_trans2374)
                        process_finalstate192 = self.process_finalstate()

                        self._state.following.pop()
                        stream_process_finalstate.add(process_finalstate192.tree)



                    else:
                        break #loop31


                CBRACE193 = self.match(self.input, CBRACE, self.FOLLOW_CBRACE_in_process_trans2377) 
                stream_CBRACE.add(CBRACE193)


                # AST Rewrite
                # elements: ID, process_events, process_finalstate
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 285:79: -> ^( TRANS_ ID process_events ( process_finalstate )* )
                # ProtoCC.g:285:82: ^( TRANS_ ID process_events ( process_finalstate )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TRANS_, "TRANS_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_1, stream_process_events.nextTree())

                # ProtoCC.g:285:109: ( process_finalstate )*
                while stream_process_finalstate.hasNext():
                    self._adaptor.addChild(root_1, stream_process_finalstate.nextTree())


                stream_process_finalstate.reset();

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "process_trans"


    class process_finalstate_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "process_finalstate"
    # ProtoCC.g:286:5: process_finalstate : COMMA process_finalident -> ^( process_finalident ) ;
    def process_finalstate(self, ):
        retval = self.process_finalstate_return()
        retval.start = self.input.LT(1)


        root_0 = None

        COMMA194 = None
        process_finalident195 = None

        COMMA194_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_process_finalident = RewriteRuleSubtreeStream(self._adaptor, "rule process_finalident")
        try:
            try:
                # ProtoCC.g:286:23: ( COMMA process_finalident -> ^( process_finalident ) )
                # ProtoCC.g:286:25: COMMA process_finalident
                pass 
                COMMA194 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_process_finalstate2400) 
                stream_COMMA.add(COMMA194)


                self._state.following.append(self.FOLLOW_process_finalident_in_process_finalstate2402)
                process_finalident195 = self.process_finalident()

                self._state.following.pop()
                stream_process_finalident.add(process_finalident195.tree)


                # AST Rewrite
                # elements: process_finalident
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 286:50: -> ^( process_finalident )
                # ProtoCC.g:286:53: ^( process_finalident )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_process_finalident.nextNode(), root_1)

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "process_finalstate"


    class process_finalident_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "process_finalident"
    # ProtoCC.g:287:5: process_finalident : ( ID | STATE ) ;
    def process_finalident(self, ):
        retval = self.process_finalident_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set196 = None

        set196_tree = None

        try:
            try:
                # ProtoCC.g:287:23: ( ( ID | STATE ) )
                # ProtoCC.g:
                pass 
                root_0 = self._adaptor.nil()


                set196 = self.input.LT(1)

                if self.input.LA(1) in {ID, STATE}:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set196))

                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "process_finalident"


    class process_events_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "process_events"
    # ProtoCC.g:288:5: process_events : ( ACCESS | EVICT | ID ) ;
    def process_events(self, ):
        retval = self.process_events_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set197 = None

        set197_tree = None

        try:
            try:
                # ProtoCC.g:288:20: ( ( ACCESS | EVICT | ID ) )
                # ProtoCC.g:
                pass 
                root_0 = self._adaptor.nil()


                set197 = self.input.LT(1)

                if self.input.LA(1) in {ACCESS, EVICT, ID}:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set197))

                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "process_events"


    class process_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "process_expr"
    # ProtoCC.g:289:5: process_expr : ( expressions | network_send | network_mcast | network_bcast | transaction );
    def process_expr(self, ):
        retval = self.process_expr_return()
        retval.start = self.input.LT(1)


        root_0 = None

        expressions198 = None
        network_send199 = None
        network_mcast200 = None
        network_bcast201 = None
        transaction202 = None


        try:
            try:
                # ProtoCC.g:289:17: ( expressions | network_send | network_mcast | network_bcast | transaction )
                alt32 = 5
                LA32 = self.input.LA(1)
                if LA32 in {ID}:
                    LA32_1 = self.input.LA(2)

                    if (LA32_1 == DOT) :
                        LA32 = self.input.LA(3)
                        if LA32 in {ID, NID, 134, 136, 138, 139, 140, 144}:
                            alt32 = 1
                        elif LA32 in {130, 143}:
                            alt32 = 2
                        elif LA32 in {121, 141}:
                            alt32 = 3
                        elif LA32 in {116, 135}:
                            alt32 = 4
                        else:
                            nvae = NoViableAltException("", 32, 9, self.input)

                            raise nvae


                    elif (LA32_1 in {EQUALSIGN, SEMICOLON}) :
                        alt32 = 1
                    else:
                        nvae = NoViableAltException("", 32, 1, self.input)

                        raise nvae


                elif LA32 in {ACCESS, IF, STALL, STATE, UNDEF, 119}:
                    alt32 = 1
                elif LA32 in {AWAIT}:
                    alt32 = 5
                else:
                    nvae = NoViableAltException("", 32, 0, self.input)

                    raise nvae


                if alt32 == 1:
                    # ProtoCC.g:289:19: expressions
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_expressions_in_process_expr2455)
                    expressions198 = self.expressions()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, expressions198.tree)



                elif alt32 == 2:
                    # ProtoCC.g:289:33: network_send
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_network_send_in_process_expr2459)
                    network_send199 = self.network_send()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, network_send199.tree)



                elif alt32 == 3:
                    # ProtoCC.g:289:48: network_mcast
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_network_mcast_in_process_expr2463)
                    network_mcast200 = self.network_mcast()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, network_mcast200.tree)



                elif alt32 == 4:
                    # ProtoCC.g:289:64: network_bcast
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_network_bcast_in_process_expr2467)
                    network_bcast201 = self.network_bcast()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, network_bcast201.tree)



                elif alt32 == 5:
                    # ProtoCC.g:289:79: transaction
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_transaction_in_process_expr2470)
                    transaction202 = self.transaction()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, transaction202.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "process_expr"


    class transaction_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "transaction"
    # ProtoCC.g:292:1: transaction : AWAIT OCBRACE ( trans )* CCBRACE -> ^( AWAIT_ ( trans )* ) ;
    def transaction(self, ):
        retval = self.transaction_return()
        retval.start = self.input.LT(1)


        root_0 = None

        AWAIT203 = None
        OCBRACE204 = None
        CCBRACE206 = None
        trans205 = None

        AWAIT203_tree = None
        OCBRACE204_tree = None
        CCBRACE206_tree = None
        stream_OCBRACE = RewriteRuleTokenStream(self._adaptor, "token OCBRACE")
        stream_AWAIT = RewriteRuleTokenStream(self._adaptor, "token AWAIT")
        stream_CCBRACE = RewriteRuleTokenStream(self._adaptor, "token CCBRACE")
        stream_trans = RewriteRuleSubtreeStream(self._adaptor, "rule trans")
        try:
            try:
                # ProtoCC.g:292:13: ( AWAIT OCBRACE ( trans )* CCBRACE -> ^( AWAIT_ ( trans )* ) )
                # ProtoCC.g:292:15: AWAIT OCBRACE ( trans )* CCBRACE
                pass 
                AWAIT203 = self.match(self.input, AWAIT, self.FOLLOW_AWAIT_in_transaction2480) 
                stream_AWAIT.add(AWAIT203)


                OCBRACE204 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_transaction2482) 
                stream_OCBRACE.add(OCBRACE204)


                # ProtoCC.g:292:29: ( trans )*
                while True: #loop33
                    alt33 = 2
                    LA33_0 = self.input.LA(1)

                    if (LA33_0 == WHEN) :
                        alt33 = 1


                    if alt33 == 1:
                        # ProtoCC.g:292:29: trans
                        pass 
                        self._state.following.append(self.FOLLOW_trans_in_transaction2484)
                        trans205 = self.trans()

                        self._state.following.pop()
                        stream_trans.add(trans205.tree)



                    else:
                        break #loop33


                CCBRACE206 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_transaction2487) 
                stream_CCBRACE.add(CCBRACE206)


                # AST Rewrite
                # elements: trans
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 292:44: -> ^( AWAIT_ ( trans )* )
                # ProtoCC.g:292:47: ^( AWAIT_ ( trans )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(AWAIT_, "AWAIT_")
                , root_1)

                # ProtoCC.g:292:56: ( trans )*
                while stream_trans.hasNext():
                    self._adaptor.addChild(root_1, stream_trans.nextTree())


                stream_trans.reset();

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "transaction"


    class trans_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "trans"
    # ProtoCC.g:293:5: trans : WHEN ID DDOT ( trans_body )* -> ^( WHEN_ ^( GUARD_ ID ) ( trans_body )* ENDWHEN_ ) ;
    def trans(self, ):
        retval = self.trans_return()
        retval.start = self.input.LT(1)


        root_0 = None

        WHEN207 = None
        ID208 = None
        DDOT209 = None
        trans_body210 = None

        WHEN207_tree = None
        ID208_tree = None
        DDOT209_tree = None
        stream_WHEN = RewriteRuleTokenStream(self._adaptor, "token WHEN")
        stream_DDOT = RewriteRuleTokenStream(self._adaptor, "token DDOT")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_trans_body = RewriteRuleSubtreeStream(self._adaptor, "rule trans_body")
        try:
            try:
                # ProtoCC.g:293:11: ( WHEN ID DDOT ( trans_body )* -> ^( WHEN_ ^( GUARD_ ID ) ( trans_body )* ENDWHEN_ ) )
                # ProtoCC.g:293:13: WHEN ID DDOT ( trans_body )*
                pass 
                WHEN207 = self.match(self.input, WHEN, self.FOLLOW_WHEN_in_trans2507) 
                stream_WHEN.add(WHEN207)


                ID208 = self.match(self.input, ID, self.FOLLOW_ID_in_trans2509) 
                stream_ID.add(ID208)


                DDOT209 = self.match(self.input, DDOT, self.FOLLOW_DDOT_in_trans2511) 
                stream_DDOT.add(DDOT209)


                # ProtoCC.g:293:26: ( trans_body )*
                while True: #loop34
                    alt34 = 2
                    LA34_0 = self.input.LA(1)

                    if (LA34_0 in {ACCESS, AWAIT, BREAK, ID, IF, NEXT, STALL, STATE, UNDEF, 119}) :
                        alt34 = 1


                    if alt34 == 1:
                        # ProtoCC.g:293:26: trans_body
                        pass 
                        self._state.following.append(self.FOLLOW_trans_body_in_trans2513)
                        trans_body210 = self.trans_body()

                        self._state.following.pop()
                        stream_trans_body.add(trans_body210.tree)



                    else:
                        break #loop34


                # AST Rewrite
                # elements: ID, trans_body
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 293:38: -> ^( WHEN_ ^( GUARD_ ID ) ( trans_body )* ENDWHEN_ )
                # ProtoCC.g:293:41: ^( WHEN_ ^( GUARD_ ID ) ( trans_body )* ENDWHEN_ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(WHEN_, "WHEN_")
                , root_1)

                # ProtoCC.g:293:49: ^( GUARD_ ID )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(GUARD_, "GUARD_")
                , root_2)

                self._adaptor.addChild(root_2, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_1, root_2)

                # ProtoCC.g:293:62: ( trans_body )*
                while stream_trans_body.hasNext():
                    self._adaptor.addChild(root_1, stream_trans_body.nextTree())


                stream_trans_body.reset();

                self._adaptor.addChild(root_1, 
                self._adaptor.createFromType(ENDWHEN_, "ENDWHEN_")
                )

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "trans"


    class trans_body_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "trans_body"
    # ProtoCC.g:294:9: trans_body : ( expressions | next_trans | next_break | transaction | network_send | network_mcast | network_bcast );
    def trans_body(self, ):
        retval = self.trans_body_return()
        retval.start = self.input.LT(1)


        root_0 = None

        expressions211 = None
        next_trans212 = None
        next_break213 = None
        transaction214 = None
        network_send215 = None
        network_mcast216 = None
        network_bcast217 = None


        try:
            try:
                # ProtoCC.g:294:20: ( expressions | next_trans | next_break | transaction | network_send | network_mcast | network_bcast )
                alt35 = 7
                LA35 = self.input.LA(1)
                if LA35 in {ID}:
                    LA35_1 = self.input.LA(2)

                    if (LA35_1 == DOT) :
                        LA35 = self.input.LA(3)
                        if LA35 in {ID, NID, 134, 136, 138, 139, 140, 144}:
                            alt35 = 1
                        elif LA35 in {130, 143}:
                            alt35 = 5
                        elif LA35 in {121, 141}:
                            alt35 = 6
                        elif LA35 in {116, 135}:
                            alt35 = 7
                        else:
                            nvae = NoViableAltException("", 35, 11, self.input)

                            raise nvae


                    elif (LA35_1 in {EQUALSIGN, SEMICOLON}) :
                        alt35 = 1
                    else:
                        nvae = NoViableAltException("", 35, 1, self.input)

                        raise nvae


                elif LA35 in {ACCESS, IF, STALL, STATE, UNDEF, 119}:
                    alt35 = 1
                elif LA35 in {NEXT}:
                    alt35 = 2
                elif LA35 in {BREAK}:
                    alt35 = 3
                elif LA35 in {AWAIT}:
                    alt35 = 4
                else:
                    nvae = NoViableAltException("", 35, 0, self.input)

                    raise nvae


                if alt35 == 1:
                    # ProtoCC.g:294:22: expressions
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_expressions_in_trans_body2546)
                    expressions211 = self.expressions()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, expressions211.tree)



                elif alt35 == 2:
                    # ProtoCC.g:294:36: next_trans
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_next_trans_in_trans_body2550)
                    next_trans212 = self.next_trans()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, next_trans212.tree)



                elif alt35 == 3:
                    # ProtoCC.g:294:49: next_break
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_next_break_in_trans_body2554)
                    next_break213 = self.next_break()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, next_break213.tree)



                elif alt35 == 4:
                    # ProtoCC.g:294:62: transaction
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_transaction_in_trans_body2558)
                    transaction214 = self.transaction()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, transaction214.tree)



                elif alt35 == 5:
                    # ProtoCC.g:294:76: network_send
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_network_send_in_trans_body2562)
                    network_send215 = self.network_send()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, network_send215.tree)



                elif alt35 == 6:
                    # ProtoCC.g:294:91: network_mcast
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_network_mcast_in_trans_body2566)
                    network_mcast216 = self.network_mcast()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, network_mcast216.tree)



                elif alt35 == 7:
                    # ProtoCC.g:294:107: network_bcast
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_network_bcast_in_trans_body2570)
                    network_bcast217 = self.network_bcast()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, network_bcast217.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "trans_body"


    class next_trans_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "next_trans"
    # ProtoCC.g:295:13: next_trans : NEXT OCBRACE ( trans )* CCBRACE -> ^( NEXT_ ( trans )* ) ;
    def next_trans(self, ):
        retval = self.next_trans_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEXT218 = None
        OCBRACE219 = None
        CCBRACE221 = None
        trans220 = None

        NEXT218_tree = None
        OCBRACE219_tree = None
        CCBRACE221_tree = None
        stream_OCBRACE = RewriteRuleTokenStream(self._adaptor, "token OCBRACE")
        stream_NEXT = RewriteRuleTokenStream(self._adaptor, "token NEXT")
        stream_CCBRACE = RewriteRuleTokenStream(self._adaptor, "token CCBRACE")
        stream_trans = RewriteRuleSubtreeStream(self._adaptor, "rule trans")
        try:
            try:
                # ProtoCC.g:295:23: ( NEXT OCBRACE ( trans )* CCBRACE -> ^( NEXT_ ( trans )* ) )
                # ProtoCC.g:295:25: NEXT OCBRACE ( trans )* CCBRACE
                pass 
                NEXT218 = self.match(self.input, NEXT, self.FOLLOW_NEXT_in_next_trans2588) 
                stream_NEXT.add(NEXT218)


                OCBRACE219 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_next_trans2590) 
                stream_OCBRACE.add(OCBRACE219)


                # ProtoCC.g:295:38: ( trans )*
                while True: #loop36
                    alt36 = 2
                    LA36_0 = self.input.LA(1)

                    if (LA36_0 == WHEN) :
                        alt36 = 1


                    if alt36 == 1:
                        # ProtoCC.g:295:38: trans
                        pass 
                        self._state.following.append(self.FOLLOW_trans_in_next_trans2592)
                        trans220 = self.trans()

                        self._state.following.pop()
                        stream_trans.add(trans220.tree)



                    else:
                        break #loop36


                CCBRACE221 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_next_trans2595) 
                stream_CCBRACE.add(CCBRACE221)


                # AST Rewrite
                # elements: trans
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 295:53: -> ^( NEXT_ ( trans )* )
                # ProtoCC.g:295:56: ^( NEXT_ ( trans )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(NEXT_, "NEXT_")
                , root_1)

                # ProtoCC.g:295:64: ( trans )*
                while stream_trans.hasNext():
                    self._adaptor.addChild(root_1, stream_trans.nextTree())


                stream_trans.reset();

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "next_trans"


    class next_break_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "next_break"
    # ProtoCC.g:297:5: next_break : BREAK SEMICOLON -> ^( BREAK_ ) ;
    def next_break(self, ):
        retval = self.next_break_return()
        retval.start = self.input.LT(1)


        root_0 = None

        BREAK222 = None
        SEMICOLON223 = None

        BREAK222_tree = None
        SEMICOLON223_tree = None
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_BREAK = RewriteRuleTokenStream(self._adaptor, "token BREAK")

        try:
            try:
                # ProtoCC.g:297:16: ( BREAK SEMICOLON -> ^( BREAK_ ) )
                # ProtoCC.g:297:18: BREAK SEMICOLON
                pass 
                BREAK222 = self.match(self.input, BREAK, self.FOLLOW_BREAK_in_next_break2616) 
                stream_BREAK.add(BREAK222)


                SEMICOLON223 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_next_break2618) 
                stream_SEMICOLON.add(SEMICOLON223)


                # AST Rewrite
                # elements: 
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 297:34: -> ^( BREAK_ )
                # ProtoCC.g:297:37: ^( BREAK_ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(BREAK_, "BREAK_")
                , root_1)

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "next_break"


    class expressions_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "expressions"
    # ProtoCC.g:300:1: expressions : ( assignment | conditional | object_block | set_block | internal_event_block | msg_stall | set_access | undefine );
    def expressions(self, ):
        retval = self.expressions_return()
        retval.start = self.input.LT(1)


        root_0 = None

        assignment224 = None
        conditional225 = None
        object_block226 = None
        set_block227 = None
        internal_event_block228 = None
        msg_stall229 = None
        set_access230 = None
        undefine231 = None


        try:
            try:
                # ProtoCC.g:300:13: ( assignment | conditional | object_block | set_block | internal_event_block | msg_stall | set_access | undefine )
                alt37 = 8
                LA37 = self.input.LA(1)
                if LA37 in {ID}:
                    LA37 = self.input.LA(2)
                    if LA37 in {DOT}:
                        LA37_8 = self.input.LA(3)

                        if (LA37_8 in {ID, NID}) :
                            alt37 = 3
                        elif (LA37_8 in {134, 136, 138, 139, 140, 144}) :
                            alt37 = 4
                        else:
                            nvae = NoViableAltException("", 37, 8, self.input)

                            raise nvae


                    elif LA37 in {EQUALSIGN}:
                        alt37 = 1
                    elif LA37 in {SEMICOLON}:
                        alt37 = 3
                    else:
                        nvae = NoViableAltException("", 37, 1, self.input)

                        raise nvae


                elif LA37 in {IF}:
                    alt37 = 2
                elif LA37 in {STATE}:
                    alt37 = 1
                elif LA37 in {119}:
                    alt37 = 5
                elif LA37 in {STALL}:
                    alt37 = 6
                elif LA37 in {ACCESS}:
                    alt37 = 7
                elif LA37 in {UNDEF}:
                    alt37 = 8
                else:
                    nvae = NoViableAltException("", 37, 0, self.input)

                    raise nvae


                if alt37 == 1:
                    # ProtoCC.g:300:15: assignment
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_assignment_in_expressions2634)
                    assignment224 = self.assignment()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, assignment224.tree)



                elif alt37 == 2:
                    # ProtoCC.g:300:28: conditional
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_conditional_in_expressions2638)
                    conditional225 = self.conditional()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, conditional225.tree)



                elif alt37 == 3:
                    # ProtoCC.g:300:42: object_block
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_object_block_in_expressions2642)
                    object_block226 = self.object_block()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, object_block226.tree)



                elif alt37 == 4:
                    # ProtoCC.g:300:57: set_block
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_set_block_in_expressions2646)
                    set_block227 = self.set_block()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, set_block227.tree)



                elif alt37 == 5:
                    # ProtoCC.g:300:69: internal_event_block
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_internal_event_block_in_expressions2650)
                    internal_event_block228 = self.internal_event_block()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, internal_event_block228.tree)



                elif alt37 == 6:
                    # ProtoCC.g:300:92: msg_stall
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_msg_stall_in_expressions2654)
                    msg_stall229 = self.msg_stall()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, msg_stall229.tree)



                elif alt37 == 7:
                    # ProtoCC.g:300:104: set_access
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_set_access_in_expressions2658)
                    set_access230 = self.set_access()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, set_access230.tree)



                elif alt37 == 8:
                    # ProtoCC.g:300:117: undefine
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_undefine_in_expressions2662)
                    undefine231 = self.undefine()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, undefine231.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "expressions"


    class assignment_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "assignment"
    # ProtoCC.g:301:1: assignment : process_finalident EQUALSIGN assign_types SEMICOLON -> ^( ASSIGN_ process_finalident EQUALSIGN assign_types ) ;
    def assignment(self, ):
        retval = self.assignment_return()
        retval.start = self.input.LT(1)


        root_0 = None

        EQUALSIGN233 = None
        SEMICOLON235 = None
        process_finalident232 = None
        assign_types234 = None

        EQUALSIGN233_tree = None
        SEMICOLON235_tree = None
        stream_EQUALSIGN = RewriteRuleTokenStream(self._adaptor, "token EQUALSIGN")
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_assign_types = RewriteRuleSubtreeStream(self._adaptor, "rule assign_types")
        stream_process_finalident = RewriteRuleSubtreeStream(self._adaptor, "rule process_finalident")
        try:
            try:
                # ProtoCC.g:301:12: ( process_finalident EQUALSIGN assign_types SEMICOLON -> ^( ASSIGN_ process_finalident EQUALSIGN assign_types ) )
                # ProtoCC.g:301:14: process_finalident EQUALSIGN assign_types SEMICOLON
                pass 
                self._state.following.append(self.FOLLOW_process_finalident_in_assignment2669)
                process_finalident232 = self.process_finalident()

                self._state.following.pop()
                stream_process_finalident.add(process_finalident232.tree)


                EQUALSIGN233 = self.match(self.input, EQUALSIGN, self.FOLLOW_EQUALSIGN_in_assignment2671) 
                stream_EQUALSIGN.add(EQUALSIGN233)


                self._state.following.append(self.FOLLOW_assign_types_in_assignment2673)
                assign_types234 = self.assign_types()

                self._state.following.pop()
                stream_assign_types.add(assign_types234.tree)


                SEMICOLON235 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_assignment2675) 
                stream_SEMICOLON.add(SEMICOLON235)


                # AST Rewrite
                # elements: process_finalident, assign_types, EQUALSIGN
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 301:65: -> ^( ASSIGN_ process_finalident EQUALSIGN assign_types )
                # ProtoCC.g:301:68: ^( ASSIGN_ process_finalident EQUALSIGN assign_types )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(ASSIGN_, "ASSIGN_")
                , root_1)

                self._adaptor.addChild(root_1, stream_process_finalident.nextTree())

                self._adaptor.addChild(root_1, 
                stream_EQUALSIGN.nextNode()
                )

                self._adaptor.addChild(root_1, stream_assign_types.nextTree())

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "assignment"


    class assign_types_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "assign_types"
    # ProtoCC.g:302:5: assign_types : ( object_expr | message_constr | math_op | set_func | INT | BOOL | NID );
    def assign_types(self, ):
        retval = self.assign_types_return()
        retval.start = self.input.LT(1)


        root_0 = None

        INT240 = None
        BOOL241 = None
        NID242 = None
        object_expr236 = None
        message_constr237 = None
        math_op238 = None
        set_func239 = None

        INT240_tree = None
        BOOL241_tree = None
        NID242_tree = None

        try:
            try:
                # ProtoCC.g:302:18: ( object_expr | message_constr | math_op | set_func | INT | BOOL | NID )
                alt38 = 7
                LA38 = self.input.LA(1)
                if LA38 in {ID}:
                    LA38 = self.input.LA(2)
                    if LA38 in {DOT}:
                        LA38_5 = self.input.LA(3)

                        if (LA38_5 in {ID, NID}) :
                            alt38 = 1
                        elif (LA38_5 in {134, 136, 138, 139, 140, 144}) :
                            alt38 = 4
                        else:
                            nvae = NoViableAltException("", 38, 5, self.input)

                            raise nvae


                    elif LA38 in {OBRACE}:
                        alt38 = 2
                    elif LA38 in {SEMICOLON}:
                        alt38 = 1
                    elif LA38 in {MINUS, PLUS}:
                        alt38 = 3
                    else:
                        nvae = NoViableAltException("", 38, 1, self.input)

                        raise nvae


                elif LA38 in {INT}:
                    LA38_2 = self.input.LA(2)

                    if (LA38_2 in {MINUS, PLUS}) :
                        alt38 = 3
                    elif (LA38_2 == SEMICOLON) :
                        alt38 = 5
                    else:
                        nvae = NoViableAltException("", 38, 2, self.input)

                        raise nvae


                elif LA38 in {BOOL}:
                    alt38 = 6
                elif LA38 in {NID}:
                    alt38 = 7
                else:
                    nvae = NoViableAltException("", 38, 0, self.input)

                    raise nvae


                if alt38 == 1:
                    # ProtoCC.g:302:20: object_expr
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_object_expr_in_assign_types2697)
                    object_expr236 = self.object_expr()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, object_expr236.tree)



                elif alt38 == 2:
                    # ProtoCC.g:302:34: message_constr
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_message_constr_in_assign_types2701)
                    message_constr237 = self.message_constr()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, message_constr237.tree)



                elif alt38 == 3:
                    # ProtoCC.g:302:51: math_op
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_math_op_in_assign_types2705)
                    math_op238 = self.math_op()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, math_op238.tree)



                elif alt38 == 4:
                    # ProtoCC.g:302:61: set_func
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_set_func_in_assign_types2709)
                    set_func239 = self.set_func()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, set_func239.tree)



                elif alt38 == 5:
                    # ProtoCC.g:302:72: INT
                    pass 
                    root_0 = self._adaptor.nil()


                    INT240 = self.match(self.input, INT, self.FOLLOW_INT_in_assign_types2713)
                    INT240_tree = self._adaptor.createWithPayload(INT240)
                    self._adaptor.addChild(root_0, INT240_tree)




                elif alt38 == 6:
                    # ProtoCC.g:302:78: BOOL
                    pass 
                    root_0 = self._adaptor.nil()


                    BOOL241 = self.match(self.input, BOOL, self.FOLLOW_BOOL_in_assign_types2717)
                    BOOL241_tree = self._adaptor.createWithPayload(BOOL241)
                    self._adaptor.addChild(root_0, BOOL241_tree)




                elif alt38 == 7:
                    # ProtoCC.g:302:85: NID
                    pass 
                    root_0 = self._adaptor.nil()


                    NID242 = self.match(self.input, NID, self.FOLLOW_NID_in_assign_types2721)
                    NID242_tree = self._adaptor.createWithPayload(NID242)
                    self._adaptor.addChild(root_0, NID242_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "assign_types"


    class math_op_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "math_op"
    # ProtoCC.g:303:5: math_op : val_range ( PLUS | MINUS ) val_range ;
    def math_op(self, ):
        retval = self.math_op_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set244 = None
        val_range243 = None
        val_range245 = None

        set244_tree = None

        try:
            try:
                # ProtoCC.g:303:13: ( val_range ( PLUS | MINUS ) val_range )
                # ProtoCC.g:303:15: val_range ( PLUS | MINUS ) val_range
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_val_range_in_math_op2732)
                val_range243 = self.val_range()

                self._state.following.pop()
                self._adaptor.addChild(root_0, val_range243.tree)


                set244 = self.input.LT(1)

                if self.input.LA(1) in {MINUS, PLUS}:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set244))

                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse



                self._state.following.append(self.FOLLOW_val_range_in_math_op2742)
                val_range245 = self.val_range()

                self._state.following.pop()
                self._adaptor.addChild(root_0, val_range245.tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "math_op"


    class msg_stall_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "msg_stall"
    # ProtoCC.g:304:1: msg_stall : STALL SEMICOLON -> ^( STALL_ ) ;
    def msg_stall(self, ):
        retval = self.msg_stall_return()
        retval.start = self.input.LT(1)


        root_0 = None

        STALL246 = None
        SEMICOLON247 = None

        STALL246_tree = None
        SEMICOLON247_tree = None
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_STALL = RewriteRuleTokenStream(self._adaptor, "token STALL")

        try:
            try:
                # ProtoCC.g:304:10: ( STALL SEMICOLON -> ^( STALL_ ) )
                # ProtoCC.g:304:12: STALL SEMICOLON
                pass 
                STALL246 = self.match(self.input, STALL, self.FOLLOW_STALL_in_msg_stall2748) 
                stream_STALL.add(STALL246)


                SEMICOLON247 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_msg_stall2750) 
                stream_SEMICOLON.add(SEMICOLON247)


                # AST Rewrite
                # elements: 
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 304:28: -> ^( STALL_ )
                # ProtoCC.g:304:31: ^( STALL_ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(STALL_, "STALL_")
                , root_1)

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "msg_stall"


    class set_access_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "set_access"
    # ProtoCC.g:305:1: set_access : ACCESS SEMICOLON -> ^( ACCESS_ ACCESS ) ;
    def set_access(self, ):
        retval = self.set_access_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ACCESS248 = None
        SEMICOLON249 = None

        ACCESS248_tree = None
        SEMICOLON249_tree = None
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_ACCESS = RewriteRuleTokenStream(self._adaptor, "token ACCESS")

        try:
            try:
                # ProtoCC.g:305:11: ( ACCESS SEMICOLON -> ^( ACCESS_ ACCESS ) )
                # ProtoCC.g:305:13: ACCESS SEMICOLON
                pass 
                ACCESS248 = self.match(self.input, ACCESS, self.FOLLOW_ACCESS_in_set_access2762) 
                stream_ACCESS.add(ACCESS248)


                SEMICOLON249 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_set_access2764) 
                stream_SEMICOLON.add(SEMICOLON249)


                # AST Rewrite
                # elements: ACCESS
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 305:30: -> ^( ACCESS_ ACCESS )
                # ProtoCC.g:305:33: ^( ACCESS_ ACCESS )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(ACCESS_, "ACCESS_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ACCESS.nextNode()
                )

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "set_access"


    class undefine_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "undefine"
    # ProtoCC.g:306:1: undefine : UNDEF ID SEMICOLON -> ^( UNDEF_ ID ) ;
    def undefine(self, ):
        retval = self.undefine_return()
        retval.start = self.input.LT(1)


        root_0 = None

        UNDEF250 = None
        ID251 = None
        SEMICOLON252 = None

        UNDEF250_tree = None
        ID251_tree = None
        SEMICOLON252_tree = None
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_UNDEF = RewriteRuleTokenStream(self._adaptor, "token UNDEF")

        try:
            try:
                # ProtoCC.g:306:9: ( UNDEF ID SEMICOLON -> ^( UNDEF_ ID ) )
                # ProtoCC.g:306:11: UNDEF ID SEMICOLON
                pass 
                UNDEF250 = self.match(self.input, UNDEF, self.FOLLOW_UNDEF_in_undefine2778) 
                stream_UNDEF.add(UNDEF250)


                ID251 = self.match(self.input, ID, self.FOLLOW_ID_in_undefine2780) 
                stream_ID.add(ID251)


                SEMICOLON252 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_undefine2782) 
                stream_SEMICOLON.add(SEMICOLON252)


                # AST Rewrite
                # elements: ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 306:30: -> ^( UNDEF_ ID )
                # ProtoCC.g:306:33: ^( UNDEF_ ID )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(UNDEF_, "UNDEF_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "undefine"


    class conditional_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "conditional"
    # ProtoCC.g:309:1: conditional : ( if_stmt | ifnot_stmt );
    def conditional(self, ):
        retval = self.conditional_return()
        retval.start = self.input.LT(1)


        root_0 = None

        if_stmt253 = None
        ifnot_stmt254 = None


        try:
            try:
                # ProtoCC.g:309:12: ( if_stmt | ifnot_stmt )
                alt39 = 2
                LA39_0 = self.input.LA(1)

                if (LA39_0 == IF) :
                    LA39_1 = self.input.LA(2)

                    if (LA39_1 == NEG) :
                        alt39 = 2
                    elif (LA39_1 in {BOOL, ID, INT, NID, OBRACE}) :
                        alt39 = 1
                    else:
                        nvae = NoViableAltException("", 39, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 39, 0, self.input)

                    raise nvae


                if alt39 == 1:
                    # ProtoCC.g:309:14: if_stmt
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_if_stmt_in_conditional2799)
                    if_stmt253 = self.if_stmt()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, if_stmt253.tree)



                elif alt39 == 2:
                    # ProtoCC.g:309:24: ifnot_stmt
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_ifnot_stmt_in_conditional2803)
                    ifnot_stmt254 = self.ifnot_stmt()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, ifnot_stmt254.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "conditional"


    class if_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "if_stmt"
    # ProtoCC.g:310:5: if_stmt : IF cond_comb OCBRACE if_expression CCBRACE ( ELSE OCBRACE else_expression CCBRACE )* -> {t_else}? ^( IFELSE_ ^( IF_ ^( COND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( NCOND_ cond_comb ) ( else_expression )* ENDIF_ ) ) -> ^( IFELSE_ ^( IF_ ^( COND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( NCOND_ cond_comb ) ENDIF_ ) ) ;
    def if_stmt(self, ):
        retval = self.if_stmt_return()
        retval.start = self.input.LT(1)


        root_0 = None

        IF255 = None
        OCBRACE257 = None
        CCBRACE259 = None
        ELSE260 = None
        OCBRACE261 = None
        CCBRACE263 = None
        cond_comb256 = None
        if_expression258 = None
        else_expression262 = None

        IF255_tree = None
        OCBRACE257_tree = None
        CCBRACE259_tree = None
        ELSE260_tree = None
        OCBRACE261_tree = None
        CCBRACE263_tree = None
        stream_OCBRACE = RewriteRuleTokenStream(self._adaptor, "token OCBRACE")
        stream_ELSE = RewriteRuleTokenStream(self._adaptor, "token ELSE")
        stream_IF = RewriteRuleTokenStream(self._adaptor, "token IF")
        stream_CCBRACE = RewriteRuleTokenStream(self._adaptor, "token CCBRACE")
        stream_else_expression = RewriteRuleSubtreeStream(self._adaptor, "rule else_expression")
        stream_if_expression = RewriteRuleSubtreeStream(self._adaptor, "rule if_expression")
        stream_cond_comb = RewriteRuleSubtreeStream(self._adaptor, "rule cond_comb")
        t_else = 0
        try:
            try:
                # ProtoCC.g:311:5: ( IF cond_comb OCBRACE if_expression CCBRACE ( ELSE OCBRACE else_expression CCBRACE )* -> {t_else}? ^( IFELSE_ ^( IF_ ^( COND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( NCOND_ cond_comb ) ( else_expression )* ENDIF_ ) ) -> ^( IFELSE_ ^( IF_ ^( COND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( NCOND_ cond_comb ) ENDIF_ ) ) )
                # ProtoCC.g:311:7: IF cond_comb OCBRACE if_expression CCBRACE ( ELSE OCBRACE else_expression CCBRACE )*
                pass 
                IF255 = self.match(self.input, IF, self.FOLLOW_IF_in_if_stmt2822) 
                stream_IF.add(IF255)


                self._state.following.append(self.FOLLOW_cond_comb_in_if_stmt2824)
                cond_comb256 = self.cond_comb()

                self._state.following.pop()
                stream_cond_comb.add(cond_comb256.tree)


                OCBRACE257 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_if_stmt2826) 
                stream_OCBRACE.add(OCBRACE257)


                self._state.following.append(self.FOLLOW_if_expression_in_if_stmt2828)
                if_expression258 = self.if_expression()

                self._state.following.pop()
                stream_if_expression.add(if_expression258.tree)


                CCBRACE259 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_if_stmt2830) 
                stream_CCBRACE.add(CCBRACE259)


                # ProtoCC.g:312:5: ( ELSE OCBRACE else_expression CCBRACE )*
                while True: #loop40
                    alt40 = 2
                    LA40_0 = self.input.LA(1)

                    if (LA40_0 == ELSE) :
                        alt40 = 1


                    if alt40 == 1:
                        # ProtoCC.g:312:6: ELSE OCBRACE else_expression CCBRACE
                        pass 
                        ELSE260 = self.match(self.input, ELSE, self.FOLLOW_ELSE_in_if_stmt2837) 
                        stream_ELSE.add(ELSE260)


                        #action start
                        t_else=1
                        #action end


                        OCBRACE261 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_if_stmt2841) 
                        stream_OCBRACE.add(OCBRACE261)


                        self._state.following.append(self.FOLLOW_else_expression_in_if_stmt2843)
                        else_expression262 = self.else_expression()

                        self._state.following.pop()
                        stream_else_expression.add(else_expression262.tree)


                        CCBRACE263 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_if_stmt2845) 
                        stream_CCBRACE.add(CCBRACE263)



                    else:
                        break #loop40


                # AST Rewrite
                # elements: cond_comb, cond_comb, if_expression, cond_comb, else_expression, if_expression, cond_comb
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                if t_else:
                    # 313:5: -> {t_else}? ^( IFELSE_ ^( IF_ ^( COND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( NCOND_ cond_comb ) ( else_expression )* ENDIF_ ) )
                    # ProtoCC.g:313:18: ^( IFELSE_ ^( IF_ ^( COND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( NCOND_ cond_comb ) ( else_expression )* ENDIF_ ) )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(IFELSE_, "IFELSE_")
                    , root_1)

                    # ProtoCC.g:313:28: ^( IF_ ^( COND_ cond_comb ) ( if_expression )* ENDIF_ )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(IF_, "IF_")
                    , root_2)

                    # ProtoCC.g:313:34: ^( COND_ cond_comb )
                    root_3 = self._adaptor.nil()
                    root_3 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(COND_, "COND_")
                    , root_3)

                    self._adaptor.addChild(root_3, stream_cond_comb.nextTree())

                    self._adaptor.addChild(root_2, root_3)

                    # ProtoCC.g:313:53: ( if_expression )*
                    while stream_if_expression.hasNext():
                        self._adaptor.addChild(root_2, stream_if_expression.nextTree())


                    stream_if_expression.reset();

                    self._adaptor.addChild(root_2, 
                    self._adaptor.createFromType(ENDIF_, "ENDIF_")
                    )

                    self._adaptor.addChild(root_1, root_2)

                    # ProtoCC.g:313:76: ^( IF_ ^( NCOND_ cond_comb ) ( else_expression )* ENDIF_ )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(IF_, "IF_")
                    , root_2)

                    # ProtoCC.g:313:82: ^( NCOND_ cond_comb )
                    root_3 = self._adaptor.nil()
                    root_3 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(NCOND_, "NCOND_")
                    , root_3)

                    self._adaptor.addChild(root_3, stream_cond_comb.nextTree())

                    self._adaptor.addChild(root_2, root_3)

                    # ProtoCC.g:313:102: ( else_expression )*
                    while stream_else_expression.hasNext():
                        self._adaptor.addChild(root_2, stream_else_expression.nextTree())


                    stream_else_expression.reset();

                    self._adaptor.addChild(root_2, 
                    self._adaptor.createFromType(ENDIF_, "ENDIF_")
                    )

                    self._adaptor.addChild(root_1, root_2)

                    self._adaptor.addChild(root_0, root_1)



                else: 
                    # 314:5: -> ^( IFELSE_ ^( IF_ ^( COND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( NCOND_ cond_comb ) ENDIF_ ) )
                    # ProtoCC.g:314:8: ^( IFELSE_ ^( IF_ ^( COND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( NCOND_ cond_comb ) ENDIF_ ) )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(IFELSE_, "IFELSE_")
                    , root_1)

                    # ProtoCC.g:314:18: ^( IF_ ^( COND_ cond_comb ) ( if_expression )* ENDIF_ )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(IF_, "IF_")
                    , root_2)

                    # ProtoCC.g:314:24: ^( COND_ cond_comb )
                    root_3 = self._adaptor.nil()
                    root_3 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(COND_, "COND_")
                    , root_3)

                    self._adaptor.addChild(root_3, stream_cond_comb.nextTree())

                    self._adaptor.addChild(root_2, root_3)

                    # ProtoCC.g:314:43: ( if_expression )*
                    while stream_if_expression.hasNext():
                        self._adaptor.addChild(root_2, stream_if_expression.nextTree())


                    stream_if_expression.reset();

                    self._adaptor.addChild(root_2, 
                    self._adaptor.createFromType(ENDIF_, "ENDIF_")
                    )

                    self._adaptor.addChild(root_1, root_2)

                    # ProtoCC.g:314:66: ^( IF_ ^( NCOND_ cond_comb ) ENDIF_ )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(IF_, "IF_")
                    , root_2)

                    # ProtoCC.g:314:72: ^( NCOND_ cond_comb )
                    root_3 = self._adaptor.nil()
                    root_3 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(NCOND_, "NCOND_")
                    , root_3)

                    self._adaptor.addChild(root_3, stream_cond_comb.nextTree())

                    self._adaptor.addChild(root_2, root_3)

                    self._adaptor.addChild(root_2, 
                    self._adaptor.createFromType(ENDIF_, "ENDIF_")
                    )

                    self._adaptor.addChild(root_1, root_2)

                    self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "if_stmt"


    class ifnot_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "ifnot_stmt"
    # ProtoCC.g:317:5: ifnot_stmt : IF NEG cond_comb OCBRACE if_expression CCBRACE ( ELSE OCBRACE else_expression CCBRACE )* -> {t_else}? ^( IFELSE_ ^( IF_ ^( NCOND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( COND_ cond_comb ) ( else_expression )* ENDIF_ ) ) -> ^( IFELSE_ ^( IF_ ^( NCOND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( COND_ cond_comb ) ENDIF_ ) ) ;
    def ifnot_stmt(self, ):
        retval = self.ifnot_stmt_return()
        retval.start = self.input.LT(1)


        root_0 = None

        IF264 = None
        NEG265 = None
        OCBRACE267 = None
        CCBRACE269 = None
        ELSE270 = None
        OCBRACE271 = None
        CCBRACE273 = None
        cond_comb266 = None
        if_expression268 = None
        else_expression272 = None

        IF264_tree = None
        NEG265_tree = None
        OCBRACE267_tree = None
        CCBRACE269_tree = None
        ELSE270_tree = None
        OCBRACE271_tree = None
        CCBRACE273_tree = None
        stream_NEG = RewriteRuleTokenStream(self._adaptor, "token NEG")
        stream_OCBRACE = RewriteRuleTokenStream(self._adaptor, "token OCBRACE")
        stream_ELSE = RewriteRuleTokenStream(self._adaptor, "token ELSE")
        stream_IF = RewriteRuleTokenStream(self._adaptor, "token IF")
        stream_CCBRACE = RewriteRuleTokenStream(self._adaptor, "token CCBRACE")
        stream_else_expression = RewriteRuleSubtreeStream(self._adaptor, "rule else_expression")
        stream_if_expression = RewriteRuleSubtreeStream(self._adaptor, "rule if_expression")
        stream_cond_comb = RewriteRuleSubtreeStream(self._adaptor, "rule cond_comb")
        t_else = 0
        try:
            try:
                # ProtoCC.g:318:5: ( IF NEG cond_comb OCBRACE if_expression CCBRACE ( ELSE OCBRACE else_expression CCBRACE )* -> {t_else}? ^( IFELSE_ ^( IF_ ^( NCOND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( COND_ cond_comb ) ( else_expression )* ENDIF_ ) ) -> ^( IFELSE_ ^( IF_ ^( NCOND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( COND_ cond_comb ) ENDIF_ ) ) )
                # ProtoCC.g:318:7: IF NEG cond_comb OCBRACE if_expression CCBRACE ( ELSE OCBRACE else_expression CCBRACE )*
                pass 
                IF264 = self.match(self.input, IF, self.FOLLOW_IF_in_ifnot_stmt2951) 
                stream_IF.add(IF264)


                NEG265 = self.match(self.input, NEG, self.FOLLOW_NEG_in_ifnot_stmt2953) 
                stream_NEG.add(NEG265)


                self._state.following.append(self.FOLLOW_cond_comb_in_ifnot_stmt2955)
                cond_comb266 = self.cond_comb()

                self._state.following.pop()
                stream_cond_comb.add(cond_comb266.tree)


                OCBRACE267 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_ifnot_stmt2957) 
                stream_OCBRACE.add(OCBRACE267)


                self._state.following.append(self.FOLLOW_if_expression_in_ifnot_stmt2959)
                if_expression268 = self.if_expression()

                self._state.following.pop()
                stream_if_expression.add(if_expression268.tree)


                CCBRACE269 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_ifnot_stmt2961) 
                stream_CCBRACE.add(CCBRACE269)


                # ProtoCC.g:319:5: ( ELSE OCBRACE else_expression CCBRACE )*
                while True: #loop41
                    alt41 = 2
                    LA41_0 = self.input.LA(1)

                    if (LA41_0 == ELSE) :
                        alt41 = 1


                    if alt41 == 1:
                        # ProtoCC.g:319:6: ELSE OCBRACE else_expression CCBRACE
                        pass 
                        ELSE270 = self.match(self.input, ELSE, self.FOLLOW_ELSE_in_ifnot_stmt2968) 
                        stream_ELSE.add(ELSE270)


                        #action start
                        t_else=1
                        #action end


                        OCBRACE271 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_ifnot_stmt2972) 
                        stream_OCBRACE.add(OCBRACE271)


                        self._state.following.append(self.FOLLOW_else_expression_in_ifnot_stmt2974)
                        else_expression272 = self.else_expression()

                        self._state.following.pop()
                        stream_else_expression.add(else_expression272.tree)


                        CCBRACE273 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_ifnot_stmt2976) 
                        stream_CCBRACE.add(CCBRACE273)



                    else:
                        break #loop41


                # AST Rewrite
                # elements: cond_comb, if_expression, if_expression, cond_comb, else_expression, cond_comb, cond_comb
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                if t_else:
                    # 320:5: -> {t_else}? ^( IFELSE_ ^( IF_ ^( NCOND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( COND_ cond_comb ) ( else_expression )* ENDIF_ ) )
                    # ProtoCC.g:320:18: ^( IFELSE_ ^( IF_ ^( NCOND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( COND_ cond_comb ) ( else_expression )* ENDIF_ ) )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(IFELSE_, "IFELSE_")
                    , root_1)

                    # ProtoCC.g:320:28: ^( IF_ ^( NCOND_ cond_comb ) ( if_expression )* ENDIF_ )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(IF_, "IF_")
                    , root_2)

                    # ProtoCC.g:320:34: ^( NCOND_ cond_comb )
                    root_3 = self._adaptor.nil()
                    root_3 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(NCOND_, "NCOND_")
                    , root_3)

                    self._adaptor.addChild(root_3, stream_cond_comb.nextTree())

                    self._adaptor.addChild(root_2, root_3)

                    # ProtoCC.g:320:54: ( if_expression )*
                    while stream_if_expression.hasNext():
                        self._adaptor.addChild(root_2, stream_if_expression.nextTree())


                    stream_if_expression.reset();

                    self._adaptor.addChild(root_2, 
                    self._adaptor.createFromType(ENDIF_, "ENDIF_")
                    )

                    self._adaptor.addChild(root_1, root_2)

                    # ProtoCC.g:320:77: ^( IF_ ^( COND_ cond_comb ) ( else_expression )* ENDIF_ )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(IF_, "IF_")
                    , root_2)

                    # ProtoCC.g:320:83: ^( COND_ cond_comb )
                    root_3 = self._adaptor.nil()
                    root_3 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(COND_, "COND_")
                    , root_3)

                    self._adaptor.addChild(root_3, stream_cond_comb.nextTree())

                    self._adaptor.addChild(root_2, root_3)

                    # ProtoCC.g:320:102: ( else_expression )*
                    while stream_else_expression.hasNext():
                        self._adaptor.addChild(root_2, stream_else_expression.nextTree())


                    stream_else_expression.reset();

                    self._adaptor.addChild(root_2, 
                    self._adaptor.createFromType(ENDIF_, "ENDIF_")
                    )

                    self._adaptor.addChild(root_1, root_2)

                    self._adaptor.addChild(root_0, root_1)



                else: 
                    # 321:5: -> ^( IFELSE_ ^( IF_ ^( NCOND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( COND_ cond_comb ) ENDIF_ ) )
                    # ProtoCC.g:321:8: ^( IFELSE_ ^( IF_ ^( NCOND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( COND_ cond_comb ) ENDIF_ ) )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(IFELSE_, "IFELSE_")
                    , root_1)

                    # ProtoCC.g:321:18: ^( IF_ ^( NCOND_ cond_comb ) ( if_expression )* ENDIF_ )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(IF_, "IF_")
                    , root_2)

                    # ProtoCC.g:321:24: ^( NCOND_ cond_comb )
                    root_3 = self._adaptor.nil()
                    root_3 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(NCOND_, "NCOND_")
                    , root_3)

                    self._adaptor.addChild(root_3, stream_cond_comb.nextTree())

                    self._adaptor.addChild(root_2, root_3)

                    # ProtoCC.g:321:44: ( if_expression )*
                    while stream_if_expression.hasNext():
                        self._adaptor.addChild(root_2, stream_if_expression.nextTree())


                    stream_if_expression.reset();

                    self._adaptor.addChild(root_2, 
                    self._adaptor.createFromType(ENDIF_, "ENDIF_")
                    )

                    self._adaptor.addChild(root_1, root_2)

                    # ProtoCC.g:321:67: ^( IF_ ^( COND_ cond_comb ) ENDIF_ )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(IF_, "IF_")
                    , root_2)

                    # ProtoCC.g:321:73: ^( COND_ cond_comb )
                    root_3 = self._adaptor.nil()
                    root_3 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(COND_, "COND_")
                    , root_3)

                    self._adaptor.addChild(root_3, stream_cond_comb.nextTree())

                    self._adaptor.addChild(root_2, root_3)

                    self._adaptor.addChild(root_2, 
                    self._adaptor.createFromType(ENDIF_, "ENDIF_")
                    )

                    self._adaptor.addChild(root_1, root_2)

                    self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "ifnot_stmt"


    class if_expression_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "if_expression"
    # ProtoCC.g:324:9: if_expression : ( exprwbreak )* ;
    def if_expression(self, ):
        retval = self.if_expression_return()
        retval.start = self.input.LT(1)


        root_0 = None

        exprwbreak274 = None


        try:
            try:
                # ProtoCC.g:324:22: ( ( exprwbreak )* )
                # ProtoCC.g:324:24: ( exprwbreak )*
                pass 
                root_0 = self._adaptor.nil()


                # ProtoCC.g:324:24: ( exprwbreak )*
                while True: #loop42
                    alt42 = 2
                    LA42_0 = self.input.LA(1)

                    if (LA42_0 in {ACCESS, AWAIT, BREAK, ID, IF, STALL, STATE, UNDEF, 119}) :
                        alt42 = 1


                    if alt42 == 1:
                        # ProtoCC.g:324:24: exprwbreak
                        pass 
                        self._state.following.append(self.FOLLOW_exprwbreak_in_if_expression3077)
                        exprwbreak274 = self.exprwbreak()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, exprwbreak274.tree)



                    else:
                        break #loop42




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "if_expression"


    class else_expression_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "else_expression"
    # ProtoCC.g:325:9: else_expression : ( exprwbreak )* ;
    def else_expression(self, ):
        retval = self.else_expression_return()
        retval.start = self.input.LT(1)


        root_0 = None

        exprwbreak275 = None


        try:
            try:
                # ProtoCC.g:325:24: ( ( exprwbreak )* )
                # ProtoCC.g:325:26: ( exprwbreak )*
                pass 
                root_0 = self._adaptor.nil()


                # ProtoCC.g:325:26: ( exprwbreak )*
                while True: #loop43
                    alt43 = 2
                    LA43_0 = self.input.LA(1)

                    if (LA43_0 in {ACCESS, AWAIT, BREAK, ID, IF, STALL, STATE, UNDEF, 119}) :
                        alt43 = 1


                    if alt43 == 1:
                        # ProtoCC.g:325:26: exprwbreak
                        pass 
                        self._state.following.append(self.FOLLOW_exprwbreak_in_else_expression3092)
                        exprwbreak275 = self.exprwbreak()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, exprwbreak275.tree)



                    else:
                        break #loop43




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "else_expression"


    class exprwbreak_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "exprwbreak"
    # ProtoCC.g:326:9: exprwbreak : ( expressions | network_send | network_mcast | network_bcast | transaction | next_break );
    def exprwbreak(self, ):
        retval = self.exprwbreak_return()
        retval.start = self.input.LT(1)


        root_0 = None

        expressions276 = None
        network_send277 = None
        network_mcast278 = None
        network_bcast279 = None
        transaction280 = None
        next_break281 = None


        try:
            try:
                # ProtoCC.g:326:19: ( expressions | network_send | network_mcast | network_bcast | transaction | next_break )
                alt44 = 6
                LA44 = self.input.LA(1)
                if LA44 in {ID}:
                    LA44_1 = self.input.LA(2)

                    if (LA44_1 == DOT) :
                        LA44 = self.input.LA(3)
                        if LA44 in {ID, NID, 134, 136, 138, 139, 140, 144}:
                            alt44 = 1
                        elif LA44 in {130, 143}:
                            alt44 = 2
                        elif LA44 in {121, 141}:
                            alt44 = 3
                        elif LA44 in {116, 135}:
                            alt44 = 4
                        else:
                            nvae = NoViableAltException("", 44, 10, self.input)

                            raise nvae


                    elif (LA44_1 in {EQUALSIGN, SEMICOLON}) :
                        alt44 = 1
                    else:
                        nvae = NoViableAltException("", 44, 1, self.input)

                        raise nvae


                elif LA44 in {ACCESS, IF, STALL, STATE, UNDEF, 119}:
                    alt44 = 1
                elif LA44 in {AWAIT}:
                    alt44 = 5
                elif LA44 in {BREAK}:
                    alt44 = 6
                else:
                    nvae = NoViableAltException("", 44, 0, self.input)

                    raise nvae


                if alt44 == 1:
                    # ProtoCC.g:326:21: expressions
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_expressions_in_exprwbreak3107)
                    expressions276 = self.expressions()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, expressions276.tree)



                elif alt44 == 2:
                    # ProtoCC.g:326:35: network_send
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_network_send_in_exprwbreak3111)
                    network_send277 = self.network_send()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, network_send277.tree)



                elif alt44 == 3:
                    # ProtoCC.g:326:50: network_mcast
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_network_mcast_in_exprwbreak3115)
                    network_mcast278 = self.network_mcast()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, network_mcast278.tree)



                elif alt44 == 4:
                    # ProtoCC.g:326:66: network_bcast
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_network_bcast_in_exprwbreak3119)
                    network_bcast279 = self.network_bcast()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, network_bcast279.tree)



                elif alt44 == 5:
                    # ProtoCC.g:326:82: transaction
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_transaction_in_exprwbreak3123)
                    transaction280 = self.transaction()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, transaction280.tree)



                elif alt44 == 6:
                    # ProtoCC.g:326:96: next_break
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_next_break_in_exprwbreak3127)
                    next_break281 = self.next_break()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, next_break281.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "exprwbreak"


    class cond_comb_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "cond_comb"
    # ProtoCC.g:327:9: cond_comb : cond_rel ( combinatorial_operator cond_rel )* ;
    def cond_comb(self, ):
        retval = self.cond_comb_return()
        retval.start = self.input.LT(1)


        root_0 = None

        cond_rel282 = None
        combinatorial_operator283 = None
        cond_rel284 = None


        try:
            try:
                # ProtoCC.g:327:18: ( cond_rel ( combinatorial_operator cond_rel )* )
                # ProtoCC.g:327:20: cond_rel ( combinatorial_operator cond_rel )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_cond_rel_in_cond_comb3141)
                cond_rel282 = self.cond_rel()

                self._state.following.pop()
                self._adaptor.addChild(root_0, cond_rel282.tree)


                # ProtoCC.g:327:29: ( combinatorial_operator cond_rel )*
                while True: #loop45
                    alt45 = 2
                    LA45_0 = self.input.LA(1)

                    if (LA45_0 in {110, 145}) :
                        alt45 = 1


                    if alt45 == 1:
                        # ProtoCC.g:327:30: combinatorial_operator cond_rel
                        pass 
                        self._state.following.append(self.FOLLOW_combinatorial_operator_in_cond_comb3144)
                        combinatorial_operator283 = self.combinatorial_operator()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, combinatorial_operator283.tree)


                        self._state.following.append(self.FOLLOW_cond_rel_in_cond_comb3146)
                        cond_rel284 = self.cond_rel()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, cond_rel284.tree)



                    else:
                        break #loop45




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "cond_comb"


    class cond_rel_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "cond_rel"
    # ProtoCC.g:328:9: cond_rel : ( OBRACE )* cond_sel ( CBRACE )* -> cond_sel ;
    def cond_rel(self, ):
        retval = self.cond_rel_return()
        retval.start = self.input.LT(1)


        root_0 = None

        OBRACE285 = None
        CBRACE287 = None
        cond_sel286 = None

        OBRACE285_tree = None
        CBRACE287_tree = None
        stream_OBRACE = RewriteRuleTokenStream(self._adaptor, "token OBRACE")
        stream_CBRACE = RewriteRuleTokenStream(self._adaptor, "token CBRACE")
        stream_cond_sel = RewriteRuleSubtreeStream(self._adaptor, "rule cond_sel")
        try:
            try:
                # ProtoCC.g:328:18: ( ( OBRACE )* cond_sel ( CBRACE )* -> cond_sel )
                # ProtoCC.g:328:20: ( OBRACE )* cond_sel ( CBRACE )*
                pass 
                # ProtoCC.g:328:20: ( OBRACE )*
                while True: #loop46
                    alt46 = 2
                    LA46_0 = self.input.LA(1)

                    if (LA46_0 == OBRACE) :
                        alt46 = 1


                    if alt46 == 1:
                        # ProtoCC.g:328:20: OBRACE
                        pass 
                        OBRACE285 = self.match(self.input, OBRACE, self.FOLLOW_OBRACE_in_cond_rel3163) 
                        stream_OBRACE.add(OBRACE285)



                    else:
                        break #loop46


                self._state.following.append(self.FOLLOW_cond_sel_in_cond_rel3166)
                cond_sel286 = self.cond_sel()

                self._state.following.pop()
                stream_cond_sel.add(cond_sel286.tree)


                # ProtoCC.g:328:37: ( CBRACE )*
                while True: #loop47
                    alt47 = 2
                    LA47_0 = self.input.LA(1)

                    if (LA47_0 == CBRACE) :
                        alt47 = 1


                    if alt47 == 1:
                        # ProtoCC.g:328:37: CBRACE
                        pass 
                        CBRACE287 = self.match(self.input, CBRACE, self.FOLLOW_CBRACE_in_cond_rel3168) 
                        stream_CBRACE.add(CBRACE287)



                    else:
                        break #loop47


                # AST Rewrite
                # elements: cond_sel
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 328:45: -> cond_sel
                self._adaptor.addChild(root_0, stream_cond_sel.nextTree())




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "cond_rel"


    class cond_sel_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "cond_sel"
    # ProtoCC.g:329:13: cond_sel : cond_type_expr ( relational_operator cond_type_expr )* ;
    def cond_sel(self, ):
        retval = self.cond_sel_return()
        retval.start = self.input.LT(1)


        root_0 = None

        cond_type_expr288 = None
        relational_operator289 = None
        cond_type_expr290 = None


        try:
            try:
                # ProtoCC.g:329:22: ( cond_type_expr ( relational_operator cond_type_expr )* )
                # ProtoCC.g:329:24: cond_type_expr ( relational_operator cond_type_expr )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_cond_type_expr_in_cond_sel3192)
                cond_type_expr288 = self.cond_type_expr()

                self._state.following.pop()
                self._adaptor.addChild(root_0, cond_type_expr288.tree)


                # ProtoCC.g:329:39: ( relational_operator cond_type_expr )*
                while True: #loop48
                    alt48 = 2
                    LA48_0 = self.input.LA(1)

                    if ((111 <= LA48_0 <= 115) or LA48_0 in {109}) :
                        alt48 = 1


                    if alt48 == 1:
                        # ProtoCC.g:329:40: relational_operator cond_type_expr
                        pass 
                        self._state.following.append(self.FOLLOW_relational_operator_in_cond_sel3195)
                        relational_operator289 = self.relational_operator()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, relational_operator289.tree)


                        self._state.following.append(self.FOLLOW_cond_type_expr_in_cond_sel3197)
                        cond_type_expr290 = self.cond_type_expr()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, cond_type_expr290.tree)



                    else:
                        break #loop48




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "cond_sel"


    class cond_type_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "cond_type_expr"
    # ProtoCC.g:330:13: cond_type_expr : cond_types ( ( PLUS | MINUS | MULT ) cond_types )* ;
    def cond_type_expr(self, ):
        retval = self.cond_type_expr_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set292 = None
        cond_types291 = None
        cond_types293 = None

        set292_tree = None

        try:
            try:
                # ProtoCC.g:330:27: ( cond_types ( ( PLUS | MINUS | MULT ) cond_types )* )
                # ProtoCC.g:330:29: cond_types ( ( PLUS | MINUS | MULT ) cond_types )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_cond_types_in_cond_type_expr3217)
                cond_types291 = self.cond_types()

                self._state.following.pop()
                self._adaptor.addChild(root_0, cond_types291.tree)


                # ProtoCC.g:330:40: ( ( PLUS | MINUS | MULT ) cond_types )*
                while True: #loop49
                    alt49 = 2
                    LA49_0 = self.input.LA(1)

                    if (LA49_0 in {MINUS, MULT, PLUS}) :
                        alt49 = 1


                    if alt49 == 1:
                        # ProtoCC.g:330:41: ( PLUS | MINUS | MULT ) cond_types
                        pass 
                        set292 = self.input.LT(1)

                        if self.input.LA(1) in {MINUS, MULT, PLUS}:
                            self.input.consume()
                            self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set292))

                            self._state.errorRecovery = False


                        else:
                            mse = MismatchedSetException(None, self.input)
                            raise mse



                        self._state.following.append(self.FOLLOW_cond_types_in_cond_type_expr3232)
                        cond_types293 = self.cond_types()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, cond_types293.tree)



                    else:
                        break #loop49




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "cond_type_expr"


    class cond_types_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "cond_types"
    # ProtoCC.g:331:13: cond_types : ( object_expr | set_func | INT | BOOL | NID );
    def cond_types(self, ):
        retval = self.cond_types_return()
        retval.start = self.input.LT(1)


        root_0 = None

        INT296 = None
        BOOL297 = None
        NID298 = None
        object_expr294 = None
        set_func295 = None

        INT296_tree = None
        BOOL297_tree = None
        NID298_tree = None

        try:
            try:
                # ProtoCC.g:331:24: ( object_expr | set_func | INT | BOOL | NID )
                alt50 = 5
                LA50 = self.input.LA(1)
                if LA50 in {ID}:
                    LA50_1 = self.input.LA(2)

                    if (LA50_1 == DOT) :
                        LA50_5 = self.input.LA(3)

                        if (LA50_5 in {ID, NID}) :
                            alt50 = 1
                        elif (LA50_5 in {134, 136, 138, 139, 140, 144}) :
                            alt50 = 2
                        else:
                            nvae = NoViableAltException("", 50, 5, self.input)

                            raise nvae


                    elif ((109 <= LA50_1 <= 115) or LA50_1 in {CBRACE, MINUS, MULT, OCBRACE, PLUS, 145}) :
                        alt50 = 1
                    else:
                        nvae = NoViableAltException("", 50, 1, self.input)

                        raise nvae


                elif LA50 in {INT}:
                    alt50 = 3
                elif LA50 in {BOOL}:
                    alt50 = 4
                elif LA50 in {NID}:
                    alt50 = 5
                else:
                    nvae = NoViableAltException("", 50, 0, self.input)

                    raise nvae


                if alt50 == 1:
                    # ProtoCC.g:331:26: object_expr
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_object_expr_in_cond_types3253)
                    object_expr294 = self.object_expr()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, object_expr294.tree)



                elif alt50 == 2:
                    # ProtoCC.g:331:40: set_func
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_set_func_in_cond_types3257)
                    set_func295 = self.set_func()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, set_func295.tree)



                elif alt50 == 3:
                    # ProtoCC.g:331:51: INT
                    pass 
                    root_0 = self._adaptor.nil()


                    INT296 = self.match(self.input, INT, self.FOLLOW_INT_in_cond_types3261)
                    INT296_tree = self._adaptor.createWithPayload(INT296)
                    self._adaptor.addChild(root_0, INT296_tree)




                elif alt50 == 4:
                    # ProtoCC.g:331:57: BOOL
                    pass 
                    root_0 = self._adaptor.nil()


                    BOOL297 = self.match(self.input, BOOL, self.FOLLOW_BOOL_in_cond_types3265)
                    BOOL297_tree = self._adaptor.createWithPayload(BOOL297)
                    self._adaptor.addChild(root_0, BOOL297_tree)




                elif alt50 == 5:
                    # ProtoCC.g:331:64: NID
                    pass 
                    root_0 = self._adaptor.nil()


                    NID298 = self.match(self.input, NID, self.FOLLOW_NID_in_cond_types3269)
                    NID298_tree = self._adaptor.createWithPayload(NID298)
                    self._adaptor.addChild(root_0, NID298_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "cond_types"


    class policy_op_type_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "policy_op_type"
    # ProtoCC.g:335:1: policy_op_type : ( 'Rd' | 'Wr' | 'RdWr' | 'None' );
    def policy_op_type(self, ):
        retval = self.policy_op_type_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set299 = None

        set299_tree = None

        try:
            try:
                # ProtoCC.g:335:15: ( 'Rd' | 'Wr' | 'RdWr' | 'None' )
                # ProtoCC.g:
                pass 
                root_0 = self._adaptor.nil()


                set299 = self.input.LT(1)

                if self.input.LA(1) in {123, 127, 128, 132}:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set299))

                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "policy_op_type"


    class policy_op_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "policy_op"
    # ProtoCC.g:336:1: policy_op : ( ( policy_op_type ( '|' policy_op_type )* ) -> ^( POLICY_OP_ ( policy_op_type )+ ) | '_' -> ^( POLICY_OP_ '_' ) );
    def policy_op(self, ):
        retval = self.policy_op_return()
        retval.start = self.input.LT(1)


        root_0 = None

        char_literal301 = None
        char_literal303 = None
        policy_op_type300 = None
        policy_op_type302 = None

        char_literal301_tree = None
        char_literal303_tree = None
        stream_133 = RewriteRuleTokenStream(self._adaptor, "token 133")
        stream_145 = RewriteRuleTokenStream(self._adaptor, "token 145")
        stream_policy_op_type = RewriteRuleSubtreeStream(self._adaptor, "rule policy_op_type")
        try:
            try:
                # ProtoCC.g:337:3: ( ( policy_op_type ( '|' policy_op_type )* ) -> ^( POLICY_OP_ ( policy_op_type )+ ) | '_' -> ^( POLICY_OP_ '_' ) )
                alt52 = 2
                LA52_0 = self.input.LA(1)

                if (LA52_0 in {123, 127, 128, 132}) :
                    alt52 = 1
                elif (LA52_0 == 133) :
                    alt52 = 2
                else:
                    nvae = NoViableAltException("", 52, 0, self.input)

                    raise nvae


                if alt52 == 1:
                    # ProtoCC.g:337:5: ( policy_op_type ( '|' policy_op_type )* )
                    pass 
                    # ProtoCC.g:337:5: ( policy_op_type ( '|' policy_op_type )* )
                    # ProtoCC.g:337:6: policy_op_type ( '|' policy_op_type )*
                    pass 
                    self._state.following.append(self.FOLLOW_policy_op_type_in_policy_op3301)
                    policy_op_type300 = self.policy_op_type()

                    self._state.following.pop()
                    stream_policy_op_type.add(policy_op_type300.tree)


                    # ProtoCC.g:337:21: ( '|' policy_op_type )*
                    while True: #loop51
                        alt51 = 2
                        LA51_0 = self.input.LA(1)

                        if (LA51_0 == 145) :
                            alt51 = 1


                        if alt51 == 1:
                            # ProtoCC.g:337:22: '|' policy_op_type
                            pass 
                            char_literal301 = self.match(self.input, 145, self.FOLLOW_145_in_policy_op3304) 
                            stream_145.add(char_literal301)


                            self._state.following.append(self.FOLLOW_policy_op_type_in_policy_op3306)
                            policy_op_type302 = self.policy_op_type()

                            self._state.following.pop()
                            stream_policy_op_type.add(policy_op_type302.tree)



                        else:
                            break #loop51





                    # AST Rewrite
                    # elements: policy_op_type
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 337:44: -> ^( POLICY_OP_ ( policy_op_type )+ )
                    # ProtoCC.g:337:47: ^( POLICY_OP_ ( policy_op_type )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(POLICY_OP_, "POLICY_OP_")
                    , root_1)

                    # ProtoCC.g:337:60: ( policy_op_type )+
                    if not (stream_policy_op_type.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_policy_op_type.hasNext():
                        self._adaptor.addChild(root_1, stream_policy_op_type.nextTree())


                    stream_policy_op_type.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt52 == 2:
                    # ProtoCC.g:338:4: '_'
                    pass 
                    char_literal303 = self.match(self.input, 133, self.FOLLOW_133_in_policy_op3323) 
                    stream_133.add(char_literal303)


                    # AST Rewrite
                    # elements: 133
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 338:43: -> ^( POLICY_OP_ '_' )
                    # ProtoCC.g:338:46: ^( POLICY_OP_ '_' )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(POLICY_OP_, "POLICY_OP_")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_133.nextNode()
                    )

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "policy_op"


    class policy_data_type_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "policy_data_type"
    # ProtoCC.g:341:1: policy_data_type : ( 'Dirty' | 'Clean' | 'P' | 'NP' | 'None' );
    def policy_data_type(self, ):
        retval = self.policy_data_type_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set304 = None

        set304_tree = None

        try:
            try:
                # ProtoCC.g:341:17: ( 'Dirty' | 'Clean' | 'P' | 'NP' | 'None' )
                # ProtoCC.g:
                pass 
                root_0 = self._adaptor.nil()


                set304 = self.input.LT(1)

                if self.input.LA(1) in {117, 118, 122, 123, 125}:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set304))

                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "policy_data_type"


    class policy_data_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "policy_data"
    # ProtoCC.g:342:1: policy_data : ( ( policy_data_type ( '|' policy_data_type )* ) -> ^( POLICY_DATA_ ( policy_data_type )+ ) | '_' -> ^( POLICY_DATA_ '_' ) );
    def policy_data(self, ):
        retval = self.policy_data_return()
        retval.start = self.input.LT(1)


        root_0 = None

        char_literal306 = None
        char_literal308 = None
        policy_data_type305 = None
        policy_data_type307 = None

        char_literal306_tree = None
        char_literal308_tree = None
        stream_133 = RewriteRuleTokenStream(self._adaptor, "token 133")
        stream_145 = RewriteRuleTokenStream(self._adaptor, "token 145")
        stream_policy_data_type = RewriteRuleSubtreeStream(self._adaptor, "rule policy_data_type")
        try:
            try:
                # ProtoCC.g:343:3: ( ( policy_data_type ( '|' policy_data_type )* ) -> ^( POLICY_DATA_ ( policy_data_type )+ ) | '_' -> ^( POLICY_DATA_ '_' ) )
                alt54 = 2
                LA54_0 = self.input.LA(1)

                if (LA54_0 in {117, 118, 122, 123, 125}) :
                    alt54 = 1
                elif (LA54_0 == 133) :
                    alt54 = 2
                else:
                    nvae = NoViableAltException("", 54, 0, self.input)

                    raise nvae


                if alt54 == 1:
                    # ProtoCC.g:343:5: ( policy_data_type ( '|' policy_data_type )* )
                    pass 
                    # ProtoCC.g:343:5: ( policy_data_type ( '|' policy_data_type )* )
                    # ProtoCC.g:343:6: policy_data_type ( '|' policy_data_type )*
                    pass 
                    self._state.following.append(self.FOLLOW_policy_data_type_in_policy_data3401)
                    policy_data_type305 = self.policy_data_type()

                    self._state.following.pop()
                    stream_policy_data_type.add(policy_data_type305.tree)


                    # ProtoCC.g:343:23: ( '|' policy_data_type )*
                    while True: #loop53
                        alt53 = 2
                        LA53_0 = self.input.LA(1)

                        if (LA53_0 == 145) :
                            alt53 = 1


                        if alt53 == 1:
                            # ProtoCC.g:343:24: '|' policy_data_type
                            pass 
                            char_literal306 = self.match(self.input, 145, self.FOLLOW_145_in_policy_data3404) 
                            stream_145.add(char_literal306)


                            self._state.following.append(self.FOLLOW_policy_data_type_in_policy_data3406)
                            policy_data_type307 = self.policy_data_type()

                            self._state.following.pop()
                            stream_policy_data_type.add(policy_data_type307.tree)



                        else:
                            break #loop53





                    # AST Rewrite
                    # elements: policy_data_type
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 343:48: -> ^( POLICY_DATA_ ( policy_data_type )+ )
                    # ProtoCC.g:343:51: ^( POLICY_DATA_ ( policy_data_type )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(POLICY_DATA_, "POLICY_DATA_")
                    , root_1)

                    # ProtoCC.g:343:66: ( policy_data_type )+
                    if not (stream_policy_data_type.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_policy_data_type.hasNext():
                        self._adaptor.addChild(root_1, stream_policy_data_type.nextTree())


                    stream_policy_data_type.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt54 == 2:
                    # ProtoCC.g:344:4: '_'
                    pass 
                    char_literal308 = self.match(self.input, 133, self.FOLLOW_133_in_policy_data3423) 
                    stream_133.add(char_literal308)


                    # AST Rewrite
                    # elements: 133
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 344:47: -> ^( POLICY_DATA_ '_' )
                    # ProtoCC.g:344:50: ^( POLICY_DATA_ '_' )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(POLICY_DATA_, "POLICY_DATA_")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_133.nextNode()
                    )

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "policy_data"


    class policy_coh_type_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "policy_coh_type"
    # ProtoCC.g:347:1: policy_coh_type : ( 'coh' | 'nco' );
    def policy_coh_type(self, ):
        retval = self.policy_coh_type_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set309 = None

        set309_tree = None

        try:
            try:
                # ProtoCC.g:347:16: ( 'coh' | 'nco' )
                # ProtoCC.g:
                pass 
                root_0 = self._adaptor.nil()


                set309 = self.input.LT(1)

                if self.input.LA(1) in {137, 142}:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set309))

                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "policy_coh_type"


    class policy_coh_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "policy_coh"
    # ProtoCC.g:348:1: policy_coh : ( ( policy_coh_type ( '|' policy_coh_type )* ) -> ^( POLICY_COH_ ( policy_coh_type )+ ) | '_' -> ^( POLICY_COH_ '_' ) );
    def policy_coh(self, ):
        retval = self.policy_coh_return()
        retval.start = self.input.LT(1)


        root_0 = None

        char_literal311 = None
        char_literal313 = None
        policy_coh_type310 = None
        policy_coh_type312 = None

        char_literal311_tree = None
        char_literal313_tree = None
        stream_133 = RewriteRuleTokenStream(self._adaptor, "token 133")
        stream_145 = RewriteRuleTokenStream(self._adaptor, "token 145")
        stream_policy_coh_type = RewriteRuleSubtreeStream(self._adaptor, "rule policy_coh_type")
        try:
            try:
                # ProtoCC.g:349:3: ( ( policy_coh_type ( '|' policy_coh_type )* ) -> ^( POLICY_COH_ ( policy_coh_type )+ ) | '_' -> ^( POLICY_COH_ '_' ) )
                alt56 = 2
                LA56_0 = self.input.LA(1)

                if (LA56_0 in {137, 142}) :
                    alt56 = 1
                elif (LA56_0 == 133) :
                    alt56 = 2
                else:
                    nvae = NoViableAltException("", 56, 0, self.input)

                    raise nvae


                if alt56 == 1:
                    # ProtoCC.g:349:5: ( policy_coh_type ( '|' policy_coh_type )* )
                    pass 
                    # ProtoCC.g:349:5: ( policy_coh_type ( '|' policy_coh_type )* )
                    # ProtoCC.g:349:6: policy_coh_type ( '|' policy_coh_type )*
                    pass 
                    self._state.following.append(self.FOLLOW_policy_coh_type_in_policy_coh3493)
                    policy_coh_type310 = self.policy_coh_type()

                    self._state.following.pop()
                    stream_policy_coh_type.add(policy_coh_type310.tree)


                    # ProtoCC.g:349:22: ( '|' policy_coh_type )*
                    while True: #loop55
                        alt55 = 2
                        LA55_0 = self.input.LA(1)

                        if (LA55_0 == 145) :
                            alt55 = 1


                        if alt55 == 1:
                            # ProtoCC.g:349:23: '|' policy_coh_type
                            pass 
                            char_literal311 = self.match(self.input, 145, self.FOLLOW_145_in_policy_coh3496) 
                            stream_145.add(char_literal311)


                            self._state.following.append(self.FOLLOW_policy_coh_type_in_policy_coh3498)
                            policy_coh_type312 = self.policy_coh_type()

                            self._state.following.pop()
                            stream_policy_coh_type.add(policy_coh_type312.tree)



                        else:
                            break #loop55





                    # AST Rewrite
                    # elements: policy_coh_type
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 349:46: -> ^( POLICY_COH_ ( policy_coh_type )+ )
                    # ProtoCC.g:349:49: ^( POLICY_COH_ ( policy_coh_type )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(POLICY_COH_, "POLICY_COH_")
                    , root_1)

                    # ProtoCC.g:349:63: ( policy_coh_type )+
                    if not (stream_policy_coh_type.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_policy_coh_type.hasNext():
                        self._adaptor.addChild(root_1, stream_policy_coh_type.nextTree())


                    stream_policy_coh_type.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt56 == 2:
                    # ProtoCC.g:350:4: '_'
                    pass 
                    char_literal313 = self.match(self.input, 133, self.FOLLOW_133_in_policy_coh3515) 
                    stream_133.add(char_literal313)


                    # AST Rewrite
                    # elements: 133
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 350:45: -> ^( POLICY_COH_ '_' )
                    # ProtoCC.g:350:48: ^( POLICY_COH_ '_' )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(POLICY_COH_, "POLICY_COH_")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_133.nextNode()
                    )

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "policy_coh"


    class label_state_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "label_state"
    # ProtoCC.g:354:1: label_state :{...}? ID OBRACE policy_op COMMA policy_data COMMA policy_coh CBRACE -> ^( LABEL_STATE_ policy_op policy_data policy_coh ) ;
    def label_state(self, ):
        retval = self.label_state_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID314 = None
        OBRACE315 = None
        COMMA317 = None
        COMMA319 = None
        CBRACE321 = None
        policy_op316 = None
        policy_data318 = None
        policy_coh320 = None

        ID314_tree = None
        OBRACE315_tree = None
        COMMA317_tree = None
        COMMA319_tree = None
        CBRACE321_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_OBRACE = RewriteRuleTokenStream(self._adaptor, "token OBRACE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CBRACE = RewriteRuleTokenStream(self._adaptor, "token CBRACE")
        stream_policy_op = RewriteRuleSubtreeStream(self._adaptor, "rule policy_op")
        stream_policy_data = RewriteRuleSubtreeStream(self._adaptor, "rule policy_data")
        stream_policy_coh = RewriteRuleSubtreeStream(self._adaptor, "rule policy_coh")
        try:
            try:
                # ProtoCC.g:354:12: ({...}? ID OBRACE policy_op COMMA policy_data COMMA policy_coh CBRACE -> ^( LABEL_STATE_ policy_op policy_data policy_coh ) )
                # ProtoCC.g:354:14: {...}? ID OBRACE policy_op COMMA policy_data COMMA policy_coh CBRACE
                pass 
                if not ((self.input.LT(1).text == 'S')):
                    raise FailedPredicateException(self.input, "label_state", "self.input.LT(1).text == 'S'")


                ID314 = self.match(self.input, ID, self.FOLLOW_ID_in_label_state3572) 
                stream_ID.add(ID314)


                OBRACE315 = self.match(self.input, OBRACE, self.FOLLOW_OBRACE_in_label_state3574) 
                stream_OBRACE.add(OBRACE315)


                self._state.following.append(self.FOLLOW_policy_op_in_label_state3576)
                policy_op316 = self.policy_op()

                self._state.following.pop()
                stream_policy_op.add(policy_op316.tree)


                COMMA317 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_label_state3578) 
                stream_COMMA.add(COMMA317)


                self._state.following.append(self.FOLLOW_policy_data_in_label_state3580)
                policy_data318 = self.policy_data()

                self._state.following.pop()
                stream_policy_data.add(policy_data318.tree)


                COMMA319 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_label_state3582) 
                stream_COMMA.add(COMMA319)


                self._state.following.append(self.FOLLOW_policy_coh_in_label_state3584)
                policy_coh320 = self.policy_coh()

                self._state.following.pop()
                stream_policy_coh.add(policy_coh320.tree)


                CBRACE321 = self.match(self.input, CBRACE, self.FOLLOW_CBRACE_in_label_state3586) 
                stream_CBRACE.add(CBRACE321)


                # AST Rewrite
                # elements: policy_op, policy_data, policy_coh
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 355:4: -> ^( LABEL_STATE_ policy_op policy_data policy_coh )
                # ProtoCC.g:355:7: ^( LABEL_STATE_ policy_op policy_data policy_coh )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(LABEL_STATE_, "LABEL_STATE_")
                , root_1)

                self._adaptor.addChild(root_1, stream_policy_op.nextTree())

                self._adaptor.addChild(root_1, stream_policy_data.nextTree())

                self._adaptor.addChild(root_1, stream_policy_coh.nextTree())

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "label_state"


    class label_message_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "label_message"
    # ProtoCC.g:357:1: label_message :{...}? ID OBRACE policy_op COMMA policy_data COMMA policy_coh CBRACE -> ^( LABEL_MESSAGE_ policy_op policy_data policy_coh ) ;
    def label_message(self, ):
        retval = self.label_message_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID322 = None
        OBRACE323 = None
        COMMA325 = None
        COMMA327 = None
        CBRACE329 = None
        policy_op324 = None
        policy_data326 = None
        policy_coh328 = None

        ID322_tree = None
        OBRACE323_tree = None
        COMMA325_tree = None
        COMMA327_tree = None
        CBRACE329_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_OBRACE = RewriteRuleTokenStream(self._adaptor, "token OBRACE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CBRACE = RewriteRuleTokenStream(self._adaptor, "token CBRACE")
        stream_policy_op = RewriteRuleSubtreeStream(self._adaptor, "rule policy_op")
        stream_policy_data = RewriteRuleSubtreeStream(self._adaptor, "rule policy_data")
        stream_policy_coh = RewriteRuleSubtreeStream(self._adaptor, "rule policy_coh")
        try:
            try:
                # ProtoCC.g:357:14: ({...}? ID OBRACE policy_op COMMA policy_data COMMA policy_coh CBRACE -> ^( LABEL_MESSAGE_ policy_op policy_data policy_coh ) )
                # ProtoCC.g:357:15: {...}? ID OBRACE policy_op COMMA policy_data COMMA policy_coh CBRACE
                pass 
                if not ((self.input.LT(1).text == 'M')):
                    raise FailedPredicateException(self.input, "label_message", "self.input.LT(1).text == 'M'")


                ID322 = self.match(self.input, ID, self.FOLLOW_ID_in_label_message3610) 
                stream_ID.add(ID322)


                OBRACE323 = self.match(self.input, OBRACE, self.FOLLOW_OBRACE_in_label_message3612) 
                stream_OBRACE.add(OBRACE323)


                self._state.following.append(self.FOLLOW_policy_op_in_label_message3614)
                policy_op324 = self.policy_op()

                self._state.following.pop()
                stream_policy_op.add(policy_op324.tree)


                COMMA325 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_label_message3616) 
                stream_COMMA.add(COMMA325)


                self._state.following.append(self.FOLLOW_policy_data_in_label_message3618)
                policy_data326 = self.policy_data()

                self._state.following.pop()
                stream_policy_data.add(policy_data326.tree)


                COMMA327 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_label_message3620) 
                stream_COMMA.add(COMMA327)


                self._state.following.append(self.FOLLOW_policy_coh_in_label_message3622)
                policy_coh328 = self.policy_coh()

                self._state.following.pop()
                stream_policy_coh.add(policy_coh328.tree)


                CBRACE329 = self.match(self.input, CBRACE, self.FOLLOW_CBRACE_in_label_message3624) 
                stream_CBRACE.add(CBRACE329)


                # AST Rewrite
                # elements: policy_data, policy_op, policy_coh
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 358:3: -> ^( LABEL_MESSAGE_ policy_op policy_data policy_coh )
                # ProtoCC.g:358:6: ^( LABEL_MESSAGE_ policy_op policy_data policy_coh )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(LABEL_MESSAGE_, "LABEL_MESSAGE_")
                , root_1)

                self._adaptor.addChild(root_1, stream_policy_op.nextTree())

                self._adaptor.addChild(root_1, stream_policy_data.nextTree())

                self._adaptor.addChild(root_1, stream_policy_coh.nextTree())

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "label_message"


    class data_rule_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "data_rule"
    # ProtoCC.g:361:1: data_rule : 'Data' OBRACE label_state CBRACE SEMICOLON -> ^( DATA_RULE_ label_state ) ;
    def data_rule(self, ):
        retval = self.data_rule_return()
        retval.start = self.input.LT(1)


        root_0 = None

        string_literal330 = None
        OBRACE331 = None
        CBRACE333 = None
        SEMICOLON334 = None
        label_state332 = None

        string_literal330_tree = None
        OBRACE331_tree = None
        CBRACE333_tree = None
        SEMICOLON334_tree = None
        stream_OBRACE = RewriteRuleTokenStream(self._adaptor, "token OBRACE")
        stream_DATA = RewriteRuleTokenStream(self._adaptor, "token DATA")
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_CBRACE = RewriteRuleTokenStream(self._adaptor, "token CBRACE")
        stream_label_state = RewriteRuleSubtreeStream(self._adaptor, "rule label_state")
        try:
            try:
                # ProtoCC.g:361:10: ( 'Data' OBRACE label_state CBRACE SEMICOLON -> ^( DATA_RULE_ label_state ) )
                # ProtoCC.g:361:12: 'Data' OBRACE label_state CBRACE SEMICOLON
                pass 
                string_literal330 = self.match(self.input, DATA, self.FOLLOW_DATA_in_data_rule3648) 
                stream_DATA.add(string_literal330)


                OBRACE331 = self.match(self.input, OBRACE, self.FOLLOW_OBRACE_in_data_rule3650) 
                stream_OBRACE.add(OBRACE331)


                self._state.following.append(self.FOLLOW_label_state_in_data_rule3652)
                label_state332 = self.label_state()

                self._state.following.pop()
                stream_label_state.add(label_state332.tree)


                CBRACE333 = self.match(self.input, CBRACE, self.FOLLOW_CBRACE_in_data_rule3654) 
                stream_CBRACE.add(CBRACE333)


                SEMICOLON334 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_data_rule3656) 
                stream_SEMICOLON.add(SEMICOLON334)


                # AST Rewrite
                # elements: label_state
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 362:3: -> ^( DATA_RULE_ label_state )
                # ProtoCC.g:362:6: ^( DATA_RULE_ label_state )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(DATA_RULE_, "DATA_RULE_")
                , root_1)

                self._adaptor.addChild(root_1, stream_label_state.nextTree())

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "data_rule"


    class local_rule_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "local_rule"
    # ProtoCC.g:364:1: local_rule : 'Local' OBRACE label_state COMMA label_message COMMA label_state CBRACE SEMICOLON -> ^( LOCAL_RULE_ label_state label_message label_state ) ;
    def local_rule(self, ):
        retval = self.local_rule_return()
        retval.start = self.input.LT(1)


        root_0 = None

        string_literal335 = None
        OBRACE336 = None
        COMMA338 = None
        COMMA340 = None
        CBRACE342 = None
        SEMICOLON343 = None
        label_state337 = None
        label_message339 = None
        label_state341 = None

        string_literal335_tree = None
        OBRACE336_tree = None
        COMMA338_tree = None
        COMMA340_tree = None
        CBRACE342_tree = None
        SEMICOLON343_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_OBRACE = RewriteRuleTokenStream(self._adaptor, "token OBRACE")
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_CBRACE = RewriteRuleTokenStream(self._adaptor, "token CBRACE")
        stream_120 = RewriteRuleTokenStream(self._adaptor, "token 120")
        stream_label_state = RewriteRuleSubtreeStream(self._adaptor, "rule label_state")
        stream_label_message = RewriteRuleSubtreeStream(self._adaptor, "rule label_message")
        try:
            try:
                # ProtoCC.g:364:11: ( 'Local' OBRACE label_state COMMA label_message COMMA label_state CBRACE SEMICOLON -> ^( LOCAL_RULE_ label_state label_message label_state ) )
                # ProtoCC.g:364:13: 'Local' OBRACE label_state COMMA label_message COMMA label_state CBRACE SEMICOLON
                pass 
                string_literal335 = self.match(self.input, 120, self.FOLLOW_120_in_local_rule3673) 
                stream_120.add(string_literal335)


                OBRACE336 = self.match(self.input, OBRACE, self.FOLLOW_OBRACE_in_local_rule3675) 
                stream_OBRACE.add(OBRACE336)


                self._state.following.append(self.FOLLOW_label_state_in_local_rule3677)
                label_state337 = self.label_state()

                self._state.following.pop()
                stream_label_state.add(label_state337.tree)


                COMMA338 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_local_rule3679) 
                stream_COMMA.add(COMMA338)


                self._state.following.append(self.FOLLOW_label_message_in_local_rule3681)
                label_message339 = self.label_message()

                self._state.following.pop()
                stream_label_message.add(label_message339.tree)


                COMMA340 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_local_rule3683) 
                stream_COMMA.add(COMMA340)


                self._state.following.append(self.FOLLOW_label_state_in_local_rule3685)
                label_state341 = self.label_state()

                self._state.following.pop()
                stream_label_state.add(label_state341.tree)


                CBRACE342 = self.match(self.input, CBRACE, self.FOLLOW_CBRACE_in_local_rule3687) 
                stream_CBRACE.add(CBRACE342)


                SEMICOLON343 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_local_rule3689) 
                stream_SEMICOLON.add(SEMICOLON343)


                # AST Rewrite
                # elements: label_message, label_state, label_state
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 365:2: -> ^( LOCAL_RULE_ label_state label_message label_state )
                # ProtoCC.g:365:5: ^( LOCAL_RULE_ label_state label_message label_state )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(LOCAL_RULE_, "LOCAL_RULE_")
                , root_1)

                self._adaptor.addChild(root_1, stream_label_state.nextTree())

                self._adaptor.addChild(root_1, stream_label_message.nextTree())

                self._adaptor.addChild(root_1, stream_label_state.nextTree())

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "local_rule"


    class rule_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "rule"
    # ProtoCC.g:368:1: rule : 'Rule' OBRACE label_state COMMA label_message COMMA label_state CBRACE SEMICOLON -> ^( RULE_ label_state label_message label_state ) ;
    def rule(self, ):
        retval = self.rule_return()
        retval.start = self.input.LT(1)


        root_0 = None

        string_literal344 = None
        OBRACE345 = None
        COMMA347 = None
        COMMA349 = None
        CBRACE351 = None
        SEMICOLON352 = None
        label_state346 = None
        label_message348 = None
        label_state350 = None

        string_literal344_tree = None
        OBRACE345_tree = None
        COMMA347_tree = None
        COMMA349_tree = None
        CBRACE351_tree = None
        SEMICOLON352_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_OBRACE = RewriteRuleTokenStream(self._adaptor, "token OBRACE")
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_129 = RewriteRuleTokenStream(self._adaptor, "token 129")
        stream_CBRACE = RewriteRuleTokenStream(self._adaptor, "token CBRACE")
        stream_label_state = RewriteRuleSubtreeStream(self._adaptor, "rule label_state")
        stream_label_message = RewriteRuleSubtreeStream(self._adaptor, "rule label_message")
        try:
            try:
                # ProtoCC.g:368:5: ( 'Rule' OBRACE label_state COMMA label_message COMMA label_state CBRACE SEMICOLON -> ^( RULE_ label_state label_message label_state ) )
                # ProtoCC.g:368:7: 'Rule' OBRACE label_state COMMA label_message COMMA label_state CBRACE SEMICOLON
                pass 
                string_literal344 = self.match(self.input, 129, self.FOLLOW_129_in_rule3710) 
                stream_129.add(string_literal344)


                OBRACE345 = self.match(self.input, OBRACE, self.FOLLOW_OBRACE_in_rule3712) 
                stream_OBRACE.add(OBRACE345)


                self._state.following.append(self.FOLLOW_label_state_in_rule3714)
                label_state346 = self.label_state()

                self._state.following.pop()
                stream_label_state.add(label_state346.tree)


                COMMA347 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_rule3716) 
                stream_COMMA.add(COMMA347)


                self._state.following.append(self.FOLLOW_label_message_in_rule3718)
                label_message348 = self.label_message()

                self._state.following.pop()
                stream_label_message.add(label_message348.tree)


                COMMA349 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_rule3720) 
                stream_COMMA.add(COMMA349)


                self._state.following.append(self.FOLLOW_label_state_in_rule3722)
                label_state350 = self.label_state()

                self._state.following.pop()
                stream_label_state.add(label_state350.tree)


                CBRACE351 = self.match(self.input, CBRACE, self.FOLLOW_CBRACE_in_rule3724) 
                stream_CBRACE.add(CBRACE351)


                SEMICOLON352 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_rule3726) 
                stream_SEMICOLON.add(SEMICOLON352)


                # AST Rewrite
                # elements: label_state, label_state, label_message
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 369:4: -> ^( RULE_ label_state label_message label_state )
                # ProtoCC.g:369:7: ^( RULE_ label_state label_message label_state )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(RULE_, "RULE_")
                , root_1)

                self._adaptor.addChild(root_1, stream_label_state.nextTree())

                self._adaptor.addChild(root_1, stream_label_message.nextTree())

                self._adaptor.addChild(root_1, stream_label_state.nextTree())

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "rule"


    class policy_rule_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "policy_rule"
    # ProtoCC.g:371:1: policy_rule : ( data_rule | local_rule | rule );
    def policy_rule(self, ):
        retval = self.policy_rule_return()
        retval.start = self.input.LT(1)


        root_0 = None

        data_rule353 = None
        local_rule354 = None
        rule355 = None


        try:
            try:
                # ProtoCC.g:371:12: ( data_rule | local_rule | rule )
                alt57 = 3
                LA57 = self.input.LA(1)
                if LA57 in {DATA}:
                    alt57 = 1
                elif LA57 in {120}:
                    alt57 = 2
                elif LA57 in {129}:
                    alt57 = 3
                else:
                    nvae = NoViableAltException("", 57, 0, self.input)

                    raise nvae


                if alt57 == 1:
                    # ProtoCC.g:371:14: data_rule
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_data_rule_in_policy_rule3748)
                    data_rule353 = self.data_rule()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, data_rule353.tree)



                elif alt57 == 2:
                    # ProtoCC.g:371:26: local_rule
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_local_rule_in_policy_rule3752)
                    local_rule354 = self.local_rule()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, local_rule354.tree)



                elif alt57 == 3:
                    # ProtoCC.g:371:39: rule
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_rule_in_policy_rule3756)
                    rule355 = self.rule()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, rule355.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "policy_rule"


    class policy_block_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "policy_block"
    # ProtoCC.g:372:1: policy_block : 'Policy' ID OCBRACE ( policy_rule )* CCBRACE -> ^( POLICY_ ID ( policy_rule )* ) ;
    def policy_block(self, ):
        retval = self.policy_block_return()
        retval.start = self.input.LT(1)


        root_0 = None

        string_literal356 = None
        ID357 = None
        OCBRACE358 = None
        CCBRACE360 = None
        policy_rule359 = None

        string_literal356_tree = None
        ID357_tree = None
        OCBRACE358_tree = None
        CCBRACE360_tree = None
        stream_126 = RewriteRuleTokenStream(self._adaptor, "token 126")
        stream_OCBRACE = RewriteRuleTokenStream(self._adaptor, "token OCBRACE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CCBRACE = RewriteRuleTokenStream(self._adaptor, "token CCBRACE")
        stream_policy_rule = RewriteRuleSubtreeStream(self._adaptor, "rule policy_rule")
        try:
            try:
                # ProtoCC.g:372:14: ( 'Policy' ID OCBRACE ( policy_rule )* CCBRACE -> ^( POLICY_ ID ( policy_rule )* ) )
                # ProtoCC.g:372:16: 'Policy' ID OCBRACE ( policy_rule )* CCBRACE
                pass 
                string_literal356 = self.match(self.input, 126, self.FOLLOW_126_in_policy_block3763) 
                stream_126.add(string_literal356)


                ID357 = self.match(self.input, ID, self.FOLLOW_ID_in_policy_block3765) 
                stream_ID.add(ID357)


                OCBRACE358 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_policy_block3767) 
                stream_OCBRACE.add(OCBRACE358)


                # ProtoCC.g:372:36: ( policy_rule )*
                while True: #loop58
                    alt58 = 2
                    LA58_0 = self.input.LA(1)

                    if (LA58_0 in {DATA, 120, 129}) :
                        alt58 = 1


                    if alt58 == 1:
                        # ProtoCC.g:372:36: policy_rule
                        pass 
                        self._state.following.append(self.FOLLOW_policy_rule_in_policy_block3769)
                        policy_rule359 = self.policy_rule()

                        self._state.following.pop()
                        stream_policy_rule.add(policy_rule359.tree)



                    else:
                        break #loop58


                CCBRACE360 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_policy_block3772) 
                stream_CCBRACE.add(CCBRACE360)


                # AST Rewrite
                # elements: ID, policy_rule
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 372:57: -> ^( POLICY_ ID ( policy_rule )* )
                # ProtoCC.g:372:60: ^( POLICY_ ID ( policy_rule )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(POLICY_, "POLICY_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # ProtoCC.g:372:73: ( policy_rule )*
                while stream_policy_rule.hasNext():
                    self._adaptor.addChild(root_1, stream_policy_rule.nextTree())


                stream_policy_rule.reset();

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "policy_block"


    class policy_file_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "policy_file"
    # ProtoCC.g:374:1: policy_file : ( policy_block )+ -> ^( POL_FILE_ ( policy_block )+ ) ;
    def policy_file(self, ):
        retval = self.policy_file_return()
        retval.start = self.input.LT(1)


        root_0 = None

        policy_block361 = None

        stream_policy_block = RewriteRuleSubtreeStream(self._adaptor, "rule policy_block")
        try:
            try:
                # ProtoCC.g:374:12: ( ( policy_block )+ -> ^( POL_FILE_ ( policy_block )+ ) )
                # ProtoCC.g:374:14: ( policy_block )+
                pass 
                # ProtoCC.g:374:14: ( policy_block )+
                cnt59 = 0
                while True: #loop59
                    alt59 = 2
                    LA59_0 = self.input.LA(1)

                    if (LA59_0 == 126) :
                        alt59 = 1


                    if alt59 == 1:
                        # ProtoCC.g:374:14: policy_block
                        pass 
                        self._state.following.append(self.FOLLOW_policy_block_in_policy_file3790)
                        policy_block361 = self.policy_block()

                        self._state.following.pop()
                        stream_policy_block.add(policy_block361.tree)



                    else:
                        if cnt59 >= 1:
                            break #loop59

                        eee = EarlyExitException(59, self.input)
                        raise eee

                    cnt59 += 1


                # AST Rewrite
                # elements: policy_block
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 375:2: -> ^( POL_FILE_ ( policy_block )+ )
                # ProtoCC.g:375:5: ^( POL_FILE_ ( policy_block )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(POL_FILE_, "POL_FILE_")
                , root_1)

                # ProtoCC.g:375:17: ( policy_block )+
                if not (stream_policy_block.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_policy_block.hasNext():
                    self._adaptor.addChild(root_1, stream_policy_block.nextTree())


                stream_policy_block.reset()

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "policy_file"



 

    FOLLOW_119_in_internal_event_function750 = frozenset([1])
    FOLLOW_const_decl_in_document1078 = frozenset([1, 4, 6, 19, 27, 33, 49, 51, 65, 68, 74, 100, 102, 104, 119])
    FOLLOW_init_hw_in_document1082 = frozenset([1, 4, 6, 19, 27, 33, 49, 51, 65, 68, 74, 100, 102, 104, 119])
    FOLLOW_arch_block_in_document1086 = frozenset([1, 4, 6, 19, 27, 33, 49, 51, 65, 68, 74, 100, 102, 104, 119])
    FOLLOW_expressions_in_document1090 = frozenset([1, 4, 6, 19, 27, 33, 49, 51, 65, 68, 74, 100, 102, 104, 119])
    FOLLOW_policy_file_in_document1098 = frozenset([1])
    FOLLOW_int_decl_in_declarations1109 = frozenset([1])
    FOLLOW_bool_decl_in_declarations1113 = frozenset([1])
    FOLLOW_state_decl_in_declarations1117 = frozenset([1])
    FOLLOW_data_decl_in_declarations1121 = frozenset([1])
    FOLLOW_id_decl_in_declarations1125 = frozenset([1])
    FOLLOW_CONSTANT_in_const_decl1137 = frozenset([49])
    FOLLOW_ID_in_const_decl1139 = frozenset([56])
    FOLLOW_INT_in_const_decl1141 = frozenset([1])
    FOLLOW_INTID_in_int_decl1163 = frozenset([82])
    FOLLOW_range_in_int_decl1165 = frozenset([49])
    FOLLOW_ID_in_int_decl1167 = frozenset([42, 93])
    FOLLOW_EQUALSIGN_in_int_decl1170 = frozenset([56])
    FOLLOW_INT_in_int_decl1172 = frozenset([42, 93])
    FOLLOW_SEMICOLON_in_int_decl1176 = frozenset([1])
    FOLLOW_BOOLID_in_bool_decl1204 = frozenset([49])
    FOLLOW_ID_in_bool_decl1206 = frozenset([42, 93])
    FOLLOW_EQUALSIGN_in_bool_decl1209 = frozenset([14])
    FOLLOW_BOOL_in_bool_decl1211 = frozenset([42, 93])
    FOLLOW_SEMICOLON_in_bool_decl1215 = frozenset([1])
    FOLLOW_STATE_in_state_decl1242 = frozenset([49])
    FOLLOW_ID_in_state_decl1244 = frozenset([93])
    FOLLOW_SEMICOLON_in_state_decl1246 = frozenset([1])
    FOLLOW_DATA_in_data_decl1265 = frozenset([49])
    FOLLOW_ID_in_data_decl1267 = frozenset([93])
    FOLLOW_SEMICOLON_in_data_decl1269 = frozenset([1])
    FOLLOW_set_decl_in_id_decl1288 = frozenset([78, 95])
    FOLLOW_NID_in_id_decl1291 = frozenset([49])
    FOLLOW_ID_in_id_decl1293 = frozenset([42, 93])
    FOLLOW_EQUALSIGN_in_id_decl1296 = frozenset([49, 95])
    FOLLOW_set_decl_in_id_decl1298 = frozenset([49, 95])
    FOLLOW_ID_in_id_decl1301 = frozenset([42, 93])
    FOLLOW_SEMICOLON_in_id_decl1305 = frozenset([1])
    FOLLOW_SET_in_set_decl1342 = frozenset([82])
    FOLLOW_OEBRACE_in_set_decl1344 = frozenset([49, 56])
    FOLLOW_val_range_in_set_decl1346 = frozenset([23])
    FOLLOW_CEBRACE_in_set_decl1348 = frozenset([1])
    FOLLOW_OEBRACE_in_range1371 = frozenset([49, 56])
    FOLLOW_val_range_in_range1373 = frozenset([35])
    FOLLOW_DOT_in_range1375 = frozenset([35])
    FOLLOW_DOT_in_range1377 = frozenset([49, 56])
    FOLLOW_val_range_in_range1379 = frozenset([23])
    FOLLOW_CEBRACE_in_range1381 = frozenset([1])
    FOLLOW_ARRAY_in_array_decl1430 = frozenset([82])
    FOLLOW_range_in_array_decl1432 = frozenset([1])
    FOLLOW_FIFO_in_fifo_decl1442 = frozenset([82])
    FOLLOW_range_in_fifo_decl1444 = frozenset([1])
    FOLLOW_network_block_in_init_hw1454 = frozenset([1])
    FOLLOW_machines_in_init_hw1458 = frozenset([1])
    FOLLOW_message_block_in_init_hw1462 = frozenset([1])
    FOLLOW_object_expr_in_object_block1473 = frozenset([93])
    FOLLOW_SEMICOLON_in_object_block1475 = frozenset([1])
    FOLLOW_object_id_in_object_expr1490 = frozenset([1])
    FOLLOW_object_func_in_object_expr1494 = frozenset([1])
    FOLLOW_ID_in_object_id1505 = frozenset([1])
    FOLLOW_ID_in_object_func1522 = frozenset([35])
    FOLLOW_DOT_in_object_func1524 = frozenset([49, 78])
    FOLLOW_object_idres_in_object_func1526 = frozenset([1, 80])
    FOLLOW_OBRACE_in_object_func1529 = frozenset([21, 24, 49])
    FOLLOW_object_expr_in_object_func1531 = frozenset([21, 24, 49])
    FOLLOW_COMMA_in_object_func1535 = frozenset([49])
    FOLLOW_object_expr_in_object_func1537 = frozenset([21, 24])
    FOLLOW_CBRACE_in_object_func1541 = frozenset([1, 80])
    FOLLOW_cache_block_in_machines1610 = frozenset([1])
    FOLLOW_dir_block_in_machines1614 = frozenset([1])
    FOLLOW_mem_block_in_machines1618 = frozenset([1])
    FOLLOW_CACHE_in_cache_block1633 = frozenset([81])
    FOLLOW_OCBRACE_in_cache_block1635 = frozenset([15, 22, 29, 57, 78, 95, 102])
    FOLLOW_declarations_in_cache_block1637 = frozenset([15, 22, 29, 57, 78, 95, 102])
    FOLLOW_CCBRACE_in_cache_block1640 = frozenset([49, 95])
    FOLLOW_objset_decl_in_cache_block1642 = frozenset([49, 95])
    FOLLOW_ID_in_cache_block1645 = frozenset([93])
    FOLLOW_SEMICOLON_in_cache_block1647 = frozenset([1])
    FOLLOW_DIR_in_dir_block1688 = frozenset([81])
    FOLLOW_OCBRACE_in_dir_block1690 = frozenset([15, 22, 29, 57, 78, 95, 102])
    FOLLOW_declarations_in_dir_block1692 = frozenset([15, 22, 29, 57, 78, 95, 102])
    FOLLOW_CCBRACE_in_dir_block1695 = frozenset([49, 95])
    FOLLOW_objset_decl_in_dir_block1697 = frozenset([49, 95])
    FOLLOW_ID_in_dir_block1700 = frozenset([93])
    FOLLOW_SEMICOLON_in_dir_block1702 = frozenset([1])
    FOLLOW_MEM_in_mem_block1743 = frozenset([81])
    FOLLOW_OCBRACE_in_mem_block1745 = frozenset([15, 22, 29, 57, 78, 95, 102])
    FOLLOW_declarations_in_mem_block1747 = frozenset([15, 22, 29, 57, 78, 95, 102])
    FOLLOW_CCBRACE_in_mem_block1750 = frozenset([49, 95])
    FOLLOW_objset_decl_in_mem_block1752 = frozenset([49, 95])
    FOLLOW_ID_in_mem_block1755 = frozenset([93])
    FOLLOW_SEMICOLON_in_mem_block1757 = frozenset([1])
    FOLLOW_SET_in_objset_decl1799 = frozenset([82])
    FOLLOW_OEBRACE_in_objset_decl1801 = frozenset([49, 56])
    FOLLOW_val_range_in_objset_decl1803 = frozenset([23])
    FOLLOW_CEBRACE_in_objset_decl1805 = frozenset([1])
    FOLLOW_NETWORK_in_network_block1831 = frozenset([81])
    FOLLOW_OCBRACE_in_network_block1833 = frozenset([22, 124, 131])
    FOLLOW_network_element_in_network_block1835 = frozenset([22, 124, 131])
    FOLLOW_CCBRACE_in_network_block1838 = frozenset([93])
    FOLLOW_SEMICOLON_in_network_block1840 = frozenset([1])
    FOLLOW_element_type_in_network_element1883 = frozenset([49])
    FOLLOW_ID_in_network_element1885 = frozenset([93])
    FOLLOW_SEMICOLON_in_network_element1887 = frozenset([1])
    FOLLOW_ID_in_network_send1908 = frozenset([35])
    FOLLOW_DOT_in_network_send1910 = frozenset([130, 143])
    FOLLOW_send_function_in_network_send1912 = frozenset([80])
    FOLLOW_OBRACE_in_network_send1914 = frozenset([49])
    FOLLOW_ID_in_network_send1916 = frozenset([21])
    FOLLOW_CBRACE_in_network_send1918 = frozenset([93])
    FOLLOW_SEMICOLON_in_network_send1920 = frozenset([1])
    FOLLOW_ID_in_network_bcast1940 = frozenset([35])
    FOLLOW_DOT_in_network_bcast1942 = frozenset([116, 135])
    FOLLOW_bcast_function_in_network_bcast1944 = frozenset([80])
    FOLLOW_OBRACE_in_network_bcast1946 = frozenset([49])
    FOLLOW_ID_in_network_bcast1948 = frozenset([21])
    FOLLOW_CBRACE_in_network_bcast1950 = frozenset([93])
    FOLLOW_SEMICOLON_in_network_bcast1952 = frozenset([1])
    FOLLOW_ID_in_network_mcast1972 = frozenset([35])
    FOLLOW_DOT_in_network_mcast1974 = frozenset([121, 141])
    FOLLOW_mcast_function_in_network_mcast1976 = frozenset([80])
    FOLLOW_OBRACE_in_network_mcast1978 = frozenset([49])
    FOLLOW_ID_in_network_mcast1980 = frozenset([24])
    FOLLOW_COMMA_in_network_mcast1982 = frozenset([49])
    FOLLOW_ID_in_network_mcast1984 = frozenset([21])
    FOLLOW_CBRACE_in_network_mcast1986 = frozenset([93])
    FOLLOW_SEMICOLON_in_network_mcast1988 = frozenset([1])
    FOLLOW_MSG_in_message_block2018 = frozenset([49])
    FOLLOW_ID_in_message_block2020 = frozenset([81])
    FOLLOW_OCBRACE_in_message_block2022 = frozenset([15, 22, 29, 57, 78, 95, 102])
    FOLLOW_declarations_in_message_block2024 = frozenset([15, 22, 29, 57, 78, 95, 102])
    FOLLOW_CCBRACE_in_message_block2027 = frozenset([93])
    FOLLOW_SEMICOLON_in_message_block2029 = frozenset([1])
    FOLLOW_ID_in_message_constr2051 = frozenset([80])
    FOLLOW_OBRACE_in_message_constr2053 = frozenset([14, 21, 24, 49, 56, 78])
    FOLLOW_message_expr_in_message_constr2055 = frozenset([14, 21, 24, 49, 56, 78])
    FOLLOW_COMMA_in_message_constr2059 = frozenset([14, 49, 56, 78])
    FOLLOW_message_expr_in_message_constr2061 = frozenset([21, 24])
    FOLLOW_CBRACE_in_message_constr2065 = frozenset([1])
    FOLLOW_object_expr_in_message_expr2087 = frozenset([1])
    FOLLOW_set_func_in_message_expr2091 = frozenset([1])
    FOLLOW_INT_in_message_expr2095 = frozenset([1])
    FOLLOW_BOOL_in_message_expr2099 = frozenset([1])
    FOLLOW_NID_in_message_expr2103 = frozenset([1])
    FOLLOW_set_func_in_set_block2121 = frozenset([93])
    FOLLOW_SEMICOLON_in_set_block2123 = frozenset([1])
    FOLLOW_ID_in_set_func2138 = frozenset([35])
    FOLLOW_DOT_in_set_func2140 = frozenset([134, 136, 138, 139, 140, 144])
    FOLLOW_set_function_types_in_set_func2142 = frozenset([80])
    FOLLOW_OBRACE_in_set_func2144 = frozenset([21, 49])
    FOLLOW_set_nest_in_set_func2146 = frozenset([21, 49])
    FOLLOW_CBRACE_in_set_func2149 = frozenset([1])
    FOLLOW_set_func_in_set_nest2187 = frozenset([1])
    FOLLOW_object_expr_in_set_nest2191 = frozenset([1])
    FOLLOW_internal_event_func_in_internal_event_block2209 = frozenset([93])
    FOLLOW_SEMICOLON_in_internal_event_block2211 = frozenset([1])
    FOLLOW_internal_event_function_in_internal_event_func2225 = frozenset([80])
    FOLLOW_OBRACE_in_internal_event_func2227 = frozenset([49])
    FOLLOW_ID_in_internal_event_func2229 = frozenset([21])
    FOLLOW_CBRACE_in_internal_event_func2231 = frozenset([1])
    FOLLOW_ARCH_in_arch_block2255 = frozenset([49])
    FOLLOW_ID_in_arch_block2257 = frozenset([81])
    FOLLOW_OCBRACE_in_arch_block2259 = frozenset([22, 89, 98])
    FOLLOW_arch_body_in_arch_block2261 = frozenset([22])
    FOLLOW_CCBRACE_in_arch_block2263 = frozenset([1])
    FOLLOW_stable_def_in_arch_body2285 = frozenset([1, 89, 98])
    FOLLOW_process_block_in_arch_body2289 = frozenset([1, 89, 98])
    FOLLOW_STABLE_in_stable_def2299 = frozenset([81])
    FOLLOW_OCBRACE_in_stable_def2301 = frozenset([49])
    FOLLOW_ID_in_stable_def2303 = frozenset([22, 24])
    FOLLOW_COMMA_in_stable_def2306 = frozenset([49])
    FOLLOW_ID_in_stable_def2308 = frozenset([22, 24])
    FOLLOW_CCBRACE_in_stable_def2312 = frozenset([1])
    FOLLOW_PROC_in_process_block2331 = frozenset([80])
    FOLLOW_process_trans_in_process_block2333 = frozenset([81])
    FOLLOW_OCBRACE_in_process_block2335 = frozenset([4, 11, 22, 49, 51, 100, 102, 104, 119])
    FOLLOW_process_expr_in_process_block2337 = frozenset([4, 11, 22, 49, 51, 100, 102, 104, 119])
    FOLLOW_CCBRACE_in_process_block2340 = frozenset([1])
    FOLLOW_OBRACE_in_process_trans2366 = frozenset([49])
    FOLLOW_ID_in_process_trans2368 = frozenset([24])
    FOLLOW_COMMA_in_process_trans2370 = frozenset([4, 45, 49])
    FOLLOW_process_events_in_process_trans2372 = frozenset([21, 24])
    FOLLOW_process_finalstate_in_process_trans2374 = frozenset([21, 24])
    FOLLOW_CBRACE_in_process_trans2377 = frozenset([1])
    FOLLOW_COMMA_in_process_finalstate2400 = frozenset([49, 102])
    FOLLOW_process_finalident_in_process_finalstate2402 = frozenset([1])
    FOLLOW_expressions_in_process_expr2455 = frozenset([1])
    FOLLOW_network_send_in_process_expr2459 = frozenset([1])
    FOLLOW_network_mcast_in_process_expr2463 = frozenset([1])
    FOLLOW_network_bcast_in_process_expr2467 = frozenset([1])
    FOLLOW_transaction_in_process_expr2470 = frozenset([1])
    FOLLOW_AWAIT_in_transaction2480 = frozenset([81])
    FOLLOW_OCBRACE_in_transaction2482 = frozenset([22, 106])
    FOLLOW_trans_in_transaction2484 = frozenset([22, 106])
    FOLLOW_CCBRACE_in_transaction2487 = frozenset([1])
    FOLLOW_WHEN_in_trans2507 = frozenset([49])
    FOLLOW_ID_in_trans2509 = frozenset([32])
    FOLLOW_DDOT_in_trans2511 = frozenset([1, 4, 11, 17, 49, 51, 76, 100, 102, 104, 119])
    FOLLOW_trans_body_in_trans2513 = frozenset([1, 4, 11, 17, 49, 51, 76, 100, 102, 104, 119])
    FOLLOW_expressions_in_trans_body2546 = frozenset([1])
    FOLLOW_next_trans_in_trans_body2550 = frozenset([1])
    FOLLOW_next_break_in_trans_body2554 = frozenset([1])
    FOLLOW_transaction_in_trans_body2558 = frozenset([1])
    FOLLOW_network_send_in_trans_body2562 = frozenset([1])
    FOLLOW_network_mcast_in_trans_body2566 = frozenset([1])
    FOLLOW_network_bcast_in_trans_body2570 = frozenset([1])
    FOLLOW_NEXT_in_next_trans2588 = frozenset([81])
    FOLLOW_OCBRACE_in_next_trans2590 = frozenset([22, 106])
    FOLLOW_trans_in_next_trans2592 = frozenset([22, 106])
    FOLLOW_CCBRACE_in_next_trans2595 = frozenset([1])
    FOLLOW_BREAK_in_next_break2616 = frozenset([93])
    FOLLOW_SEMICOLON_in_next_break2618 = frozenset([1])
    FOLLOW_assignment_in_expressions2634 = frozenset([1])
    FOLLOW_conditional_in_expressions2638 = frozenset([1])
    FOLLOW_object_block_in_expressions2642 = frozenset([1])
    FOLLOW_set_block_in_expressions2646 = frozenset([1])
    FOLLOW_internal_event_block_in_expressions2650 = frozenset([1])
    FOLLOW_msg_stall_in_expressions2654 = frozenset([1])
    FOLLOW_set_access_in_expressions2658 = frozenset([1])
    FOLLOW_undefine_in_expressions2662 = frozenset([1])
    FOLLOW_process_finalident_in_assignment2669 = frozenset([42])
    FOLLOW_EQUALSIGN_in_assignment2671 = frozenset([14, 49, 56, 78])
    FOLLOW_assign_types_in_assignment2673 = frozenset([93])
    FOLLOW_SEMICOLON_in_assignment2675 = frozenset([1])
    FOLLOW_object_expr_in_assign_types2697 = frozenset([1])
    FOLLOW_message_constr_in_assign_types2701 = frozenset([1])
    FOLLOW_math_op_in_assign_types2705 = frozenset([1])
    FOLLOW_set_func_in_assign_types2709 = frozenset([1])
    FOLLOW_INT_in_assign_types2713 = frozenset([1])
    FOLLOW_BOOL_in_assign_types2717 = frozenset([1])
    FOLLOW_NID_in_assign_types2721 = frozenset([1])
    FOLLOW_val_range_in_math_op2732 = frozenset([67, 83])
    FOLLOW_set_in_math_op2734 = frozenset([49, 56])
    FOLLOW_val_range_in_math_op2742 = frozenset([1])
    FOLLOW_STALL_in_msg_stall2748 = frozenset([93])
    FOLLOW_SEMICOLON_in_msg_stall2750 = frozenset([1])
    FOLLOW_ACCESS_in_set_access2762 = frozenset([93])
    FOLLOW_SEMICOLON_in_set_access2764 = frozenset([1])
    FOLLOW_UNDEF_in_undefine2778 = frozenset([49])
    FOLLOW_ID_in_undefine2780 = frozenset([93])
    FOLLOW_SEMICOLON_in_undefine2782 = frozenset([1])
    FOLLOW_if_stmt_in_conditional2799 = frozenset([1])
    FOLLOW_ifnot_stmt_in_conditional2803 = frozenset([1])
    FOLLOW_IF_in_if_stmt2822 = frozenset([14, 49, 56, 78, 80])
    FOLLOW_cond_comb_in_if_stmt2824 = frozenset([81])
    FOLLOW_OCBRACE_in_if_stmt2826 = frozenset([4, 11, 17, 22, 49, 51, 100, 102, 104, 119])
    FOLLOW_if_expression_in_if_stmt2828 = frozenset([22])
    FOLLOW_CCBRACE_in_if_stmt2830 = frozenset([1, 37])
    FOLLOW_ELSE_in_if_stmt2837 = frozenset([81])
    FOLLOW_OCBRACE_in_if_stmt2841 = frozenset([4, 11, 17, 22, 49, 51, 100, 102, 104, 119])
    FOLLOW_else_expression_in_if_stmt2843 = frozenset([22])
    FOLLOW_CCBRACE_in_if_stmt2845 = frozenset([1, 37])
    FOLLOW_IF_in_ifnot_stmt2951 = frozenset([73])
    FOLLOW_NEG_in_ifnot_stmt2953 = frozenset([14, 49, 56, 78, 80])
    FOLLOW_cond_comb_in_ifnot_stmt2955 = frozenset([81])
    FOLLOW_OCBRACE_in_ifnot_stmt2957 = frozenset([4, 11, 17, 22, 49, 51, 100, 102, 104, 119])
    FOLLOW_if_expression_in_ifnot_stmt2959 = frozenset([22])
    FOLLOW_CCBRACE_in_ifnot_stmt2961 = frozenset([1, 37])
    FOLLOW_ELSE_in_ifnot_stmt2968 = frozenset([81])
    FOLLOW_OCBRACE_in_ifnot_stmt2972 = frozenset([4, 11, 17, 22, 49, 51, 100, 102, 104, 119])
    FOLLOW_else_expression_in_ifnot_stmt2974 = frozenset([22])
    FOLLOW_CCBRACE_in_ifnot_stmt2976 = frozenset([1, 37])
    FOLLOW_exprwbreak_in_if_expression3077 = frozenset([1, 4, 11, 17, 49, 51, 100, 102, 104, 119])
    FOLLOW_exprwbreak_in_else_expression3092 = frozenset([1, 4, 11, 17, 49, 51, 100, 102, 104, 119])
    FOLLOW_expressions_in_exprwbreak3107 = frozenset([1])
    FOLLOW_network_send_in_exprwbreak3111 = frozenset([1])
    FOLLOW_network_mcast_in_exprwbreak3115 = frozenset([1])
    FOLLOW_network_bcast_in_exprwbreak3119 = frozenset([1])
    FOLLOW_transaction_in_exprwbreak3123 = frozenset([1])
    FOLLOW_next_break_in_exprwbreak3127 = frozenset([1])
    FOLLOW_cond_rel_in_cond_comb3141 = frozenset([1, 110, 145])
    FOLLOW_combinatorial_operator_in_cond_comb3144 = frozenset([14, 49, 56, 78, 80])
    FOLLOW_cond_rel_in_cond_comb3146 = frozenset([1, 110, 145])
    FOLLOW_OBRACE_in_cond_rel3163 = frozenset([14, 49, 56, 78, 80])
    FOLLOW_cond_sel_in_cond_rel3166 = frozenset([1, 21])
    FOLLOW_CBRACE_in_cond_rel3168 = frozenset([1, 21])
    FOLLOW_cond_type_expr_in_cond_sel3192 = frozenset([1, 109, 111, 112, 113, 114, 115])
    FOLLOW_relational_operator_in_cond_sel3195 = frozenset([14, 49, 56, 78])
    FOLLOW_cond_type_expr_in_cond_sel3197 = frozenset([1, 109, 111, 112, 113, 114, 115])
    FOLLOW_cond_types_in_cond_type_expr3217 = frozenset([1, 67, 71, 83])
    FOLLOW_set_in_cond_type_expr3220 = frozenset([14, 49, 56, 78])
    FOLLOW_cond_types_in_cond_type_expr3232 = frozenset([1, 67, 71, 83])
    FOLLOW_object_expr_in_cond_types3253 = frozenset([1])
    FOLLOW_set_func_in_cond_types3257 = frozenset([1])
    FOLLOW_INT_in_cond_types3261 = frozenset([1])
    FOLLOW_BOOL_in_cond_types3265 = frozenset([1])
    FOLLOW_NID_in_cond_types3269 = frozenset([1])
    FOLLOW_policy_op_type_in_policy_op3301 = frozenset([1, 145])
    FOLLOW_145_in_policy_op3304 = frozenset([123, 127, 128, 132])
    FOLLOW_policy_op_type_in_policy_op3306 = frozenset([1, 145])
    FOLLOW_133_in_policy_op3323 = frozenset([1])
    FOLLOW_policy_data_type_in_policy_data3401 = frozenset([1, 145])
    FOLLOW_145_in_policy_data3404 = frozenset([117, 118, 122, 123, 125])
    FOLLOW_policy_data_type_in_policy_data3406 = frozenset([1, 145])
    FOLLOW_133_in_policy_data3423 = frozenset([1])
    FOLLOW_policy_coh_type_in_policy_coh3493 = frozenset([1, 145])
    FOLLOW_145_in_policy_coh3496 = frozenset([137, 142])
    FOLLOW_policy_coh_type_in_policy_coh3498 = frozenset([1, 145])
    FOLLOW_133_in_policy_coh3515 = frozenset([1])
    FOLLOW_ID_in_label_state3572 = frozenset([80])
    FOLLOW_OBRACE_in_label_state3574 = frozenset([123, 127, 128, 132, 133])
    FOLLOW_policy_op_in_label_state3576 = frozenset([24])
    FOLLOW_COMMA_in_label_state3578 = frozenset([117, 118, 122, 123, 125, 133])
    FOLLOW_policy_data_in_label_state3580 = frozenset([24])
    FOLLOW_COMMA_in_label_state3582 = frozenset([133, 137, 142])
    FOLLOW_policy_coh_in_label_state3584 = frozenset([21])
    FOLLOW_CBRACE_in_label_state3586 = frozenset([1])
    FOLLOW_ID_in_label_message3610 = frozenset([80])
    FOLLOW_OBRACE_in_label_message3612 = frozenset([123, 127, 128, 132, 133])
    FOLLOW_policy_op_in_label_message3614 = frozenset([24])
    FOLLOW_COMMA_in_label_message3616 = frozenset([117, 118, 122, 123, 125, 133])
    FOLLOW_policy_data_in_label_message3618 = frozenset([24])
    FOLLOW_COMMA_in_label_message3620 = frozenset([133, 137, 142])
    FOLLOW_policy_coh_in_label_message3622 = frozenset([21])
    FOLLOW_CBRACE_in_label_message3624 = frozenset([1])
    FOLLOW_DATA_in_data_rule3648 = frozenset([80])
    FOLLOW_OBRACE_in_data_rule3650 = frozenset([49])
    FOLLOW_label_state_in_data_rule3652 = frozenset([21])
    FOLLOW_CBRACE_in_data_rule3654 = frozenset([93])
    FOLLOW_SEMICOLON_in_data_rule3656 = frozenset([1])
    FOLLOW_120_in_local_rule3673 = frozenset([80])
    FOLLOW_OBRACE_in_local_rule3675 = frozenset([49])
    FOLLOW_label_state_in_local_rule3677 = frozenset([24])
    FOLLOW_COMMA_in_local_rule3679 = frozenset([49])
    FOLLOW_label_message_in_local_rule3681 = frozenset([24])
    FOLLOW_COMMA_in_local_rule3683 = frozenset([49])
    FOLLOW_label_state_in_local_rule3685 = frozenset([21])
    FOLLOW_CBRACE_in_local_rule3687 = frozenset([93])
    FOLLOW_SEMICOLON_in_local_rule3689 = frozenset([1])
    FOLLOW_129_in_rule3710 = frozenset([80])
    FOLLOW_OBRACE_in_rule3712 = frozenset([49])
    FOLLOW_label_state_in_rule3714 = frozenset([24])
    FOLLOW_COMMA_in_rule3716 = frozenset([49])
    FOLLOW_label_message_in_rule3718 = frozenset([24])
    FOLLOW_COMMA_in_rule3720 = frozenset([49])
    FOLLOW_label_state_in_rule3722 = frozenset([21])
    FOLLOW_CBRACE_in_rule3724 = frozenset([93])
    FOLLOW_SEMICOLON_in_rule3726 = frozenset([1])
    FOLLOW_data_rule_in_policy_rule3748 = frozenset([1])
    FOLLOW_local_rule_in_policy_rule3752 = frozenset([1])
    FOLLOW_rule_in_policy_rule3756 = frozenset([1])
    FOLLOW_126_in_policy_block3763 = frozenset([49])
    FOLLOW_ID_in_policy_block3765 = frozenset([81])
    FOLLOW_OCBRACE_in_policy_block3767 = frozenset([22, 29, 120, 129])
    FOLLOW_policy_rule_in_policy_block3769 = frozenset([22, 29, 120, 129])
    FOLLOW_CCBRACE_in_policy_block3772 = frozenset([1])
    FOLLOW_policy_block_in_policy_file3790 = frozenset([1, 126])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("ProtoCCLexer", ProtoCCParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
