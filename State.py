class State(object):
    def __init__(self,state_type, next_state=None):
        self.state_type = state_type
        self.transitions  = list()
        self.next_state = next_state


    def add_transition(self, next_state, character=None):
        transition = {'char': character, 'next': next_state }
        self.transitions.append(transition)


    def get_next_state(self, character=None):
        if self.state_type == "Start":
            return self.next_state

        if self.state_type == "Read":
            if character == "":
                return self.transitions[0]['next']

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
             if not tape:
                 next_state = self.get_next_state(character="").action(tape[1:], stack)
             else:
                 next_state = self.get_next_state(character=tape[0]).action(tape[1:], stack)
         elif self.state_type == "Push":
             stack.append(char)
             self.get_next_state().action(tape, stack)
         elif self.state_type == "Pop":
             if not stack:
                self.get_next_state(character="").action(tape,stack)
             else:
                 char = stack.pop()
                 self.get_next_state(character=char).action(tape,stack)
         elif self.state_type == "Accept":
                 print("Tape accepted!") 
         else:
             print("else")
