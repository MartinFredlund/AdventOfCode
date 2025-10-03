def value(input, mostCommon):
    pos = 1
    listOne.clear()
    listZero.clear()
    while(len(input) != 1):
        for line in input:
            if(line[pos] == "1"):
                listOne.append(line)
            else:
                listZero.append(line)
        input.clear()
        if(mostCommon):
            if(len(listOne) >= len(listZero)):
                input.extend(listOne)
            else:
                input.extend(listZero)
        else:
            if(len(listOne) < len(listZero)):
                input.extend(listOne)
            else:
                input.extend(listZero)
        listOne.clear()
        listZero.clear()
        pos += 1
    return int(input[0], 2)
        
file = open('input.txt', 'r')
listOne = []
listZero = []
for line in file:
    if(line[0] == "1"):
        listOne.append(line)
    else:
        listZero.append(line)
oxygen = []
co2 = []
if(len(listOne) > len(listZero)):
    oxygen.extend(listOne)
    co2.extend(listZero)
else:
    oxygen.extend(listZero)
    co2.extend(listOne)
print(value(oxygen, True) * value(co2, False))