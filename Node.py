class Node:
    """
  Override eq and gt to be able to compare two nodes.
  h, g and f are estimated cost to end node, cost from start node and the total cost respectively.
  """

    def __init__(self, lowest_cost_parent=None, pos=None):
        self.pos = pos
        self.children = []
        self.lowest_cost_parent = lowest_cost_parent
        self.g = 0
        self.h = 0

    def __eq__(self, other):
        return self.pos == other.pos

    def __gt__(self, other):
        return self.get_f() > other.get_f()

    def get_f(self):
        return self.g + self.h
