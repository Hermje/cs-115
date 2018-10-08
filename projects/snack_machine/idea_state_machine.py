class SuperState:
    def __init__(self, name, states):
        self.s = states
        self.n = name

    def add_state(self, state):
        self.s.append(state)

    def get_name(self):
        return self.n

    def get_states(self):
        return self.s

class State:
    def __init__(self, id):
        self.i = id

    def get_name(self):
        return self.i

state_a = State("idle")
state_b = State("insert")
state_c = State("select")

vending_machine = SuperState("Vending Machine", [state_a, state_b, state_c])

for state in vending_machine.get_states():
    print(state.get_name())
