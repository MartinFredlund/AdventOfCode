file = open("input.txt")
result = 0
for line in file:
    row = line
    syntax = []
    for char in row:
        if char in {"(", "<", "{", "["}:
            syntax += char
        elif char == ")":
            if syntax[-1] == "(":
                syntax.pop()
            else:
                result += 3
                break
        elif char == ">":
            if syntax[-1] == "<":
                syntax.pop()
            else:
                result += 25137
                break
        elif char == "]":
            if syntax[-1] == "[":
                syntax.pop()
            else:
                result += 57
                break
        elif char == "}":
            if syntax[-1] == "{":
                syntax.pop()
            else:
                result += 1197
                break
print(result)
