class PDA(object):
    def __init__(self):
        self.states = []

    def add_state(self, state):
        self.states.add(state)

    def start(self, tape):
        self.states[0].action(tape, stack)
