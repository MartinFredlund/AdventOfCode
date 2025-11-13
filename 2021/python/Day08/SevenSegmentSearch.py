file = open("input.txt", "r")
ONE = 2
FOUR = 4
SEVEN = 3
EIGHT = 7
result = 0
for l in file:
    seg = l.split("|")
    digits = seg[1].split()
    for dig in digits:
        if len(dig) in (ONE, FOUR, SEVEN, EIGHT):
            result += 1
print(result)
