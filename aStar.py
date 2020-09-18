import Map
from Node import Node

connected_nodes_directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def a_star_search(map, start, end):
    """Based on A* pseudo-code from Medium'"""
    open_nodes = []
    closed_nodes = []
    start_node = Node(None, start)
    start_node.h = abs(start_node.pos[0] - end[0]) + \
        abs(start_node.pos[1] - end[1])
    open_nodes.append(start_node)
    end_node = Node(None, end)

    while open_nodes:
        current_node = open_nodes.pop(0)
        closed_nodes.append(current_node)

        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.pos)
                current = current.lowest_cost_parent
            return path[::-1]
        children = []
        for new_pos in connected_nodes_directions:
            node_pos = (
                current_node.pos[0] + new_pos[0], current_node.pos[1] + new_pos[1])

            # It's a wall, cannot walk here
            if map[node_pos[0]][node_pos[1]] == -1:
                continue

            # Create new child in this new pos
            new_node = Node(current_node, node_pos)
            children.append(new_node)

        # Adds the child to the parents child-list
        for child in children:
            # The tile cost is the g cost of the current child, it is found on the map
            tile_cost = map[child.pos[0]][child.pos[1]]

            # Checks if the child has previously been created, and therefor is either in open or closed nodes
            # if it is, we rather look at the old version and update it
            for i in range(len(open_nodes)):
                if open_nodes[i] == child:
                    child = open_nodes[i]
            for j in range(len(closed_nodes)):
                if closed_nodes[j] == child:
                    child = closed_nodes[j]

            # appending the correct node to children list
            current_node.children.append(child)

            if child not in open_nodes and child not in closed_nodes:
                # It has not yet been evaluated, and we don't need to propagate it
                create_parent_child_relation(
                    child, current_node, end, tile_cost)
                open_nodes.append(child)
                open_nodes.sort()

            # (found cheaper path to the child):
            elif current_node.g + tile_cost < child.g:
                # ∗ attach-and-eval(S,X)
                # ∗ If S ∈ CLOSED then propagate-path-improvements(S)
                create_parent_child_relation(
                    child, current_node, end, tile_cost)
                if child in closed_nodes:
                    propagate_path_improvements(child)

    return False


def create_parent_child_relation(child, parent, end, tile_cost):
    child.lowest_cost_parent = parent
    child.g = parent.g + tile_cost
    child.h = abs(child.pos[0] - end[0]) + abs(child.pos[1] - end[1])


def propagate_path_improvements(parent):
    """Goes through the children and possibly many other decedents
    If parent is no longer their best parent, the propagation ceases,
    if any child can have parent as its best parent it must be updated
    and propagated further to the children of the children"""
    for child in parent.children:
        if parent.g + 1 < child.g:
            child.lowest_cost_parent = parent
            child.g = parent.g + 1
            propagate_path_improvements(child)


def add_path_to_map(map, path):
    for n in path:
        map.set_cell_value(n, " p ")


def main():
    while (True):
        n = -1
        while not (5 > n > 0):
            n = int(input("Task number (1-4): "))
        map = Map.Map_Obj(n)
        int_map, str_map = map.get_maps()
        map.show_map()
        start_pos = (map.get_start_pos()[0], map.get_start_pos()[1])
        end_pos = (map.get_goal_pos()[0], map.get_goal_pos()[1])
        path = a_star_search(int_map, start_pos, end_pos)
        add_path_to_map(map, path)
        int_map, str_map = map.get_maps()
        map.show_map()
        if ('q' == input("'q' to quit: ")):
            break


main()
