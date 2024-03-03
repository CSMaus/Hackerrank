def calculate_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


def find_closest_cell_and_distance(current_pos, dirty_cells):
    closest_cell = None
    min_distance = float('inf')
    for d in dirty_cells:
        distance = calculate_distance(current_pos, d)
        if distance < min_distance:
            min_distance = distance
            closest_cell = d
    return closest_cell, min_distance


def find_shortest_path(start_pos, dirty_cells):
    path = [start_pos]
    total_distance = 0
    current_pos = start_pos
    cells_to_visit = dirty_cells.copy()

    while cells_to_visit:
        closest_cell, distance = find_closest_cell_and_distance(current_pos, cells_to_visit)
        if closest_cell:
            path.append(closest_cell)
            total_distance += distance
            cells_to_visit.remove(closest_cell)
            current_pos = closest_cell

    return path[1:], total_distance


def next_move(posr, posc, board):
    if board[posr][posc] == 'd':
        print("CLEAN")
    else:
        start_pos = (posr, posc)
        dirty_cells = [(i, j) for i in range(len(board)) for j in range(len(board[i])) if board[i][j] == 'd']

        shortest_path, _ = find_shortest_path(start_pos, dirty_cells)

        if not shortest_path:
            return

        while (shortest_path[0] == start_pos):
            shortest_path.pop(0)
        print(shortest_path)

        """d0 = shortest_path[0][0]
        d1 = shortest_path[0][1]
        if (d0 - posr) > 0:
            print("DOWN")
        elif (d0 - posr) < 0:
            print("UP")
        elif (d1 - posc) > 0:
            print("RIGHT")
        elif (d1 - posc) < 0:
            print("LEFT")"""

if __name__ == "__main__":
    posr, posc = [int(i) for i in input().strip().split()]
    board = [input().strip() for _ in range(5)]

    next_move(posr, posc, board)
