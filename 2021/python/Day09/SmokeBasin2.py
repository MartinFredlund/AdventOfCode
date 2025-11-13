def checkIfAdded(x, y, area, temp):
    if not [x, y] in area:
        area.append([x, y])
        temp.append([x, y])


def lowArea(board, x, y):
    area = []
    temp = []
    area.append([x, y])
    newFound = [[x, y]]

    while len(newFound) != 0:
        temp.clear()
        for new in newFound:
            x = new[0]
            y = new[1]
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < ROWS and 0 <= ny < COLS:
                    if board[x][y] < board[nx][ny] and board[nx][ny] != 9:
                        checkIfAdded(nx, ny, area, temp)
        newFound.clear()
        newFound += temp
    return len(area)


def checkLow(board):

    areaSize = []
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
                areaSize.append(lowArea(board, x, y))

    return areaSize


def calcScore(board):
    result = 1
    sizeList = sorted(checkLow(board), reverse=True)[:3]
    for value in sizeList:
        result *= value

    return result


file = open("input.txt", "r")
board = []
for line in file:
    row = [int(char) for char in line.strip()]
    board.append(row)
ROWS = len(board)
COLS = len(board[0])
print(calcScore(board))
