import regex as re

file = open("input.txt", "r")
il = {
    "first": "",
    "second": "",
    "third": "",
}
il["second"] = "." + next(file).rstrip() + "."
il["first"] = "." * len(il["second"])
sum = 0
start_index = 0


def gear_ratio(n):
    global start_index
    global sum
    numbers = []
    index = il["second"].index(n, start_index)
    start_index = index + 1
    for i in range(index - 1, index + 2):
        if il["first"][i].isnumeric():
            nmb = il["first"][i]
            for x in range(i - 1, i - 3, -1):
                if il["first"][x].isnumeric():
                    nmb = il["first"][x] + nmb
                else:
                    break
            for x in range(i + 1, i + 3):
                if il["first"][x].isnumeric():
                    nmb = nmb + il["first"][x]
                else:
                    break
            numbers.append(nmb)

        if il["third"][i].isnumeric():
            nmb = il["third"][i]
            for x in range(i - 1, i - 3, -1):
                if il["third"][x].isnumeric():
                    nmb = il["third"][x] + nmb
                else:
                    break
            for x in range(i + 1, i + 3):
                if il["third"][x].isnumeric():
                    nmb = nmb + il["third"][x]
                else:
                    break
            numbers.append(nmb)

    if il["second"][index - 1].isnumeric():
        nmb = il["second"][index - 1]
        for x in range(index - 2, index - 5, -1):
            if il["second"][x].isnumeric():
                nmb = il["second"][x] + nmb
            else:
                break
        numbers.append(nmb)
    if il["second"][index + 1].isnumeric():
        nmb = il["second"][index + 1]
        for x in range(index + 2, index + 5):
            if il["second"][x].isnumeric():
                nmb = nmb + il["second"][x]
            else:
                break
        numbers.append(nmb)
    numbers = list(dict.fromkeys(numbers))
    if len(numbers) == 2:
        sum = sum + int(numbers[0]) * int(numbers[1])


for line in file:
    start_index = 0
    il["third"] = "." + line.rstrip() + "."
    gears = re.findall("\*", il["second"])
    for n in gears:
        gear_ratio(n)
    il["first"] = il["second"]
    il["second"] = il["third"]

start_index = 0
il["third"] = "." * len(il["second"])
numbers = re.findall(r"\*", il["second"])
for n in numbers:
    gear_ratio(n)
print(sum)
