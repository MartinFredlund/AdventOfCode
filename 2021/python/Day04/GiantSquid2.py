BOARD_SIZE = 5

def check_win(board,x,y):

    # Check rows and columns for a win
    amountX = 0
    amountY = 0
    for i in range(BOARD_SIZE):
        if board[x][i] == "x":
            amountX += 1
        if board[i][y] == "x":
            amountY += 1
    return (amountX == BOARD_SIZE or amountY == BOARD_SIZE)


def board_score(board, last_number):
    boardSum = 0
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            if board[x][y] != "x":
                boardSum += int(board[x][y])
    return boardSum * int(last_number)

def parse_boards(file):
    boards = []
    while True:
        line = file.readline()
        if not line:
            break
        if line.strip() == "":
            board = []
            for _ in range(BOARD_SIZE):
                row = file.readline().strip().split()
                board.append(row)
            boards.append(board)
    return boards

def play_bingo(draw_numbers, boards):
    for n in draw_numbers:
        for board in boards[:]:
            for x in range(BOARD_SIZE):
                for y in range(BOARD_SIZE):
                    if board[x][y] == n:
                        board[x][y] = "x"
                        if check_win(board,x,y):
                            if(len(boards) > 1):
                                boards.remove(board)
                            else:
                                print(board_score(board, n))
                                return

def main():
    with open('input.txt', 'r') as file:
        draw_numbers = file.readline().strip().split(",")
        boards = parse_boards(file)
    play_bingo(draw_numbers, boards)

if __name__ == "__main__":
    main()