"""This is an example of building a PDA to detect contiguous substrings 
of a's followed by the same number of b's, repeatedly."""
from PDA import *
from State import *

accept5 = State(state_type="Accept")
pop4 = State(state_type="Pop")
pop3 = State(state_type="Pop")
push2 = State(state_type="Push")
read1 = State(state_type="Read")

# add transitions for 'a', 'b', and the 'end' of the tape.
read1.add_transition(push2, character="a")
read1.add_transition(pop3, character="b")
read1.add_transition(pop4, character="!")

push2.add_transition(read1, character="X")
pop3.add_transition(read1, character="X")

pop4.add_transition(accept5, character="!")

start_state = State(state_type="Start", next_state=read1)

my_pda = PDA(start_state)

# Testing a^21 b^20, which is not in the language of this PDA
tape_word = "a"*21 + "b"*20 + "!"
my_pda.start(tape=tape_word, stack=['!'])

# Testing a^20 b^20, which is in the language of this PDA
tape_word = "a"*20 + "b"*20 + "!"
my_pda.start(tape=tape_word, stack=['!'])

tape_word = "a"*20 + "b"*20 + "a"*12 + "b"*12 + "a"*192 + "b"*192 + "!"
my_pda.start(tape=tape_word, stack=['!'])

tape_word = "a"*100+ "b"*100 + "!"
my_pda.start(tape=tape_word, stack=['!'])
