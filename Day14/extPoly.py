file = open("input.txt", "r")
input = ""
input =  file.readline().strip("\n")
extend = dict()
print(input)
for line in file:
    next = line.strip("\n").split(" -> ")
    if(len(next) == 2):
        extend[next[0]] = next[1]
print(extend)
loops = 10
for i in range(0,loops):
    newInput = input[0]
    for x in range(1, len(input)):
        searchWord = input[x-1] + input[x]
        newInput += extend.get(searchWord)
        newInput += input[x]
        #print(input[x])
    input = newInput
values = list(set(extend.values()))
maxL = 0
minL = 10000
for val in values:
    count = input.count(val)
    print(val, count)
    if(count > maxL):
        maxL = count
    elif(count < minL):
        minL = count
print(maxL - minL)
print(len(input))