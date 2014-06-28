python-dpda
===========

Python Deterministic Push Down Automaton

This module allows a user to:
    - Create a PDA object with a designated start state
    - Create multiple State objects, of the types:
        - Read states<br>
        - Push states<br>
        - Pop states<br> 
        - Accept states<br>
        - Implicit Reject states<br>
    - Add transitions to each state, which determine the behavior of the automaton<br>
    - Start a PDA by feeding it a tape (list or string)<br> 
