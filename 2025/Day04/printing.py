roll_map = []
with open("input.txt","r") as file:
    for row in file:
        roll_map.append("." + row.strip() + ".")
extra_lines = "." * len(roll_map[0])
roll_map.insert(0, extra_lines)
roll_map.append(extra_lines)

score = 0
for x in range(1, len(roll_map)):
    for y in range(1, len(roll_map[0])):
        if roll_map[x][y] == "@":
            amount = 0
            for nx in range(-1,2):
                for ny in range(-1,2):
                    if roll_map[x+nx][y+ny] == "@":
                        amount += 1
            if amount < 5:
                score += 1
print(score)