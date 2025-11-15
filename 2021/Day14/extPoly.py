def extender(times, charList, translator):
    newInput = charList[0]
    for x in range(1, len(charList)):
        searchWord = charList[x - 1] + charList[x]
        newInput += translator.get(searchWord)
        newInput += charList[x]
    times -= 1
    if times != 0:
        extender(times, newInput, translator)
    return newInput


file = open("input.txt", "r")
input = file.readline().strip("\n")
extend = dict()
for line in file:
    next = line.strip("\n").split(" -> ")
    if len(next) == 2:
        extend[next[0]] = next[1]

result = extender(10, input, extend)
values = list(set(extend.values()))
maxL = 0
minL = max(int)
for val in values:
    count = input.count(val)
    if count > maxL:
        maxL = count
    elif count < minL:
        minL = count
print(maxL - minL)
