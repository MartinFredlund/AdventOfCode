file = open("input.txt", "r")
sum = 0
for line in file:
    game = line.split(":")
    id = int(game[0].split()[1])
    game_round = game[1].split(";")
    red = 0
    blue = 0
    green = 0
    for r in game_round:
        hand = r.split(",")
        for amount in hand:
            col = amount.split()
            if col[1] == "red" and int(col[0]) > red:
                red = int(col[0])
            if col[1] == "green" and int(col[0]) > green:
                green = int(col[0])
            if col[1] == "blue" and int(col[0]) > blue:
                blue = int(col[0])
    sum += red * blue * green
print(sum)
