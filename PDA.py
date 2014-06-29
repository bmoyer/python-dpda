class PDA(object):
    def __init__(self, start_state, tape=""):
        """Automata are created by supplying an initial state."""
        self.start_state = start_state

    def start(self, tape, stack=[]):
        """After we have the tape, stack, and the inital state, we simply call
        the action() function of the initial state."""
        self.start_state.action(tape, stack)
