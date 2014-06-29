python-dpda
===========

Python Deterministic Push Down Automaton<br>

This module allows a user to:<br>
    - Create a PDA object with a designated start state<br>
    - Create multiple State objects, of the types:<br>
        * Read states<br>
        * Push states<br>
        * Pop states<br> 
        * Accept states<br>
        * Implicit Reject states<br>
    - Add transitions to each state, which determine the behavior of the automaton<br>
    - Start a PDA by feeding it a tape (list or string)<br> 
<br>
If the python-dpda crashes, it means that the tape word was not in the language expressed by your pushdown automaton.  This program is built to resemble a theoretical PDA, which is quite capable of crashing!

http://i.imgur.com/43bvWTp.png
![alt tag](http://i.imgur.com/43bvWTp.png)
