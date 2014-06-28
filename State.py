import weakref

class State(object):
    def __init__(self,state_type="Default", next_state=None):
        self.state_type = state_type
        self.transitions  = set()
        if state_type == "Start":
            self.next_state == next_state
        

    def add_transition(self, character, next_state):
        transition = {'char': character, 'next': next_state }
        self.transitions.add(transition)

    def get_next_state(self):
        if self.state_type == "Start":
            return self.next_state

        if self.state_type == "Default":
            for transition in self.transitions:
                

    def action(self, tape, stack):
         if self.state_type == "Default":
             self.tape = tape
             self.stack = stack
             self.get_next_state().action(tape, stack)
         if self.state_type == "Push":
            
