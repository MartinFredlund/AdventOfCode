def increaseAdj(x, y):
    board[x][y] = "x"
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if i >= 0 and i < 10 and j >= 0 and j < 10:
                if board[i][j] != "x":
                    board[i][j] = str(int(board[i][j]) + 1)
                    if board[i][j] != "x" and int(board[i][j]) > 9:
                        increaseAdj(i, j)


file = open("input.txt")
board = []
step = 0
for row in file:
    board.append(list((row.strip("\n"))))
while True:
    flash = 0
    newFlash = False
    for row in board:
        for x in range(0, len(row)):
            row[x] = int(row[x]) + 1
            if row[x] > 9:
                newFlash = True
    if newFlash:
        for x in range(0, 10):
            for y in range(0, 10):
                if board[x][y] != "x" and int(board[x][y]) > 9:
                    increaseAdj(x, y)
    for row in board:
        for z in range(0, 10):
            if row[z] == "x":
                row[z] = 0
                flash += 1
    step += 1
    if flash == 100:
        print(step)
        break
