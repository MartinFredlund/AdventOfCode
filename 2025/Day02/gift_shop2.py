def find_period(s):
    i = (s + s).find(s, 1, -1)
    return 0 if i == -1 else 1


file = open("input.txt", "r")
score = 0
ranges = file.readline().split(",")
for r in ranges:
    s, e = map(int, r.split("-"))
    for val in range(s, e + 1):
        if find_period(str(val)):
            score += val

print(score)
