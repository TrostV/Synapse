# $ANTLR 3.5.3 ProtoCC.g 2026-11-18 17:36:23

import sys
from antlr3 import *

from antlr3.tree import *




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

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ACCESS", "ACCESS_", "ARCH", "ARCH_", "ARRAY", "ARRAY_", "ASSIGN_", 
    "AWAIT", "AWAIT_", "BCAST_", "BOOL", "BOOLID", "BOOL_", "BREAK", "BREAK_", 
    "CACHE", "CACHE_", "CBRACE", "CCBRACE", "CEBRACE", "COMMA", "COMMENT", 
    "COND_", "CONSTANT", "CONSTANT_", "DATA", "DATA_", "DATA_RULE_", "DDOT", 
    "DIR", "DIR_", "DOT", "ELEMENT_", "ELSE", "ENDIFELSE_", "ENDIF_", "ENDPROC_", 
    "ENDWHEN_", "EQUALSIGN", "EVENT_", "EVENT_ACK_", "EVICT", "FIFO", "FIFO_", 
    "FUNCTION_CALL_", "GUARD_", "ID", "ID_", "IF", "IFELSE_", "IF_", "INITSTATE_", 
    "INITVAL_", "INT", "INTID", "INT_", "LABEL_MESSAGE_", "LABEL_STATE_", 
    "LINE_COMMENT", "LOCAL_RULE_", "MACHN_", "MCAST_", "MEM", "MEM_", "MINUS", 
    "MSG", "MSGCSTR_", "MSG_", "MULT", "NCOND_", "NEG", "NETWORK", "NETWORK_", 
    "NEXT", "NEXT_", "NID", "OBJSET_", "OBRACE", "OCBRACE", "OEBRACE", "PLUS", 
    "POLICY_", "POLICY_ACTION_", "POLICY_COH_", "POLICY_DATA_", "POLICY_OP_", 
    "POL_FILE_", "PROC", "PROC_", "RANGE_", "RULE_", "SEMICOLON", "SEND_", 
    "SET", "SETFUNC_", "SET_", "STABLE", "STABLE_", "STALL", "STALL_", "STATE", 
    "TRANS_", "UNDEF", "UNDEF_", "WHEN", "WHEN_", "WS", "'!='", "'&'", "'<'", 
    "'<='", "'=='", "'>'", "'>='", "'Bcast'", "'Clean'", "'Dirty'", "'Event'", 
    "'Local'", "'Mcast'", "'NP'", "'None'", "'Ordered'", "'P'", "'Policy'", 
    "'Rd'", "'RdWr'", "'Rule'", "'Send'", "'Unordered'", "'Wr'", "'_'", 
    "'action'", "'add'", "'bcast'", "'clear'", "'coh'", "'contains'", "'count'", 
    "'del'", "'mcast'", "'nco'", "'send'", "'smallest'", "'|'"
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
    # ProtoCC.g:142:1: send_function : ( 'send' | 'Send' );
    def send_function(self, ):
        retval = self.send_function_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set1 = None

        set1_tree = None

        try:
            try:
                # ProtoCC.g:143:2: ( 'send' | 'Send' )
                # ProtoCC.g:
                pass 
                root_0 = self._adaptor.nil()


                set1 = self.input.LT(1)

                if self.input.LA(1) in {132, 146}:
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
    # ProtoCC.g:147:1: mcast_function : ( 'mcast' | 'Mcast' );
    def mcast_function(self, ):
        retval = self.mcast_function_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set2 = None

        set2_tree = None

        try:
            try:
                # ProtoCC.g:148:2: ( 'mcast' | 'Mcast' )
                # ProtoCC.g:
                pass 
                root_0 = self._adaptor.nil()


                set2 = self.input.LT(1)

                if self.input.LA(1) in {123, 144}:
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
    # ProtoCC.g:152:1: bcast_function : ( 'bcast' | 'Bcast' );
    def bcast_function(self, ):
        retval = self.bcast_function_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set3 = None

        set3_tree = None

        try:
            try:
                # ProtoCC.g:153:2: ( 'bcast' | 'Bcast' )
                # ProtoCC.g:
                pass 
                root_0 = self._adaptor.nil()


                set3 = self.input.LT(1)

                if self.input.LA(1) in {118, 138}:
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
    # ProtoCC.g:157:1: internal_event_function : 'Event' ;
    def internal_event_function(self, ):
        retval = self.internal_event_function_return()
        retval.start = self.input.LT(1)


        root_0 = None

        string_literal4 = None

        string_literal4_tree = None

        try:
            try:
                # ProtoCC.g:158:2: ( 'Event' )
                # ProtoCC.g:158:4: 'Event'
                pass 
                root_0 = self._adaptor.nil()


                string_literal4 = self.match(self.input, 121, self.FOLLOW_121_in_internal_event_function757)
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
    # ProtoCC.g:161:1: set_function_types : ( 'add' | 'count' | 'contains' | 'del' | 'clear' | 'smallest' );
    def set_function_types(self, ):
        retval = self.set_function_types_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set5 = None

        set5_tree = None

        try:
            try:
                # ProtoCC.g:162:2: ( 'add' | 'count' | 'contains' | 'del' | 'clear' | 'smallest' )
                # ProtoCC.g:
                pass 
                root_0 = self._adaptor.nil()


                set5 = self.input.LT(1)

                if self.input.LA(1) in {137, 139, 141, 142, 143, 147}:
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
    # ProtoCC.g:170:1: relational_operator : ( '==' | '!=' | '<=' | '>=' | '<' | '>' );
    def relational_operator(self, ):
        retval = self.relational_operator_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set6 = None

        set6_tree = None

        try:
            try:
                # ProtoCC.g:171:2: ( '==' | '!=' | '<=' | '>=' | '<' | '>' )
                # ProtoCC.g:
                pass 
                root_0 = self._adaptor.nil()


                set6 = self.input.LT(1)

                if (113 <= self.input.LA(1) <= 117) or self.input.LA(1) in {111}:
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
    # ProtoCC.g:179:1: combinatorial_operator : ( '&' | '|' );
    def combinatorial_operator(self, ):
        retval = self.combinatorial_operator_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set7 = None

        set7_tree = None

        try:
            try:
                # ProtoCC.g:180:5: ( '&' | '|' )
                # ProtoCC.g:
                pass 
                root_0 = self._adaptor.nil()


                set7 = self.input.LT(1)

                if self.input.LA(1) in {112, 148}:
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
    # ProtoCC.g:210:1: document : ( ( const_decl | init_hw | arch_block | expressions )* | policy_file );
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
                # ProtoCC.g:211:2: ( ( const_decl | init_hw | arch_block | expressions )* | policy_file )
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if (LA2_0 in {EOF, ACCESS, ARCH, CACHE, CONSTANT, DIR, ID, IF, MEM, MSG, NETWORK, STALL, STATE, UNDEF, 121}) :
                    alt2 = 1
                elif (LA2_0 == 128) :
                    alt2 = 2
                else:
                    nvae = NoViableAltException("", 2, 0, self.input)

                    raise nvae


                if alt2 == 1:
                    # ProtoCC.g:211:4: ( const_decl | init_hw | arch_block | expressions )*
                    pass 
                    root_0 = self._adaptor.nil()


                    # ProtoCC.g:211:4: ( const_decl | init_hw | arch_block | expressions )*
                    while True: #loop1
                        alt1 = 5
                        LA1 = self.input.LA(1)
                        if LA1 in {CONSTANT}:
                            alt1 = 1
                        elif LA1 in {CACHE, DIR, MEM, MSG, NETWORK}:
                            alt1 = 2
                        elif LA1 in {ARCH}:
                            alt1 = 3
                        elif LA1 in {ACCESS, ID, IF, STALL, STATE, UNDEF, 121}:
                            alt1 = 4

                        if alt1 == 1:
                            # ProtoCC.g:211:5: const_decl
                            pass 
                            self._state.following.append(self.FOLLOW_const_decl_in_document1085)
                            const_decl8 = self.const_decl()

                            self._state.following.pop()
                            self._adaptor.addChild(root_0, const_decl8.tree)



                        elif alt1 == 2:
                            # ProtoCC.g:211:18: init_hw
                            pass 
                            self._state.following.append(self.FOLLOW_init_hw_in_document1089)
                            init_hw9 = self.init_hw()

                            self._state.following.pop()
                            self._adaptor.addChild(root_0, init_hw9.tree)



                        elif alt1 == 3:
                            # ProtoCC.g:211:28: arch_block
                            pass 
                            self._state.following.append(self.FOLLOW_arch_block_in_document1093)
                            arch_block10 = self.arch_block()

                            self._state.following.pop()
                            self._adaptor.addChild(root_0, arch_block10.tree)



                        elif alt1 == 4:
                            # ProtoCC.g:211:41: expressions
                            pass 
                            self._state.following.append(self.FOLLOW_expressions_in_document1097)
                            expressions11 = self.expressions()

                            self._state.following.pop()
                            self._adaptor.addChild(root_0, expressions11.tree)



                        else:
                            break #loop1



                elif alt2 == 2:
                    # ProtoCC.g:212:4: policy_file
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_policy_file_in_document1105)
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
    # ProtoCC.g:216:1: declarations : ( int_decl | bool_decl | state_decl | data_decl | id_decl );
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
                # ProtoCC.g:216:14: ( int_decl | bool_decl | state_decl | data_decl | id_decl )
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
                    # ProtoCC.g:216:16: int_decl
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_int_decl_in_declarations1116)
                    int_decl13 = self.int_decl()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, int_decl13.tree)



                elif alt3 == 2:
                    # ProtoCC.g:216:27: bool_decl
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_bool_decl_in_declarations1120)
                    bool_decl14 = self.bool_decl()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, bool_decl14.tree)



                elif alt3 == 3:
                    # ProtoCC.g:216:39: state_decl
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_state_decl_in_declarations1124)
                    state_decl15 = self.state_decl()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, state_decl15.tree)



                elif alt3 == 4:
                    # ProtoCC.g:216:52: data_decl
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_data_decl_in_declarations1128)
                    data_decl16 = self.data_decl()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, data_decl16.tree)



                elif alt3 == 5:
                    # ProtoCC.g:216:64: id_decl
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_id_decl_in_declarations1132)
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
    # ProtoCC.g:218:5: const_decl : CONSTANT ID INT -> ^( CONSTANT_ ID INT ) ;
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
                # ProtoCC.g:218:16: ( CONSTANT ID INT -> ^( CONSTANT_ ID INT ) )
                # ProtoCC.g:218:18: CONSTANT ID INT
                pass 
                CONSTANT18 = self.match(self.input, CONSTANT, self.FOLLOW_CONSTANT_in_const_decl1144) 
                stream_CONSTANT.add(CONSTANT18)


                ID19 = self.match(self.input, ID, self.FOLLOW_ID_in_const_decl1146) 
                stream_ID.add(ID19)


                INT20 = self.match(self.input, INT, self.FOLLOW_INT_in_const_decl1148) 
                stream_INT.add(INT20)


                # AST Rewrite
                # elements: INT, ID
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
                # 218:34: -> ^( CONSTANT_ ID INT )
                # ProtoCC.g:218:37: ^( CONSTANT_ ID INT )
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
    # ProtoCC.g:220:5: int_decl : INTID range ID ( EQUALSIGN INT )* SEMICOLON -> ^( INT_ ID range ( ^( INITVAL_ INT ) )* ) ;
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
                # ProtoCC.g:220:14: ( INTID range ID ( EQUALSIGN INT )* SEMICOLON -> ^( INT_ ID range ( ^( INITVAL_ INT ) )* ) )
                # ProtoCC.g:220:16: INTID range ID ( EQUALSIGN INT )* SEMICOLON
                pass 
                INTID21 = self.match(self.input, INTID, self.FOLLOW_INTID_in_int_decl1170) 
                stream_INTID.add(INTID21)


                self._state.following.append(self.FOLLOW_range_in_int_decl1172)
                range22 = self.range()

                self._state.following.pop()
                stream_range.add(range22.tree)


                ID23 = self.match(self.input, ID, self.FOLLOW_ID_in_int_decl1174) 
                stream_ID.add(ID23)


                # ProtoCC.g:220:31: ( EQUALSIGN INT )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == EQUALSIGN) :
                        alt4 = 1


                    if alt4 == 1:
                        # ProtoCC.g:220:32: EQUALSIGN INT
                        pass 
                        EQUALSIGN24 = self.match(self.input, EQUALSIGN, self.FOLLOW_EQUALSIGN_in_int_decl1177) 
                        stream_EQUALSIGN.add(EQUALSIGN24)


                        INT25 = self.match(self.input, INT, self.FOLLOW_INT_in_int_decl1179) 
                        stream_INT.add(INT25)



                    else:
                        break #loop4


                SEMICOLON26 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_int_decl1183) 
                stream_SEMICOLON.add(SEMICOLON26)


                # AST Rewrite
                # elements: range, ID, INT
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
                # 220:58: -> ^( INT_ ID range ( ^( INITVAL_ INT ) )* )
                # ProtoCC.g:220:61: ^( INT_ ID range ( ^( INITVAL_ INT ) )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(INT_, "INT_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_1, stream_range.nextTree())

                # ProtoCC.g:220:77: ( ^( INITVAL_ INT ) )*
                while stream_INT.hasNext():
                    # ProtoCC.g:220:77: ^( INITVAL_ INT )
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
    # ProtoCC.g:221:5: bool_decl : BOOLID ID ( EQUALSIGN BOOL )* SEMICOLON -> ^( BOOL_ ID ( ^( INITVAL_ BOOL ) )* ) ;
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
                # ProtoCC.g:221:15: ( BOOLID ID ( EQUALSIGN BOOL )* SEMICOLON -> ^( BOOL_ ID ( ^( INITVAL_ BOOL ) )* ) )
                # ProtoCC.g:221:17: BOOLID ID ( EQUALSIGN BOOL )* SEMICOLON
                pass 
                BOOLID27 = self.match(self.input, BOOLID, self.FOLLOW_BOOLID_in_bool_decl1211) 
                stream_BOOLID.add(BOOLID27)


                ID28 = self.match(self.input, ID, self.FOLLOW_ID_in_bool_decl1213) 
                stream_ID.add(ID28)


                # ProtoCC.g:221:27: ( EQUALSIGN BOOL )*
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == EQUALSIGN) :
                        alt5 = 1


                    if alt5 == 1:
                        # ProtoCC.g:221:28: EQUALSIGN BOOL
                        pass 
                        EQUALSIGN29 = self.match(self.input, EQUALSIGN, self.FOLLOW_EQUALSIGN_in_bool_decl1216) 
                        stream_EQUALSIGN.add(EQUALSIGN29)


                        BOOL30 = self.match(self.input, BOOL, self.FOLLOW_BOOL_in_bool_decl1218) 
                        stream_BOOL.add(BOOL30)



                    else:
                        break #loop5


                SEMICOLON31 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_bool_decl1222) 
                stream_SEMICOLON.add(SEMICOLON31)


                # AST Rewrite
                # elements: BOOL, ID
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
                # 221:55: -> ^( BOOL_ ID ( ^( INITVAL_ BOOL ) )* )
                # ProtoCC.g:221:58: ^( BOOL_ ID ( ^( INITVAL_ BOOL ) )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(BOOL_, "BOOL_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # ProtoCC.g:221:69: ( ^( INITVAL_ BOOL ) )*
                while stream_BOOL.hasNext():
                    # ProtoCC.g:221:69: ^( INITVAL_ BOOL )
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
    # ProtoCC.g:223:5: state_decl : STATE ID SEMICOLON -> ^( INITSTATE_ ID ) ;
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
                # ProtoCC.g:223:16: ( STATE ID SEMICOLON -> ^( INITSTATE_ ID ) )
                # ProtoCC.g:223:18: STATE ID SEMICOLON
                pass 
                STATE32 = self.match(self.input, STATE, self.FOLLOW_STATE_in_state_decl1249) 
                stream_STATE.add(STATE32)


                ID33 = self.match(self.input, ID, self.FOLLOW_ID_in_state_decl1251) 
                stream_ID.add(ID33)


                SEMICOLON34 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_state_decl1253) 
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
                # 223:37: -> ^( INITSTATE_ ID )
                # ProtoCC.g:223:40: ^( INITSTATE_ ID )
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
    # ProtoCC.g:224:5: data_decl : DATA ID SEMICOLON -> ^( DATA_ ID ) ;
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
                # ProtoCC.g:224:15: ( DATA ID SEMICOLON -> ^( DATA_ ID ) )
                # ProtoCC.g:224:17: DATA ID SEMICOLON
                pass 
                DATA35 = self.match(self.input, DATA, self.FOLLOW_DATA_in_data_decl1272) 
                stream_DATA.add(DATA35)


                ID36 = self.match(self.input, ID, self.FOLLOW_ID_in_data_decl1274) 
                stream_ID.add(ID36)


                SEMICOLON37 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_data_decl1276) 
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
                # 224:35: -> ^( DATA_ ID )
                # ProtoCC.g:224:38: ^( DATA_ ID )
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
    # ProtoCC.g:225:5: id_decl : ( set_decl )* NID ID ( EQUALSIGN ( set_decl )* ID )* SEMICOLON -> ^( ID_ ID ( set_decl )* ( ^( INITVAL_ ( set_decl )* ID ) )* ) ;
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
                # ProtoCC.g:225:13: ( ( set_decl )* NID ID ( EQUALSIGN ( set_decl )* ID )* SEMICOLON -> ^( ID_ ID ( set_decl )* ( ^( INITVAL_ ( set_decl )* ID ) )* ) )
                # ProtoCC.g:225:15: ( set_decl )* NID ID ( EQUALSIGN ( set_decl )* ID )* SEMICOLON
                pass 
                # ProtoCC.g:225:15: ( set_decl )*
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == SET) :
                        alt6 = 1


                    if alt6 == 1:
                        # ProtoCC.g:225:15: set_decl
                        pass 
                        self._state.following.append(self.FOLLOW_set_decl_in_id_decl1295)
                        set_decl38 = self.set_decl()

                        self._state.following.pop()
                        stream_set_decl.add(set_decl38.tree)



                    else:
                        break #loop6


                NID39 = self.match(self.input, NID, self.FOLLOW_NID_in_id_decl1298) 
                stream_NID.add(NID39)


                ID40 = self.match(self.input, ID, self.FOLLOW_ID_in_id_decl1300) 
                stream_ID.add(ID40)


                # ProtoCC.g:225:32: ( EQUALSIGN ( set_decl )* ID )*
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == EQUALSIGN) :
                        alt8 = 1


                    if alt8 == 1:
                        # ProtoCC.g:225:33: EQUALSIGN ( set_decl )* ID
                        pass 
                        EQUALSIGN41 = self.match(self.input, EQUALSIGN, self.FOLLOW_EQUALSIGN_in_id_decl1303) 
                        stream_EQUALSIGN.add(EQUALSIGN41)


                        # ProtoCC.g:225:43: ( set_decl )*
                        while True: #loop7
                            alt7 = 2
                            LA7_0 = self.input.LA(1)

                            if (LA7_0 == SET) :
                                alt7 = 1


                            if alt7 == 1:
                                # ProtoCC.g:225:43: set_decl
                                pass 
                                self._state.following.append(self.FOLLOW_set_decl_in_id_decl1305)
                                set_decl42 = self.set_decl()

                                self._state.following.pop()
                                stream_set_decl.add(set_decl42.tree)



                            else:
                                break #loop7


                        ID43 = self.match(self.input, ID, self.FOLLOW_ID_in_id_decl1308) 
                        stream_ID.add(ID43)



                    else:
                        break #loop8


                SEMICOLON44 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_id_decl1312) 
                stream_SEMICOLON.add(SEMICOLON44)


                # AST Rewrite
                # elements: ID, set_decl, set_decl, ID
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
                # 225:68: -> ^( ID_ ID ( set_decl )* ( ^( INITVAL_ ( set_decl )* ID ) )* )
                # ProtoCC.g:225:71: ^( ID_ ID ( set_decl )* ( ^( INITVAL_ ( set_decl )* ID ) )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(ID_, "ID_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # ProtoCC.g:225:80: ( set_decl )*
                while stream_set_decl.hasNext():
                    self._adaptor.addChild(root_1, stream_set_decl.nextTree())


                stream_set_decl.reset();

                # ProtoCC.g:225:90: ( ^( INITVAL_ ( set_decl )* ID ) )*
                while stream_ID.hasNext():
                    # ProtoCC.g:225:90: ^( INITVAL_ ( set_decl )* ID )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(INITVAL_, "INITVAL_")
                    , root_2)

                    # ProtoCC.g:225:101: ( set_decl )*
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
    # ProtoCC.g:227:9: set_decl : SET OEBRACE val_range CEBRACE -> ^( SET_ val_range ) ;
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
                # ProtoCC.g:227:18: ( SET OEBRACE val_range CEBRACE -> ^( SET_ val_range ) )
                # ProtoCC.g:227:20: SET OEBRACE val_range CEBRACE
                pass 
                SET45 = self.match(self.input, SET, self.FOLLOW_SET_in_set_decl1349) 
                stream_SET.add(SET45)


                OEBRACE46 = self.match(self.input, OEBRACE, self.FOLLOW_OEBRACE_in_set_decl1351) 
                stream_OEBRACE.add(OEBRACE46)


                self._state.following.append(self.FOLLOW_val_range_in_set_decl1353)
                val_range47 = self.val_range()

                self._state.following.pop()
                stream_val_range.add(val_range47.tree)


                CEBRACE48 = self.match(self.input, CEBRACE, self.FOLLOW_CEBRACE_in_set_decl1355) 
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
                # 227:50: -> ^( SET_ val_range )
                # ProtoCC.g:227:53: ^( SET_ val_range )
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
    # ProtoCC.g:228:9: range : OEBRACE val_range DOT DOT val_range CEBRACE -> ^( RANGE_ OEBRACE val_range DOT DOT val_range CEBRACE ) ;
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
                # ProtoCC.g:228:15: ( OEBRACE val_range DOT DOT val_range CEBRACE -> ^( RANGE_ OEBRACE val_range DOT DOT val_range CEBRACE ) )
                # ProtoCC.g:228:17: OEBRACE val_range DOT DOT val_range CEBRACE
                pass 
                OEBRACE49 = self.match(self.input, OEBRACE, self.FOLLOW_OEBRACE_in_range1378) 
                stream_OEBRACE.add(OEBRACE49)


                self._state.following.append(self.FOLLOW_val_range_in_range1380)
                val_range50 = self.val_range()

                self._state.following.pop()
                stream_val_range.add(val_range50.tree)


                DOT51 = self.match(self.input, DOT, self.FOLLOW_DOT_in_range1382) 
                stream_DOT.add(DOT51)


                DOT52 = self.match(self.input, DOT, self.FOLLOW_DOT_in_range1384) 
                stream_DOT.add(DOT52)


                self._state.following.append(self.FOLLOW_val_range_in_range1386)
                val_range53 = self.val_range()

                self._state.following.pop()
                stream_val_range.add(val_range53.tree)


                CEBRACE54 = self.match(self.input, CEBRACE, self.FOLLOW_CEBRACE_in_range1388) 
                stream_CEBRACE.add(CEBRACE54)


                # AST Rewrite
                # elements: val_range, DOT, DOT, CEBRACE, OEBRACE, val_range
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
                # 228:61: -> ^( RANGE_ OEBRACE val_range DOT DOT val_range CEBRACE )
                # ProtoCC.g:228:64: ^( RANGE_ OEBRACE val_range DOT DOT val_range CEBRACE )
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
    # ProtoCC.g:229:9: val_range : ( INT | ID );
    def val_range(self, ):
        retval = self.val_range_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set55 = None

        set55_tree = None

        try:
            try:
                # ProtoCC.g:229:19: ( INT | ID )
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
    # ProtoCC.g:231:5: array_decl : ARRAY range ;
    def array_decl(self, ):
        retval = self.array_decl_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ARRAY56 = None
        range57 = None

        ARRAY56_tree = None

        try:
            try:
                # ProtoCC.g:231:16: ( ARRAY range )
                # ProtoCC.g:231:18: ARRAY range
                pass 
                root_0 = self._adaptor.nil()


                ARRAY56 = self.match(self.input, ARRAY, self.FOLLOW_ARRAY_in_array_decl1437)
                ARRAY56_tree = self._adaptor.createWithPayload(ARRAY56)
                self._adaptor.addChild(root_0, ARRAY56_tree)



                self._state.following.append(self.FOLLOW_range_in_array_decl1439)
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
    # ProtoCC.g:232:5: fifo_decl : FIFO range ;
    def fifo_decl(self, ):
        retval = self.fifo_decl_return()
        retval.start = self.input.LT(1)


        root_0 = None

        FIFO58 = None
        range59 = None

        FIFO58_tree = None

        try:
            try:
                # ProtoCC.g:232:14: ( FIFO range )
                # ProtoCC.g:232:16: FIFO range
                pass 
                root_0 = self._adaptor.nil()


                FIFO58 = self.match(self.input, FIFO, self.FOLLOW_FIFO_in_fifo_decl1449)
                FIFO58_tree = self._adaptor.createWithPayload(FIFO58)
                self._adaptor.addChild(root_0, FIFO58_tree)



                self._state.following.append(self.FOLLOW_range_in_fifo_decl1451)
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
    # ProtoCC.g:235:1: init_hw : ( network_block | machines | message_block );
    def init_hw(self, ):
        retval = self.init_hw_return()
        retval.start = self.input.LT(1)


        root_0 = None

        network_block60 = None
        machines61 = None
        message_block62 = None


        try:
            try:
                # ProtoCC.g:235:9: ( network_block | machines | message_block )
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
                    # ProtoCC.g:235:11: network_block
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_network_block_in_init_hw1461)
                    network_block60 = self.network_block()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, network_block60.tree)



                elif alt9 == 2:
                    # ProtoCC.g:235:27: machines
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_machines_in_init_hw1465)
                    machines61 = self.machines()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, machines61.tree)



                elif alt9 == 3:
                    # ProtoCC.g:235:38: message_block
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_message_block_in_init_hw1469)
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
    # ProtoCC.g:236:5: object_block : object_expr SEMICOLON -> object_expr ;
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
                # ProtoCC.g:236:18: ( object_expr SEMICOLON -> object_expr )
                # ProtoCC.g:236:20: object_expr SEMICOLON
                pass 
                self._state.following.append(self.FOLLOW_object_expr_in_object_block1480)
                object_expr63 = self.object_expr()

                self._state.following.pop()
                stream_object_expr.add(object_expr63.tree)


                SEMICOLON64 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_object_block1482) 
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
                # 236:42: -> object_expr
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
    # ProtoCC.g:237:5: object_expr : ( object_id | object_func );
    def object_expr(self, ):
        retval = self.object_expr_return()
        retval.start = self.input.LT(1)


        root_0 = None

        object_id65 = None
        object_func66 = None


        try:
            try:
                # ProtoCC.g:237:17: ( object_id | object_func )
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (LA10_0 == ID) :
                    LA10_1 = self.input.LA(2)

                    if (LA10_1 == DOT) :
                        alt10 = 2
                    elif ((111 <= LA10_1 <= 117) or LA10_1 in {BOOL, CBRACE, COMMA, ID, INT, MINUS, MULT, NID, OCBRACE, PLUS, SEMICOLON, 148}) :
                        alt10 = 1
                    else:
                        nvae = NoViableAltException("", 10, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 10, 0, self.input)

                    raise nvae


                if alt10 == 1:
                    # ProtoCC.g:237:19: object_id
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_object_id_in_object_expr1497)
                    object_id65 = self.object_id()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, object_id65.tree)



                elif alt10 == 2:
                    # ProtoCC.g:237:31: object_func
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_object_func_in_object_expr1501)
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
    # ProtoCC.g:238:5: object_id : ID -> ^( ID ) ;
    def object_id(self, ):
        retval = self.object_id_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID67 = None

        ID67_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # ProtoCC.g:238:14: ( ID -> ^( ID ) )
                # ProtoCC.g:238:17: ID
                pass 
                ID67 = self.match(self.input, ID, self.FOLLOW_ID_in_object_id1512) 
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
                # 238:20: -> ^( ID )
                # ProtoCC.g:238:23: ^( ID )
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
    # ProtoCC.g:239:5: object_func : ID DOT object_idres ( OBRACE ( object_expr )* ( COMMA object_expr )* CBRACE )* -> ^( ID DOT object_idres ( OBRACE ( object_expr )* ( COMMA object_expr )* CBRACE )* ) ;
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
                # ProtoCC.g:239:17: ( ID DOT object_idres ( OBRACE ( object_expr )* ( COMMA object_expr )* CBRACE )* -> ^( ID DOT object_idres ( OBRACE ( object_expr )* ( COMMA object_expr )* CBRACE )* ) )
                # ProtoCC.g:239:19: ID DOT object_idres ( OBRACE ( object_expr )* ( COMMA object_expr )* CBRACE )*
                pass 
                ID68 = self.match(self.input, ID, self.FOLLOW_ID_in_object_func1529) 
                stream_ID.add(ID68)


                DOT69 = self.match(self.input, DOT, self.FOLLOW_DOT_in_object_func1531) 
                stream_DOT.add(DOT69)


                self._state.following.append(self.FOLLOW_object_idres_in_object_func1533)
                object_idres70 = self.object_idres()

                self._state.following.pop()
                stream_object_idres.add(object_idres70.tree)


                # ProtoCC.g:239:39: ( OBRACE ( object_expr )* ( COMMA object_expr )* CBRACE )*
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == OBRACE) :
                        alt13 = 1


                    if alt13 == 1:
                        # ProtoCC.g:239:40: OBRACE ( object_expr )* ( COMMA object_expr )* CBRACE
                        pass 
                        OBRACE71 = self.match(self.input, OBRACE, self.FOLLOW_OBRACE_in_object_func1536) 
                        stream_OBRACE.add(OBRACE71)


                        # ProtoCC.g:239:47: ( object_expr )*
                        while True: #loop11
                            alt11 = 2
                            LA11_0 = self.input.LA(1)

                            if (LA11_0 == ID) :
                                alt11 = 1


                            if alt11 == 1:
                                # ProtoCC.g:239:47: object_expr
                                pass 
                                self._state.following.append(self.FOLLOW_object_expr_in_object_func1538)
                                object_expr72 = self.object_expr()

                                self._state.following.pop()
                                stream_object_expr.add(object_expr72.tree)



                            else:
                                break #loop11


                        # ProtoCC.g:239:60: ( COMMA object_expr )*
                        while True: #loop12
                            alt12 = 2
                            LA12_0 = self.input.LA(1)

                            if (LA12_0 == COMMA) :
                                alt12 = 1


                            if alt12 == 1:
                                # ProtoCC.g:239:61: COMMA object_expr
                                pass 
                                COMMA73 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_object_func1542) 
                                stream_COMMA.add(COMMA73)


                                self._state.following.append(self.FOLLOW_object_expr_in_object_func1544)
                                object_expr74 = self.object_expr()

                                self._state.following.pop()
                                stream_object_expr.add(object_expr74.tree)



                            else:
                                break #loop12


                        CBRACE75 = self.match(self.input, CBRACE, self.FOLLOW_CBRACE_in_object_func1548) 
                        stream_CBRACE.add(CBRACE75)



                    else:
                        break #loop13


                # AST Rewrite
                # elements: COMMA, DOT, object_expr, object_idres, object_expr, ID, OBRACE, CBRACE
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
                # 239:90: -> ^( ID DOT object_idres ( OBRACE ( object_expr )* ( COMMA object_expr )* CBRACE )* )
                # ProtoCC.g:240:9: ^( ID DOT object_idres ( OBRACE ( object_expr )* ( COMMA object_expr )* CBRACE )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                stream_ID.nextNode()
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_DOT.nextNode()
                )

                self._adaptor.addChild(root_1, stream_object_idres.nextTree())

                # ProtoCC.g:240:31: ( OBRACE ( object_expr )* ( COMMA object_expr )* CBRACE )*
                while stream_OBRACE.hasNext() or stream_CBRACE.hasNext():
                    self._adaptor.addChild(root_1, 
                    stream_OBRACE.nextNode()
                    )

                    # ProtoCC.g:240:39: ( object_expr )*
                    while stream_object_expr.hasNext():
                        self._adaptor.addChild(root_1, stream_object_expr.nextTree())


                    stream_object_expr.reset();

                    # ProtoCC.g:240:52: ( COMMA object_expr )*
                    while stream_COMMA.hasNext() or stream_object_expr.hasNext():
                        self._adaptor.addChild(root_1, 
                        stream_COMMA.nextNode()
                        )

                        self._adaptor.addChild(root_1, stream_object_expr.nextTree())


                    stream_COMMA.reset();
                    stream_object_expr.reset();

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


    class function_call_block_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "function_call_block"
    # ProtoCC.g:241:5: function_call_block : function_call SEMICOLON -> function_call ;
    def function_call_block(self, ):
        retval = self.function_call_block_return()
        retval.start = self.input.LT(1)


        root_0 = None

        SEMICOLON77 = None
        function_call76 = None

        SEMICOLON77_tree = None
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_function_call = RewriteRuleSubtreeStream(self._adaptor, "rule function_call")
        try:
            try:
                # ProtoCC.g:241:25: ( function_call SEMICOLON -> function_call )
                # ProtoCC.g:241:27: function_call SEMICOLON
                pass 
                self._state.following.append(self.FOLLOW_function_call_in_function_call_block1596)
                function_call76 = self.function_call()

                self._state.following.pop()
                stream_function_call.add(function_call76.tree)


                SEMICOLON77 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_function_call_block1598) 
                stream_SEMICOLON.add(SEMICOLON77)


                # AST Rewrite
                # elements: function_call
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
                # 241:51: -> function_call
                self._adaptor.addChild(root_0, stream_function_call.nextTree())




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

    # $ANTLR end "function_call_block"


    class function_call_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "function_call"
    # ProtoCC.g:242:5: function_call : ID OBRACE CBRACE -> ^( FUNCTION_CALL_ ID ) ;
    def function_call(self, ):
        retval = self.function_call_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID78 = None
        OBRACE79 = None
        CBRACE80 = None

        ID78_tree = None
        OBRACE79_tree = None
        CBRACE80_tree = None
        stream_OBRACE = RewriteRuleTokenStream(self._adaptor, "token OBRACE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CBRACE = RewriteRuleTokenStream(self._adaptor, "token CBRACE")

        try:
            try:
                # ProtoCC.g:242:19: ( ID OBRACE CBRACE -> ^( FUNCTION_CALL_ ID ) )
                # ProtoCC.g:242:21: ID OBRACE CBRACE
                pass 
                ID78 = self.match(self.input, ID, self.FOLLOW_ID_in_function_call1613) 
                stream_ID.add(ID78)


                OBRACE79 = self.match(self.input, OBRACE, self.FOLLOW_OBRACE_in_function_call1615) 
                stream_OBRACE.add(OBRACE79)


                CBRACE80 = self.match(self.input, CBRACE, self.FOLLOW_CBRACE_in_function_call1617) 
                stream_CBRACE.add(CBRACE80)


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
                # 242:38: -> ^( FUNCTION_CALL_ ID )
                # ProtoCC.g:242:41: ^( FUNCTION_CALL_ ID )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(FUNCTION_CALL_, "FUNCTION_CALL_")
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

    # $ANTLR end "function_call"


    class object_idres_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "object_idres"
    # ProtoCC.g:243:5: object_idres : ( ID | NID );
    def object_idres(self, ):
        retval = self.object_idres_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set81 = None

        set81_tree = None

        try:
            try:
                # ProtoCC.g:243:17: ( ID | NID )
                # ProtoCC.g:
                pass 
                root_0 = self._adaptor.nil()


                set81 = self.input.LT(1)

                if self.input.LA(1) in {ID, NID}:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set81))

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
    # ProtoCC.g:246:5: machines : ( cache_block | dir_block | mem_block );
    def machines(self, ):
        retval = self.machines_return()
        retval.start = self.input.LT(1)


        root_0 = None

        cache_block82 = None
        dir_block83 = None
        mem_block84 = None


        try:
            try:
                # ProtoCC.g:246:14: ( cache_block | dir_block | mem_block )
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
                    # ProtoCC.g:246:16: cache_block
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_cache_block_in_machines1657)
                    cache_block82 = self.cache_block()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, cache_block82.tree)



                elif alt14 == 2:
                    # ProtoCC.g:246:30: dir_block
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_dir_block_in_machines1661)
                    dir_block83 = self.dir_block()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, dir_block83.tree)



                elif alt14 == 3:
                    # ProtoCC.g:246:42: mem_block
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_mem_block_in_machines1665)
                    mem_block84 = self.mem_block()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, mem_block84.tree)



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
    # ProtoCC.g:247:9: cache_block : CACHE OCBRACE ( declarations )* CCBRACE ( objset_decl )* ID SEMICOLON -> ^( CACHE_ ID ( objset_decl )* ( declarations )* ) ;
    def cache_block(self, ):
        retval = self.cache_block_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CACHE85 = None
        OCBRACE86 = None
        CCBRACE88 = None
        ID90 = None
        SEMICOLON91 = None
        declarations87 = None
        objset_decl89 = None

        CACHE85_tree = None
        OCBRACE86_tree = None
        CCBRACE88_tree = None
        ID90_tree = None
        SEMICOLON91_tree = None
        stream_OCBRACE = RewriteRuleTokenStream(self._adaptor, "token OCBRACE")
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CACHE = RewriteRuleTokenStream(self._adaptor, "token CACHE")
        stream_CCBRACE = RewriteRuleTokenStream(self._adaptor, "token CCBRACE")
        stream_objset_decl = RewriteRuleSubtreeStream(self._adaptor, "rule objset_decl")
        stream_declarations = RewriteRuleSubtreeStream(self._adaptor, "rule declarations")
        try:
            try:
                # ProtoCC.g:247:21: ( CACHE OCBRACE ( declarations )* CCBRACE ( objset_decl )* ID SEMICOLON -> ^( CACHE_ ID ( objset_decl )* ( declarations )* ) )
                # ProtoCC.g:247:23: CACHE OCBRACE ( declarations )* CCBRACE ( objset_decl )* ID SEMICOLON
                pass 
                CACHE85 = self.match(self.input, CACHE, self.FOLLOW_CACHE_in_cache_block1680) 
                stream_CACHE.add(CACHE85)


                OCBRACE86 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_cache_block1682) 
                stream_OCBRACE.add(OCBRACE86)


                # ProtoCC.g:247:37: ( declarations )*
                while True: #loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if (LA15_0 in {BOOLID, DATA, INTID, NID, SET, STATE}) :
                        alt15 = 1


                    if alt15 == 1:
                        # ProtoCC.g:247:37: declarations
                        pass 
                        self._state.following.append(self.FOLLOW_declarations_in_cache_block1684)
                        declarations87 = self.declarations()

                        self._state.following.pop()
                        stream_declarations.add(declarations87.tree)



                    else:
                        break #loop15


                CCBRACE88 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_cache_block1687) 
                stream_CCBRACE.add(CCBRACE88)


                # ProtoCC.g:247:59: ( objset_decl )*
                while True: #loop16
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if (LA16_0 == SET) :
                        alt16 = 1


                    if alt16 == 1:
                        # ProtoCC.g:247:59: objset_decl
                        pass 
                        self._state.following.append(self.FOLLOW_objset_decl_in_cache_block1689)
                        objset_decl89 = self.objset_decl()

                        self._state.following.pop()
                        stream_objset_decl.add(objset_decl89.tree)



                    else:
                        break #loop16


                ID90 = self.match(self.input, ID, self.FOLLOW_ID_in_cache_block1692) 
                stream_ID.add(ID90)


                SEMICOLON91 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_cache_block1694) 
                stream_SEMICOLON.add(SEMICOLON91)


                # AST Rewrite
                # elements: ID, declarations, objset_decl
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
                # 247:85: -> ^( CACHE_ ID ( objset_decl )* ( declarations )* )
                # ProtoCC.g:248:13: ^( CACHE_ ID ( objset_decl )* ( declarations )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(CACHE_, "CACHE_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # ProtoCC.g:248:25: ( objset_decl )*
                while stream_objset_decl.hasNext():
                    self._adaptor.addChild(root_1, stream_objset_decl.nextTree())


                stream_objset_decl.reset();

                # ProtoCC.g:248:38: ( declarations )*
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
    # ProtoCC.g:249:9: dir_block : DIR OCBRACE ( declarations )* CCBRACE ( objset_decl )* ID SEMICOLON -> ^( DIR_ ID ( objset_decl )* ( declarations )* ) ;
    def dir_block(self, ):
        retval = self.dir_block_return()
        retval.start = self.input.LT(1)


        root_0 = None

        DIR92 = None
        OCBRACE93 = None
        CCBRACE95 = None
        ID97 = None
        SEMICOLON98 = None
        declarations94 = None
        objset_decl96 = None

        DIR92_tree = None
        OCBRACE93_tree = None
        CCBRACE95_tree = None
        ID97_tree = None
        SEMICOLON98_tree = None
        stream_OCBRACE = RewriteRuleTokenStream(self._adaptor, "token OCBRACE")
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_DIR = RewriteRuleTokenStream(self._adaptor, "token DIR")
        stream_CCBRACE = RewriteRuleTokenStream(self._adaptor, "token CCBRACE")
        stream_objset_decl = RewriteRuleSubtreeStream(self._adaptor, "rule objset_decl")
        stream_declarations = RewriteRuleSubtreeStream(self._adaptor, "rule declarations")
        try:
            try:
                # ProtoCC.g:249:19: ( DIR OCBRACE ( declarations )* CCBRACE ( objset_decl )* ID SEMICOLON -> ^( DIR_ ID ( objset_decl )* ( declarations )* ) )
                # ProtoCC.g:249:21: DIR OCBRACE ( declarations )* CCBRACE ( objset_decl )* ID SEMICOLON
                pass 
                DIR92 = self.match(self.input, DIR, self.FOLLOW_DIR_in_dir_block1735) 
                stream_DIR.add(DIR92)


                OCBRACE93 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_dir_block1737) 
                stream_OCBRACE.add(OCBRACE93)


                # ProtoCC.g:249:33: ( declarations )*
                while True: #loop17
                    alt17 = 2
                    LA17_0 = self.input.LA(1)

                    if (LA17_0 in {BOOLID, DATA, INTID, NID, SET, STATE}) :
                        alt17 = 1


                    if alt17 == 1:
                        # ProtoCC.g:249:33: declarations
                        pass 
                        self._state.following.append(self.FOLLOW_declarations_in_dir_block1739)
                        declarations94 = self.declarations()

                        self._state.following.pop()
                        stream_declarations.add(declarations94.tree)



                    else:
                        break #loop17


                CCBRACE95 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_dir_block1742) 
                stream_CCBRACE.add(CCBRACE95)


                # ProtoCC.g:249:55: ( objset_decl )*
                while True: #loop18
                    alt18 = 2
                    LA18_0 = self.input.LA(1)

                    if (LA18_0 == SET) :
                        alt18 = 1


                    if alt18 == 1:
                        # ProtoCC.g:249:55: objset_decl
                        pass 
                        self._state.following.append(self.FOLLOW_objset_decl_in_dir_block1744)
                        objset_decl96 = self.objset_decl()

                        self._state.following.pop()
                        stream_objset_decl.add(objset_decl96.tree)



                    else:
                        break #loop18


                ID97 = self.match(self.input, ID, self.FOLLOW_ID_in_dir_block1747) 
                stream_ID.add(ID97)


                SEMICOLON98 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_dir_block1749) 
                stream_SEMICOLON.add(SEMICOLON98)


                # AST Rewrite
                # elements: objset_decl, ID, declarations
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
                # 249:81: -> ^( DIR_ ID ( objset_decl )* ( declarations )* )
                # ProtoCC.g:250:13: ^( DIR_ ID ( objset_decl )* ( declarations )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(DIR_, "DIR_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # ProtoCC.g:250:23: ( objset_decl )*
                while stream_objset_decl.hasNext():
                    self._adaptor.addChild(root_1, stream_objset_decl.nextTree())


                stream_objset_decl.reset();

                # ProtoCC.g:250:36: ( declarations )*
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
    # ProtoCC.g:251:9: mem_block : MEM OCBRACE ( declarations )* CCBRACE ( objset_decl )* ID SEMICOLON -> ^( MEM_ ID ( objset_decl )* ( declarations )* ) ;
    def mem_block(self, ):
        retval = self.mem_block_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MEM99 = None
        OCBRACE100 = None
        CCBRACE102 = None
        ID104 = None
        SEMICOLON105 = None
        declarations101 = None
        objset_decl103 = None

        MEM99_tree = None
        OCBRACE100_tree = None
        CCBRACE102_tree = None
        ID104_tree = None
        SEMICOLON105_tree = None
        stream_MEM = RewriteRuleTokenStream(self._adaptor, "token MEM")
        stream_OCBRACE = RewriteRuleTokenStream(self._adaptor, "token OCBRACE")
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CCBRACE = RewriteRuleTokenStream(self._adaptor, "token CCBRACE")
        stream_objset_decl = RewriteRuleSubtreeStream(self._adaptor, "rule objset_decl")
        stream_declarations = RewriteRuleSubtreeStream(self._adaptor, "rule declarations")
        try:
            try:
                # ProtoCC.g:251:19: ( MEM OCBRACE ( declarations )* CCBRACE ( objset_decl )* ID SEMICOLON -> ^( MEM_ ID ( objset_decl )* ( declarations )* ) )
                # ProtoCC.g:251:21: MEM OCBRACE ( declarations )* CCBRACE ( objset_decl )* ID SEMICOLON
                pass 
                MEM99 = self.match(self.input, MEM, self.FOLLOW_MEM_in_mem_block1790) 
                stream_MEM.add(MEM99)


                OCBRACE100 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_mem_block1792) 
                stream_OCBRACE.add(OCBRACE100)


                # ProtoCC.g:251:33: ( declarations )*
                while True: #loop19
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if (LA19_0 in {BOOLID, DATA, INTID, NID, SET, STATE}) :
                        alt19 = 1


                    if alt19 == 1:
                        # ProtoCC.g:251:33: declarations
                        pass 
                        self._state.following.append(self.FOLLOW_declarations_in_mem_block1794)
                        declarations101 = self.declarations()

                        self._state.following.pop()
                        stream_declarations.add(declarations101.tree)



                    else:
                        break #loop19


                CCBRACE102 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_mem_block1797) 
                stream_CCBRACE.add(CCBRACE102)


                # ProtoCC.g:251:55: ( objset_decl )*
                while True: #loop20
                    alt20 = 2
                    LA20_0 = self.input.LA(1)

                    if (LA20_0 == SET) :
                        alt20 = 1


                    if alt20 == 1:
                        # ProtoCC.g:251:55: objset_decl
                        pass 
                        self._state.following.append(self.FOLLOW_objset_decl_in_mem_block1799)
                        objset_decl103 = self.objset_decl()

                        self._state.following.pop()
                        stream_objset_decl.add(objset_decl103.tree)



                    else:
                        break #loop20


                ID104 = self.match(self.input, ID, self.FOLLOW_ID_in_mem_block1802) 
                stream_ID.add(ID104)


                SEMICOLON105 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_mem_block1804) 
                stream_SEMICOLON.add(SEMICOLON105)


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
                # 251:81: -> ^( MEM_ ID ( objset_decl )* ( declarations )* )
                # ProtoCC.g:252:13: ^( MEM_ ID ( objset_decl )* ( declarations )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(MEM_, "MEM_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # ProtoCC.g:252:23: ( objset_decl )*
                while stream_objset_decl.hasNext():
                    self._adaptor.addChild(root_1, stream_objset_decl.nextTree())


                stream_objset_decl.reset();

                # ProtoCC.g:252:36: ( declarations )*
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
    # ProtoCC.g:254:9: objset_decl : SET OEBRACE val_range CEBRACE -> ^( OBJSET_ val_range ) ;
    def objset_decl(self, ):
        retval = self.objset_decl_return()
        retval.start = self.input.LT(1)


        root_0 = None

        SET106 = None
        OEBRACE107 = None
        CEBRACE109 = None
        val_range108 = None

        SET106_tree = None
        OEBRACE107_tree = None
        CEBRACE109_tree = None
        stream_SET = RewriteRuleTokenStream(self._adaptor, "token SET")
        stream_CEBRACE = RewriteRuleTokenStream(self._adaptor, "token CEBRACE")
        stream_OEBRACE = RewriteRuleTokenStream(self._adaptor, "token OEBRACE")
        stream_val_range = RewriteRuleSubtreeStream(self._adaptor, "rule val_range")
        try:
            try:
                # ProtoCC.g:254:21: ( SET OEBRACE val_range CEBRACE -> ^( OBJSET_ val_range ) )
                # ProtoCC.g:254:23: SET OEBRACE val_range CEBRACE
                pass 
                SET106 = self.match(self.input, SET, self.FOLLOW_SET_in_objset_decl1846) 
                stream_SET.add(SET106)


                OEBRACE107 = self.match(self.input, OEBRACE, self.FOLLOW_OEBRACE_in_objset_decl1848) 
                stream_OEBRACE.add(OEBRACE107)


                self._state.following.append(self.FOLLOW_val_range_in_objset_decl1850)
                val_range108 = self.val_range()

                self._state.following.pop()
                stream_val_range.add(val_range108.tree)


                CEBRACE109 = self.match(self.input, CEBRACE, self.FOLLOW_CEBRACE_in_objset_decl1852) 
                stream_CEBRACE.add(CEBRACE109)


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
                # 254:53: -> ^( OBJSET_ val_range )
                # ProtoCC.g:254:56: ^( OBJSET_ val_range )
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
    # ProtoCC.g:257:5: network_block : NETWORK OCBRACE ( network_element )* CCBRACE SEMICOLON -> ^( NETWORK_ ( network_element )* ) ;
    def network_block(self, ):
        retval = self.network_block_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NETWORK110 = None
        OCBRACE111 = None
        CCBRACE113 = None
        SEMICOLON114 = None
        network_element112 = None

        NETWORK110_tree = None
        OCBRACE111_tree = None
        CCBRACE113_tree = None
        SEMICOLON114_tree = None
        stream_NETWORK = RewriteRuleTokenStream(self._adaptor, "token NETWORK")
        stream_OCBRACE = RewriteRuleTokenStream(self._adaptor, "token OCBRACE")
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_CCBRACE = RewriteRuleTokenStream(self._adaptor, "token CCBRACE")
        stream_network_element = RewriteRuleSubtreeStream(self._adaptor, "rule network_element")
        try:
            try:
                # ProtoCC.g:257:19: ( NETWORK OCBRACE ( network_element )* CCBRACE SEMICOLON -> ^( NETWORK_ ( network_element )* ) )
                # ProtoCC.g:257:21: NETWORK OCBRACE ( network_element )* CCBRACE SEMICOLON
                pass 
                NETWORK110 = self.match(self.input, NETWORK, self.FOLLOW_NETWORK_in_network_block1878) 
                stream_NETWORK.add(NETWORK110)


                OCBRACE111 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_network_block1880) 
                stream_OCBRACE.add(OCBRACE111)


                # ProtoCC.g:257:37: ( network_element )*
                while True: #loop21
                    alt21 = 2
                    LA21_0 = self.input.LA(1)

                    if (LA21_0 in {126, 133}) :
                        alt21 = 1


                    if alt21 == 1:
                        # ProtoCC.g:257:37: network_element
                        pass 
                        self._state.following.append(self.FOLLOW_network_element_in_network_block1882)
                        network_element112 = self.network_element()

                        self._state.following.pop()
                        stream_network_element.add(network_element112.tree)



                    else:
                        break #loop21


                CCBRACE113 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_network_block1885) 
                stream_CCBRACE.add(CCBRACE113)


                SEMICOLON114 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_network_block1887) 
                stream_SEMICOLON.add(SEMICOLON114)


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
                # 257:72: -> ^( NETWORK_ ( network_element )* )
                # ProtoCC.g:257:75: ^( NETWORK_ ( network_element )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(NETWORK_, "NETWORK_")
                , root_1)

                # ProtoCC.g:257:86: ( network_element )*
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
    # ProtoCC.g:258:9: element_type : ( 'Ordered' | 'Unordered' );
    def element_type(self, ):
        retval = self.element_type_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set115 = None

        set115_tree = None

        try:
            try:
                # ProtoCC.g:258:22: ( 'Ordered' | 'Unordered' )
                # ProtoCC.g:
                pass 
                root_0 = self._adaptor.nil()


                set115 = self.input.LT(1)

                if self.input.LA(1) in {126, 133}:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set115))

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
    # ProtoCC.g:259:9: network_element : element_type ID SEMICOLON -> ^( ELEMENT_ element_type ID ) ;
    def network_element(self, ):
        retval = self.network_element_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID117 = None
        SEMICOLON118 = None
        element_type116 = None

        ID117_tree = None
        SEMICOLON118_tree = None
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_element_type = RewriteRuleSubtreeStream(self._adaptor, "rule element_type")
        try:
            try:
                # ProtoCC.g:259:25: ( element_type ID SEMICOLON -> ^( ELEMENT_ element_type ID ) )
                # ProtoCC.g:259:27: element_type ID SEMICOLON
                pass 
                self._state.following.append(self.FOLLOW_element_type_in_network_element1930)
                element_type116 = self.element_type()

                self._state.following.pop()
                stream_element_type.add(element_type116.tree)


                ID117 = self.match(self.input, ID, self.FOLLOW_ID_in_network_element1932) 
                stream_ID.add(ID117)


                SEMICOLON118 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_network_element1934) 
                stream_SEMICOLON.add(SEMICOLON118)


                # AST Rewrite
                # elements: ID, element_type
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
                # 259:53: -> ^( ELEMENT_ element_type ID )
                # ProtoCC.g:259:56: ^( ELEMENT_ element_type ID )
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
    # ProtoCC.g:260:5: network_send : ID DOT send_function OBRACE ID CBRACE SEMICOLON -> ^( SEND_ ID ID ) ;
    def network_send(self, ):
        retval = self.network_send_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID119 = None
        DOT120 = None
        OBRACE122 = None
        ID123 = None
        CBRACE124 = None
        SEMICOLON125 = None
        send_function121 = None

        ID119_tree = None
        DOT120_tree = None
        OBRACE122_tree = None
        ID123_tree = None
        CBRACE124_tree = None
        SEMICOLON125_tree = None
        stream_OBRACE = RewriteRuleTokenStream(self._adaptor, "token OBRACE")
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CBRACE = RewriteRuleTokenStream(self._adaptor, "token CBRACE")
        stream_send_function = RewriteRuleSubtreeStream(self._adaptor, "rule send_function")
        try:
            try:
                # ProtoCC.g:260:18: ( ID DOT send_function OBRACE ID CBRACE SEMICOLON -> ^( SEND_ ID ID ) )
                # ProtoCC.g:260:20: ID DOT send_function OBRACE ID CBRACE SEMICOLON
                pass 
                ID119 = self.match(self.input, ID, self.FOLLOW_ID_in_network_send1955) 
                stream_ID.add(ID119)


                DOT120 = self.match(self.input, DOT, self.FOLLOW_DOT_in_network_send1957) 
                stream_DOT.add(DOT120)


                self._state.following.append(self.FOLLOW_send_function_in_network_send1959)
                send_function121 = self.send_function()

                self._state.following.pop()
                stream_send_function.add(send_function121.tree)


                OBRACE122 = self.match(self.input, OBRACE, self.FOLLOW_OBRACE_in_network_send1961) 
                stream_OBRACE.add(OBRACE122)


                ID123 = self.match(self.input, ID, self.FOLLOW_ID_in_network_send1963) 
                stream_ID.add(ID123)


                CBRACE124 = self.match(self.input, CBRACE, self.FOLLOW_CBRACE_in_network_send1965) 
                stream_CBRACE.add(CBRACE124)


                SEMICOLON125 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_network_send1967) 
                stream_SEMICOLON.add(SEMICOLON125)


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
                # 260:68: -> ^( SEND_ ID ID )
                # ProtoCC.g:260:71: ^( SEND_ ID ID )
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
    # ProtoCC.g:261:5: network_bcast : ID DOT bcast_function OBRACE ID CBRACE SEMICOLON -> ^( BCAST_ ID ID ) ;
    def network_bcast(self, ):
        retval = self.network_bcast_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID126 = None
        DOT127 = None
        OBRACE129 = None
        ID130 = None
        CBRACE131 = None
        SEMICOLON132 = None
        bcast_function128 = None

        ID126_tree = None
        DOT127_tree = None
        OBRACE129_tree = None
        ID130_tree = None
        CBRACE131_tree = None
        SEMICOLON132_tree = None
        stream_OBRACE = RewriteRuleTokenStream(self._adaptor, "token OBRACE")
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CBRACE = RewriteRuleTokenStream(self._adaptor, "token CBRACE")
        stream_bcast_function = RewriteRuleSubtreeStream(self._adaptor, "rule bcast_function")
        try:
            try:
                # ProtoCC.g:261:18: ( ID DOT bcast_function OBRACE ID CBRACE SEMICOLON -> ^( BCAST_ ID ID ) )
                # ProtoCC.g:261:20: ID DOT bcast_function OBRACE ID CBRACE SEMICOLON
                pass 
                ID126 = self.match(self.input, ID, self.FOLLOW_ID_in_network_bcast1987) 
                stream_ID.add(ID126)


                DOT127 = self.match(self.input, DOT, self.FOLLOW_DOT_in_network_bcast1989) 
                stream_DOT.add(DOT127)


                self._state.following.append(self.FOLLOW_bcast_function_in_network_bcast1991)
                bcast_function128 = self.bcast_function()

                self._state.following.pop()
                stream_bcast_function.add(bcast_function128.tree)


                OBRACE129 = self.match(self.input, OBRACE, self.FOLLOW_OBRACE_in_network_bcast1993) 
                stream_OBRACE.add(OBRACE129)


                ID130 = self.match(self.input, ID, self.FOLLOW_ID_in_network_bcast1995) 
                stream_ID.add(ID130)


                CBRACE131 = self.match(self.input, CBRACE, self.FOLLOW_CBRACE_in_network_bcast1997) 
                stream_CBRACE.add(CBRACE131)


                SEMICOLON132 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_network_bcast1999) 
                stream_SEMICOLON.add(SEMICOLON132)


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
                # 261:69: -> ^( BCAST_ ID ID )
                # ProtoCC.g:261:72: ^( BCAST_ ID ID )
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
    # ProtoCC.g:262:5: network_mcast : ID DOT mcast_function OBRACE ID COMMA ID CBRACE SEMICOLON -> ^( MCAST_ ID ID ID ) ;
    def network_mcast(self, ):
        retval = self.network_mcast_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID133 = None
        DOT134 = None
        OBRACE136 = None
        ID137 = None
        COMMA138 = None
        ID139 = None
        CBRACE140 = None
        SEMICOLON141 = None
        mcast_function135 = None

        ID133_tree = None
        DOT134_tree = None
        OBRACE136_tree = None
        ID137_tree = None
        COMMA138_tree = None
        ID139_tree = None
        CBRACE140_tree = None
        SEMICOLON141_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_OBRACE = RewriteRuleTokenStream(self._adaptor, "token OBRACE")
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CBRACE = RewriteRuleTokenStream(self._adaptor, "token CBRACE")
        stream_mcast_function = RewriteRuleSubtreeStream(self._adaptor, "rule mcast_function")
        try:
            try:
                # ProtoCC.g:262:18: ( ID DOT mcast_function OBRACE ID COMMA ID CBRACE SEMICOLON -> ^( MCAST_ ID ID ID ) )
                # ProtoCC.g:262:20: ID DOT mcast_function OBRACE ID COMMA ID CBRACE SEMICOLON
                pass 
                ID133 = self.match(self.input, ID, self.FOLLOW_ID_in_network_mcast2019) 
                stream_ID.add(ID133)


                DOT134 = self.match(self.input, DOT, self.FOLLOW_DOT_in_network_mcast2021) 
                stream_DOT.add(DOT134)


                self._state.following.append(self.FOLLOW_mcast_function_in_network_mcast2023)
                mcast_function135 = self.mcast_function()

                self._state.following.pop()
                stream_mcast_function.add(mcast_function135.tree)


                OBRACE136 = self.match(self.input, OBRACE, self.FOLLOW_OBRACE_in_network_mcast2025) 
                stream_OBRACE.add(OBRACE136)


                ID137 = self.match(self.input, ID, self.FOLLOW_ID_in_network_mcast2027) 
                stream_ID.add(ID137)


                COMMA138 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_network_mcast2029) 
                stream_COMMA.add(COMMA138)


                ID139 = self.match(self.input, ID, self.FOLLOW_ID_in_network_mcast2031) 
                stream_ID.add(ID139)


                CBRACE140 = self.match(self.input, CBRACE, self.FOLLOW_CBRACE_in_network_mcast2033) 
                stream_CBRACE.add(CBRACE140)


                SEMICOLON141 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_network_mcast2035) 
                stream_SEMICOLON.add(SEMICOLON141)


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
                # 262:78: -> ^( MCAST_ ID ID ID )
                # ProtoCC.g:262:81: ^( MCAST_ ID ID ID )
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
    # ProtoCC.g:265:5: message_block : MSG ID OCBRACE ( declarations )* CCBRACE SEMICOLON -> ^( MSG_ ID ( declarations )* ) ;
    def message_block(self, ):
        retval = self.message_block_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MSG142 = None
        ID143 = None
        OCBRACE144 = None
        CCBRACE146 = None
        SEMICOLON147 = None
        declarations145 = None

        MSG142_tree = None
        ID143_tree = None
        OCBRACE144_tree = None
        CCBRACE146_tree = None
        SEMICOLON147_tree = None
        stream_MSG = RewriteRuleTokenStream(self._adaptor, "token MSG")
        stream_OCBRACE = RewriteRuleTokenStream(self._adaptor, "token OCBRACE")
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CCBRACE = RewriteRuleTokenStream(self._adaptor, "token CCBRACE")
        stream_declarations = RewriteRuleSubtreeStream(self._adaptor, "rule declarations")
        try:
            try:
                # ProtoCC.g:265:19: ( MSG ID OCBRACE ( declarations )* CCBRACE SEMICOLON -> ^( MSG_ ID ( declarations )* ) )
                # ProtoCC.g:265:21: MSG ID OCBRACE ( declarations )* CCBRACE SEMICOLON
                pass 
                MSG142 = self.match(self.input, MSG, self.FOLLOW_MSG_in_message_block2065) 
                stream_MSG.add(MSG142)


                ID143 = self.match(self.input, ID, self.FOLLOW_ID_in_message_block2067) 
                stream_ID.add(ID143)


                OCBRACE144 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_message_block2069) 
                stream_OCBRACE.add(OCBRACE144)


                # ProtoCC.g:265:36: ( declarations )*
                while True: #loop22
                    alt22 = 2
                    LA22_0 = self.input.LA(1)

                    if (LA22_0 in {BOOLID, DATA, INTID, NID, SET, STATE}) :
                        alt22 = 1


                    if alt22 == 1:
                        # ProtoCC.g:265:36: declarations
                        pass 
                        self._state.following.append(self.FOLLOW_declarations_in_message_block2071)
                        declarations145 = self.declarations()

                        self._state.following.pop()
                        stream_declarations.add(declarations145.tree)



                    else:
                        break #loop22


                CCBRACE146 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_message_block2074) 
                stream_CCBRACE.add(CCBRACE146)


                SEMICOLON147 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_message_block2076) 
                stream_SEMICOLON.add(SEMICOLON147)


                # AST Rewrite
                # elements: ID, declarations
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
                # 265:68: -> ^( MSG_ ID ( declarations )* )
                # ProtoCC.g:265:71: ^( MSG_ ID ( declarations )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(MSG_, "MSG_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # ProtoCC.g:265:81: ( declarations )*
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
    # ProtoCC.g:266:5: message_constr : ID OBRACE ( message_expr )* ( COMMA message_expr )* CBRACE -> ^( MSGCSTR_ ID ( message_expr )* ) ;
    def message_constr(self, ):
        retval = self.message_constr_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID148 = None
        OBRACE149 = None
        COMMA151 = None
        CBRACE153 = None
        message_expr150 = None
        message_expr152 = None

        ID148_tree = None
        OBRACE149_tree = None
        COMMA151_tree = None
        CBRACE153_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_OBRACE = RewriteRuleTokenStream(self._adaptor, "token OBRACE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CBRACE = RewriteRuleTokenStream(self._adaptor, "token CBRACE")
        stream_message_expr = RewriteRuleSubtreeStream(self._adaptor, "rule message_expr")
        try:
            try:
                # ProtoCC.g:266:20: ( ID OBRACE ( message_expr )* ( COMMA message_expr )* CBRACE -> ^( MSGCSTR_ ID ( message_expr )* ) )
                # ProtoCC.g:266:22: ID OBRACE ( message_expr )* ( COMMA message_expr )* CBRACE
                pass 
                ID148 = self.match(self.input, ID, self.FOLLOW_ID_in_message_constr2098) 
                stream_ID.add(ID148)


                OBRACE149 = self.match(self.input, OBRACE, self.FOLLOW_OBRACE_in_message_constr2100) 
                stream_OBRACE.add(OBRACE149)


                # ProtoCC.g:266:32: ( message_expr )*
                while True: #loop23
                    alt23 = 2
                    LA23_0 = self.input.LA(1)

                    if (LA23_0 in {BOOL, ID, INT, NID}) :
                        alt23 = 1


                    if alt23 == 1:
                        # ProtoCC.g:266:32: message_expr
                        pass 
                        self._state.following.append(self.FOLLOW_message_expr_in_message_constr2102)
                        message_expr150 = self.message_expr()

                        self._state.following.pop()
                        stream_message_expr.add(message_expr150.tree)



                    else:
                        break #loop23


                # ProtoCC.g:266:46: ( COMMA message_expr )*
                while True: #loop24
                    alt24 = 2
                    LA24_0 = self.input.LA(1)

                    if (LA24_0 == COMMA) :
                        alt24 = 1


                    if alt24 == 1:
                        # ProtoCC.g:266:47: COMMA message_expr
                        pass 
                        COMMA151 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_message_constr2106) 
                        stream_COMMA.add(COMMA151)


                        self._state.following.append(self.FOLLOW_message_expr_in_message_constr2108)
                        message_expr152 = self.message_expr()

                        self._state.following.pop()
                        stream_message_expr.add(message_expr152.tree)



                    else:
                        break #loop24


                CBRACE153 = self.match(self.input, CBRACE, self.FOLLOW_CBRACE_in_message_constr2112) 
                stream_CBRACE.add(CBRACE153)


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
                # 266:75: -> ^( MSGCSTR_ ID ( message_expr )* )
                # ProtoCC.g:266:78: ^( MSGCSTR_ ID ( message_expr )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(MSGCSTR_, "MSGCSTR_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # ProtoCC.g:266:92: ( message_expr )*
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
    # ProtoCC.g:267:5: message_expr : ( object_expr | set_func | INT | BOOL | NID );
    def message_expr(self, ):
        retval = self.message_expr_return()
        retval.start = self.input.LT(1)


        root_0 = None

        INT156 = None
        BOOL157 = None
        NID158 = None
        object_expr154 = None
        set_func155 = None

        INT156_tree = None
        BOOL157_tree = None
        NID158_tree = None

        try:
            try:
                # ProtoCC.g:267:18: ( object_expr | set_func | INT | BOOL | NID )
                alt25 = 5
                LA25 = self.input.LA(1)
                if LA25 in {ID}:
                    LA25_1 = self.input.LA(2)

                    if (LA25_1 == DOT) :
                        LA25_5 = self.input.LA(3)

                        if (LA25_5 in {ID, NID}) :
                            alt25 = 1
                        elif (LA25_5 in {137, 139, 141, 142, 143, 147}) :
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
                    # ProtoCC.g:267:20: object_expr
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_object_expr_in_message_expr2134)
                    object_expr154 = self.object_expr()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, object_expr154.tree)



                elif alt25 == 2:
                    # ProtoCC.g:267:34: set_func
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_set_func_in_message_expr2138)
                    set_func155 = self.set_func()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, set_func155.tree)



                elif alt25 == 3:
                    # ProtoCC.g:267:45: INT
                    pass 
                    root_0 = self._adaptor.nil()


                    INT156 = self.match(self.input, INT, self.FOLLOW_INT_in_message_expr2142)
                    INT156_tree = self._adaptor.createWithPayload(INT156)
                    self._adaptor.addChild(root_0, INT156_tree)




                elif alt25 == 4:
                    # ProtoCC.g:267:51: BOOL
                    pass 
                    root_0 = self._adaptor.nil()


                    BOOL157 = self.match(self.input, BOOL, self.FOLLOW_BOOL_in_message_expr2146)
                    BOOL157_tree = self._adaptor.createWithPayload(BOOL157)
                    self._adaptor.addChild(root_0, BOOL157_tree)




                elif alt25 == 5:
                    # ProtoCC.g:267:58: NID
                    pass 
                    root_0 = self._adaptor.nil()


                    NID158 = self.match(self.input, NID, self.FOLLOW_NID_in_message_expr2150)
                    NID158_tree = self._adaptor.createWithPayload(NID158)
                    self._adaptor.addChild(root_0, NID158_tree)




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
    # ProtoCC.g:270:5: set_block : set_func SEMICOLON -> set_func ;
    def set_block(self, ):
        retval = self.set_block_return()
        retval.start = self.input.LT(1)


        root_0 = None

        SEMICOLON160 = None
        set_func159 = None

        SEMICOLON160_tree = None
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_set_func = RewriteRuleSubtreeStream(self._adaptor, "rule set_func")
        try:
            try:
                # ProtoCC.g:270:15: ( set_func SEMICOLON -> set_func )
                # ProtoCC.g:270:17: set_func SEMICOLON
                pass 
                self._state.following.append(self.FOLLOW_set_func_in_set_block2168)
                set_func159 = self.set_func()

                self._state.following.pop()
                stream_set_func.add(set_func159.tree)


                SEMICOLON160 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_set_block2170) 
                stream_SEMICOLON.add(SEMICOLON160)


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
                # 270:36: -> set_func
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
    # ProtoCC.g:271:5: set_func : ID DOT set_function_types OBRACE ( set_nest )* CBRACE -> ^( SETFUNC_ ID DOT set_function_types OBRACE ( set_nest )* CBRACE ) ;
    def set_func(self, ):
        retval = self.set_func_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID161 = None
        DOT162 = None
        OBRACE164 = None
        CBRACE166 = None
        set_function_types163 = None
        set_nest165 = None

        ID161_tree = None
        DOT162_tree = None
        OBRACE164_tree = None
        CBRACE166_tree = None
        stream_OBRACE = RewriteRuleTokenStream(self._adaptor, "token OBRACE")
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CBRACE = RewriteRuleTokenStream(self._adaptor, "token CBRACE")
        stream_set_function_types = RewriteRuleSubtreeStream(self._adaptor, "rule set_function_types")
        stream_set_nest = RewriteRuleSubtreeStream(self._adaptor, "rule set_nest")
        try:
            try:
                # ProtoCC.g:271:14: ( ID DOT set_function_types OBRACE ( set_nest )* CBRACE -> ^( SETFUNC_ ID DOT set_function_types OBRACE ( set_nest )* CBRACE ) )
                # ProtoCC.g:271:16: ID DOT set_function_types OBRACE ( set_nest )* CBRACE
                pass 
                ID161 = self.match(self.input, ID, self.FOLLOW_ID_in_set_func2185) 
                stream_ID.add(ID161)


                DOT162 = self.match(self.input, DOT, self.FOLLOW_DOT_in_set_func2187) 
                stream_DOT.add(DOT162)


                self._state.following.append(self.FOLLOW_set_function_types_in_set_func2189)
                set_function_types163 = self.set_function_types()

                self._state.following.pop()
                stream_set_function_types.add(set_function_types163.tree)


                OBRACE164 = self.match(self.input, OBRACE, self.FOLLOW_OBRACE_in_set_func2191) 
                stream_OBRACE.add(OBRACE164)


                # ProtoCC.g:271:49: ( set_nest )*
                while True: #loop26
                    alt26 = 2
                    LA26_0 = self.input.LA(1)

                    if (LA26_0 == ID) :
                        alt26 = 1


                    if alt26 == 1:
                        # ProtoCC.g:271:49: set_nest
                        pass 
                        self._state.following.append(self.FOLLOW_set_nest_in_set_func2193)
                        set_nest165 = self.set_nest()

                        self._state.following.pop()
                        stream_set_nest.add(set_nest165.tree)



                    else:
                        break #loop26


                CBRACE166 = self.match(self.input, CBRACE, self.FOLLOW_CBRACE_in_set_func2196) 
                stream_CBRACE.add(CBRACE166)


                # AST Rewrite
                # elements: set_function_types, ID, set_nest, DOT, OBRACE, CBRACE
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
                # 271:66: -> ^( SETFUNC_ ID DOT set_function_types OBRACE ( set_nest )* CBRACE )
                # ProtoCC.g:272:9: ^( SETFUNC_ ID DOT set_function_types OBRACE ( set_nest )* CBRACE )
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

                # ProtoCC.g:272:53: ( set_nest )*
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
    # ProtoCC.g:273:5: set_nest : ( set_func | object_expr );
    def set_nest(self, ):
        retval = self.set_nest_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set_func167 = None
        object_expr168 = None


        try:
            try:
                # ProtoCC.g:273:14: ( set_func | object_expr )
                alt27 = 2
                LA27_0 = self.input.LA(1)

                if (LA27_0 == ID) :
                    LA27_1 = self.input.LA(2)

                    if (LA27_1 == DOT) :
                        LA27_2 = self.input.LA(3)

                        if (LA27_2 in {137, 139, 141, 142, 143, 147}) :
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
                    # ProtoCC.g:273:16: set_func
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_set_func_in_set_nest2234)
                    set_func167 = self.set_func()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, set_func167.tree)



                elif alt27 == 2:
                    # ProtoCC.g:273:27: object_expr
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_object_expr_in_set_nest2238)
                    object_expr168 = self.object_expr()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, object_expr168.tree)



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
    # ProtoCC.g:277:5: internal_event_block : internal_event_func SEMICOLON -> internal_event_func ;
    def internal_event_block(self, ):
        retval = self.internal_event_block_return()
        retval.start = self.input.LT(1)


        root_0 = None

        SEMICOLON170 = None
        internal_event_func169 = None

        SEMICOLON170_tree = None
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_internal_event_func = RewriteRuleSubtreeStream(self._adaptor, "rule internal_event_func")
        try:
            try:
                # ProtoCC.g:277:25: ( internal_event_func SEMICOLON -> internal_event_func )
                # ProtoCC.g:277:27: internal_event_func SEMICOLON
                pass 
                self._state.following.append(self.FOLLOW_internal_event_func_in_internal_event_block2256)
                internal_event_func169 = self.internal_event_func()

                self._state.following.pop()
                stream_internal_event_func.add(internal_event_func169.tree)


                SEMICOLON170 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_internal_event_block2258) 
                stream_SEMICOLON.add(SEMICOLON170)


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
                # 277:57: -> internal_event_func
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
    # ProtoCC.g:278:5: internal_event_func : internal_event_function OBRACE ID CBRACE -> ^( EVENT_ ID ) ^( EVENT_ACK_ ID ) ;
    def internal_event_func(self, ):
        retval = self.internal_event_func_return()
        retval.start = self.input.LT(1)


        root_0 = None

        OBRACE172 = None
        ID173 = None
        CBRACE174 = None
        internal_event_function171 = None

        OBRACE172_tree = None
        ID173_tree = None
        CBRACE174_tree = None
        stream_OBRACE = RewriteRuleTokenStream(self._adaptor, "token OBRACE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CBRACE = RewriteRuleTokenStream(self._adaptor, "token CBRACE")
        stream_internal_event_function = RewriteRuleSubtreeStream(self._adaptor, "rule internal_event_function")
        try:
            try:
                # ProtoCC.g:278:24: ( internal_event_function OBRACE ID CBRACE -> ^( EVENT_ ID ) ^( EVENT_ACK_ ID ) )
                # ProtoCC.g:278:26: internal_event_function OBRACE ID CBRACE
                pass 
                self._state.following.append(self.FOLLOW_internal_event_function_in_internal_event_func2272)
                internal_event_function171 = self.internal_event_function()

                self._state.following.pop()
                stream_internal_event_function.add(internal_event_function171.tree)


                OBRACE172 = self.match(self.input, OBRACE, self.FOLLOW_OBRACE_in_internal_event_func2274) 
                stream_OBRACE.add(OBRACE172)


                ID173 = self.match(self.input, ID, self.FOLLOW_ID_in_internal_event_func2276) 
                stream_ID.add(ID173)


                CBRACE174 = self.match(self.input, CBRACE, self.FOLLOW_CBRACE_in_internal_event_func2278) 
                stream_CBRACE.add(CBRACE174)


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
                # 278:67: -> ^( EVENT_ ID ) ^( EVENT_ACK_ ID )
                # ProtoCC.g:278:70: ^( EVENT_ ID )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(EVENT_, "EVENT_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_0, root_1)

                # ProtoCC.g:278:83: ^( EVENT_ACK_ ID )
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
    # ProtoCC.g:281:1: arch_block : ARCH ID OCBRACE arch_body CCBRACE -> ^( ARCH_ ^( MACHN_ ID ) arch_body ) ;
    def arch_block(self, ):
        retval = self.arch_block_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ARCH175 = None
        ID176 = None
        OCBRACE177 = None
        CCBRACE179 = None
        arch_body178 = None

        ARCH175_tree = None
        ID176_tree = None
        OCBRACE177_tree = None
        CCBRACE179_tree = None
        stream_OCBRACE = RewriteRuleTokenStream(self._adaptor, "token OCBRACE")
        stream_ARCH = RewriteRuleTokenStream(self._adaptor, "token ARCH")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CCBRACE = RewriteRuleTokenStream(self._adaptor, "token CCBRACE")
        stream_arch_body = RewriteRuleSubtreeStream(self._adaptor, "rule arch_body")
        try:
            try:
                # ProtoCC.g:281:12: ( ARCH ID OCBRACE arch_body CCBRACE -> ^( ARCH_ ^( MACHN_ ID ) arch_body ) )
                # ProtoCC.g:281:14: ARCH ID OCBRACE arch_body CCBRACE
                pass 
                ARCH175 = self.match(self.input, ARCH, self.FOLLOW_ARCH_in_arch_block2302) 
                stream_ARCH.add(ARCH175)


                ID176 = self.match(self.input, ID, self.FOLLOW_ID_in_arch_block2304) 
                stream_ID.add(ID176)


                OCBRACE177 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_arch_block2306) 
                stream_OCBRACE.add(OCBRACE177)


                self._state.following.append(self.FOLLOW_arch_body_in_arch_block2308)
                arch_body178 = self.arch_body()

                self._state.following.pop()
                stream_arch_body.add(arch_body178.tree)


                CCBRACE179 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_arch_block2310) 
                stream_CCBRACE.add(CCBRACE179)


                # AST Rewrite
                # elements: arch_body, ID
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
                # 281:48: -> ^( ARCH_ ^( MACHN_ ID ) arch_body )
                # ProtoCC.g:281:51: ^( ARCH_ ^( MACHN_ ID ) arch_body )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(ARCH_, "ARCH_")
                , root_1)

                # ProtoCC.g:281:59: ^( MACHN_ ID )
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
    # ProtoCC.g:283:1: arch_body : ( stable_def | process_block )* ;
    def arch_body(self, ):
        retval = self.arch_body_return()
        retval.start = self.input.LT(1)


        root_0 = None

        stable_def180 = None
        process_block181 = None


        try:
            try:
                # ProtoCC.g:283:10: ( ( stable_def | process_block )* )
                # ProtoCC.g:283:12: ( stable_def | process_block )*
                pass 
                root_0 = self._adaptor.nil()


                # ProtoCC.g:283:12: ( stable_def | process_block )*
                while True: #loop28
                    alt28 = 3
                    LA28_0 = self.input.LA(1)

                    if (LA28_0 == STABLE) :
                        alt28 = 1
                    elif (LA28_0 == PROC) :
                        alt28 = 2


                    if alt28 == 1:
                        # ProtoCC.g:283:13: stable_def
                        pass 
                        self._state.following.append(self.FOLLOW_stable_def_in_arch_body2332)
                        stable_def180 = self.stable_def()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, stable_def180.tree)



                    elif alt28 == 2:
                        # ProtoCC.g:283:26: process_block
                        pass 
                        self._state.following.append(self.FOLLOW_process_block_in_arch_body2336)
                        process_block181 = self.process_block()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, process_block181.tree)



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
    # ProtoCC.g:285:1: stable_def : STABLE OCBRACE ID ( COMMA ID )* CCBRACE -> ^( STABLE_ ID ( ID )* ) ;
    def stable_def(self, ):
        retval = self.stable_def_return()
        retval.start = self.input.LT(1)


        root_0 = None

        STABLE182 = None
        OCBRACE183 = None
        ID184 = None
        COMMA185 = None
        ID186 = None
        CCBRACE187 = None

        STABLE182_tree = None
        OCBRACE183_tree = None
        ID184_tree = None
        COMMA185_tree = None
        ID186_tree = None
        CCBRACE187_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_OCBRACE = RewriteRuleTokenStream(self._adaptor, "token OCBRACE")
        stream_STABLE = RewriteRuleTokenStream(self._adaptor, "token STABLE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CCBRACE = RewriteRuleTokenStream(self._adaptor, "token CCBRACE")

        try:
            try:
                # ProtoCC.g:285:12: ( STABLE OCBRACE ID ( COMMA ID )* CCBRACE -> ^( STABLE_ ID ( ID )* ) )
                # ProtoCC.g:285:14: STABLE OCBRACE ID ( COMMA ID )* CCBRACE
                pass 
                STABLE182 = self.match(self.input, STABLE, self.FOLLOW_STABLE_in_stable_def2346) 
                stream_STABLE.add(STABLE182)


                OCBRACE183 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_stable_def2348) 
                stream_OCBRACE.add(OCBRACE183)


                ID184 = self.match(self.input, ID, self.FOLLOW_ID_in_stable_def2350) 
                stream_ID.add(ID184)


                # ProtoCC.g:285:32: ( COMMA ID )*
                while True: #loop29
                    alt29 = 2
                    LA29_0 = self.input.LA(1)

                    if (LA29_0 == COMMA) :
                        alt29 = 1


                    if alt29 == 1:
                        # ProtoCC.g:285:33: COMMA ID
                        pass 
                        COMMA185 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_stable_def2353) 
                        stream_COMMA.add(COMMA185)


                        ID186 = self.match(self.input, ID, self.FOLLOW_ID_in_stable_def2355) 
                        stream_ID.add(ID186)



                    else:
                        break #loop29


                CCBRACE187 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_stable_def2359) 
                stream_CCBRACE.add(CCBRACE187)


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
                # 285:52: -> ^( STABLE_ ID ( ID )* )
                # ProtoCC.g:285:55: ^( STABLE_ ID ( ID )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(STABLE_, "STABLE_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # ProtoCC.g:285:68: ( ID )*
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
    # ProtoCC.g:287:1: process_block : PROC process_trans OCBRACE ( process_expr )* CCBRACE -> ^( PROC_ process_trans ( process_expr )* ^( ENDPROC_ ) ) ;
    def process_block(self, ):
        retval = self.process_block_return()
        retval.start = self.input.LT(1)


        root_0 = None

        PROC188 = None
        OCBRACE190 = None
        CCBRACE192 = None
        process_trans189 = None
        process_expr191 = None

        PROC188_tree = None
        OCBRACE190_tree = None
        CCBRACE192_tree = None
        stream_PROC = RewriteRuleTokenStream(self._adaptor, "token PROC")
        stream_OCBRACE = RewriteRuleTokenStream(self._adaptor, "token OCBRACE")
        stream_CCBRACE = RewriteRuleTokenStream(self._adaptor, "token CCBRACE")
        stream_process_trans = RewriteRuleSubtreeStream(self._adaptor, "rule process_trans")
        stream_process_expr = RewriteRuleSubtreeStream(self._adaptor, "rule process_expr")
        try:
            try:
                # ProtoCC.g:287:15: ( PROC process_trans OCBRACE ( process_expr )* CCBRACE -> ^( PROC_ process_trans ( process_expr )* ^( ENDPROC_ ) ) )
                # ProtoCC.g:287:17: PROC process_trans OCBRACE ( process_expr )* CCBRACE
                pass 
                PROC188 = self.match(self.input, PROC, self.FOLLOW_PROC_in_process_block2378) 
                stream_PROC.add(PROC188)


                self._state.following.append(self.FOLLOW_process_trans_in_process_block2380)
                process_trans189 = self.process_trans()

                self._state.following.pop()
                stream_process_trans.add(process_trans189.tree)


                OCBRACE190 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_process_block2382) 
                stream_OCBRACE.add(OCBRACE190)


                # ProtoCC.g:287:44: ( process_expr )*
                while True: #loop30
                    alt30 = 2
                    LA30_0 = self.input.LA(1)

                    if (LA30_0 in {ACCESS, AWAIT, ID, IF, STALL, STATE, UNDEF, 121}) :
                        alt30 = 1


                    if alt30 == 1:
                        # ProtoCC.g:287:44: process_expr
                        pass 
                        self._state.following.append(self.FOLLOW_process_expr_in_process_block2384)
                        process_expr191 = self.process_expr()

                        self._state.following.pop()
                        stream_process_expr.add(process_expr191.tree)



                    else:
                        break #loop30


                CCBRACE192 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_process_block2387) 
                stream_CCBRACE.add(CCBRACE192)


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
                # 287:66: -> ^( PROC_ process_trans ( process_expr )* ^( ENDPROC_ ) )
                # ProtoCC.g:287:69: ^( PROC_ process_trans ( process_expr )* ^( ENDPROC_ ) )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(PROC_, "PROC_")
                , root_1)

                self._adaptor.addChild(root_1, stream_process_trans.nextTree())

                # ProtoCC.g:287:91: ( process_expr )*
                while stream_process_expr.hasNext():
                    self._adaptor.addChild(root_1, stream_process_expr.nextTree())


                stream_process_expr.reset();

                # ProtoCC.g:287:105: ^( ENDPROC_ )
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
    # ProtoCC.g:288:5: process_trans : OBRACE ID COMMA process_events ( process_finalstate )* CBRACE -> ^( TRANS_ ID process_events ( process_finalstate )* ) ;
    def process_trans(self, ):
        retval = self.process_trans_return()
        retval.start = self.input.LT(1)


        root_0 = None

        OBRACE193 = None
        ID194 = None
        COMMA195 = None
        CBRACE198 = None
        process_events196 = None
        process_finalstate197 = None

        OBRACE193_tree = None
        ID194_tree = None
        COMMA195_tree = None
        CBRACE198_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_OBRACE = RewriteRuleTokenStream(self._adaptor, "token OBRACE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CBRACE = RewriteRuleTokenStream(self._adaptor, "token CBRACE")
        stream_process_events = RewriteRuleSubtreeStream(self._adaptor, "rule process_events")
        stream_process_finalstate = RewriteRuleSubtreeStream(self._adaptor, "rule process_finalstate")
        try:
            try:
                # ProtoCC.g:288:19: ( OBRACE ID COMMA process_events ( process_finalstate )* CBRACE -> ^( TRANS_ ID process_events ( process_finalstate )* ) )
                # ProtoCC.g:288:21: OBRACE ID COMMA process_events ( process_finalstate )* CBRACE
                pass 
                OBRACE193 = self.match(self.input, OBRACE, self.FOLLOW_OBRACE_in_process_trans2413) 
                stream_OBRACE.add(OBRACE193)


                ID194 = self.match(self.input, ID, self.FOLLOW_ID_in_process_trans2415) 
                stream_ID.add(ID194)


                COMMA195 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_process_trans2417) 
                stream_COMMA.add(COMMA195)


                self._state.following.append(self.FOLLOW_process_events_in_process_trans2419)
                process_events196 = self.process_events()

                self._state.following.pop()
                stream_process_events.add(process_events196.tree)


                # ProtoCC.g:288:52: ( process_finalstate )*
                while True: #loop31
                    alt31 = 2
                    LA31_0 = self.input.LA(1)

                    if (LA31_0 == COMMA) :
                        alt31 = 1


                    if alt31 == 1:
                        # ProtoCC.g:288:52: process_finalstate
                        pass 
                        self._state.following.append(self.FOLLOW_process_finalstate_in_process_trans2421)
                        process_finalstate197 = self.process_finalstate()

                        self._state.following.pop()
                        stream_process_finalstate.add(process_finalstate197.tree)



                    else:
                        break #loop31


                CBRACE198 = self.match(self.input, CBRACE, self.FOLLOW_CBRACE_in_process_trans2424) 
                stream_CBRACE.add(CBRACE198)


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
                # 288:79: -> ^( TRANS_ ID process_events ( process_finalstate )* )
                # ProtoCC.g:288:82: ^( TRANS_ ID process_events ( process_finalstate )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TRANS_, "TRANS_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_1, stream_process_events.nextTree())

                # ProtoCC.g:288:109: ( process_finalstate )*
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
    # ProtoCC.g:289:5: process_finalstate : COMMA process_finalident -> ^( process_finalident ) ;
    def process_finalstate(self, ):
        retval = self.process_finalstate_return()
        retval.start = self.input.LT(1)


        root_0 = None

        COMMA199 = None
        process_finalident200 = None

        COMMA199_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_process_finalident = RewriteRuleSubtreeStream(self._adaptor, "rule process_finalident")
        try:
            try:
                # ProtoCC.g:289:23: ( COMMA process_finalident -> ^( process_finalident ) )
                # ProtoCC.g:289:25: COMMA process_finalident
                pass 
                COMMA199 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_process_finalstate2447) 
                stream_COMMA.add(COMMA199)


                self._state.following.append(self.FOLLOW_process_finalident_in_process_finalstate2449)
                process_finalident200 = self.process_finalident()

                self._state.following.pop()
                stream_process_finalident.add(process_finalident200.tree)


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
                # 289:50: -> ^( process_finalident )
                # ProtoCC.g:289:53: ^( process_finalident )
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
    # ProtoCC.g:290:5: process_finalident : ( ID | STATE ) ;
    def process_finalident(self, ):
        retval = self.process_finalident_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set201 = None

        set201_tree = None

        try:
            try:
                # ProtoCC.g:290:23: ( ( ID | STATE ) )
                # ProtoCC.g:
                pass 
                root_0 = self._adaptor.nil()


                set201 = self.input.LT(1)

                if self.input.LA(1) in {ID, STATE}:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set201))

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
    # ProtoCC.g:291:5: process_events : ( ACCESS | EVICT | ID ) ;
    def process_events(self, ):
        retval = self.process_events_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set202 = None

        set202_tree = None

        try:
            try:
                # ProtoCC.g:291:20: ( ( ACCESS | EVICT | ID ) )
                # ProtoCC.g:
                pass 
                root_0 = self._adaptor.nil()


                set202 = self.input.LT(1)

                if self.input.LA(1) in {ACCESS, EVICT, ID}:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set202))

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
    # ProtoCC.g:292:5: process_expr : ( expressions | network_send | network_mcast | network_bcast | transaction );
    def process_expr(self, ):
        retval = self.process_expr_return()
        retval.start = self.input.LT(1)


        root_0 = None

        expressions203 = None
        network_send204 = None
        network_mcast205 = None
        network_bcast206 = None
        transaction207 = None


        try:
            try:
                # ProtoCC.g:292:17: ( expressions | network_send | network_mcast | network_bcast | transaction )
                alt32 = 5
                LA32 = self.input.LA(1)
                if LA32 in {ID}:
                    LA32_1 = self.input.LA(2)

                    if (LA32_1 == DOT) :
                        LA32 = self.input.LA(3)
                        if LA32 in {ID, NID, 137, 139, 141, 142, 143, 147}:
                            alt32 = 1
                        elif LA32 in {132, 146}:
                            alt32 = 2
                        elif LA32 in {123, 144}:
                            alt32 = 3
                        elif LA32 in {118, 138}:
                            alt32 = 4
                        else:
                            nvae = NoViableAltException("", 32, 9, self.input)

                            raise nvae


                    elif (LA32_1 in {EQUALSIGN, OBRACE, SEMICOLON}) :
                        alt32 = 1
                    else:
                        nvae = NoViableAltException("", 32, 1, self.input)

                        raise nvae


                elif LA32 in {ACCESS, IF, STALL, STATE, UNDEF, 121}:
                    alt32 = 1
                elif LA32 in {AWAIT}:
                    alt32 = 5
                else:
                    nvae = NoViableAltException("", 32, 0, self.input)

                    raise nvae


                if alt32 == 1:
                    # ProtoCC.g:292:19: expressions
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_expressions_in_process_expr2502)
                    expressions203 = self.expressions()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, expressions203.tree)



                elif alt32 == 2:
                    # ProtoCC.g:292:33: network_send
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_network_send_in_process_expr2506)
                    network_send204 = self.network_send()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, network_send204.tree)



                elif alt32 == 3:
                    # ProtoCC.g:292:48: network_mcast
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_network_mcast_in_process_expr2510)
                    network_mcast205 = self.network_mcast()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, network_mcast205.tree)



                elif alt32 == 4:
                    # ProtoCC.g:292:64: network_bcast
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_network_bcast_in_process_expr2514)
                    network_bcast206 = self.network_bcast()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, network_bcast206.tree)



                elif alt32 == 5:
                    # ProtoCC.g:292:79: transaction
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_transaction_in_process_expr2517)
                    transaction207 = self.transaction()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, transaction207.tree)



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
    # ProtoCC.g:295:1: transaction : AWAIT OCBRACE ( trans )* CCBRACE -> ^( AWAIT_ ( trans )* ) ;
    def transaction(self, ):
        retval = self.transaction_return()
        retval.start = self.input.LT(1)


        root_0 = None

        AWAIT208 = None
        OCBRACE209 = None
        CCBRACE211 = None
        trans210 = None

        AWAIT208_tree = None
        OCBRACE209_tree = None
        CCBRACE211_tree = None
        stream_OCBRACE = RewriteRuleTokenStream(self._adaptor, "token OCBRACE")
        stream_AWAIT = RewriteRuleTokenStream(self._adaptor, "token AWAIT")
        stream_CCBRACE = RewriteRuleTokenStream(self._adaptor, "token CCBRACE")
        stream_trans = RewriteRuleSubtreeStream(self._adaptor, "rule trans")
        try:
            try:
                # ProtoCC.g:295:13: ( AWAIT OCBRACE ( trans )* CCBRACE -> ^( AWAIT_ ( trans )* ) )
                # ProtoCC.g:295:15: AWAIT OCBRACE ( trans )* CCBRACE
                pass 
                AWAIT208 = self.match(self.input, AWAIT, self.FOLLOW_AWAIT_in_transaction2527) 
                stream_AWAIT.add(AWAIT208)


                OCBRACE209 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_transaction2529) 
                stream_OCBRACE.add(OCBRACE209)


                # ProtoCC.g:295:29: ( trans )*
                while True: #loop33
                    alt33 = 2
                    LA33_0 = self.input.LA(1)

                    if (LA33_0 == WHEN) :
                        alt33 = 1


                    if alt33 == 1:
                        # ProtoCC.g:295:29: trans
                        pass 
                        self._state.following.append(self.FOLLOW_trans_in_transaction2531)
                        trans210 = self.trans()

                        self._state.following.pop()
                        stream_trans.add(trans210.tree)



                    else:
                        break #loop33


                CCBRACE211 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_transaction2534) 
                stream_CCBRACE.add(CCBRACE211)


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
                # 295:44: -> ^( AWAIT_ ( trans )* )
                # ProtoCC.g:295:47: ^( AWAIT_ ( trans )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(AWAIT_, "AWAIT_")
                , root_1)

                # ProtoCC.g:295:56: ( trans )*
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
    # ProtoCC.g:296:5: trans : WHEN ID DDOT ( trans_body )* -> ^( WHEN_ ^( GUARD_ ID ) ( trans_body )* ENDWHEN_ ) ;
    def trans(self, ):
        retval = self.trans_return()
        retval.start = self.input.LT(1)


        root_0 = None

        WHEN212 = None
        ID213 = None
        DDOT214 = None
        trans_body215 = None

        WHEN212_tree = None
        ID213_tree = None
        DDOT214_tree = None
        stream_WHEN = RewriteRuleTokenStream(self._adaptor, "token WHEN")
        stream_DDOT = RewriteRuleTokenStream(self._adaptor, "token DDOT")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_trans_body = RewriteRuleSubtreeStream(self._adaptor, "rule trans_body")
        try:
            try:
                # ProtoCC.g:296:11: ( WHEN ID DDOT ( trans_body )* -> ^( WHEN_ ^( GUARD_ ID ) ( trans_body )* ENDWHEN_ ) )
                # ProtoCC.g:296:13: WHEN ID DDOT ( trans_body )*
                pass 
                WHEN212 = self.match(self.input, WHEN, self.FOLLOW_WHEN_in_trans2554) 
                stream_WHEN.add(WHEN212)


                ID213 = self.match(self.input, ID, self.FOLLOW_ID_in_trans2556) 
                stream_ID.add(ID213)


                DDOT214 = self.match(self.input, DDOT, self.FOLLOW_DDOT_in_trans2558) 
                stream_DDOT.add(DDOT214)


                # ProtoCC.g:296:26: ( trans_body )*
                while True: #loop34
                    alt34 = 2
                    LA34_0 = self.input.LA(1)

                    if (LA34_0 in {ACCESS, AWAIT, BREAK, ID, IF, NEXT, STALL, STATE, UNDEF, 121}) :
                        alt34 = 1


                    if alt34 == 1:
                        # ProtoCC.g:296:26: trans_body
                        pass 
                        self._state.following.append(self.FOLLOW_trans_body_in_trans2560)
                        trans_body215 = self.trans_body()

                        self._state.following.pop()
                        stream_trans_body.add(trans_body215.tree)



                    else:
                        break #loop34


                # AST Rewrite
                # elements: trans_body, ID
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
                # 296:38: -> ^( WHEN_ ^( GUARD_ ID ) ( trans_body )* ENDWHEN_ )
                # ProtoCC.g:296:41: ^( WHEN_ ^( GUARD_ ID ) ( trans_body )* ENDWHEN_ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(WHEN_, "WHEN_")
                , root_1)

                # ProtoCC.g:296:49: ^( GUARD_ ID )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(GUARD_, "GUARD_")
                , root_2)

                self._adaptor.addChild(root_2, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_1, root_2)

                # ProtoCC.g:296:62: ( trans_body )*
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
    # ProtoCC.g:297:9: trans_body : ( expressions | next_trans | next_break | transaction | network_send | network_mcast | network_bcast );
    def trans_body(self, ):
        retval = self.trans_body_return()
        retval.start = self.input.LT(1)


        root_0 = None

        expressions216 = None
        next_trans217 = None
        next_break218 = None
        transaction219 = None
        network_send220 = None
        network_mcast221 = None
        network_bcast222 = None


        try:
            try:
                # ProtoCC.g:297:20: ( expressions | next_trans | next_break | transaction | network_send | network_mcast | network_bcast )
                alt35 = 7
                LA35 = self.input.LA(1)
                if LA35 in {ID}:
                    LA35_1 = self.input.LA(2)

                    if (LA35_1 == DOT) :
                        LA35 = self.input.LA(3)
                        if LA35 in {ID, NID, 137, 139, 141, 142, 143, 147}:
                            alt35 = 1
                        elif LA35 in {132, 146}:
                            alt35 = 5
                        elif LA35 in {123, 144}:
                            alt35 = 6
                        elif LA35 in {118, 138}:
                            alt35 = 7
                        else:
                            nvae = NoViableAltException("", 35, 11, self.input)

                            raise nvae


                    elif (LA35_1 in {EQUALSIGN, OBRACE, SEMICOLON}) :
                        alt35 = 1
                    else:
                        nvae = NoViableAltException("", 35, 1, self.input)

                        raise nvae


                elif LA35 in {ACCESS, IF, STALL, STATE, UNDEF, 121}:
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
                    # ProtoCC.g:297:22: expressions
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_expressions_in_trans_body2593)
                    expressions216 = self.expressions()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, expressions216.tree)



                elif alt35 == 2:
                    # ProtoCC.g:297:36: next_trans
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_next_trans_in_trans_body2597)
                    next_trans217 = self.next_trans()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, next_trans217.tree)



                elif alt35 == 3:
                    # ProtoCC.g:297:49: next_break
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_next_break_in_trans_body2601)
                    next_break218 = self.next_break()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, next_break218.tree)



                elif alt35 == 4:
                    # ProtoCC.g:297:62: transaction
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_transaction_in_trans_body2605)
                    transaction219 = self.transaction()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, transaction219.tree)



                elif alt35 == 5:
                    # ProtoCC.g:297:76: network_send
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_network_send_in_trans_body2609)
                    network_send220 = self.network_send()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, network_send220.tree)



                elif alt35 == 6:
                    # ProtoCC.g:297:91: network_mcast
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_network_mcast_in_trans_body2613)
                    network_mcast221 = self.network_mcast()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, network_mcast221.tree)



                elif alt35 == 7:
                    # ProtoCC.g:297:107: network_bcast
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_network_bcast_in_trans_body2617)
                    network_bcast222 = self.network_bcast()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, network_bcast222.tree)



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
    # ProtoCC.g:298:13: next_trans : NEXT OCBRACE ( trans )* CCBRACE -> ^( NEXT_ ( trans )* ) ;
    def next_trans(self, ):
        retval = self.next_trans_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEXT223 = None
        OCBRACE224 = None
        CCBRACE226 = None
        trans225 = None

        NEXT223_tree = None
        OCBRACE224_tree = None
        CCBRACE226_tree = None
        stream_OCBRACE = RewriteRuleTokenStream(self._adaptor, "token OCBRACE")
        stream_NEXT = RewriteRuleTokenStream(self._adaptor, "token NEXT")
        stream_CCBRACE = RewriteRuleTokenStream(self._adaptor, "token CCBRACE")
        stream_trans = RewriteRuleSubtreeStream(self._adaptor, "rule trans")
        try:
            try:
                # ProtoCC.g:298:23: ( NEXT OCBRACE ( trans )* CCBRACE -> ^( NEXT_ ( trans )* ) )
                # ProtoCC.g:298:25: NEXT OCBRACE ( trans )* CCBRACE
                pass 
                NEXT223 = self.match(self.input, NEXT, self.FOLLOW_NEXT_in_next_trans2635) 
                stream_NEXT.add(NEXT223)


                OCBRACE224 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_next_trans2637) 
                stream_OCBRACE.add(OCBRACE224)


                # ProtoCC.g:298:38: ( trans )*
                while True: #loop36
                    alt36 = 2
                    LA36_0 = self.input.LA(1)

                    if (LA36_0 == WHEN) :
                        alt36 = 1


                    if alt36 == 1:
                        # ProtoCC.g:298:38: trans
                        pass 
                        self._state.following.append(self.FOLLOW_trans_in_next_trans2639)
                        trans225 = self.trans()

                        self._state.following.pop()
                        stream_trans.add(trans225.tree)



                    else:
                        break #loop36


                CCBRACE226 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_next_trans2642) 
                stream_CCBRACE.add(CCBRACE226)


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
                # 298:53: -> ^( NEXT_ ( trans )* )
                # ProtoCC.g:298:56: ^( NEXT_ ( trans )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(NEXT_, "NEXT_")
                , root_1)

                # ProtoCC.g:298:64: ( trans )*
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
    # ProtoCC.g:300:5: next_break : BREAK SEMICOLON -> ^( BREAK_ ) ;
    def next_break(self, ):
        retval = self.next_break_return()
        retval.start = self.input.LT(1)


        root_0 = None

        BREAK227 = None
        SEMICOLON228 = None

        BREAK227_tree = None
        SEMICOLON228_tree = None
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_BREAK = RewriteRuleTokenStream(self._adaptor, "token BREAK")

        try:
            try:
                # ProtoCC.g:300:16: ( BREAK SEMICOLON -> ^( BREAK_ ) )
                # ProtoCC.g:300:18: BREAK SEMICOLON
                pass 
                BREAK227 = self.match(self.input, BREAK, self.FOLLOW_BREAK_in_next_break2663) 
                stream_BREAK.add(BREAK227)


                SEMICOLON228 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_next_break2665) 
                stream_SEMICOLON.add(SEMICOLON228)


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
                # 300:34: -> ^( BREAK_ )
                # ProtoCC.g:300:37: ^( BREAK_ )
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
    # ProtoCC.g:303:1: expressions : ( assignment | conditional | object_block | function_call_block | set_block | internal_event_block | msg_stall | set_access | undefine );
    def expressions(self, ):
        retval = self.expressions_return()
        retval.start = self.input.LT(1)


        root_0 = None

        assignment229 = None
        conditional230 = None
        object_block231 = None
        function_call_block232 = None
        set_block233 = None
        internal_event_block234 = None
        msg_stall235 = None
        set_access236 = None
        undefine237 = None


        try:
            try:
                # ProtoCC.g:303:13: ( assignment | conditional | object_block | function_call_block | set_block | internal_event_block | msg_stall | set_access | undefine )
                alt37 = 9
                LA37 = self.input.LA(1)
                if LA37 in {ID}:
                    LA37 = self.input.LA(2)
                    if LA37 in {DOT}:
                        LA37_8 = self.input.LA(3)

                        if (LA37_8 in {ID, NID}) :
                            alt37 = 3
                        elif (LA37_8 in {137, 139, 141, 142, 143, 147}) :
                            alt37 = 5
                        else:
                            nvae = NoViableAltException("", 37, 8, self.input)

                            raise nvae


                    elif LA37 in {OBRACE}:
                        alt37 = 4
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
                elif LA37 in {121}:
                    alt37 = 6
                elif LA37 in {STALL}:
                    alt37 = 7
                elif LA37 in {ACCESS}:
                    alt37 = 8
                elif LA37 in {UNDEF}:
                    alt37 = 9
                else:
                    nvae = NoViableAltException("", 37, 0, self.input)

                    raise nvae


                if alt37 == 1:
                    # ProtoCC.g:303:15: assignment
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_assignment_in_expressions2681)
                    assignment229 = self.assignment()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, assignment229.tree)



                elif alt37 == 2:
                    # ProtoCC.g:303:28: conditional
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_conditional_in_expressions2685)
                    conditional230 = self.conditional()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, conditional230.tree)



                elif alt37 == 3:
                    # ProtoCC.g:303:42: object_block
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_object_block_in_expressions2689)
                    object_block231 = self.object_block()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, object_block231.tree)



                elif alt37 == 4:
                    # ProtoCC.g:303:57: function_call_block
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_function_call_block_in_expressions2693)
                    function_call_block232 = self.function_call_block()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, function_call_block232.tree)



                elif alt37 == 5:
                    # ProtoCC.g:303:79: set_block
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_set_block_in_expressions2697)
                    set_block233 = self.set_block()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, set_block233.tree)



                elif alt37 == 6:
                    # ProtoCC.g:303:91: internal_event_block
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_internal_event_block_in_expressions2701)
                    internal_event_block234 = self.internal_event_block()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, internal_event_block234.tree)



                elif alt37 == 7:
                    # ProtoCC.g:303:114: msg_stall
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_msg_stall_in_expressions2705)
                    msg_stall235 = self.msg_stall()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, msg_stall235.tree)



                elif alt37 == 8:
                    # ProtoCC.g:303:126: set_access
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_set_access_in_expressions2709)
                    set_access236 = self.set_access()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, set_access236.tree)



                elif alt37 == 9:
                    # ProtoCC.g:303:139: undefine
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_undefine_in_expressions2713)
                    undefine237 = self.undefine()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, undefine237.tree)



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
    # ProtoCC.g:304:1: assignment : process_finalident EQUALSIGN assign_types SEMICOLON -> ^( ASSIGN_ process_finalident EQUALSIGN assign_types ) ;
    def assignment(self, ):
        retval = self.assignment_return()
        retval.start = self.input.LT(1)


        root_0 = None

        EQUALSIGN239 = None
        SEMICOLON241 = None
        process_finalident238 = None
        assign_types240 = None

        EQUALSIGN239_tree = None
        SEMICOLON241_tree = None
        stream_EQUALSIGN = RewriteRuleTokenStream(self._adaptor, "token EQUALSIGN")
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_assign_types = RewriteRuleSubtreeStream(self._adaptor, "rule assign_types")
        stream_process_finalident = RewriteRuleSubtreeStream(self._adaptor, "rule process_finalident")
        try:
            try:
                # ProtoCC.g:304:12: ( process_finalident EQUALSIGN assign_types SEMICOLON -> ^( ASSIGN_ process_finalident EQUALSIGN assign_types ) )
                # ProtoCC.g:304:14: process_finalident EQUALSIGN assign_types SEMICOLON
                pass 
                self._state.following.append(self.FOLLOW_process_finalident_in_assignment2720)
                process_finalident238 = self.process_finalident()

                self._state.following.pop()
                stream_process_finalident.add(process_finalident238.tree)


                EQUALSIGN239 = self.match(self.input, EQUALSIGN, self.FOLLOW_EQUALSIGN_in_assignment2722) 
                stream_EQUALSIGN.add(EQUALSIGN239)


                self._state.following.append(self.FOLLOW_assign_types_in_assignment2724)
                assign_types240 = self.assign_types()

                self._state.following.pop()
                stream_assign_types.add(assign_types240.tree)


                SEMICOLON241 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_assignment2726) 
                stream_SEMICOLON.add(SEMICOLON241)


                # AST Rewrite
                # elements: assign_types, process_finalident, EQUALSIGN
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
                # 304:65: -> ^( ASSIGN_ process_finalident EQUALSIGN assign_types )
                # ProtoCC.g:304:68: ^( ASSIGN_ process_finalident EQUALSIGN assign_types )
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
    # ProtoCC.g:305:5: assign_types : ( object_expr | message_constr | math_op | set_func | INT | BOOL | NID );
    def assign_types(self, ):
        retval = self.assign_types_return()
        retval.start = self.input.LT(1)


        root_0 = None

        INT246 = None
        BOOL247 = None
        NID248 = None
        object_expr242 = None
        message_constr243 = None
        math_op244 = None
        set_func245 = None

        INT246_tree = None
        BOOL247_tree = None
        NID248_tree = None

        try:
            try:
                # ProtoCC.g:305:18: ( object_expr | message_constr | math_op | set_func | INT | BOOL | NID )
                alt38 = 7
                LA38 = self.input.LA(1)
                if LA38 in {ID}:
                    LA38 = self.input.LA(2)
                    if LA38 in {DOT}:
                        LA38_5 = self.input.LA(3)

                        if (LA38_5 in {ID, NID}) :
                            alt38 = 1
                        elif (LA38_5 in {137, 139, 141, 142, 143, 147}) :
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
                    # ProtoCC.g:305:20: object_expr
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_object_expr_in_assign_types2748)
                    object_expr242 = self.object_expr()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, object_expr242.tree)



                elif alt38 == 2:
                    # ProtoCC.g:305:34: message_constr
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_message_constr_in_assign_types2752)
                    message_constr243 = self.message_constr()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, message_constr243.tree)



                elif alt38 == 3:
                    # ProtoCC.g:305:51: math_op
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_math_op_in_assign_types2756)
                    math_op244 = self.math_op()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, math_op244.tree)



                elif alt38 == 4:
                    # ProtoCC.g:305:61: set_func
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_set_func_in_assign_types2760)
                    set_func245 = self.set_func()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, set_func245.tree)



                elif alt38 == 5:
                    # ProtoCC.g:305:72: INT
                    pass 
                    root_0 = self._adaptor.nil()


                    INT246 = self.match(self.input, INT, self.FOLLOW_INT_in_assign_types2764)
                    INT246_tree = self._adaptor.createWithPayload(INT246)
                    self._adaptor.addChild(root_0, INT246_tree)




                elif alt38 == 6:
                    # ProtoCC.g:305:78: BOOL
                    pass 
                    root_0 = self._adaptor.nil()


                    BOOL247 = self.match(self.input, BOOL, self.FOLLOW_BOOL_in_assign_types2768)
                    BOOL247_tree = self._adaptor.createWithPayload(BOOL247)
                    self._adaptor.addChild(root_0, BOOL247_tree)




                elif alt38 == 7:
                    # ProtoCC.g:305:85: NID
                    pass 
                    root_0 = self._adaptor.nil()


                    NID248 = self.match(self.input, NID, self.FOLLOW_NID_in_assign_types2772)
                    NID248_tree = self._adaptor.createWithPayload(NID248)
                    self._adaptor.addChild(root_0, NID248_tree)




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
    # ProtoCC.g:306:5: math_op : val_range ( PLUS | MINUS ) val_range ;
    def math_op(self, ):
        retval = self.math_op_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set250 = None
        val_range249 = None
        val_range251 = None

        set250_tree = None

        try:
            try:
                # ProtoCC.g:306:13: ( val_range ( PLUS | MINUS ) val_range )
                # ProtoCC.g:306:15: val_range ( PLUS | MINUS ) val_range
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_val_range_in_math_op2783)
                val_range249 = self.val_range()

                self._state.following.pop()
                self._adaptor.addChild(root_0, val_range249.tree)


                set250 = self.input.LT(1)

                if self.input.LA(1) in {MINUS, PLUS}:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set250))

                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse



                self._state.following.append(self.FOLLOW_val_range_in_math_op2793)
                val_range251 = self.val_range()

                self._state.following.pop()
                self._adaptor.addChild(root_0, val_range251.tree)




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
    # ProtoCC.g:307:1: msg_stall : STALL SEMICOLON -> ^( STALL_ ) ;
    def msg_stall(self, ):
        retval = self.msg_stall_return()
        retval.start = self.input.LT(1)


        root_0 = None

        STALL252 = None
        SEMICOLON253 = None

        STALL252_tree = None
        SEMICOLON253_tree = None
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_STALL = RewriteRuleTokenStream(self._adaptor, "token STALL")

        try:
            try:
                # ProtoCC.g:307:10: ( STALL SEMICOLON -> ^( STALL_ ) )
                # ProtoCC.g:307:12: STALL SEMICOLON
                pass 
                STALL252 = self.match(self.input, STALL, self.FOLLOW_STALL_in_msg_stall2799) 
                stream_STALL.add(STALL252)


                SEMICOLON253 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_msg_stall2801) 
                stream_SEMICOLON.add(SEMICOLON253)


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
                # 307:28: -> ^( STALL_ )
                # ProtoCC.g:307:31: ^( STALL_ )
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
    # ProtoCC.g:308:1: set_access : ACCESS SEMICOLON -> ^( ACCESS_ ACCESS ) ;
    def set_access(self, ):
        retval = self.set_access_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ACCESS254 = None
        SEMICOLON255 = None

        ACCESS254_tree = None
        SEMICOLON255_tree = None
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_ACCESS = RewriteRuleTokenStream(self._adaptor, "token ACCESS")

        try:
            try:
                # ProtoCC.g:308:11: ( ACCESS SEMICOLON -> ^( ACCESS_ ACCESS ) )
                # ProtoCC.g:308:13: ACCESS SEMICOLON
                pass 
                ACCESS254 = self.match(self.input, ACCESS, self.FOLLOW_ACCESS_in_set_access2813) 
                stream_ACCESS.add(ACCESS254)


                SEMICOLON255 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_set_access2815) 
                stream_SEMICOLON.add(SEMICOLON255)


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
                # 308:30: -> ^( ACCESS_ ACCESS )
                # ProtoCC.g:308:33: ^( ACCESS_ ACCESS )
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
    # ProtoCC.g:309:1: undefine : UNDEF ID SEMICOLON -> ^( UNDEF_ ID ) ;
    def undefine(self, ):
        retval = self.undefine_return()
        retval.start = self.input.LT(1)


        root_0 = None

        UNDEF256 = None
        ID257 = None
        SEMICOLON258 = None

        UNDEF256_tree = None
        ID257_tree = None
        SEMICOLON258_tree = None
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_UNDEF = RewriteRuleTokenStream(self._adaptor, "token UNDEF")

        try:
            try:
                # ProtoCC.g:309:9: ( UNDEF ID SEMICOLON -> ^( UNDEF_ ID ) )
                # ProtoCC.g:309:11: UNDEF ID SEMICOLON
                pass 
                UNDEF256 = self.match(self.input, UNDEF, self.FOLLOW_UNDEF_in_undefine2829) 
                stream_UNDEF.add(UNDEF256)


                ID257 = self.match(self.input, ID, self.FOLLOW_ID_in_undefine2831) 
                stream_ID.add(ID257)


                SEMICOLON258 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_undefine2833) 
                stream_SEMICOLON.add(SEMICOLON258)


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
                # 309:30: -> ^( UNDEF_ ID )
                # ProtoCC.g:309:33: ^( UNDEF_ ID )
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
    # ProtoCC.g:312:1: conditional : ( if_stmt | ifnot_stmt );
    def conditional(self, ):
        retval = self.conditional_return()
        retval.start = self.input.LT(1)


        root_0 = None

        if_stmt259 = None
        ifnot_stmt260 = None


        try:
            try:
                # ProtoCC.g:312:12: ( if_stmt | ifnot_stmt )
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
                    # ProtoCC.g:312:14: if_stmt
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_if_stmt_in_conditional2850)
                    if_stmt259 = self.if_stmt()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, if_stmt259.tree)



                elif alt39 == 2:
                    # ProtoCC.g:312:24: ifnot_stmt
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_ifnot_stmt_in_conditional2854)
                    ifnot_stmt260 = self.ifnot_stmt()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, ifnot_stmt260.tree)



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
    # ProtoCC.g:313:5: if_stmt : IF cond_comb OCBRACE if_expression CCBRACE ( ELSE OCBRACE else_expression CCBRACE )* -> {t_else}? ^( IFELSE_ ^( IF_ ^( COND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( NCOND_ cond_comb ) ( else_expression )* ENDIF_ ) ) -> ^( IFELSE_ ^( IF_ ^( COND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( NCOND_ cond_comb ) ENDIF_ ) ) ;
    def if_stmt(self, ):
        retval = self.if_stmt_return()
        retval.start = self.input.LT(1)


        root_0 = None

        IF261 = None
        OCBRACE263 = None
        CCBRACE265 = None
        ELSE266 = None
        OCBRACE267 = None
        CCBRACE269 = None
        cond_comb262 = None
        if_expression264 = None
        else_expression268 = None

        IF261_tree = None
        OCBRACE263_tree = None
        CCBRACE265_tree = None
        ELSE266_tree = None
        OCBRACE267_tree = None
        CCBRACE269_tree = None
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
                # ProtoCC.g:314:5: ( IF cond_comb OCBRACE if_expression CCBRACE ( ELSE OCBRACE else_expression CCBRACE )* -> {t_else}? ^( IFELSE_ ^( IF_ ^( COND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( NCOND_ cond_comb ) ( else_expression )* ENDIF_ ) ) -> ^( IFELSE_ ^( IF_ ^( COND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( NCOND_ cond_comb ) ENDIF_ ) ) )
                # ProtoCC.g:314:7: IF cond_comb OCBRACE if_expression CCBRACE ( ELSE OCBRACE else_expression CCBRACE )*
                pass 
                IF261 = self.match(self.input, IF, self.FOLLOW_IF_in_if_stmt2873) 
                stream_IF.add(IF261)


                self._state.following.append(self.FOLLOW_cond_comb_in_if_stmt2875)
                cond_comb262 = self.cond_comb()

                self._state.following.pop()
                stream_cond_comb.add(cond_comb262.tree)


                OCBRACE263 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_if_stmt2877) 
                stream_OCBRACE.add(OCBRACE263)


                self._state.following.append(self.FOLLOW_if_expression_in_if_stmt2879)
                if_expression264 = self.if_expression()

                self._state.following.pop()
                stream_if_expression.add(if_expression264.tree)


                CCBRACE265 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_if_stmt2881) 
                stream_CCBRACE.add(CCBRACE265)


                # ProtoCC.g:315:5: ( ELSE OCBRACE else_expression CCBRACE )*
                while True: #loop40
                    alt40 = 2
                    LA40_0 = self.input.LA(1)

                    if (LA40_0 == ELSE) :
                        alt40 = 1


                    if alt40 == 1:
                        # ProtoCC.g:315:6: ELSE OCBRACE else_expression CCBRACE
                        pass 
                        ELSE266 = self.match(self.input, ELSE, self.FOLLOW_ELSE_in_if_stmt2888) 
                        stream_ELSE.add(ELSE266)


                        #action start
                        t_else=1
                        #action end


                        OCBRACE267 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_if_stmt2892) 
                        stream_OCBRACE.add(OCBRACE267)


                        self._state.following.append(self.FOLLOW_else_expression_in_if_stmt2894)
                        else_expression268 = self.else_expression()

                        self._state.following.pop()
                        stream_else_expression.add(else_expression268.tree)


                        CCBRACE269 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_if_stmt2896) 
                        stream_CCBRACE.add(CCBRACE269)



                    else:
                        break #loop40


                # AST Rewrite
                # elements: if_expression, cond_comb, cond_comb, cond_comb, cond_comb, if_expression, else_expression
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
                    # 316:5: -> {t_else}? ^( IFELSE_ ^( IF_ ^( COND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( NCOND_ cond_comb ) ( else_expression )* ENDIF_ ) )
                    # ProtoCC.g:316:18: ^( IFELSE_ ^( IF_ ^( COND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( NCOND_ cond_comb ) ( else_expression )* ENDIF_ ) )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(IFELSE_, "IFELSE_")
                    , root_1)

                    # ProtoCC.g:316:28: ^( IF_ ^( COND_ cond_comb ) ( if_expression )* ENDIF_ )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(IF_, "IF_")
                    , root_2)

                    # ProtoCC.g:316:34: ^( COND_ cond_comb )
                    root_3 = self._adaptor.nil()
                    root_3 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(COND_, "COND_")
                    , root_3)

                    self._adaptor.addChild(root_3, stream_cond_comb.nextTree())

                    self._adaptor.addChild(root_2, root_3)

                    # ProtoCC.g:316:53: ( if_expression )*
                    while stream_if_expression.hasNext():
                        self._adaptor.addChild(root_2, stream_if_expression.nextTree())


                    stream_if_expression.reset();

                    self._adaptor.addChild(root_2, 
                    self._adaptor.createFromType(ENDIF_, "ENDIF_")
                    )

                    self._adaptor.addChild(root_1, root_2)

                    # ProtoCC.g:316:76: ^( IF_ ^( NCOND_ cond_comb ) ( else_expression )* ENDIF_ )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(IF_, "IF_")
                    , root_2)

                    # ProtoCC.g:316:82: ^( NCOND_ cond_comb )
                    root_3 = self._adaptor.nil()
                    root_3 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(NCOND_, "NCOND_")
                    , root_3)

                    self._adaptor.addChild(root_3, stream_cond_comb.nextTree())

                    self._adaptor.addChild(root_2, root_3)

                    # ProtoCC.g:316:102: ( else_expression )*
                    while stream_else_expression.hasNext():
                        self._adaptor.addChild(root_2, stream_else_expression.nextTree())


                    stream_else_expression.reset();

                    self._adaptor.addChild(root_2, 
                    self._adaptor.createFromType(ENDIF_, "ENDIF_")
                    )

                    self._adaptor.addChild(root_1, root_2)

                    self._adaptor.addChild(root_0, root_1)



                else: 
                    # 317:5: -> ^( IFELSE_ ^( IF_ ^( COND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( NCOND_ cond_comb ) ENDIF_ ) )
                    # ProtoCC.g:317:8: ^( IFELSE_ ^( IF_ ^( COND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( NCOND_ cond_comb ) ENDIF_ ) )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(IFELSE_, "IFELSE_")
                    , root_1)

                    # ProtoCC.g:317:18: ^( IF_ ^( COND_ cond_comb ) ( if_expression )* ENDIF_ )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(IF_, "IF_")
                    , root_2)

                    # ProtoCC.g:317:24: ^( COND_ cond_comb )
                    root_3 = self._adaptor.nil()
                    root_3 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(COND_, "COND_")
                    , root_3)

                    self._adaptor.addChild(root_3, stream_cond_comb.nextTree())

                    self._adaptor.addChild(root_2, root_3)

                    # ProtoCC.g:317:43: ( if_expression )*
                    while stream_if_expression.hasNext():
                        self._adaptor.addChild(root_2, stream_if_expression.nextTree())


                    stream_if_expression.reset();

                    self._adaptor.addChild(root_2, 
                    self._adaptor.createFromType(ENDIF_, "ENDIF_")
                    )

                    self._adaptor.addChild(root_1, root_2)

                    # ProtoCC.g:317:66: ^( IF_ ^( NCOND_ cond_comb ) ENDIF_ )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(IF_, "IF_")
                    , root_2)

                    # ProtoCC.g:317:72: ^( NCOND_ cond_comb )
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
    # ProtoCC.g:320:5: ifnot_stmt : IF NEG cond_comb OCBRACE if_expression CCBRACE ( ELSE OCBRACE else_expression CCBRACE )* -> {t_else}? ^( IFELSE_ ^( IF_ ^( NCOND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( COND_ cond_comb ) ( else_expression )* ENDIF_ ) ) -> ^( IFELSE_ ^( IF_ ^( NCOND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( COND_ cond_comb ) ENDIF_ ) ) ;
    def ifnot_stmt(self, ):
        retval = self.ifnot_stmt_return()
        retval.start = self.input.LT(1)


        root_0 = None

        IF270 = None
        NEG271 = None
        OCBRACE273 = None
        CCBRACE275 = None
        ELSE276 = None
        OCBRACE277 = None
        CCBRACE279 = None
        cond_comb272 = None
        if_expression274 = None
        else_expression278 = None

        IF270_tree = None
        NEG271_tree = None
        OCBRACE273_tree = None
        CCBRACE275_tree = None
        ELSE276_tree = None
        OCBRACE277_tree = None
        CCBRACE279_tree = None
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
                # ProtoCC.g:321:5: ( IF NEG cond_comb OCBRACE if_expression CCBRACE ( ELSE OCBRACE else_expression CCBRACE )* -> {t_else}? ^( IFELSE_ ^( IF_ ^( NCOND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( COND_ cond_comb ) ( else_expression )* ENDIF_ ) ) -> ^( IFELSE_ ^( IF_ ^( NCOND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( COND_ cond_comb ) ENDIF_ ) ) )
                # ProtoCC.g:321:7: IF NEG cond_comb OCBRACE if_expression CCBRACE ( ELSE OCBRACE else_expression CCBRACE )*
                pass 
                IF270 = self.match(self.input, IF, self.FOLLOW_IF_in_ifnot_stmt3002) 
                stream_IF.add(IF270)


                NEG271 = self.match(self.input, NEG, self.FOLLOW_NEG_in_ifnot_stmt3004) 
                stream_NEG.add(NEG271)


                self._state.following.append(self.FOLLOW_cond_comb_in_ifnot_stmt3006)
                cond_comb272 = self.cond_comb()

                self._state.following.pop()
                stream_cond_comb.add(cond_comb272.tree)


                OCBRACE273 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_ifnot_stmt3008) 
                stream_OCBRACE.add(OCBRACE273)


                self._state.following.append(self.FOLLOW_if_expression_in_ifnot_stmt3010)
                if_expression274 = self.if_expression()

                self._state.following.pop()
                stream_if_expression.add(if_expression274.tree)


                CCBRACE275 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_ifnot_stmt3012) 
                stream_CCBRACE.add(CCBRACE275)


                # ProtoCC.g:322:5: ( ELSE OCBRACE else_expression CCBRACE )*
                while True: #loop41
                    alt41 = 2
                    LA41_0 = self.input.LA(1)

                    if (LA41_0 == ELSE) :
                        alt41 = 1


                    if alt41 == 1:
                        # ProtoCC.g:322:6: ELSE OCBRACE else_expression CCBRACE
                        pass 
                        ELSE276 = self.match(self.input, ELSE, self.FOLLOW_ELSE_in_ifnot_stmt3019) 
                        stream_ELSE.add(ELSE276)


                        #action start
                        t_else=1
                        #action end


                        OCBRACE277 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_ifnot_stmt3023) 
                        stream_OCBRACE.add(OCBRACE277)


                        self._state.following.append(self.FOLLOW_else_expression_in_ifnot_stmt3025)
                        else_expression278 = self.else_expression()

                        self._state.following.pop()
                        stream_else_expression.add(else_expression278.tree)


                        CCBRACE279 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_ifnot_stmt3027) 
                        stream_CCBRACE.add(CCBRACE279)



                    else:
                        break #loop41


                # AST Rewrite
                # elements: cond_comb, cond_comb, cond_comb, else_expression, cond_comb, if_expression, if_expression
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
                    # 323:5: -> {t_else}? ^( IFELSE_ ^( IF_ ^( NCOND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( COND_ cond_comb ) ( else_expression )* ENDIF_ ) )
                    # ProtoCC.g:323:18: ^( IFELSE_ ^( IF_ ^( NCOND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( COND_ cond_comb ) ( else_expression )* ENDIF_ ) )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(IFELSE_, "IFELSE_")
                    , root_1)

                    # ProtoCC.g:323:28: ^( IF_ ^( NCOND_ cond_comb ) ( if_expression )* ENDIF_ )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(IF_, "IF_")
                    , root_2)

                    # ProtoCC.g:323:34: ^( NCOND_ cond_comb )
                    root_3 = self._adaptor.nil()
                    root_3 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(NCOND_, "NCOND_")
                    , root_3)

                    self._adaptor.addChild(root_3, stream_cond_comb.nextTree())

                    self._adaptor.addChild(root_2, root_3)

                    # ProtoCC.g:323:54: ( if_expression )*
                    while stream_if_expression.hasNext():
                        self._adaptor.addChild(root_2, stream_if_expression.nextTree())


                    stream_if_expression.reset();

                    self._adaptor.addChild(root_2, 
                    self._adaptor.createFromType(ENDIF_, "ENDIF_")
                    )

                    self._adaptor.addChild(root_1, root_2)

                    # ProtoCC.g:323:77: ^( IF_ ^( COND_ cond_comb ) ( else_expression )* ENDIF_ )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(IF_, "IF_")
                    , root_2)

                    # ProtoCC.g:323:83: ^( COND_ cond_comb )
                    root_3 = self._adaptor.nil()
                    root_3 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(COND_, "COND_")
                    , root_3)

                    self._adaptor.addChild(root_3, stream_cond_comb.nextTree())

                    self._adaptor.addChild(root_2, root_3)

                    # ProtoCC.g:323:102: ( else_expression )*
                    while stream_else_expression.hasNext():
                        self._adaptor.addChild(root_2, stream_else_expression.nextTree())


                    stream_else_expression.reset();

                    self._adaptor.addChild(root_2, 
                    self._adaptor.createFromType(ENDIF_, "ENDIF_")
                    )

                    self._adaptor.addChild(root_1, root_2)

                    self._adaptor.addChild(root_0, root_1)



                else: 
                    # 324:5: -> ^( IFELSE_ ^( IF_ ^( NCOND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( COND_ cond_comb ) ENDIF_ ) )
                    # ProtoCC.g:324:8: ^( IFELSE_ ^( IF_ ^( NCOND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( COND_ cond_comb ) ENDIF_ ) )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(IFELSE_, "IFELSE_")
                    , root_1)

                    # ProtoCC.g:324:18: ^( IF_ ^( NCOND_ cond_comb ) ( if_expression )* ENDIF_ )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(IF_, "IF_")
                    , root_2)

                    # ProtoCC.g:324:24: ^( NCOND_ cond_comb )
                    root_3 = self._adaptor.nil()
                    root_3 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(NCOND_, "NCOND_")
                    , root_3)

                    self._adaptor.addChild(root_3, stream_cond_comb.nextTree())

                    self._adaptor.addChild(root_2, root_3)

                    # ProtoCC.g:324:44: ( if_expression )*
                    while stream_if_expression.hasNext():
                        self._adaptor.addChild(root_2, stream_if_expression.nextTree())


                    stream_if_expression.reset();

                    self._adaptor.addChild(root_2, 
                    self._adaptor.createFromType(ENDIF_, "ENDIF_")
                    )

                    self._adaptor.addChild(root_1, root_2)

                    # ProtoCC.g:324:67: ^( IF_ ^( COND_ cond_comb ) ENDIF_ )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(IF_, "IF_")
                    , root_2)

                    # ProtoCC.g:324:73: ^( COND_ cond_comb )
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
    # ProtoCC.g:327:9: if_expression : ( exprwbreak )* ;
    def if_expression(self, ):
        retval = self.if_expression_return()
        retval.start = self.input.LT(1)


        root_0 = None

        exprwbreak280 = None


        try:
            try:
                # ProtoCC.g:327:22: ( ( exprwbreak )* )
                # ProtoCC.g:327:24: ( exprwbreak )*
                pass 
                root_0 = self._adaptor.nil()


                # ProtoCC.g:327:24: ( exprwbreak )*
                while True: #loop42
                    alt42 = 2
                    LA42_0 = self.input.LA(1)

                    if (LA42_0 in {ACCESS, AWAIT, BREAK, ID, IF, STALL, STATE, UNDEF, 121}) :
                        alt42 = 1


                    if alt42 == 1:
                        # ProtoCC.g:327:24: exprwbreak
                        pass 
                        self._state.following.append(self.FOLLOW_exprwbreak_in_if_expression3128)
                        exprwbreak280 = self.exprwbreak()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, exprwbreak280.tree)



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
    # ProtoCC.g:328:9: else_expression : ( exprwbreak )* ;
    def else_expression(self, ):
        retval = self.else_expression_return()
        retval.start = self.input.LT(1)


        root_0 = None

        exprwbreak281 = None


        try:
            try:
                # ProtoCC.g:328:24: ( ( exprwbreak )* )
                # ProtoCC.g:328:26: ( exprwbreak )*
                pass 
                root_0 = self._adaptor.nil()


                # ProtoCC.g:328:26: ( exprwbreak )*
                while True: #loop43
                    alt43 = 2
                    LA43_0 = self.input.LA(1)

                    if (LA43_0 in {ACCESS, AWAIT, BREAK, ID, IF, STALL, STATE, UNDEF, 121}) :
                        alt43 = 1


                    if alt43 == 1:
                        # ProtoCC.g:328:26: exprwbreak
                        pass 
                        self._state.following.append(self.FOLLOW_exprwbreak_in_else_expression3143)
                        exprwbreak281 = self.exprwbreak()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, exprwbreak281.tree)



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
    # ProtoCC.g:329:9: exprwbreak : ( expressions | network_send | network_mcast | network_bcast | transaction | next_break );
    def exprwbreak(self, ):
        retval = self.exprwbreak_return()
        retval.start = self.input.LT(1)


        root_0 = None

        expressions282 = None
        network_send283 = None
        network_mcast284 = None
        network_bcast285 = None
        transaction286 = None
        next_break287 = None


        try:
            try:
                # ProtoCC.g:329:19: ( expressions | network_send | network_mcast | network_bcast | transaction | next_break )
                alt44 = 6
                LA44 = self.input.LA(1)
                if LA44 in {ID}:
                    LA44_1 = self.input.LA(2)

                    if (LA44_1 == DOT) :
                        LA44 = self.input.LA(3)
                        if LA44 in {ID, NID, 137, 139, 141, 142, 143, 147}:
                            alt44 = 1
                        elif LA44 in {132, 146}:
                            alt44 = 2
                        elif LA44 in {123, 144}:
                            alt44 = 3
                        elif LA44 in {118, 138}:
                            alt44 = 4
                        else:
                            nvae = NoViableAltException("", 44, 10, self.input)

                            raise nvae


                    elif (LA44_1 in {EQUALSIGN, OBRACE, SEMICOLON}) :
                        alt44 = 1
                    else:
                        nvae = NoViableAltException("", 44, 1, self.input)

                        raise nvae


                elif LA44 in {ACCESS, IF, STALL, STATE, UNDEF, 121}:
                    alt44 = 1
                elif LA44 in {AWAIT}:
                    alt44 = 5
                elif LA44 in {BREAK}:
                    alt44 = 6
                else:
                    nvae = NoViableAltException("", 44, 0, self.input)

                    raise nvae


                if alt44 == 1:
                    # ProtoCC.g:329:21: expressions
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_expressions_in_exprwbreak3158)
                    expressions282 = self.expressions()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, expressions282.tree)



                elif alt44 == 2:
                    # ProtoCC.g:329:35: network_send
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_network_send_in_exprwbreak3162)
                    network_send283 = self.network_send()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, network_send283.tree)



                elif alt44 == 3:
                    # ProtoCC.g:329:50: network_mcast
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_network_mcast_in_exprwbreak3166)
                    network_mcast284 = self.network_mcast()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, network_mcast284.tree)



                elif alt44 == 4:
                    # ProtoCC.g:329:66: network_bcast
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_network_bcast_in_exprwbreak3170)
                    network_bcast285 = self.network_bcast()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, network_bcast285.tree)



                elif alt44 == 5:
                    # ProtoCC.g:329:82: transaction
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_transaction_in_exprwbreak3174)
                    transaction286 = self.transaction()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, transaction286.tree)



                elif alt44 == 6:
                    # ProtoCC.g:329:96: next_break
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_next_break_in_exprwbreak3178)
                    next_break287 = self.next_break()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, next_break287.tree)



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
    # ProtoCC.g:330:9: cond_comb : cond_rel ( combinatorial_operator cond_rel )* ;
    def cond_comb(self, ):
        retval = self.cond_comb_return()
        retval.start = self.input.LT(1)


        root_0 = None

        cond_rel288 = None
        combinatorial_operator289 = None
        cond_rel290 = None


        try:
            try:
                # ProtoCC.g:330:18: ( cond_rel ( combinatorial_operator cond_rel )* )
                # ProtoCC.g:330:20: cond_rel ( combinatorial_operator cond_rel )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_cond_rel_in_cond_comb3192)
                cond_rel288 = self.cond_rel()

                self._state.following.pop()
                self._adaptor.addChild(root_0, cond_rel288.tree)


                # ProtoCC.g:330:29: ( combinatorial_operator cond_rel )*
                while True: #loop45
                    alt45 = 2
                    LA45_0 = self.input.LA(1)

                    if (LA45_0 in {112, 148}) :
                        alt45 = 1


                    if alt45 == 1:
                        # ProtoCC.g:330:30: combinatorial_operator cond_rel
                        pass 
                        self._state.following.append(self.FOLLOW_combinatorial_operator_in_cond_comb3195)
                        combinatorial_operator289 = self.combinatorial_operator()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, combinatorial_operator289.tree)


                        self._state.following.append(self.FOLLOW_cond_rel_in_cond_comb3197)
                        cond_rel290 = self.cond_rel()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, cond_rel290.tree)



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
    # ProtoCC.g:331:9: cond_rel : ( OBRACE )* cond_sel ( CBRACE )* -> cond_sel ;
    def cond_rel(self, ):
        retval = self.cond_rel_return()
        retval.start = self.input.LT(1)


        root_0 = None

        OBRACE291 = None
        CBRACE293 = None
        cond_sel292 = None

        OBRACE291_tree = None
        CBRACE293_tree = None
        stream_OBRACE = RewriteRuleTokenStream(self._adaptor, "token OBRACE")
        stream_CBRACE = RewriteRuleTokenStream(self._adaptor, "token CBRACE")
        stream_cond_sel = RewriteRuleSubtreeStream(self._adaptor, "rule cond_sel")
        try:
            try:
                # ProtoCC.g:331:18: ( ( OBRACE )* cond_sel ( CBRACE )* -> cond_sel )
                # ProtoCC.g:331:20: ( OBRACE )* cond_sel ( CBRACE )*
                pass 
                # ProtoCC.g:331:20: ( OBRACE )*
                while True: #loop46
                    alt46 = 2
                    LA46_0 = self.input.LA(1)

                    if (LA46_0 == OBRACE) :
                        alt46 = 1


                    if alt46 == 1:
                        # ProtoCC.g:331:20: OBRACE
                        pass 
                        OBRACE291 = self.match(self.input, OBRACE, self.FOLLOW_OBRACE_in_cond_rel3214) 
                        stream_OBRACE.add(OBRACE291)



                    else:
                        break #loop46


                self._state.following.append(self.FOLLOW_cond_sel_in_cond_rel3217)
                cond_sel292 = self.cond_sel()

                self._state.following.pop()
                stream_cond_sel.add(cond_sel292.tree)


                # ProtoCC.g:331:37: ( CBRACE )*
                while True: #loop47
                    alt47 = 2
                    LA47_0 = self.input.LA(1)

                    if (LA47_0 == CBRACE) :
                        alt47 = 1


                    if alt47 == 1:
                        # ProtoCC.g:331:37: CBRACE
                        pass 
                        CBRACE293 = self.match(self.input, CBRACE, self.FOLLOW_CBRACE_in_cond_rel3219) 
                        stream_CBRACE.add(CBRACE293)



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
                # 331:45: -> cond_sel
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
    # ProtoCC.g:332:13: cond_sel : cond_type_expr ( relational_operator cond_type_expr )* ;
    def cond_sel(self, ):
        retval = self.cond_sel_return()
        retval.start = self.input.LT(1)


        root_0 = None

        cond_type_expr294 = None
        relational_operator295 = None
        cond_type_expr296 = None


        try:
            try:
                # ProtoCC.g:332:22: ( cond_type_expr ( relational_operator cond_type_expr )* )
                # ProtoCC.g:332:24: cond_type_expr ( relational_operator cond_type_expr )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_cond_type_expr_in_cond_sel3243)
                cond_type_expr294 = self.cond_type_expr()

                self._state.following.pop()
                self._adaptor.addChild(root_0, cond_type_expr294.tree)


                # ProtoCC.g:332:39: ( relational_operator cond_type_expr )*
                while True: #loop48
                    alt48 = 2
                    LA48_0 = self.input.LA(1)

                    if ((113 <= LA48_0 <= 117) or LA48_0 in {111}) :
                        alt48 = 1


                    if alt48 == 1:
                        # ProtoCC.g:332:40: relational_operator cond_type_expr
                        pass 
                        self._state.following.append(self.FOLLOW_relational_operator_in_cond_sel3246)
                        relational_operator295 = self.relational_operator()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, relational_operator295.tree)


                        self._state.following.append(self.FOLLOW_cond_type_expr_in_cond_sel3248)
                        cond_type_expr296 = self.cond_type_expr()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, cond_type_expr296.tree)



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
    # ProtoCC.g:333:13: cond_type_expr : cond_types ( ( PLUS | MINUS | MULT ) cond_types )* ;
    def cond_type_expr(self, ):
        retval = self.cond_type_expr_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set298 = None
        cond_types297 = None
        cond_types299 = None

        set298_tree = None

        try:
            try:
                # ProtoCC.g:333:27: ( cond_types ( ( PLUS | MINUS | MULT ) cond_types )* )
                # ProtoCC.g:333:29: cond_types ( ( PLUS | MINUS | MULT ) cond_types )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_cond_types_in_cond_type_expr3268)
                cond_types297 = self.cond_types()

                self._state.following.pop()
                self._adaptor.addChild(root_0, cond_types297.tree)


                # ProtoCC.g:333:40: ( ( PLUS | MINUS | MULT ) cond_types )*
                while True: #loop49
                    alt49 = 2
                    LA49_0 = self.input.LA(1)

                    if (LA49_0 in {MINUS, MULT, PLUS}) :
                        alt49 = 1


                    if alt49 == 1:
                        # ProtoCC.g:333:41: ( PLUS | MINUS | MULT ) cond_types
                        pass 
                        set298 = self.input.LT(1)

                        if self.input.LA(1) in {MINUS, MULT, PLUS}:
                            self.input.consume()
                            self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set298))

                            self._state.errorRecovery = False


                        else:
                            mse = MismatchedSetException(None, self.input)
                            raise mse



                        self._state.following.append(self.FOLLOW_cond_types_in_cond_type_expr3283)
                        cond_types299 = self.cond_types()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, cond_types299.tree)



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
    # ProtoCC.g:334:13: cond_types : ( object_expr | set_func | INT | BOOL | NID );
    def cond_types(self, ):
        retval = self.cond_types_return()
        retval.start = self.input.LT(1)


        root_0 = None

        INT302 = None
        BOOL303 = None
        NID304 = None
        object_expr300 = None
        set_func301 = None

        INT302_tree = None
        BOOL303_tree = None
        NID304_tree = None

        try:
            try:
                # ProtoCC.g:334:24: ( object_expr | set_func | INT | BOOL | NID )
                alt50 = 5
                LA50 = self.input.LA(1)
                if LA50 in {ID}:
                    LA50_1 = self.input.LA(2)

                    if (LA50_1 == DOT) :
                        LA50_5 = self.input.LA(3)

                        if (LA50_5 in {ID, NID}) :
                            alt50 = 1
                        elif (LA50_5 in {137, 139, 141, 142, 143, 147}) :
                            alt50 = 2
                        else:
                            nvae = NoViableAltException("", 50, 5, self.input)

                            raise nvae


                    elif ((111 <= LA50_1 <= 117) or LA50_1 in {CBRACE, MINUS, MULT, OCBRACE, PLUS, 148}) :
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
                    # ProtoCC.g:334:26: object_expr
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_object_expr_in_cond_types3304)
                    object_expr300 = self.object_expr()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, object_expr300.tree)



                elif alt50 == 2:
                    # ProtoCC.g:334:40: set_func
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_set_func_in_cond_types3308)
                    set_func301 = self.set_func()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, set_func301.tree)



                elif alt50 == 3:
                    # ProtoCC.g:334:51: INT
                    pass 
                    root_0 = self._adaptor.nil()


                    INT302 = self.match(self.input, INT, self.FOLLOW_INT_in_cond_types3312)
                    INT302_tree = self._adaptor.createWithPayload(INT302)
                    self._adaptor.addChild(root_0, INT302_tree)




                elif alt50 == 4:
                    # ProtoCC.g:334:57: BOOL
                    pass 
                    root_0 = self._adaptor.nil()


                    BOOL303 = self.match(self.input, BOOL, self.FOLLOW_BOOL_in_cond_types3316)
                    BOOL303_tree = self._adaptor.createWithPayload(BOOL303)
                    self._adaptor.addChild(root_0, BOOL303_tree)




                elif alt50 == 5:
                    # ProtoCC.g:334:64: NID
                    pass 
                    root_0 = self._adaptor.nil()


                    NID304 = self.match(self.input, NID, self.FOLLOW_NID_in_cond_types3320)
                    NID304_tree = self._adaptor.createWithPayload(NID304)
                    self._adaptor.addChild(root_0, NID304_tree)




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
    # ProtoCC.g:338:1: policy_op_type : ( 'Rd' | 'Wr' | 'RdWr' | 'None' );
    def policy_op_type(self, ):
        retval = self.policy_op_type_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set305 = None

        set305_tree = None

        try:
            try:
                # ProtoCC.g:338:15: ( 'Rd' | 'Wr' | 'RdWr' | 'None' )
                # ProtoCC.g:
                pass 
                root_0 = self._adaptor.nil()


                set305 = self.input.LT(1)

                if self.input.LA(1) in {125, 129, 130, 134}:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set305))

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
    # ProtoCC.g:339:1: policy_op : ( ( policy_op_type ( '|' policy_op_type )* ) -> ^( POLICY_OP_ ( policy_op_type )+ ) | '_' -> ^( POLICY_OP_ '_' ) );
    def policy_op(self, ):
        retval = self.policy_op_return()
        retval.start = self.input.LT(1)


        root_0 = None

        char_literal307 = None
        char_literal309 = None
        policy_op_type306 = None
        policy_op_type308 = None

        char_literal307_tree = None
        char_literal309_tree = None
        stream_135 = RewriteRuleTokenStream(self._adaptor, "token 135")
        stream_148 = RewriteRuleTokenStream(self._adaptor, "token 148")
        stream_policy_op_type = RewriteRuleSubtreeStream(self._adaptor, "rule policy_op_type")
        try:
            try:
                # ProtoCC.g:340:3: ( ( policy_op_type ( '|' policy_op_type )* ) -> ^( POLICY_OP_ ( policy_op_type )+ ) | '_' -> ^( POLICY_OP_ '_' ) )
                alt52 = 2
                LA52_0 = self.input.LA(1)

                if (LA52_0 in {125, 129, 130, 134}) :
                    alt52 = 1
                elif (LA52_0 == 135) :
                    alt52 = 2
                else:
                    nvae = NoViableAltException("", 52, 0, self.input)

                    raise nvae


                if alt52 == 1:
                    # ProtoCC.g:340:5: ( policy_op_type ( '|' policy_op_type )* )
                    pass 
                    # ProtoCC.g:340:5: ( policy_op_type ( '|' policy_op_type )* )
                    # ProtoCC.g:340:6: policy_op_type ( '|' policy_op_type )*
                    pass 
                    self._state.following.append(self.FOLLOW_policy_op_type_in_policy_op3352)
                    policy_op_type306 = self.policy_op_type()

                    self._state.following.pop()
                    stream_policy_op_type.add(policy_op_type306.tree)


                    # ProtoCC.g:340:21: ( '|' policy_op_type )*
                    while True: #loop51
                        alt51 = 2
                        LA51_0 = self.input.LA(1)

                        if (LA51_0 == 148) :
                            alt51 = 1


                        if alt51 == 1:
                            # ProtoCC.g:340:22: '|' policy_op_type
                            pass 
                            char_literal307 = self.match(self.input, 148, self.FOLLOW_148_in_policy_op3355) 
                            stream_148.add(char_literal307)


                            self._state.following.append(self.FOLLOW_policy_op_type_in_policy_op3357)
                            policy_op_type308 = self.policy_op_type()

                            self._state.following.pop()
                            stream_policy_op_type.add(policy_op_type308.tree)



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
                    # 340:44: -> ^( POLICY_OP_ ( policy_op_type )+ )
                    # ProtoCC.g:340:47: ^( POLICY_OP_ ( policy_op_type )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(POLICY_OP_, "POLICY_OP_")
                    , root_1)

                    # ProtoCC.g:340:60: ( policy_op_type )+
                    if not (stream_policy_op_type.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_policy_op_type.hasNext():
                        self._adaptor.addChild(root_1, stream_policy_op_type.nextTree())


                    stream_policy_op_type.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt52 == 2:
                    # ProtoCC.g:341:4: '_'
                    pass 
                    char_literal309 = self.match(self.input, 135, self.FOLLOW_135_in_policy_op3374) 
                    stream_135.add(char_literal309)


                    # AST Rewrite
                    # elements: 135
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
                    # 341:43: -> ^( POLICY_OP_ '_' )
                    # ProtoCC.g:341:46: ^( POLICY_OP_ '_' )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(POLICY_OP_, "POLICY_OP_")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_135.nextNode()
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
    # ProtoCC.g:344:1: policy_data_type : ( 'Dirty' | 'Clean' | 'P' | 'NP' | 'None' );
    def policy_data_type(self, ):
        retval = self.policy_data_type_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set310 = None

        set310_tree = None

        try:
            try:
                # ProtoCC.g:344:17: ( 'Dirty' | 'Clean' | 'P' | 'NP' | 'None' )
                # ProtoCC.g:
                pass 
                root_0 = self._adaptor.nil()


                set310 = self.input.LT(1)

                if self.input.LA(1) in {119, 120, 124, 125, 127}:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set310))

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
    # ProtoCC.g:345:1: policy_data : ( ( policy_data_type ( '|' policy_data_type )* ) -> ^( POLICY_DATA_ ( policy_data_type )+ ) | '_' -> ^( POLICY_DATA_ '_' ) );
    def policy_data(self, ):
        retval = self.policy_data_return()
        retval.start = self.input.LT(1)


        root_0 = None

        char_literal312 = None
        char_literal314 = None
        policy_data_type311 = None
        policy_data_type313 = None

        char_literal312_tree = None
        char_literal314_tree = None
        stream_135 = RewriteRuleTokenStream(self._adaptor, "token 135")
        stream_148 = RewriteRuleTokenStream(self._adaptor, "token 148")
        stream_policy_data_type = RewriteRuleSubtreeStream(self._adaptor, "rule policy_data_type")
        try:
            try:
                # ProtoCC.g:346:3: ( ( policy_data_type ( '|' policy_data_type )* ) -> ^( POLICY_DATA_ ( policy_data_type )+ ) | '_' -> ^( POLICY_DATA_ '_' ) )
                alt54 = 2
                LA54_0 = self.input.LA(1)

                if (LA54_0 in {119, 120, 124, 125, 127}) :
                    alt54 = 1
                elif (LA54_0 == 135) :
                    alt54 = 2
                else:
                    nvae = NoViableAltException("", 54, 0, self.input)

                    raise nvae


                if alt54 == 1:
                    # ProtoCC.g:346:5: ( policy_data_type ( '|' policy_data_type )* )
                    pass 
                    # ProtoCC.g:346:5: ( policy_data_type ( '|' policy_data_type )* )
                    # ProtoCC.g:346:6: policy_data_type ( '|' policy_data_type )*
                    pass 
                    self._state.following.append(self.FOLLOW_policy_data_type_in_policy_data3452)
                    policy_data_type311 = self.policy_data_type()

                    self._state.following.pop()
                    stream_policy_data_type.add(policy_data_type311.tree)


                    # ProtoCC.g:346:23: ( '|' policy_data_type )*
                    while True: #loop53
                        alt53 = 2
                        LA53_0 = self.input.LA(1)

                        if (LA53_0 == 148) :
                            alt53 = 1


                        if alt53 == 1:
                            # ProtoCC.g:346:24: '|' policy_data_type
                            pass 
                            char_literal312 = self.match(self.input, 148, self.FOLLOW_148_in_policy_data3455) 
                            stream_148.add(char_literal312)


                            self._state.following.append(self.FOLLOW_policy_data_type_in_policy_data3457)
                            policy_data_type313 = self.policy_data_type()

                            self._state.following.pop()
                            stream_policy_data_type.add(policy_data_type313.tree)



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
                    # 346:48: -> ^( POLICY_DATA_ ( policy_data_type )+ )
                    # ProtoCC.g:346:51: ^( POLICY_DATA_ ( policy_data_type )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(POLICY_DATA_, "POLICY_DATA_")
                    , root_1)

                    # ProtoCC.g:346:66: ( policy_data_type )+
                    if not (stream_policy_data_type.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_policy_data_type.hasNext():
                        self._adaptor.addChild(root_1, stream_policy_data_type.nextTree())


                    stream_policy_data_type.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt54 == 2:
                    # ProtoCC.g:347:4: '_'
                    pass 
                    char_literal314 = self.match(self.input, 135, self.FOLLOW_135_in_policy_data3474) 
                    stream_135.add(char_literal314)


                    # AST Rewrite
                    # elements: 135
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
                    # 347:47: -> ^( POLICY_DATA_ '_' )
                    # ProtoCC.g:347:50: ^( POLICY_DATA_ '_' )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(POLICY_DATA_, "POLICY_DATA_")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_135.nextNode()
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
    # ProtoCC.g:350:1: policy_coh_type : ( 'coh' | 'nco' );
    def policy_coh_type(self, ):
        retval = self.policy_coh_type_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set315 = None

        set315_tree = None

        try:
            try:
                # ProtoCC.g:350:16: ( 'coh' | 'nco' )
                # ProtoCC.g:
                pass 
                root_0 = self._adaptor.nil()


                set315 = self.input.LT(1)

                if self.input.LA(1) in {140, 145}:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set315))

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
    # ProtoCC.g:351:1: policy_coh : ( ( policy_coh_type ( '|' policy_coh_type )* ) -> ^( POLICY_COH_ ( policy_coh_type )+ ) | '_' -> ^( POLICY_COH_ '_' ) );
    def policy_coh(self, ):
        retval = self.policy_coh_return()
        retval.start = self.input.LT(1)


        root_0 = None

        char_literal317 = None
        char_literal319 = None
        policy_coh_type316 = None
        policy_coh_type318 = None

        char_literal317_tree = None
        char_literal319_tree = None
        stream_135 = RewriteRuleTokenStream(self._adaptor, "token 135")
        stream_148 = RewriteRuleTokenStream(self._adaptor, "token 148")
        stream_policy_coh_type = RewriteRuleSubtreeStream(self._adaptor, "rule policy_coh_type")
        try:
            try:
                # ProtoCC.g:352:3: ( ( policy_coh_type ( '|' policy_coh_type )* ) -> ^( POLICY_COH_ ( policy_coh_type )+ ) | '_' -> ^( POLICY_COH_ '_' ) )
                alt56 = 2
                LA56_0 = self.input.LA(1)

                if (LA56_0 in {140, 145}) :
                    alt56 = 1
                elif (LA56_0 == 135) :
                    alt56 = 2
                else:
                    nvae = NoViableAltException("", 56, 0, self.input)

                    raise nvae


                if alt56 == 1:
                    # ProtoCC.g:352:5: ( policy_coh_type ( '|' policy_coh_type )* )
                    pass 
                    # ProtoCC.g:352:5: ( policy_coh_type ( '|' policy_coh_type )* )
                    # ProtoCC.g:352:6: policy_coh_type ( '|' policy_coh_type )*
                    pass 
                    self._state.following.append(self.FOLLOW_policy_coh_type_in_policy_coh3544)
                    policy_coh_type316 = self.policy_coh_type()

                    self._state.following.pop()
                    stream_policy_coh_type.add(policy_coh_type316.tree)


                    # ProtoCC.g:352:22: ( '|' policy_coh_type )*
                    while True: #loop55
                        alt55 = 2
                        LA55_0 = self.input.LA(1)

                        if (LA55_0 == 148) :
                            alt55 = 1


                        if alt55 == 1:
                            # ProtoCC.g:352:23: '|' policy_coh_type
                            pass 
                            char_literal317 = self.match(self.input, 148, self.FOLLOW_148_in_policy_coh3547) 
                            stream_148.add(char_literal317)


                            self._state.following.append(self.FOLLOW_policy_coh_type_in_policy_coh3549)
                            policy_coh_type318 = self.policy_coh_type()

                            self._state.following.pop()
                            stream_policy_coh_type.add(policy_coh_type318.tree)



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
                    # 352:46: -> ^( POLICY_COH_ ( policy_coh_type )+ )
                    # ProtoCC.g:352:49: ^( POLICY_COH_ ( policy_coh_type )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(POLICY_COH_, "POLICY_COH_")
                    , root_1)

                    # ProtoCC.g:352:63: ( policy_coh_type )+
                    if not (stream_policy_coh_type.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_policy_coh_type.hasNext():
                        self._adaptor.addChild(root_1, stream_policy_coh_type.nextTree())


                    stream_policy_coh_type.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt56 == 2:
                    # ProtoCC.g:353:4: '_'
                    pass 
                    char_literal319 = self.match(self.input, 135, self.FOLLOW_135_in_policy_coh3566) 
                    stream_135.add(char_literal319)


                    # AST Rewrite
                    # elements: 135
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
                    # 353:45: -> ^( POLICY_COH_ '_' )
                    # ProtoCC.g:353:48: ^( POLICY_COH_ '_' )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(POLICY_COH_, "POLICY_COH_")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_135.nextNode()
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
    # ProtoCC.g:357:1: label_state :{...}? ID OBRACE policy_op COMMA policy_data COMMA policy_coh CBRACE -> ^( LABEL_STATE_ policy_op policy_data policy_coh ) ;
    def label_state(self, ):
        retval = self.label_state_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID320 = None
        OBRACE321 = None
        COMMA323 = None
        COMMA325 = None
        CBRACE327 = None
        policy_op322 = None
        policy_data324 = None
        policy_coh326 = None

        ID320_tree = None
        OBRACE321_tree = None
        COMMA323_tree = None
        COMMA325_tree = None
        CBRACE327_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_OBRACE = RewriteRuleTokenStream(self._adaptor, "token OBRACE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CBRACE = RewriteRuleTokenStream(self._adaptor, "token CBRACE")
        stream_policy_op = RewriteRuleSubtreeStream(self._adaptor, "rule policy_op")
        stream_policy_data = RewriteRuleSubtreeStream(self._adaptor, "rule policy_data")
        stream_policy_coh = RewriteRuleSubtreeStream(self._adaptor, "rule policy_coh")
        try:
            try:
                # ProtoCC.g:357:12: ({...}? ID OBRACE policy_op COMMA policy_data COMMA policy_coh CBRACE -> ^( LABEL_STATE_ policy_op policy_data policy_coh ) )
                # ProtoCC.g:357:14: {...}? ID OBRACE policy_op COMMA policy_data COMMA policy_coh CBRACE
                pass 
                if not ((self.input.LT(1).text == 'S')):
                    raise FailedPredicateException(self.input, "label_state", "self.input.LT(1).text == 'S'")


                ID320 = self.match(self.input, ID, self.FOLLOW_ID_in_label_state3623) 
                stream_ID.add(ID320)


                OBRACE321 = self.match(self.input, OBRACE, self.FOLLOW_OBRACE_in_label_state3625) 
                stream_OBRACE.add(OBRACE321)


                self._state.following.append(self.FOLLOW_policy_op_in_label_state3627)
                policy_op322 = self.policy_op()

                self._state.following.pop()
                stream_policy_op.add(policy_op322.tree)


                COMMA323 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_label_state3629) 
                stream_COMMA.add(COMMA323)


                self._state.following.append(self.FOLLOW_policy_data_in_label_state3631)
                policy_data324 = self.policy_data()

                self._state.following.pop()
                stream_policy_data.add(policy_data324.tree)


                COMMA325 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_label_state3633) 
                stream_COMMA.add(COMMA325)


                self._state.following.append(self.FOLLOW_policy_coh_in_label_state3635)
                policy_coh326 = self.policy_coh()

                self._state.following.pop()
                stream_policy_coh.add(policy_coh326.tree)


                CBRACE327 = self.match(self.input, CBRACE, self.FOLLOW_CBRACE_in_label_state3637) 
                stream_CBRACE.add(CBRACE327)


                # AST Rewrite
                # elements: policy_coh, policy_data, policy_op
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
                # 358:4: -> ^( LABEL_STATE_ policy_op policy_data policy_coh )
                # ProtoCC.g:358:7: ^( LABEL_STATE_ policy_op policy_data policy_coh )
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
    # ProtoCC.g:360:1: label_message :{...}? ID OBRACE policy_op COMMA policy_data COMMA policy_coh CBRACE -> ^( LABEL_MESSAGE_ policy_op policy_data policy_coh ) ;
    def label_message(self, ):
        retval = self.label_message_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID328 = None
        OBRACE329 = None
        COMMA331 = None
        COMMA333 = None
        CBRACE335 = None
        policy_op330 = None
        policy_data332 = None
        policy_coh334 = None

        ID328_tree = None
        OBRACE329_tree = None
        COMMA331_tree = None
        COMMA333_tree = None
        CBRACE335_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_OBRACE = RewriteRuleTokenStream(self._adaptor, "token OBRACE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CBRACE = RewriteRuleTokenStream(self._adaptor, "token CBRACE")
        stream_policy_op = RewriteRuleSubtreeStream(self._adaptor, "rule policy_op")
        stream_policy_data = RewriteRuleSubtreeStream(self._adaptor, "rule policy_data")
        stream_policy_coh = RewriteRuleSubtreeStream(self._adaptor, "rule policy_coh")
        try:
            try:
                # ProtoCC.g:360:14: ({...}? ID OBRACE policy_op COMMA policy_data COMMA policy_coh CBRACE -> ^( LABEL_MESSAGE_ policy_op policy_data policy_coh ) )
                # ProtoCC.g:360:15: {...}? ID OBRACE policy_op COMMA policy_data COMMA policy_coh CBRACE
                pass 
                if not ((self.input.LT(1).text == 'M')):
                    raise FailedPredicateException(self.input, "label_message", "self.input.LT(1).text == 'M'")


                ID328 = self.match(self.input, ID, self.FOLLOW_ID_in_label_message3661) 
                stream_ID.add(ID328)


                OBRACE329 = self.match(self.input, OBRACE, self.FOLLOW_OBRACE_in_label_message3663) 
                stream_OBRACE.add(OBRACE329)


                self._state.following.append(self.FOLLOW_policy_op_in_label_message3665)
                policy_op330 = self.policy_op()

                self._state.following.pop()
                stream_policy_op.add(policy_op330.tree)


                COMMA331 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_label_message3667) 
                stream_COMMA.add(COMMA331)


                self._state.following.append(self.FOLLOW_policy_data_in_label_message3669)
                policy_data332 = self.policy_data()

                self._state.following.pop()
                stream_policy_data.add(policy_data332.tree)


                COMMA333 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_label_message3671) 
                stream_COMMA.add(COMMA333)


                self._state.following.append(self.FOLLOW_policy_coh_in_label_message3673)
                policy_coh334 = self.policy_coh()

                self._state.following.pop()
                stream_policy_coh.add(policy_coh334.tree)


                CBRACE335 = self.match(self.input, CBRACE, self.FOLLOW_CBRACE_in_label_message3675) 
                stream_CBRACE.add(CBRACE335)


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
                # 361:3: -> ^( LABEL_MESSAGE_ policy_op policy_data policy_coh )
                # ProtoCC.g:361:6: ^( LABEL_MESSAGE_ policy_op policy_data policy_coh )
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
    # ProtoCC.g:364:1: data_rule : 'Data' OBRACE label_state CBRACE SEMICOLON -> ^( DATA_RULE_ label_state ) ;
    def data_rule(self, ):
        retval = self.data_rule_return()
        retval.start = self.input.LT(1)


        root_0 = None

        string_literal336 = None
        OBRACE337 = None
        CBRACE339 = None
        SEMICOLON340 = None
        label_state338 = None

        string_literal336_tree = None
        OBRACE337_tree = None
        CBRACE339_tree = None
        SEMICOLON340_tree = None
        stream_OBRACE = RewriteRuleTokenStream(self._adaptor, "token OBRACE")
        stream_DATA = RewriteRuleTokenStream(self._adaptor, "token DATA")
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_CBRACE = RewriteRuleTokenStream(self._adaptor, "token CBRACE")
        stream_label_state = RewriteRuleSubtreeStream(self._adaptor, "rule label_state")
        try:
            try:
                # ProtoCC.g:364:10: ( 'Data' OBRACE label_state CBRACE SEMICOLON -> ^( DATA_RULE_ label_state ) )
                # ProtoCC.g:364:12: 'Data' OBRACE label_state CBRACE SEMICOLON
                pass 
                string_literal336 = self.match(self.input, DATA, self.FOLLOW_DATA_in_data_rule3699) 
                stream_DATA.add(string_literal336)


                OBRACE337 = self.match(self.input, OBRACE, self.FOLLOW_OBRACE_in_data_rule3701) 
                stream_OBRACE.add(OBRACE337)


                self._state.following.append(self.FOLLOW_label_state_in_data_rule3703)
                label_state338 = self.label_state()

                self._state.following.pop()
                stream_label_state.add(label_state338.tree)


                CBRACE339 = self.match(self.input, CBRACE, self.FOLLOW_CBRACE_in_data_rule3705) 
                stream_CBRACE.add(CBRACE339)


                SEMICOLON340 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_data_rule3707) 
                stream_SEMICOLON.add(SEMICOLON340)


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
                # 365:3: -> ^( DATA_RULE_ label_state )
                # ProtoCC.g:365:6: ^( DATA_RULE_ label_state )
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
    # ProtoCC.g:367:1: local_rule : 'Local' OBRACE label_state COMMA label_message COMMA label_state CBRACE SEMICOLON -> ^( LOCAL_RULE_ label_state label_message label_state ) ;
    def local_rule(self, ):
        retval = self.local_rule_return()
        retval.start = self.input.LT(1)


        root_0 = None

        string_literal341 = None
        OBRACE342 = None
        COMMA344 = None
        COMMA346 = None
        CBRACE348 = None
        SEMICOLON349 = None
        label_state343 = None
        label_message345 = None
        label_state347 = None

        string_literal341_tree = None
        OBRACE342_tree = None
        COMMA344_tree = None
        COMMA346_tree = None
        CBRACE348_tree = None
        SEMICOLON349_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_122 = RewriteRuleTokenStream(self._adaptor, "token 122")
        stream_OBRACE = RewriteRuleTokenStream(self._adaptor, "token OBRACE")
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_CBRACE = RewriteRuleTokenStream(self._adaptor, "token CBRACE")
        stream_label_state = RewriteRuleSubtreeStream(self._adaptor, "rule label_state")
        stream_label_message = RewriteRuleSubtreeStream(self._adaptor, "rule label_message")
        try:
            try:
                # ProtoCC.g:367:11: ( 'Local' OBRACE label_state COMMA label_message COMMA label_state CBRACE SEMICOLON -> ^( LOCAL_RULE_ label_state label_message label_state ) )
                # ProtoCC.g:367:13: 'Local' OBRACE label_state COMMA label_message COMMA label_state CBRACE SEMICOLON
                pass 
                string_literal341 = self.match(self.input, 122, self.FOLLOW_122_in_local_rule3724) 
                stream_122.add(string_literal341)


                OBRACE342 = self.match(self.input, OBRACE, self.FOLLOW_OBRACE_in_local_rule3726) 
                stream_OBRACE.add(OBRACE342)


                self._state.following.append(self.FOLLOW_label_state_in_local_rule3728)
                label_state343 = self.label_state()

                self._state.following.pop()
                stream_label_state.add(label_state343.tree)


                COMMA344 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_local_rule3730) 
                stream_COMMA.add(COMMA344)


                self._state.following.append(self.FOLLOW_label_message_in_local_rule3732)
                label_message345 = self.label_message()

                self._state.following.pop()
                stream_label_message.add(label_message345.tree)


                COMMA346 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_local_rule3734) 
                stream_COMMA.add(COMMA346)


                self._state.following.append(self.FOLLOW_label_state_in_local_rule3736)
                label_state347 = self.label_state()

                self._state.following.pop()
                stream_label_state.add(label_state347.tree)


                CBRACE348 = self.match(self.input, CBRACE, self.FOLLOW_CBRACE_in_local_rule3738) 
                stream_CBRACE.add(CBRACE348)


                SEMICOLON349 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_local_rule3740) 
                stream_SEMICOLON.add(SEMICOLON349)


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
                # 368:2: -> ^( LOCAL_RULE_ label_state label_message label_state )
                # ProtoCC.g:368:5: ^( LOCAL_RULE_ label_state label_message label_state )
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


    class rule_action_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "rule_action"
    # ProtoCC.g:370:1: rule_action : 'action' EQUALSIGN OCBRACE ( expressions )* CCBRACE -> ^( POLICY_ACTION_ ( expressions )* ) ;
    def rule_action(self, ):
        retval = self.rule_action_return()
        retval.start = self.input.LT(1)


        root_0 = None

        string_literal350 = None
        EQUALSIGN351 = None
        OCBRACE352 = None
        CCBRACE354 = None
        expressions353 = None

        string_literal350_tree = None
        EQUALSIGN351_tree = None
        OCBRACE352_tree = None
        CCBRACE354_tree = None
        stream_EQUALSIGN = RewriteRuleTokenStream(self._adaptor, "token EQUALSIGN")
        stream_136 = RewriteRuleTokenStream(self._adaptor, "token 136")
        stream_OCBRACE = RewriteRuleTokenStream(self._adaptor, "token OCBRACE")
        stream_CCBRACE = RewriteRuleTokenStream(self._adaptor, "token CCBRACE")
        stream_expressions = RewriteRuleSubtreeStream(self._adaptor, "rule expressions")
        try:
            try:
                # ProtoCC.g:370:12: ( 'action' EQUALSIGN OCBRACE ( expressions )* CCBRACE -> ^( POLICY_ACTION_ ( expressions )* ) )
                # ProtoCC.g:370:14: 'action' EQUALSIGN OCBRACE ( expressions )* CCBRACE
                pass 
                string_literal350 = self.match(self.input, 136, self.FOLLOW_136_in_rule_action3760) 
                stream_136.add(string_literal350)


                EQUALSIGN351 = self.match(self.input, EQUALSIGN, self.FOLLOW_EQUALSIGN_in_rule_action3762) 
                stream_EQUALSIGN.add(EQUALSIGN351)


                OCBRACE352 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_rule_action3764) 
                stream_OCBRACE.add(OCBRACE352)


                # ProtoCC.g:370:41: ( expressions )*
                while True: #loop57
                    alt57 = 2
                    LA57_0 = self.input.LA(1)

                    if (LA57_0 in {ACCESS, ID, IF, STALL, STATE, UNDEF, 121}) :
                        alt57 = 1


                    if alt57 == 1:
                        # ProtoCC.g:370:41: expressions
                        pass 
                        self._state.following.append(self.FOLLOW_expressions_in_rule_action3766)
                        expressions353 = self.expressions()

                        self._state.following.pop()
                        stream_expressions.add(expressions353.tree)



                    else:
                        break #loop57


                CCBRACE354 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_rule_action3769) 
                stream_CCBRACE.add(CCBRACE354)


                # AST Rewrite
                # elements: expressions
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
                # 370:62: -> ^( POLICY_ACTION_ ( expressions )* )
                # ProtoCC.g:370:65: ^( POLICY_ACTION_ ( expressions )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(POLICY_ACTION_, "POLICY_ACTION_")
                , root_1)

                # ProtoCC.g:370:82: ( expressions )*
                while stream_expressions.hasNext():
                    self._adaptor.addChild(root_1, stream_expressions.nextTree())


                stream_expressions.reset();

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

    # $ANTLR end "rule_action"


    class rule_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "rule"
    # ProtoCC.g:372:1: rule : 'Rule' OBRACE label_state COMMA label_message COMMA label_state ( COMMA rule_action )? CBRACE SEMICOLON -> ^( RULE_ label_state label_message label_state ( rule_action )? ) ;
    def rule(self, ):
        retval = self.rule_return()
        retval.start = self.input.LT(1)


        root_0 = None

        string_literal355 = None
        OBRACE356 = None
        COMMA358 = None
        COMMA360 = None
        COMMA362 = None
        CBRACE364 = None
        SEMICOLON365 = None
        label_state357 = None
        label_message359 = None
        label_state361 = None
        rule_action363 = None

        string_literal355_tree = None
        OBRACE356_tree = None
        COMMA358_tree = None
        COMMA360_tree = None
        COMMA362_tree = None
        CBRACE364_tree = None
        SEMICOLON365_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_OBRACE = RewriteRuleTokenStream(self._adaptor, "token OBRACE")
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_CBRACE = RewriteRuleTokenStream(self._adaptor, "token CBRACE")
        stream_131 = RewriteRuleTokenStream(self._adaptor, "token 131")
        stream_rule_action = RewriteRuleSubtreeStream(self._adaptor, "rule rule_action")
        stream_label_state = RewriteRuleSubtreeStream(self._adaptor, "rule label_state")
        stream_label_message = RewriteRuleSubtreeStream(self._adaptor, "rule label_message")
        try:
            try:
                # ProtoCC.g:372:5: ( 'Rule' OBRACE label_state COMMA label_message COMMA label_state ( COMMA rule_action )? CBRACE SEMICOLON -> ^( RULE_ label_state label_message label_state ( rule_action )? ) )
                # ProtoCC.g:372:7: 'Rule' OBRACE label_state COMMA label_message COMMA label_state ( COMMA rule_action )? CBRACE SEMICOLON
                pass 
                string_literal355 = self.match(self.input, 131, self.FOLLOW_131_in_rule3785) 
                stream_131.add(string_literal355)


                OBRACE356 = self.match(self.input, OBRACE, self.FOLLOW_OBRACE_in_rule3787) 
                stream_OBRACE.add(OBRACE356)


                self._state.following.append(self.FOLLOW_label_state_in_rule3789)
                label_state357 = self.label_state()

                self._state.following.pop()
                stream_label_state.add(label_state357.tree)


                COMMA358 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_rule3791) 
                stream_COMMA.add(COMMA358)


                self._state.following.append(self.FOLLOW_label_message_in_rule3793)
                label_message359 = self.label_message()

                self._state.following.pop()
                stream_label_message.add(label_message359.tree)


                COMMA360 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_rule3795) 
                stream_COMMA.add(COMMA360)


                self._state.following.append(self.FOLLOW_label_state_in_rule3797)
                label_state361 = self.label_state()

                self._state.following.pop()
                stream_label_state.add(label_state361.tree)


                # ProtoCC.g:372:71: ( COMMA rule_action )?
                alt58 = 2
                LA58_0 = self.input.LA(1)

                if (LA58_0 == COMMA) :
                    alt58 = 1
                if alt58 == 1:
                    # ProtoCC.g:372:72: COMMA rule_action
                    pass 
                    COMMA362 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_rule3800) 
                    stream_COMMA.add(COMMA362)


                    self._state.following.append(self.FOLLOW_rule_action_in_rule3802)
                    rule_action363 = self.rule_action()

                    self._state.following.pop()
                    stream_rule_action.add(rule_action363.tree)





                CBRACE364 = self.match(self.input, CBRACE, self.FOLLOW_CBRACE_in_rule3806) 
                stream_CBRACE.add(CBRACE364)


                SEMICOLON365 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_rule3808) 
                stream_SEMICOLON.add(SEMICOLON365)


                # AST Rewrite
                # elements: rule_action, label_message, label_state, label_state
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
                # 373:4: -> ^( RULE_ label_state label_message label_state ( rule_action )? )
                # ProtoCC.g:373:7: ^( RULE_ label_state label_message label_state ( rule_action )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(RULE_, "RULE_")
                , root_1)

                self._adaptor.addChild(root_1, stream_label_state.nextTree())

                self._adaptor.addChild(root_1, stream_label_message.nextTree())

                self._adaptor.addChild(root_1, stream_label_state.nextTree())

                # ProtoCC.g:373:53: ( rule_action )?
                if stream_rule_action.hasNext():
                    self._adaptor.addChild(root_1, stream_rule_action.nextTree())


                stream_rule_action.reset();

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
    # ProtoCC.g:375:1: policy_rule : ( data_rule | local_rule | rule );
    def policy_rule(self, ):
        retval = self.policy_rule_return()
        retval.start = self.input.LT(1)


        root_0 = None

        data_rule366 = None
        local_rule367 = None
        rule368 = None


        try:
            try:
                # ProtoCC.g:375:12: ( data_rule | local_rule | rule )
                alt59 = 3
                LA59 = self.input.LA(1)
                if LA59 in {DATA}:
                    alt59 = 1
                elif LA59 in {122}:
                    alt59 = 2
                elif LA59 in {131}:
                    alt59 = 3
                else:
                    nvae = NoViableAltException("", 59, 0, self.input)

                    raise nvae


                if alt59 == 1:
                    # ProtoCC.g:375:14: data_rule
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_data_rule_in_policy_rule3833)
                    data_rule366 = self.data_rule()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, data_rule366.tree)



                elif alt59 == 2:
                    # ProtoCC.g:375:26: local_rule
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_local_rule_in_policy_rule3837)
                    local_rule367 = self.local_rule()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, local_rule367.tree)



                elif alt59 == 3:
                    # ProtoCC.g:375:39: rule
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_rule_in_policy_rule3841)
                    rule368 = self.rule()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, rule368.tree)



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
    # ProtoCC.g:376:1: policy_block : 'Policy' ID OCBRACE ( policy_rule )* CCBRACE -> ^( POLICY_ ID ( policy_rule )* ) ;
    def policy_block(self, ):
        retval = self.policy_block_return()
        retval.start = self.input.LT(1)


        root_0 = None

        string_literal369 = None
        ID370 = None
        OCBRACE371 = None
        CCBRACE373 = None
        policy_rule372 = None

        string_literal369_tree = None
        ID370_tree = None
        OCBRACE371_tree = None
        CCBRACE373_tree = None
        stream_OCBRACE = RewriteRuleTokenStream(self._adaptor, "token OCBRACE")
        stream_128 = RewriteRuleTokenStream(self._adaptor, "token 128")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CCBRACE = RewriteRuleTokenStream(self._adaptor, "token CCBRACE")
        stream_policy_rule = RewriteRuleSubtreeStream(self._adaptor, "rule policy_rule")
        try:
            try:
                # ProtoCC.g:376:14: ( 'Policy' ID OCBRACE ( policy_rule )* CCBRACE -> ^( POLICY_ ID ( policy_rule )* ) )
                # ProtoCC.g:376:16: 'Policy' ID OCBRACE ( policy_rule )* CCBRACE
                pass 
                string_literal369 = self.match(self.input, 128, self.FOLLOW_128_in_policy_block3848) 
                stream_128.add(string_literal369)


                ID370 = self.match(self.input, ID, self.FOLLOW_ID_in_policy_block3850) 
                stream_ID.add(ID370)


                OCBRACE371 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_policy_block3852) 
                stream_OCBRACE.add(OCBRACE371)


                # ProtoCC.g:376:36: ( policy_rule )*
                while True: #loop60
                    alt60 = 2
                    LA60_0 = self.input.LA(1)

                    if (LA60_0 in {DATA, 122, 131}) :
                        alt60 = 1


                    if alt60 == 1:
                        # ProtoCC.g:376:36: policy_rule
                        pass 
                        self._state.following.append(self.FOLLOW_policy_rule_in_policy_block3854)
                        policy_rule372 = self.policy_rule()

                        self._state.following.pop()
                        stream_policy_rule.add(policy_rule372.tree)



                    else:
                        break #loop60


                CCBRACE373 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_policy_block3857) 
                stream_CCBRACE.add(CCBRACE373)


                # AST Rewrite
                # elements: policy_rule, ID
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
                # 376:57: -> ^( POLICY_ ID ( policy_rule )* )
                # ProtoCC.g:376:60: ^( POLICY_ ID ( policy_rule )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(POLICY_, "POLICY_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # ProtoCC.g:376:73: ( policy_rule )*
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
    # ProtoCC.g:378:1: policy_file : ( policy_block )+ -> ^( POL_FILE_ ( policy_block )+ ) ;
    def policy_file(self, ):
        retval = self.policy_file_return()
        retval.start = self.input.LT(1)


        root_0 = None

        policy_block374 = None

        stream_policy_block = RewriteRuleSubtreeStream(self._adaptor, "rule policy_block")
        try:
            try:
                # ProtoCC.g:378:12: ( ( policy_block )+ -> ^( POL_FILE_ ( policy_block )+ ) )
                # ProtoCC.g:378:14: ( policy_block )+
                pass 
                # ProtoCC.g:378:14: ( policy_block )+
                cnt61 = 0
                while True: #loop61
                    alt61 = 2
                    LA61_0 = self.input.LA(1)

                    if (LA61_0 == 128) :
                        alt61 = 1


                    if alt61 == 1:
                        # ProtoCC.g:378:14: policy_block
                        pass 
                        self._state.following.append(self.FOLLOW_policy_block_in_policy_file3875)
                        policy_block374 = self.policy_block()

                        self._state.following.pop()
                        stream_policy_block.add(policy_block374.tree)



                    else:
                        if cnt61 >= 1:
                            break #loop61

                        eee = EarlyExitException(61, self.input)
                        raise eee

                    cnt61 += 1


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
                # 379:2: -> ^( POL_FILE_ ( policy_block )+ )
                # ProtoCC.g:379:5: ^( POL_FILE_ ( policy_block )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(POL_FILE_, "POL_FILE_")
                , root_1)

                # ProtoCC.g:379:17: ( policy_block )+
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



 

    FOLLOW_121_in_internal_event_function757 = frozenset([1])
    FOLLOW_const_decl_in_document1085 = frozenset([1, 4, 6, 19, 27, 33, 50, 52, 66, 69, 75, 102, 104, 106, 121])
    FOLLOW_init_hw_in_document1089 = frozenset([1, 4, 6, 19, 27, 33, 50, 52, 66, 69, 75, 102, 104, 106, 121])
    FOLLOW_arch_block_in_document1093 = frozenset([1, 4, 6, 19, 27, 33, 50, 52, 66, 69, 75, 102, 104, 106, 121])
    FOLLOW_expressions_in_document1097 = frozenset([1, 4, 6, 19, 27, 33, 50, 52, 66, 69, 75, 102, 104, 106, 121])
    FOLLOW_policy_file_in_document1105 = frozenset([1])
    FOLLOW_int_decl_in_declarations1116 = frozenset([1])
    FOLLOW_bool_decl_in_declarations1120 = frozenset([1])
    FOLLOW_state_decl_in_declarations1124 = frozenset([1])
    FOLLOW_data_decl_in_declarations1128 = frozenset([1])
    FOLLOW_id_decl_in_declarations1132 = frozenset([1])
    FOLLOW_CONSTANT_in_const_decl1144 = frozenset([50])
    FOLLOW_ID_in_const_decl1146 = frozenset([57])
    FOLLOW_INT_in_const_decl1148 = frozenset([1])
    FOLLOW_INTID_in_int_decl1170 = frozenset([83])
    FOLLOW_range_in_int_decl1172 = frozenset([50])
    FOLLOW_ID_in_int_decl1174 = frozenset([42, 95])
    FOLLOW_EQUALSIGN_in_int_decl1177 = frozenset([57])
    FOLLOW_INT_in_int_decl1179 = frozenset([42, 95])
    FOLLOW_SEMICOLON_in_int_decl1183 = frozenset([1])
    FOLLOW_BOOLID_in_bool_decl1211 = frozenset([50])
    FOLLOW_ID_in_bool_decl1213 = frozenset([42, 95])
    FOLLOW_EQUALSIGN_in_bool_decl1216 = frozenset([14])
    FOLLOW_BOOL_in_bool_decl1218 = frozenset([42, 95])
    FOLLOW_SEMICOLON_in_bool_decl1222 = frozenset([1])
    FOLLOW_STATE_in_state_decl1249 = frozenset([50])
    FOLLOW_ID_in_state_decl1251 = frozenset([95])
    FOLLOW_SEMICOLON_in_state_decl1253 = frozenset([1])
    FOLLOW_DATA_in_data_decl1272 = frozenset([50])
    FOLLOW_ID_in_data_decl1274 = frozenset([95])
    FOLLOW_SEMICOLON_in_data_decl1276 = frozenset([1])
    FOLLOW_set_decl_in_id_decl1295 = frozenset([79, 97])
    FOLLOW_NID_in_id_decl1298 = frozenset([50])
    FOLLOW_ID_in_id_decl1300 = frozenset([42, 95])
    FOLLOW_EQUALSIGN_in_id_decl1303 = frozenset([50, 97])
    FOLLOW_set_decl_in_id_decl1305 = frozenset([50, 97])
    FOLLOW_ID_in_id_decl1308 = frozenset([42, 95])
    FOLLOW_SEMICOLON_in_id_decl1312 = frozenset([1])
    FOLLOW_SET_in_set_decl1349 = frozenset([83])
    FOLLOW_OEBRACE_in_set_decl1351 = frozenset([50, 57])
    FOLLOW_val_range_in_set_decl1353 = frozenset([23])
    FOLLOW_CEBRACE_in_set_decl1355 = frozenset([1])
    FOLLOW_OEBRACE_in_range1378 = frozenset([50, 57])
    FOLLOW_val_range_in_range1380 = frozenset([35])
    FOLLOW_DOT_in_range1382 = frozenset([35])
    FOLLOW_DOT_in_range1384 = frozenset([50, 57])
    FOLLOW_val_range_in_range1386 = frozenset([23])
    FOLLOW_CEBRACE_in_range1388 = frozenset([1])
    FOLLOW_ARRAY_in_array_decl1437 = frozenset([83])
    FOLLOW_range_in_array_decl1439 = frozenset([1])
    FOLLOW_FIFO_in_fifo_decl1449 = frozenset([83])
    FOLLOW_range_in_fifo_decl1451 = frozenset([1])
    FOLLOW_network_block_in_init_hw1461 = frozenset([1])
    FOLLOW_machines_in_init_hw1465 = frozenset([1])
    FOLLOW_message_block_in_init_hw1469 = frozenset([1])
    FOLLOW_object_expr_in_object_block1480 = frozenset([95])
    FOLLOW_SEMICOLON_in_object_block1482 = frozenset([1])
    FOLLOW_object_id_in_object_expr1497 = frozenset([1])
    FOLLOW_object_func_in_object_expr1501 = frozenset([1])
    FOLLOW_ID_in_object_id1512 = frozenset([1])
    FOLLOW_ID_in_object_func1529 = frozenset([35])
    FOLLOW_DOT_in_object_func1531 = frozenset([50, 79])
    FOLLOW_object_idres_in_object_func1533 = frozenset([1, 81])
    FOLLOW_OBRACE_in_object_func1536 = frozenset([21, 24, 50])
    FOLLOW_object_expr_in_object_func1538 = frozenset([21, 24, 50])
    FOLLOW_COMMA_in_object_func1542 = frozenset([50])
    FOLLOW_object_expr_in_object_func1544 = frozenset([21, 24])
    FOLLOW_CBRACE_in_object_func1548 = frozenset([1, 81])
    FOLLOW_function_call_in_function_call_block1596 = frozenset([95])
    FOLLOW_SEMICOLON_in_function_call_block1598 = frozenset([1])
    FOLLOW_ID_in_function_call1613 = frozenset([81])
    FOLLOW_OBRACE_in_function_call1615 = frozenset([21])
    FOLLOW_CBRACE_in_function_call1617 = frozenset([1])
    FOLLOW_cache_block_in_machines1657 = frozenset([1])
    FOLLOW_dir_block_in_machines1661 = frozenset([1])
    FOLLOW_mem_block_in_machines1665 = frozenset([1])
    FOLLOW_CACHE_in_cache_block1680 = frozenset([82])
    FOLLOW_OCBRACE_in_cache_block1682 = frozenset([15, 22, 29, 58, 79, 97, 104])
    FOLLOW_declarations_in_cache_block1684 = frozenset([15, 22, 29, 58, 79, 97, 104])
    FOLLOW_CCBRACE_in_cache_block1687 = frozenset([50, 97])
    FOLLOW_objset_decl_in_cache_block1689 = frozenset([50, 97])
    FOLLOW_ID_in_cache_block1692 = frozenset([95])
    FOLLOW_SEMICOLON_in_cache_block1694 = frozenset([1])
    FOLLOW_DIR_in_dir_block1735 = frozenset([82])
    FOLLOW_OCBRACE_in_dir_block1737 = frozenset([15, 22, 29, 58, 79, 97, 104])
    FOLLOW_declarations_in_dir_block1739 = frozenset([15, 22, 29, 58, 79, 97, 104])
    FOLLOW_CCBRACE_in_dir_block1742 = frozenset([50, 97])
    FOLLOW_objset_decl_in_dir_block1744 = frozenset([50, 97])
    FOLLOW_ID_in_dir_block1747 = frozenset([95])
    FOLLOW_SEMICOLON_in_dir_block1749 = frozenset([1])
    FOLLOW_MEM_in_mem_block1790 = frozenset([82])
    FOLLOW_OCBRACE_in_mem_block1792 = frozenset([15, 22, 29, 58, 79, 97, 104])
    FOLLOW_declarations_in_mem_block1794 = frozenset([15, 22, 29, 58, 79, 97, 104])
    FOLLOW_CCBRACE_in_mem_block1797 = frozenset([50, 97])
    FOLLOW_objset_decl_in_mem_block1799 = frozenset([50, 97])
    FOLLOW_ID_in_mem_block1802 = frozenset([95])
    FOLLOW_SEMICOLON_in_mem_block1804 = frozenset([1])
    FOLLOW_SET_in_objset_decl1846 = frozenset([83])
    FOLLOW_OEBRACE_in_objset_decl1848 = frozenset([50, 57])
    FOLLOW_val_range_in_objset_decl1850 = frozenset([23])
    FOLLOW_CEBRACE_in_objset_decl1852 = frozenset([1])
    FOLLOW_NETWORK_in_network_block1878 = frozenset([82])
    FOLLOW_OCBRACE_in_network_block1880 = frozenset([22, 126, 133])
    FOLLOW_network_element_in_network_block1882 = frozenset([22, 126, 133])
    FOLLOW_CCBRACE_in_network_block1885 = frozenset([95])
    FOLLOW_SEMICOLON_in_network_block1887 = frozenset([1])
    FOLLOW_element_type_in_network_element1930 = frozenset([50])
    FOLLOW_ID_in_network_element1932 = frozenset([95])
    FOLLOW_SEMICOLON_in_network_element1934 = frozenset([1])
    FOLLOW_ID_in_network_send1955 = frozenset([35])
    FOLLOW_DOT_in_network_send1957 = frozenset([132, 146])
    FOLLOW_send_function_in_network_send1959 = frozenset([81])
    FOLLOW_OBRACE_in_network_send1961 = frozenset([50])
    FOLLOW_ID_in_network_send1963 = frozenset([21])
    FOLLOW_CBRACE_in_network_send1965 = frozenset([95])
    FOLLOW_SEMICOLON_in_network_send1967 = frozenset([1])
    FOLLOW_ID_in_network_bcast1987 = frozenset([35])
    FOLLOW_DOT_in_network_bcast1989 = frozenset([118, 138])
    FOLLOW_bcast_function_in_network_bcast1991 = frozenset([81])
    FOLLOW_OBRACE_in_network_bcast1993 = frozenset([50])
    FOLLOW_ID_in_network_bcast1995 = frozenset([21])
    FOLLOW_CBRACE_in_network_bcast1997 = frozenset([95])
    FOLLOW_SEMICOLON_in_network_bcast1999 = frozenset([1])
    FOLLOW_ID_in_network_mcast2019 = frozenset([35])
    FOLLOW_DOT_in_network_mcast2021 = frozenset([123, 144])
    FOLLOW_mcast_function_in_network_mcast2023 = frozenset([81])
    FOLLOW_OBRACE_in_network_mcast2025 = frozenset([50])
    FOLLOW_ID_in_network_mcast2027 = frozenset([24])
    FOLLOW_COMMA_in_network_mcast2029 = frozenset([50])
    FOLLOW_ID_in_network_mcast2031 = frozenset([21])
    FOLLOW_CBRACE_in_network_mcast2033 = frozenset([95])
    FOLLOW_SEMICOLON_in_network_mcast2035 = frozenset([1])
    FOLLOW_MSG_in_message_block2065 = frozenset([50])
    FOLLOW_ID_in_message_block2067 = frozenset([82])
    FOLLOW_OCBRACE_in_message_block2069 = frozenset([15, 22, 29, 58, 79, 97, 104])
    FOLLOW_declarations_in_message_block2071 = frozenset([15, 22, 29, 58, 79, 97, 104])
    FOLLOW_CCBRACE_in_message_block2074 = frozenset([95])
    FOLLOW_SEMICOLON_in_message_block2076 = frozenset([1])
    FOLLOW_ID_in_message_constr2098 = frozenset([81])
    FOLLOW_OBRACE_in_message_constr2100 = frozenset([14, 21, 24, 50, 57, 79])
    FOLLOW_message_expr_in_message_constr2102 = frozenset([14, 21, 24, 50, 57, 79])
    FOLLOW_COMMA_in_message_constr2106 = frozenset([14, 50, 57, 79])
    FOLLOW_message_expr_in_message_constr2108 = frozenset([21, 24])
    FOLLOW_CBRACE_in_message_constr2112 = frozenset([1])
    FOLLOW_object_expr_in_message_expr2134 = frozenset([1])
    FOLLOW_set_func_in_message_expr2138 = frozenset([1])
    FOLLOW_INT_in_message_expr2142 = frozenset([1])
    FOLLOW_BOOL_in_message_expr2146 = frozenset([1])
    FOLLOW_NID_in_message_expr2150 = frozenset([1])
    FOLLOW_set_func_in_set_block2168 = frozenset([95])
    FOLLOW_SEMICOLON_in_set_block2170 = frozenset([1])
    FOLLOW_ID_in_set_func2185 = frozenset([35])
    FOLLOW_DOT_in_set_func2187 = frozenset([137, 139, 141, 142, 143, 147])
    FOLLOW_set_function_types_in_set_func2189 = frozenset([81])
    FOLLOW_OBRACE_in_set_func2191 = frozenset([21, 50])
    FOLLOW_set_nest_in_set_func2193 = frozenset([21, 50])
    FOLLOW_CBRACE_in_set_func2196 = frozenset([1])
    FOLLOW_set_func_in_set_nest2234 = frozenset([1])
    FOLLOW_object_expr_in_set_nest2238 = frozenset([1])
    FOLLOW_internal_event_func_in_internal_event_block2256 = frozenset([95])
    FOLLOW_SEMICOLON_in_internal_event_block2258 = frozenset([1])
    FOLLOW_internal_event_function_in_internal_event_func2272 = frozenset([81])
    FOLLOW_OBRACE_in_internal_event_func2274 = frozenset([50])
    FOLLOW_ID_in_internal_event_func2276 = frozenset([21])
    FOLLOW_CBRACE_in_internal_event_func2278 = frozenset([1])
    FOLLOW_ARCH_in_arch_block2302 = frozenset([50])
    FOLLOW_ID_in_arch_block2304 = frozenset([82])
    FOLLOW_OCBRACE_in_arch_block2306 = frozenset([22, 91, 100])
    FOLLOW_arch_body_in_arch_block2308 = frozenset([22])
    FOLLOW_CCBRACE_in_arch_block2310 = frozenset([1])
    FOLLOW_stable_def_in_arch_body2332 = frozenset([1, 91, 100])
    FOLLOW_process_block_in_arch_body2336 = frozenset([1, 91, 100])
    FOLLOW_STABLE_in_stable_def2346 = frozenset([82])
    FOLLOW_OCBRACE_in_stable_def2348 = frozenset([50])
    FOLLOW_ID_in_stable_def2350 = frozenset([22, 24])
    FOLLOW_COMMA_in_stable_def2353 = frozenset([50])
    FOLLOW_ID_in_stable_def2355 = frozenset([22, 24])
    FOLLOW_CCBRACE_in_stable_def2359 = frozenset([1])
    FOLLOW_PROC_in_process_block2378 = frozenset([81])
    FOLLOW_process_trans_in_process_block2380 = frozenset([82])
    FOLLOW_OCBRACE_in_process_block2382 = frozenset([4, 11, 22, 50, 52, 102, 104, 106, 121])
    FOLLOW_process_expr_in_process_block2384 = frozenset([4, 11, 22, 50, 52, 102, 104, 106, 121])
    FOLLOW_CCBRACE_in_process_block2387 = frozenset([1])
    FOLLOW_OBRACE_in_process_trans2413 = frozenset([50])
    FOLLOW_ID_in_process_trans2415 = frozenset([24])
    FOLLOW_COMMA_in_process_trans2417 = frozenset([4, 45, 50])
    FOLLOW_process_events_in_process_trans2419 = frozenset([21, 24])
    FOLLOW_process_finalstate_in_process_trans2421 = frozenset([21, 24])
    FOLLOW_CBRACE_in_process_trans2424 = frozenset([1])
    FOLLOW_COMMA_in_process_finalstate2447 = frozenset([50, 104])
    FOLLOW_process_finalident_in_process_finalstate2449 = frozenset([1])
    FOLLOW_expressions_in_process_expr2502 = frozenset([1])
    FOLLOW_network_send_in_process_expr2506 = frozenset([1])
    FOLLOW_network_mcast_in_process_expr2510 = frozenset([1])
    FOLLOW_network_bcast_in_process_expr2514 = frozenset([1])
    FOLLOW_transaction_in_process_expr2517 = frozenset([1])
    FOLLOW_AWAIT_in_transaction2527 = frozenset([82])
    FOLLOW_OCBRACE_in_transaction2529 = frozenset([22, 108])
    FOLLOW_trans_in_transaction2531 = frozenset([22, 108])
    FOLLOW_CCBRACE_in_transaction2534 = frozenset([1])
    FOLLOW_WHEN_in_trans2554 = frozenset([50])
    FOLLOW_ID_in_trans2556 = frozenset([32])
    FOLLOW_DDOT_in_trans2558 = frozenset([1, 4, 11, 17, 50, 52, 77, 102, 104, 106, 121])
    FOLLOW_trans_body_in_trans2560 = frozenset([1, 4, 11, 17, 50, 52, 77, 102, 104, 106, 121])
    FOLLOW_expressions_in_trans_body2593 = frozenset([1])
    FOLLOW_next_trans_in_trans_body2597 = frozenset([1])
    FOLLOW_next_break_in_trans_body2601 = frozenset([1])
    FOLLOW_transaction_in_trans_body2605 = frozenset([1])
    FOLLOW_network_send_in_trans_body2609 = frozenset([1])
    FOLLOW_network_mcast_in_trans_body2613 = frozenset([1])
    FOLLOW_network_bcast_in_trans_body2617 = frozenset([1])
    FOLLOW_NEXT_in_next_trans2635 = frozenset([82])
    FOLLOW_OCBRACE_in_next_trans2637 = frozenset([22, 108])
    FOLLOW_trans_in_next_trans2639 = frozenset([22, 108])
    FOLLOW_CCBRACE_in_next_trans2642 = frozenset([1])
    FOLLOW_BREAK_in_next_break2663 = frozenset([95])
    FOLLOW_SEMICOLON_in_next_break2665 = frozenset([1])
    FOLLOW_assignment_in_expressions2681 = frozenset([1])
    FOLLOW_conditional_in_expressions2685 = frozenset([1])
    FOLLOW_object_block_in_expressions2689 = frozenset([1])
    FOLLOW_function_call_block_in_expressions2693 = frozenset([1])
    FOLLOW_set_block_in_expressions2697 = frozenset([1])
    FOLLOW_internal_event_block_in_expressions2701 = frozenset([1])
    FOLLOW_msg_stall_in_expressions2705 = frozenset([1])
    FOLLOW_set_access_in_expressions2709 = frozenset([1])
    FOLLOW_undefine_in_expressions2713 = frozenset([1])
    FOLLOW_process_finalident_in_assignment2720 = frozenset([42])
    FOLLOW_EQUALSIGN_in_assignment2722 = frozenset([14, 50, 57, 79])
    FOLLOW_assign_types_in_assignment2724 = frozenset([95])
    FOLLOW_SEMICOLON_in_assignment2726 = frozenset([1])
    FOLLOW_object_expr_in_assign_types2748 = frozenset([1])
    FOLLOW_message_constr_in_assign_types2752 = frozenset([1])
    FOLLOW_math_op_in_assign_types2756 = frozenset([1])
    FOLLOW_set_func_in_assign_types2760 = frozenset([1])
    FOLLOW_INT_in_assign_types2764 = frozenset([1])
    FOLLOW_BOOL_in_assign_types2768 = frozenset([1])
    FOLLOW_NID_in_assign_types2772 = frozenset([1])
    FOLLOW_val_range_in_math_op2783 = frozenset([68, 84])
    FOLLOW_set_in_math_op2785 = frozenset([50, 57])
    FOLLOW_val_range_in_math_op2793 = frozenset([1])
    FOLLOW_STALL_in_msg_stall2799 = frozenset([95])
    FOLLOW_SEMICOLON_in_msg_stall2801 = frozenset([1])
    FOLLOW_ACCESS_in_set_access2813 = frozenset([95])
    FOLLOW_SEMICOLON_in_set_access2815 = frozenset([1])
    FOLLOW_UNDEF_in_undefine2829 = frozenset([50])
    FOLLOW_ID_in_undefine2831 = frozenset([95])
    FOLLOW_SEMICOLON_in_undefine2833 = frozenset([1])
    FOLLOW_if_stmt_in_conditional2850 = frozenset([1])
    FOLLOW_ifnot_stmt_in_conditional2854 = frozenset([1])
    FOLLOW_IF_in_if_stmt2873 = frozenset([14, 50, 57, 79, 81])
    FOLLOW_cond_comb_in_if_stmt2875 = frozenset([82])
    FOLLOW_OCBRACE_in_if_stmt2877 = frozenset([4, 11, 17, 22, 50, 52, 102, 104, 106, 121])
    FOLLOW_if_expression_in_if_stmt2879 = frozenset([22])
    FOLLOW_CCBRACE_in_if_stmt2881 = frozenset([1, 37])
    FOLLOW_ELSE_in_if_stmt2888 = frozenset([82])
    FOLLOW_OCBRACE_in_if_stmt2892 = frozenset([4, 11, 17, 22, 50, 52, 102, 104, 106, 121])
    FOLLOW_else_expression_in_if_stmt2894 = frozenset([22])
    FOLLOW_CCBRACE_in_if_stmt2896 = frozenset([1, 37])
    FOLLOW_IF_in_ifnot_stmt3002 = frozenset([74])
    FOLLOW_NEG_in_ifnot_stmt3004 = frozenset([14, 50, 57, 79, 81])
    FOLLOW_cond_comb_in_ifnot_stmt3006 = frozenset([82])
    FOLLOW_OCBRACE_in_ifnot_stmt3008 = frozenset([4, 11, 17, 22, 50, 52, 102, 104, 106, 121])
    FOLLOW_if_expression_in_ifnot_stmt3010 = frozenset([22])
    FOLLOW_CCBRACE_in_ifnot_stmt3012 = frozenset([1, 37])
    FOLLOW_ELSE_in_ifnot_stmt3019 = frozenset([82])
    FOLLOW_OCBRACE_in_ifnot_stmt3023 = frozenset([4, 11, 17, 22, 50, 52, 102, 104, 106, 121])
    FOLLOW_else_expression_in_ifnot_stmt3025 = frozenset([22])
    FOLLOW_CCBRACE_in_ifnot_stmt3027 = frozenset([1, 37])
    FOLLOW_exprwbreak_in_if_expression3128 = frozenset([1, 4, 11, 17, 50, 52, 102, 104, 106, 121])
    FOLLOW_exprwbreak_in_else_expression3143 = frozenset([1, 4, 11, 17, 50, 52, 102, 104, 106, 121])
    FOLLOW_expressions_in_exprwbreak3158 = frozenset([1])
    FOLLOW_network_send_in_exprwbreak3162 = frozenset([1])
    FOLLOW_network_mcast_in_exprwbreak3166 = frozenset([1])
    FOLLOW_network_bcast_in_exprwbreak3170 = frozenset([1])
    FOLLOW_transaction_in_exprwbreak3174 = frozenset([1])
    FOLLOW_next_break_in_exprwbreak3178 = frozenset([1])
    FOLLOW_cond_rel_in_cond_comb3192 = frozenset([1, 112, 148])
    FOLLOW_combinatorial_operator_in_cond_comb3195 = frozenset([14, 50, 57, 79, 81])
    FOLLOW_cond_rel_in_cond_comb3197 = frozenset([1, 112, 148])
    FOLLOW_OBRACE_in_cond_rel3214 = frozenset([14, 50, 57, 79, 81])
    FOLLOW_cond_sel_in_cond_rel3217 = frozenset([1, 21])
    FOLLOW_CBRACE_in_cond_rel3219 = frozenset([1, 21])
    FOLLOW_cond_type_expr_in_cond_sel3243 = frozenset([1, 111, 113, 114, 115, 116, 117])
    FOLLOW_relational_operator_in_cond_sel3246 = frozenset([14, 50, 57, 79])
    FOLLOW_cond_type_expr_in_cond_sel3248 = frozenset([1, 111, 113, 114, 115, 116, 117])
    FOLLOW_cond_types_in_cond_type_expr3268 = frozenset([1, 68, 72, 84])
    FOLLOW_set_in_cond_type_expr3271 = frozenset([14, 50, 57, 79])
    FOLLOW_cond_types_in_cond_type_expr3283 = frozenset([1, 68, 72, 84])
    FOLLOW_object_expr_in_cond_types3304 = frozenset([1])
    FOLLOW_set_func_in_cond_types3308 = frozenset([1])
    FOLLOW_INT_in_cond_types3312 = frozenset([1])
    FOLLOW_BOOL_in_cond_types3316 = frozenset([1])
    FOLLOW_NID_in_cond_types3320 = frozenset([1])
    FOLLOW_policy_op_type_in_policy_op3352 = frozenset([1, 148])
    FOLLOW_148_in_policy_op3355 = frozenset([125, 129, 130, 134])
    FOLLOW_policy_op_type_in_policy_op3357 = frozenset([1, 148])
    FOLLOW_135_in_policy_op3374 = frozenset([1])
    FOLLOW_policy_data_type_in_policy_data3452 = frozenset([1, 148])
    FOLLOW_148_in_policy_data3455 = frozenset([119, 120, 124, 125, 127])
    FOLLOW_policy_data_type_in_policy_data3457 = frozenset([1, 148])
    FOLLOW_135_in_policy_data3474 = frozenset([1])
    FOLLOW_policy_coh_type_in_policy_coh3544 = frozenset([1, 148])
    FOLLOW_148_in_policy_coh3547 = frozenset([140, 145])
    FOLLOW_policy_coh_type_in_policy_coh3549 = frozenset([1, 148])
    FOLLOW_135_in_policy_coh3566 = frozenset([1])
    FOLLOW_ID_in_label_state3623 = frozenset([81])
    FOLLOW_OBRACE_in_label_state3625 = frozenset([125, 129, 130, 134, 135])
    FOLLOW_policy_op_in_label_state3627 = frozenset([24])
    FOLLOW_COMMA_in_label_state3629 = frozenset([119, 120, 124, 125, 127, 135])
    FOLLOW_policy_data_in_label_state3631 = frozenset([24])
    FOLLOW_COMMA_in_label_state3633 = frozenset([135, 140, 145])
    FOLLOW_policy_coh_in_label_state3635 = frozenset([21])
    FOLLOW_CBRACE_in_label_state3637 = frozenset([1])
    FOLLOW_ID_in_label_message3661 = frozenset([81])
    FOLLOW_OBRACE_in_label_message3663 = frozenset([125, 129, 130, 134, 135])
    FOLLOW_policy_op_in_label_message3665 = frozenset([24])
    FOLLOW_COMMA_in_label_message3667 = frozenset([119, 120, 124, 125, 127, 135])
    FOLLOW_policy_data_in_label_message3669 = frozenset([24])
    FOLLOW_COMMA_in_label_message3671 = frozenset([135, 140, 145])
    FOLLOW_policy_coh_in_label_message3673 = frozenset([21])
    FOLLOW_CBRACE_in_label_message3675 = frozenset([1])
    FOLLOW_DATA_in_data_rule3699 = frozenset([81])
    FOLLOW_OBRACE_in_data_rule3701 = frozenset([50])
    FOLLOW_label_state_in_data_rule3703 = frozenset([21])
    FOLLOW_CBRACE_in_data_rule3705 = frozenset([95])
    FOLLOW_SEMICOLON_in_data_rule3707 = frozenset([1])
    FOLLOW_122_in_local_rule3724 = frozenset([81])
    FOLLOW_OBRACE_in_local_rule3726 = frozenset([50])
    FOLLOW_label_state_in_local_rule3728 = frozenset([24])
    FOLLOW_COMMA_in_local_rule3730 = frozenset([50])
    FOLLOW_label_message_in_local_rule3732 = frozenset([24])
    FOLLOW_COMMA_in_local_rule3734 = frozenset([50])
    FOLLOW_label_state_in_local_rule3736 = frozenset([21])
    FOLLOW_CBRACE_in_local_rule3738 = frozenset([95])
    FOLLOW_SEMICOLON_in_local_rule3740 = frozenset([1])
    FOLLOW_136_in_rule_action3760 = frozenset([42])
    FOLLOW_EQUALSIGN_in_rule_action3762 = frozenset([82])
    FOLLOW_OCBRACE_in_rule_action3764 = frozenset([4, 22, 50, 52, 102, 104, 106, 121])
    FOLLOW_expressions_in_rule_action3766 = frozenset([4, 22, 50, 52, 102, 104, 106, 121])
    FOLLOW_CCBRACE_in_rule_action3769 = frozenset([1])
    FOLLOW_131_in_rule3785 = frozenset([81])
    FOLLOW_OBRACE_in_rule3787 = frozenset([50])
    FOLLOW_label_state_in_rule3789 = frozenset([24])
    FOLLOW_COMMA_in_rule3791 = frozenset([50])
    FOLLOW_label_message_in_rule3793 = frozenset([24])
    FOLLOW_COMMA_in_rule3795 = frozenset([50])
    FOLLOW_label_state_in_rule3797 = frozenset([21, 24])
    FOLLOW_COMMA_in_rule3800 = frozenset([136])
    FOLLOW_rule_action_in_rule3802 = frozenset([21])
    FOLLOW_CBRACE_in_rule3806 = frozenset([95])
    FOLLOW_SEMICOLON_in_rule3808 = frozenset([1])
    FOLLOW_data_rule_in_policy_rule3833 = frozenset([1])
    FOLLOW_local_rule_in_policy_rule3837 = frozenset([1])
    FOLLOW_rule_in_policy_rule3841 = frozenset([1])
    FOLLOW_128_in_policy_block3848 = frozenset([50])
    FOLLOW_ID_in_policy_block3850 = frozenset([82])
    FOLLOW_OCBRACE_in_policy_block3852 = frozenset([22, 29, 122, 131])
    FOLLOW_policy_rule_in_policy_block3854 = frozenset([22, 29, 122, 131])
    FOLLOW_CCBRACE_in_policy_block3857 = frozenset([1])
    FOLLOW_policy_block_in_policy_file3875 = frozenset([1, 128])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("ProtoCCLexer", ProtoCCParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
