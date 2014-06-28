class PDA(object):
    def __init__(self, start_state, tape=""):
        self.start_state = start_state

    def start(self, tape):
        self.start_state.action(tape, stack=[])
