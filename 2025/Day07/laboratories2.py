tachyon_dict = dict()
with open("input.txt", "r") as file:
    tachyon_dict[file.readline().strip().find("S")] = 1
    for line in file:
        next_int = line.find("^")
        while next_int != -1:
            if next_int in tachyon_dict:
                tachyon_dict[next_int + 1] = (
                    tachyon_dict.get(next_int + 1, 0) + tachyon_dict[next_int]
                )
                tachyon_dict[next_int - 1] = (
                    tachyon_dict.get(next_int - 1, 0) + tachyon_dict[next_int]
                )

                del tachyon_dict[next_int]

            next_int = line.find("^", next_int + 1)
print(sum(tachyon_dict.values()))
