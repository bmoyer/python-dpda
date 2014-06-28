import weakref

class State(object):
    def __init__(self,state_type="Default", next_state=None):
        self.state_type = state_type
        self.transitions  = set()
        self.next_state = next_state

    def add_transition(self, character=None, next_state):
        transition = {'char': character, 'next': next_state }
        self.transitions.add(transition)

    def get_next_state(self, character=None):
        if self.state_type == "Start":
            (next_state, ) = self.transitions
            return next_state

        if self.state_type == "Default":
            for transition in self.transitions:
                if transition['char'] == character:
                    return transition['next']

        if self.state_type == "Push":
            return self.next_state
                  
        if self.state_type = "Pop":


                

    def action(self, tape, stack):
         if self.state_type == "Default":
             self.get_next_state(character=tape[0]).action(tape, stack)
         if self.state_type == "Push":
             stack.append(
