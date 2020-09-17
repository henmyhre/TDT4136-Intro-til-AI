import Map as map


def main():

    task_number = -1
    while not (5 > task_number > 0):
        task_number = int(input("Task number: "))

    board = map.Map_Obj(task_number)
    map1, map2 = board.get_maps()
    board.show_map()

    start_pos = (board.get_start_pos()[0], board.get_start_pos()[1])
    end_pos = (board.get_goal_pos()[0], board.get_goal_pos()[1])
    print("Start:", start_pos, " Goal:", end_pos)


main()
