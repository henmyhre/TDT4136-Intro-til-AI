class Node:
    def __init__(self, lowest_cost_parent=None, pos=None):
        self.pos = pos
        self.children = []
        self.lowest_cost_parent = lowest_cost_parent
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.pos == other.pos

    def __gt__(self, other):
        self.set_f()
        return self.get_f() > other.get_f()

    def __str__(self):
        self.set_f()
        return "Position: " + str(self.pos) + ". Total cost: " + str(self.get_f())

    def set_f(self):
        self.f = self.g + self.h

    def get_f(self):
        return self.f
