file = open("input.txt", "r")
score = 0
ranges = file.readline().split(",")
for r in ranges:
    s, e = map(int, r.split("-"))
    for val in range(s, e + 1):
        val_list = list(str(val))
        if (
            len(val_list) % 2 == 0
            and val_list[: len(val_list) // 2] == val_list[len(val_list) // 2 :]
        ):
            score += val
print(score)
