def check(board, x, y, n):
    amountX = 0
    amountY = 0
    boardSum = 0
    for i in range(5):
        if board[x][i] == "x":
            amountX += 1
        if board[i][y] == "x":
            amountY += 1

    if amountX == 5 or amountY == 5:
        for x in range(5):
            for y in range(5):
                if board[x][y] != "x":
                    boardSum += int(board[x][y])
        print(boardSum * int(n))
        exit()


boards = []
file = open("input.txt", "r")
drawNumber = file.readline().strip().split(",")
while True:
    line = file.readline()
    if not line:
        break
    if line.strip() == "":
        new_board = []
        for _ in range(5):
            row = file.readline().strip()

            row_values = row.split()
            new_board.append(row_values)
        boards.append(new_board)
for n in drawNumber:
    for b in boards:
        for x in range(5):
            for y in range(5):
                if b[x][y] == n:
                    b[x][y] = "x"
                    check(b, x, y, n)
