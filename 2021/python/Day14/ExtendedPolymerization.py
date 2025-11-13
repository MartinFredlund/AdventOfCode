def extender(charList, translator):
    newInput = charList[0]
    for x in range(1, len(charList)):
        searchWord = charList[x - 1] + charList[x]
        newInput += translator.get(searchWord)
        newInput += charList[x]
    return newInput


# Input
file = open("input.txt", "r")
result = file.readline().strip("\n")
extend = dict()
for line in file:
    next = line.strip("\n").split(" -> ")
    if len(next) == 2:
        extend[next[0]] = next[1]

# Run extender
loops = 10
for x in range(loops):
    result = extender(result, extend)

# Calc score
values = list(set(extend.values()))
maxL = 0
minL = 10000
for val in values:
    count = result.count(val)
    if count > maxL:
        maxL = count
    elif count < minL:
        minL = count
print(maxL - minL)
