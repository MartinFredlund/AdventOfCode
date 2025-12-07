tachyon_set = set()
score = 0
with open("input.txt", "r") as file:
    tachyon_set.add(file.readline().strip().find("S"))
    for line in file:
        next_int = line.find("^")
        while next_int != -1:
            if next_int in tachyon_set:
                tachyon_set.remove(next_int)
                tachyon_set.add(next_int + 1)
                tachyon_set.add(next_int - 1)
                score += 1
            next_int = line.find("^", next_int + 1)
print(score)
