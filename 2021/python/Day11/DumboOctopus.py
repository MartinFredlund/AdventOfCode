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
RUN = 100
board = []
flash = 0

for row in file:
    board.append(list((row.strip("\n"))))
for i in range(0, RUN):
    newFlash = False
    for row in board:
        for i in range(0, len(row)):
            row[i] = int(row[i]) + 1
            if row[i] > 9:
                newFlash = True
    if newFlash:
        for x in range(0, 10):
            for y in range(0, 10):
                if board[x][y] != "x" and int(board[x][y]) > 9:
                    increaseAdj(x, y)
    for row in board:
        for i in range(0, 10):
            if row[i] == "x":
                row[i] = 0
                flash += 1

print(flash)
