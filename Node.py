class Node:
    def __init__(self, best_parent=None, position=None):
        """
        Initialize the node. Nodes are born without parents. The optimal parent is added later: like adoption
        :param position: is the x and y coordinate of the node
        """
        self.position = position
        self.children = []
        self.best_parent = best_parent

        self.g = 0
        self.h = 0

    def get_total_cost(self):
        return self.g + self.h

    def __eq__(self, other):
        """We overload eq so that we can compare two nodes"""
        return self.position == other.position

    def __gt__(self, other):
        """We overload gt so that we can sort the list based on f - value"""
        return self.get_total_cost() > other.get_total_cost()

    def __str__(self):
        return "|Position: " + str(self.position) + " f-value: " + str(self.get_total_cost()) + "| "
