#  Caching policies (Synapse, Sec. V-A, VI-A).
#
#  A policy is an ordered list of rules
#      Rule( S(op,data,coh), M(op,data,coh), S(op,data,coh) );
#  read as  initialState + Message -> finalState  (pattern semantics in Labels.py). For a request
#  received from a child, the first rule whose initial-state pattern matches the label of the current
#  client state and whose message pattern matches the label of the request gives the abstract state
#  the client must reach before the manager serves the request (Alg. 1, line 3).
#
#  Policy files reuse the SSP comment syntax:
#      // write-back, inclusive
#      Policy WB_INCL {
#          Rule( S(_,NP,_), M(Rd,None,_), S(Rd,P,_) );   // read miss
#      }
#  A file may contain several policies; `load_policy(path, name)` selects one by name.
#
#  A rule written `Local( ... )` instead of `Rule( ... )` is served by the controller on its own: it
#  takes the final state without asking its parent (e.g. the bytes of a child's non-temporal store
#  written into an LLC that owns the block's address range). The parent's protocol is rewritten for
#  it (LocalWrite.py); every block must have a single cache at the controller's level.
#
#  Requests from the parent are steered by the client (Alg. 1, line 11): by default the children
#  are downgraded only as far as the client's final state requires. A policy can ask for more with
#      Downgrade( S(op,data,coh), M(op,data,coh), S(op,data,coh) );
#  read as: on a request from the parent matching M, received in a client state matching the first
#  S, downgrade the children to at most the second S (e.g. an inclusive LLC that recalls the block
#  from its children on every forward that takes write permission away from it). The short form
#      Downgrade( M(op,data,coh), S(op,data,coh) );
#  applies in any client state.
#
#  Where the controller keeps the data (inclusion, Alg. 1 lines 4 and 8):
#      Data( S(op,data,coh) );
#  the controller holds a copy of the block only while its children's abstract state (the label of
#  the manager state) matches the pattern; elsewhere the block's data lives in the children and the
#  controller keeps the coherence state only (a tag). Without it the controller always holds the
#  data (inclusive). `Data( S(None,NP,_) )` is an exclusive controller.
#
#  A child that drops its copy must then hand the data back with the message it sends (the
#  protocol's evictions carry the block, e.g. MESIF PutS/PutE); the controller keeps it where the
#  policy places the data (Synthesis._keep_returned_data).

from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional

from Algorithms.Synapse.Labels import Label, LabelPattern
from Debug.Monitor.ClassDebug import Debug
from Parser import ProtoCCLexer, ProtoCCParser
from third_party.antlr3.streams import CommonTokenStream, InputStream


@dataclass(frozen=True)
class Rule:
    start: LabelPattern
    msg: LabelPattern
    final: LabelPattern
    text: str = ""
    local: bool = False     # Local( ... ): reached without the parent

    def __post_init__(self):
        if (self.start.kind, self.msg.kind, self.final.kind) != ("S", "M", "S"):
            raise ValueError(f"a rule must be Rule(S(..), M(..), S(..)): {self.text}")

    def matches(self, state: Label, msg: Label) -> bool:
        return self.start.matches(state) and self.msg.matches(msg)

    def __str__(self):
        return f"{'Local' if self.local else 'Rule'}( {self.start}, {self.msg}, {self.final} )"

    @staticmethod
    def parse(rule_tree) -> Rule | None: 
        local = False
        if rule_tree.type == ProtoCCParser.LOCAL_RULE_:
            local = True
        elif not rule_tree.type == ProtoCCParser.RULE_:
            return None

        start_tree, msg_tree, final_tree = rule_tree.getChildren()
        start = LabelPattern.parse(start_tree)
        msg   = LabelPattern.parse(msg_tree)
        final = LabelPattern.parse(final_tree)
        if start is None or msg is None or final is None: 
            return None     

        return Rule(start, msg, final, f"Rule({start}, {msg}, {final})", local)

class Policy:
    def __init__(self, name: str, rules: List[Rule],
                 data: Optional[LabelPattern] = None):
        self.name = name
        self.rules = rules
        self.data = data

    @property
    def local_rules(self) -> List[Rule]:
        return [rule for rule in self.rules if rule.local]

    @property
    def exclusive(self) -> bool:
        return self.data is not None

    def keeps_data(self, children: Label) -> bool:
        """Data( ... ): whether the controller holds the block's data while its children are in the
        abstract state `children` (always, without the directive)."""
        return self.data is None or self.data.matches(children)

    def match_rule(self, state: Label, msg: Label) -> Optional[Rule]:
        """policy.match-rule() of Alg. 1: the first rule matching (client state, request)."""
        for rule in self.rules:
            if rule.matches(state, msg):
                return rule
        return None

    def __str__(self):
        extra = [f"Data( {self.data} )"] if self.data is not None else []
        return f"Policy {self.name} {{\n" + "".join(f"    {rule};\n" for rule in self.rules + self.downgrades) \
            + "".join(f"    {line};\n" for line in extra) + "}"

    @staticmethod 
    def parse(path: Path) -> List[Policy] | None:
        policies: List[Policy] = []
    
        with open(path) as f:
            tokens = CommonTokenStream(ProtoCCLexer.ProtoCCLexer(InputStream(f)))
        parser = ProtoCCParser.ProtoCCParser(tokens)
        file_tree = parser.document().tree
        if file_tree is None:
            return None # Empty file

        if file_tree.type != ProtoCCParser.POL_FILE_:
            return None # No Error here, this just might be a pcc file.
        
        for pol_tree in file_tree.getChildren():
            if pol_tree.type != ProtoCCParser.POLICY_:
                # This should never happen, the parser should have rejected the file. 
                raise ValueError(f"Expected a policy in {path}, got {pol_tree.toStringTree()}")
            
            name = pol_tree.getChild(0).getText()

            rules: List[Rule] = []
            data_rule: LabelPattern | None = None
            for rule_tree in pol_tree.getChildren()[1:]:
                match rule_tree.type:
                    case ProtoCCParser.RULE_:
                        rule = Rule.parse(rule_tree)
                        if rule: 
                            rules.append(rule)
                    case ProtoCCParser.DATA_RULE_:
                        if not data_rule is None:
                            raise ValueError(f"Policy {name} in {path} has more than one Data( ... ) directive")

                        data_rule = LabelPattern.parse(rule_tree.getChild(0))
                    case ProtoCCParser.LOCAL_RULE_:
                        l_rule = Rule.parse(rule_tree.getChild(0))
                        if l_rule:
                            rules.append(l_rule)

                    case _: # Shouldn't happen, the parser should have rejected the file.
                        raise ValueError(f"Unexpected rule type {rule_tree.type} in policy {name} in {path}")

            if len(rules) == 0:
                Debug.pwaring(f"Policy {name} in {path} has no rules!")

            pol = Policy(name, rules, data_rule)
            policies.append(pol)

        return policies


def load_policy(path: Path, name: Optional[str] = None) -> Policy:
    """Loads the policy `name` of a file (the only one of the file if no name is given)."""
    policies = Policy.parse(path)
    if name is None:
        if len(policies) != 1:
            raise ValueError(f"{path} defines {[p.name for p in policies]}, select one by name")
        return policies[0]
    for policy in policies:
        if policy.name == name:
            return policy
    raise ValueError(f"policy {name} not found in {path}")
