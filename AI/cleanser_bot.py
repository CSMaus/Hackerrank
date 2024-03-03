def next_move(posr, posc, board):
    board = [list(row) for row in board]

    if board[posr][posc] == 'd':
        print("CLEAN")
    else:
        dirty_cells = [(i, j) for i in range(len(board)) for j in range(len(board[i])) if board[i][j] == 'd']

        d0 = 0
        d1 = 0
        val = float('inf')
        for d in dirty_cells:
            if val > abs(posr - d[0]) + abs(posc - d[1]):
                val = abs(posr - d[0]) + abs(posc - d[1])
                d0 = d[0]
                d1 = d[1]

        if (d0 - posr) > 0:
            print("DOWN")
        elif (d0 - posr) < 0:
            print("UP")
        elif (d1 - posc) > 0:
            print("RIGHT")
        elif (d1 - posc) < 0:
            print("LEFT")


if __name__ == "__main__":
    posr, posc = [int(i) for i in input().strip().split()]
    board = [input().strip() for _ in range(5)]

    next_move(posr, posc, board)
