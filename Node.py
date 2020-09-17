class Node:
    def __init__(self, lowest_cost_parent=None, pos=None):
        self.pos = pos
        self.children = []
        self.lowest_cost_parent = lowest_cost_parent

        self.g = 0
        self.h = 0

    def get_total_cost(self):
        return self.g + self.h

    def __eq__(self, other):
        return self.pos == other.pos

    def __gt__(self, other):
        return self.get_total_cost() > other.get_total_cost()

    def __str__(self):
        return "Position: " + str(self.pos) + ". Total cost: " + str(self.get_total_cost())
