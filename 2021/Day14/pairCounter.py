file = open("input.txt", "r")
input = ""
input =  file.readline().strip("\n")
extend = dict()
for line in file:
    next = line.strip("\n").split(" -> ")
    if(len(next) == 2):
        extend[next[0]] = next[1]

allPairs = dict()
newPairs = dict()
for pair in extend.keys():
    allPairs[pair] = 0
for i in range(1, len(input)):
    allPairs[input[i-1] + input[i]] += 1
for x in range(40):
    for pair in extend.keys():
        newPairs[pair] = 0
    for key in allPairs.keys():
        pair1 = key[0] + extend.get(key)
        pair2 = extend.get(key) + key[1]
        newPairs[pair1] += allPairs[key]
        newPairs[pair2] += allPairs[key]
    allPairs = newPairs.copy()
print(allPairs)
values = list(set(extend.values()))
result = dict()
for val in values:
    result[val] = 0
result[input[0]] += 1
result[input[-1]] += 1
for key in allPairs.keys():
    result[key[0]] += allPairs[key]
    result[key[1]] += allPairs[key]
print(result)
print(result)
amount = max(result.values())/2 - min(result.values())/2
print(int(amount))