from PDA import *
from State import *

state5 = State(state_type="Accept")
state4 = State(state_type="Pop")
state3 = State(state_type="Pop")
state2 = State(state_type="Push")
state1 = State(state_type="Read")

# add transitions for 'a', 'b', and the 'end' of the tape.
state1.add_transition(state2, character="a")
state1.add_transition(state3, character="b")
state1.add_transition(state4, character="!")

state2.add_transition(state1, character="X")
state3.add_transition(state1, character="X")

state4.add_transition(state5, character="!")

start_state = State(state_type="Start", next_state=state1)

# Give the start state the first "real state" as a parameter.
start_state.add_transition(state1)

my_pda = PDA(start_state)
my_pda.start(tape="aaaaabbb!", stack=['!'])
