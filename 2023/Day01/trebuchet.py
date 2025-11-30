import regex as re

file = open("input.txt", "r")
amount = 0

for line in file:
    line = line.rstrip()
    first = re.search("[0-9]", line).group()
    revers = line[::-1]
    last = re.search("[0-9]", revers).group()
    first = first + last
    amount += int(first)

print(amount)
