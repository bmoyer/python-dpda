import PDA, State


state3 = State(state_type="Accept")
state2 = State(state_type="Read")
state1 = State(state_type="Read")

state1.add_transition(state2, character="a")
state2.add_transition(state3, character="b")

start_state = State(state_type="Start", next_state=state1)

# Give the start state the first "real state" as a parameter.
start_state.add_transition(state1)

my_pda = PDA(start1, tape="ab")
my_pda.start()
