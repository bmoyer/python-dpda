Python Deterministic Pushdown Automaton
===========

Python Deterministic Push Down Automaton<br>

This module allows a user to:<br>
    * Create a PDA object with a designated start state<br>
    * Create multiple State objects, of the types:<br>
     * Read states
     * Push states<br>
     * Pop states<br> 
     * Accept states<br>
     * Implicit Reject states<br>
    * Add transitions to each state, which determine the behavior of the automaton<br>
    * Start a PDA by feeding it a tape (list or string)<br> 
<br>
The code in this README will assemble and test the following pushdown automaton.  We use '!' for the END symbol on both the tape and the stack.

![alt tag](http://i.imgur.com/jheP0Zl.png )

Usage
===========

Creating a PDA and States:
    
    from PDA import *
    from State import *
     
    # Create each state, give start_state the first processing state of the PDA .
    accept5 = State(state_type="Accept")
    pop4 = State(state_type="Pop")
    pop3 = State(state_type="Pop")
    push2 = State(state_type="Push")
    read1 = State(state_type="Read")
    start_state = State(state_type="Start", next_state=read1)


    # Adding transitions to each state we've created.
    read1.add_transition(push2, character="a")
    read1.add_transition(pop3, character="b")
    read1.add_transition(pop4, character="!")
    push2.add_transition(read1, character="X")
    pop3.add_transition(read1, character="X")
    pop4.add_transition(accept5, character="!")

    # Now that our states are set up, we create the PDA with the start state as the sole argument.
    my_pda = PDA(start_state)

Running a tape through the PDA to check language membership:


    word = "a"*42 + "b"*42

    # '!' will be our END symbol, so we append it to the end of the tape.
    my_tape = word + "!"

    # Create a stack containing only the END symbol.
    my_stack = ['!']

    # Start the PDA by giving it a tape and stack as input.
    my_pda.start(tape=my_tape, stack=my_stack)

Output
==========
The PDA will print whether the tape was accepted or rejected.  If the PDA constructor is given the parameter verbose=True, then the states will report via STDOUT whenever they perform any action.  Verbose mode is suggested for students trying to solidify their understanding of pushdown automata.
