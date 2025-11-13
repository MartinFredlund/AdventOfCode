def checkLow(board):
    lowBoard = [[0] * COLS for _ in range(ROWS)]
    for x in range(ROWS):
        for y in range(COLS):
            currentVal = board[x][y]
            is_low = True

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < ROWS and 0 <= ny < COLS:
                    if currentVal >= board[nx][ny]:
                        is_low = False
                        break
            if is_low:
                lowBoard[x][y] = 1

    return lowBoard


def calcScore(board):
    result = 0
    horLow = checkLow(board)
    for x in range(len(board)):
        for y in range(len(board[0])):
            if horLow[x][y] == 1:
                result += board[x][y] + 1
    return result


file = open("input.txt", "r")
board = []
for line in file:
    row = [int(char) for char in line.strip()]
    board.append(row)
ROWS = len(board)
COLS = len(board[0])
print(calcScore(board))
