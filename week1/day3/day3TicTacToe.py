SIZE = 3
empty = " "
board = []

for y in range(SIZE):
    board.append([])
    for x in range(SIZE):
        board[y].append("[%s]" % (empty))

for row in board:
    for column in row:
        print("%s  " % column, end="")
    print("\n")

