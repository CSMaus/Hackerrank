# here while gives errors sometimes
def calculate_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


def find_closest_cell(current_pos, dirty_cells):
    closest_cell = None
    min_distance = float('inf')
    for d in dirty_cells:
        distance = calculate_distance(current_pos, d)
        if distance < min_distance:
            min_distance = distance
            closest_cell = d
    return closest_cell


def find_shortest_path_recursive(current_pos, dirty_cells, path=[]):
    if not dirty_cells:
        return path
    closest_cell = find_closest_cell(current_pos, dirty_cells)
    if closest_cell:
        new_dirty_cells = dirty_cells.copy()
        new_dirty_cells.remove(closest_cell)
        path.append(closest_cell)
        return find_shortest_path_recursive(closest_cell, new_dirty_cells, path)
    else:
        return path


def generate_paths(points, current_path, all_paths):
    if not points:
        all_paths.append(current_path)
        return
    for i in range(len(points)):
        next_point = points[i]
        remaining_points = points[:i] + points[i+1:]
        generate_paths(remaining_points, current_path + [next_point], all_paths)


def find_shortest_path(start_pos, dirty_cells):
    all_points = dirty_cells + [start_pos]
    all_paths = []
    generate_paths(all_points, [start_pos], all_paths)

    min_distance = float('inf')
    shortest_path = None
    for path in all_paths:
        path_distance = sum(calculate_distance(path[i], path[i+1]) for i in range(len(path)-1))
        if path_distance < min_distance:
            min_distance = path_distance
            shortest_path = path

    return shortest_path


def next_move(posr, posc, board):
    if board[posr][posc] == 'd':
        print("CLEAN")
    else:
        start_pos = (posr, posc)
        dirty_cells = [(i, j) for i in range(len(board)) for j in range(len(board[i])) if board[i][j] == 'd']
        if start_pos not in dirty_cells:
            dirty_cells.append(start_pos)

        shortest_path = find_shortest_path(start_pos, dirty_cells)
        # print("was:")
        # print("[(1, 0), (1, 1), (2, 2), (2, 3), (1, 4), (0, 4), (4, 4), (3, 2)]")

        while (shortest_path[0] == start_pos):
            shortest_path.pop(0)
        print(shortest_path)
        """"d0 = shortest_path[0][0]
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
