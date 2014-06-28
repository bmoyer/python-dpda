class State(object):
    def __init__(self,state_type, next_state=None):
        self.state_type = state_type
        self.transitions  = set()
        self.next_state = next_state


    def add_transition(self, next_state, character=None):
        transition = {'char': character, 'next': next_state }
        self.transitions.add(transition)


    def get_next_state(self, character=None):
        if self.state_type == "Start":
            (next_state, ) = self.transitions
            return next_state

        if self.state_type == "Read":
            for transition in self.transitions:
                if transition['char'] == character:
                    return transition['next']

        if self.state_type == "Push":
            return self.next_state
                  
        if self.state_type == "Pop":
            for transition in self.transitions:
                if transition['char'] == character:
                    return transition['next']


    def action(self, tape, stack, char=None):
         if self.state_type == "Start":
            self.get_next_state().action(tape, stack)

         elif self.state_type == "Read":
             next_state = self.get_next_state(character=tape[0]).action(tape[1:], stack)
         elif self.state_type == "Push":
             stack.append(char)
             self.get_next_state().action(tape, stack)
         elif self.state_type == "Pop":
             char = stack.pop()
             self.get_next_state(character=char).action(tape,stack)
         elif self.state_type == "Accept":
             print("Tape accepted!") 
             return
