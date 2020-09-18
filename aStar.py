import Map
from Node import Node

"""Based on A* pseudo-code from Medium'"""


def a_star_search(map, start, end):
    start_node = Node(None, start)
    start_node.h = abs(start_node.pos[0] - end[0]) + \
        abs(start_node.pos[1] - end[1])
    open_nodes = []
    closed_nodes = []
    open_nodes.append(start_node)
    end_node = Node(None, end)

    while open_nodes:
        current_node = open_nodes.pop(0)
        closed_nodes.append(current_node)
        children = []

        if current_node == end_node:
            path = []
            while (current_node):
                path.append(current_node.pos)
                current_node = current_node.lowest_cost_parent
            return path[::-1]

        for direction_to_connected_node in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            node_pos = (
                current_node.pos[0] + direction_to_connected_node[0], current_node.pos[1] + direction_to_connected_node[1])
            if map[node_pos[0]][node_pos[1]] != -1:
                new_node = Node(current_node, node_pos)
                children.append(new_node)

        for child in children:
            tile_cost = map[child.pos[0]][child.pos[1]]
            for i in range(len(open_nodes)):
                if open_nodes[i] == child:
                    child = open_nodes[i]
            for i in range(len(closed_nodes)):
                if closed_nodes[i] == child:
                    child = closed_nodes[i]
            current_node.children.append(child)
            if child not in closed_nodes and child not in open_nodes:
                create_parent_relation(
                    child, current_node, end, tile_cost)
                open_nodes.append(child)
                open_nodes.sort()
            elif current_node.g + tile_cost < child.g:
                create_parent_relation(
                    child, current_node, end, tile_cost)
                if child in closed_nodes:
                    propagate_path_improvements(child)
    return False


def create_parent_relation(child, parent, end, tile_cost):
    child.lowest_cost_parent = parent
    child.g = parent.g + tile_cost
    child.h = abs(child.pos[0] - end[0]) + abs(child.pos[1] - end[1])


def propagate_path_improvements(node):
    for child in node.children:
        if child.g > node.g + 1:
            child.lowest_cost_parent = node
            child.g = node.g + 1
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
