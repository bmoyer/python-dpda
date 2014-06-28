python-dpda
===========

Python Deterministic Push Down Automaton

This module allows a user to:
    - Create a PDA object with a designated start state
    - Create multiple State objects, of the types:
        - Read states 
        - Push states 
        - Pop states 
        - Accept states 
        - Implicit Reject states 
    - Add transitions to each state, which determine the behavior of the automaton 
    - Start a PDA by feeding it a tape (list or string) 
