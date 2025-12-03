file = open("input.txt", "r")
score = 0
for battery in file:
    battery = battery.strip()
    f = 0
    s = 0
    for i in range(0, len(battery)):
        val = int(battery[i])
        if val > f and i != len(battery)-1:
            f = val
            s = 0
        elif val > s:
            s = val
    f *= 10
    f += s
    score += f
print(score)