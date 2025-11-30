from uu import Error
import regex as re
from word2number import w2n

file = open("input.txt", "r")
amount = 0

for line in file:
    line = line.rstrip()
    first = re.search(
        "three|one|two|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9", line
    ).group()

    revers = line[::-1]
    last = re.search(
        "eerht|eno|owt|ruof|evif|xis|neves|thgie|enin|1|2|3|4|5|6|7|8|9", revers
    ).group()
    try:
        first = w2n.word_to_num(first)
    except Error:
        print(first)
    last = last[::-1]
    try:
        last = w2n.word_to_num(last)
    except Error:
        print(last)
    first = first * 10 + last
    amount += int(first)

print(amount)
