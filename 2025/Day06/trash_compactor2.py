lines = []
with open("input.txt", "r") as file:
    for row in file:
        lines.append(row.strip("\n"))


def fix_and_calc(operator, i):
    if operator == "+":
        temp_score = 0
    elif operator == "*":
        temp_score = 1
    else:
        return 0
    for x in range(len(lines[0]) - i):
        val = ""
        for c in lines[:-1]:
            if c[i + x] != " ":
                val += c[i + x]
        if val:
            if operator == "+":
                temp_score += int(val)
            elif operator == "*":
                temp_score *= int(val)
        else:
            return temp_score
    return 0


score = sum(fix_and_calc(operator, i) for i, operator in enumerate(lines[-1]))
print(score)
