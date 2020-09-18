import Map
from Node import Node


def a_star_search(map, start, end):
    """
    Partly based on A* pseudo-code from Medium:
    https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
    The differences is based on what I remembered from videos I watched. 
    """
    start_node = Node(None, start)
    start_node.h = abs(start_node.pos[0] - end[0]) + \
        abs(start_node.pos[1] - end[1])
    open_list = []
    closed_list = []
    open_list.append(start_node)
    end_node = Node(None, end)

    """Code stops if no open nodes left"""
    while open_list:
        current_node = open_list.pop(0)
        closed_list.append(current_node)
        children = []

        """Backtracking to calculate path when end node is reached"""
        if current_node == end_node:
            path = []
            while (current_node):
                path.append(current_node.pos)
                current_node = current_node.lowest_cost_parent
            return path

        """Checks all possible directions (up, right, down, left) and add them as children"""
        for direction_to_connected_node in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            node_pos = (
                current_node.pos[0] + direction_to_connected_node[0], current_node.pos[1] + direction_to_connected_node[1])
            if map[node_pos[0]][node_pos[1]] != -1:
                new_node = Node(current_node, node_pos)
                children.append(new_node)

        """
    Goes through children nodes.
    Skips if node is in closed_list.
    Checks if they aldready exists in open_list to not use recreated nodes.
    Adds parent relation if node is 'new'.
    Replaces parent relation and iproves children cost if new parent is better than old.
    """
        for child in children:
            tile_cost = map[child.pos[0]][child.pos[1]]
            open_node = False
            for closed_child in closed_list:
                if child == closed_child:
                    continue
            for i in range(len(open_list)):
                if open_list[i] == child:
                    child = open_list[i]
                    open_node = True
            current_node.children.append(child)
            if not open_node:
                create_parent_relation(
                    child, current_node, end, tile_cost)
                open_list.append(child)
                open_list.sort()
            elif current_node.g + tile_cost < child.g:
                create_parent_relation(
                    child, current_node, end, tile_cost)
                if child in closed_list:
                    improve_children_cost(child)

    return False


def create_parent_relation(child, parent, end, tile_cost):
    """Creates parent relation and updates child g and h cost"""
    child.lowest_cost_parent = parent
    child.g = parent.g + tile_cost
    child.h = abs(child.pos[0] - end[0]) + abs(child.pos[1] - end[1])


def improve_children_cost(node):
    """Improves a nodes children cost if new path from given node is better"""
    for child in node.children:
        if child.g > node.g + 1:
            child.lowest_cost_parent = node
            child.g = node.g + 1
            improve_children_cost(child)


def add_path_to_map(map, path):
    """Adds path to map"""
    for n in path:
        map.set_cell_value(n, " p ")


def main():
    """
    Runs until user stops.
    User choses which task to show.
    Prints both map with and without path.
    """
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
        if (not path):
            print('no path')
            break
        else:
            add_path_to_map(map, path)
            int_map, str_map = map.get_maps()
            map.show_map()
        if ('q' == input("'q' to quit: ")):
            break


main()
