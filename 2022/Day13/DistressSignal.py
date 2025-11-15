file = open("input.txt", "r")
def f(x, y):
    if type(x) == int:
        if type(y) == int:
            return y - x
        else:
            return f([x], y)
    else:
        if type(y) == int:
            return f(x, [y])
    
    for a, b in zip(x, y):
        v = f(a, b)
        if v:
            return v
    
    return len(y) - len(x)

t = 0
index = 0
lines = []
for line in file:
    lines.append(line.rstrip())
    if len(lines) == 3:
        left = lines[0]
        right = lines[1]
        lines = []
    if len(lines) == 0:
        index += 1
        if f(eval(left), eval(right)) > 0:
            t += index
print(t)