def extendPair40(pair, itr):
    global TIMES
    global result
    global dataBase
    #print(pair)
    input = pair[0]
    input += pair[1]
    if(pair in dataBase):
        print("test")
        input = dataBase[pair]
        for i in range(1, len(input)-1):
            result[input[i]] += 1
    else:
        for i in range(0,20):
            newInput = input[0]
            for x in range(1, len(input)):
                searchWord = extend.get(input[x-1] + input[x])
                newInput += searchWord
                result[searchWord] += 1
                newInput += input[x]
            input = newInput
            dataBase[pair] = input
    if(itr + 20 != TIMES):
        print(input)
        for z in range(1, len(input)):            
            print(input[z-1] + input[z], itr+20)
            extendPair40(input[z-1]+input[z], itr+20)        
    

file = open("input.txt", "r")
input = ""
input =  file.readline().strip("\n")
TIMES = 40
extend = dict()
result = dict()
dataBase = dict()
for line in file:
    next = line.strip("\n").split(" -> ")
    if(len(next) == 2):
        extend[next[0]] = next[1]
values = list(set(extend.values()))

for val in values:
    result[val] = 0
for i in input:
    result[i] += 1


for x in range(1, len(input)):
    extendPair40(input[x-1] + input[x], 0)        
print(result)
amount = max(result.values()) - min(result.values())
print(amount)