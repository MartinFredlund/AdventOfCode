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


def part_number(n):
    global sum
    global start_index
    nLen = len(n)
    index = il["second"].index(n, start_index)
    start_index = index + nLen
    for i in range(index - 1, index + nLen + 1):
        if (not il["first"][i].isnumeric() and il["first"][i] != ".") or (
            not il["third"][i].isnumeric() and il["third"][i] != "."
        ):
            sum += int(n)
            return
    if il["second"][index - 1] != "." or il["second"][index + nLen] != ".":
        sum += int(n)

        return


for line in file:
    start_index = 0
    il["third"] = "." + line.rstrip() + "."
    numbers = re.findall(r"\d+", il["second"])
    for n in numbers:
        part_number(n)
    il["first"] = il["second"]
    il["second"] = il["third"]


start_index = 0
il["third"] = "." * len(il["second"])
numbers = re.findall(r"\d+", il["second"])
for n in numbers:
    part_number(n)
print(sum)
