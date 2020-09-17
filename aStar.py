import Map
from Node import Node


def a_star(board, start, end):
    """Based on A* pseudo-code from Medium'"""
    open_nodes = []
    closed_nodes = []
    start_node = Node(None, start)
    start_node.h = get_distance_between_nodes(start_node.pos, end)
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

        # Generate children, they can be north, south, east or west of the parent
        children = []
        for new_pos in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            # For moving diagonally [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
            node_pos = (
                current_node.pos[0] + new_pos[0], current_node.pos[1] + new_pos[1])

            # It's a wall, cannot walk here
            if board[node_pos[0]][node_pos[1]] == -1:
                continue

            # Create new child in this new pos
            new_node = Node(current_node, node_pos)
            children.append(new_node)

        # Adds the child to the parents child-list
        for child in children:
            # The tile cost is the g cost of the current child, it is found on the board
            tile_cost = board[child.pos[0]][child.pos[1]]

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
                attach_and_eval(child, current_node, end, tile_cost)
                open_nodes.append(child)
                open_nodes.sort()

            # (found cheaper path to the child):
            elif current_node.g + tile_cost < child.g:
                # ∗ attach-and-eval(S,X)
                # ∗ If S ∈ CLOSED then propagate-path-improvements(S)
                attach_and_eval(child, current_node, end, tile_cost)
                if child in closed_nodes:
                    propagate_path_improvements(child)

    return False


def get_distance_between_nodes(node_1, node_2):
    return abs(node_1[0] - node_2[0]) + abs(node_1[1] - node_2[1])


def attach_and_eval(child, parent, end, tile_cost):
    """Attaches a node to its best parent (so far)
    the child's g'value is computed based on parent, h independently"""
    child.lowest_cost_parent = parent
    child.g = parent.g + tile_cost
    child.h = get_distance_between_nodes(child.pos, end)


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


def draw_path(board, path):
    for node in path:
        board.set_cell_value(node, " Ø ", True)


def main():
    quit = False
    while not (quit):
        task = -1
        while not (5 > task > 0):
            task = int(input("Task number (1-4): "))
        board = Map.Map_Obj(task)
        int_map, str_map = board.get_maps()
        board.show_map()
        # print(int_map)
        # print(str_map)
        tuple_start = (board.get_start_pos()[0], board.get_start_pos()[1])
        tuple_end = (board.get_goal_pos()[0], board.get_goal_pos()[1])
        # print("Start:", tuple_start, " Goal:", tuple_end)
        path = a_star(int_map, tuple_start, tuple_end)
        # print("Path:", path)
        # print("ready to draw")
        try:
            draw_path(board, path)
            print("Found path")
        except TypeError:
            print("Found not path")
        int_map, str_map = board.get_maps()
        # print(str_map)
        board.show_map()
        if ('q' == input("'q' to quit. Anything else continues: ")):
            quit = True


main()
