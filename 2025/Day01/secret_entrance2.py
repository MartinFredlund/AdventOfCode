file = open("input.txt")

current_value = 50
score = 0

for row in file:
    if row[0] == "L":
        step = int(row[1:]) * -1
    else:
        step = int(row[1:])
    prev = current_value
    div, current_value = divmod(current_value + step, 100)

    # Count boundary crossings
    crossings = abs(div)
    # Don't count if we start at 0 and move left (negative div)
    if prev == 0 and div < 0:
        crossings -= 1
    # Add 1 if we land on 0 while moving left
    if current_value == 0 and step < 0:
        crossings += 1

    score += crossings

print(score)
