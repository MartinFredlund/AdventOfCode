file = open("input.txt")
result = []
for line in file:
    row = line
    syntax = []
    corrupt = False
    for char in row:
        if char in {"(", "<", "{", "["}:
            syntax += char
        elif char == ")":
            if syntax[-1] == "(":
                syntax.pop()
            else:
                currupt = True
                break
        elif char == ">":
            if syntax[-1] == "<":
                syntax.pop()
            else:
                corrupt = True
                break
        elif char == "]":
            if syntax[-1] == "[":
                syntax.pop()
            else:
                corrupt = True
                break
        elif char == "}":
            if syntax[-1] == "{":
                syntax.pop()
            else:
                corrupt = True
                break
    if not corrupt:
        amount = 0
        for char in reversed(syntax):
            amount *= 5
            if char == "(":
                amount += 1
            elif char == "[":
                amount += 2
            elif char == "{":
                amount += 3
            elif char == "<":
                amount += 4
        result.append(amount)
result = sorted(result)
middle = int((len(result) - 1) / 2)
print(result[middle])
