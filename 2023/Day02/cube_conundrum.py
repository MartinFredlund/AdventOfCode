file = open("input.txt", "r")
sum = 0
for line in file:
    possible = True
    game = line.split(":")
    id = int(game[0].split()[1])
    game_round = game[1].split(";")
    for r in game_round:
        hand = r.split(",")
        for amount in hand:
            col = amount.split()
            if col[1] == "red" and int(col[0]) > 12:
                possible = False
                break
            if col[1] == "green" and int(col[0]) > 13:
                possible = False
                break
            if col[1] == "blue" and int(col[0]) > 14:
                possible = False
                break
    if possible:
        sum += id
print(sum)
