def checkIfAdded(x,y):
    if(not [str(x), str(y)] in area):
        area.append([str(x), str(y)])
        temp.append([str(x), str(y)])
        
        
def lowArea(i, x):
    area.clear()
    area.append([str(i), str(x)])
    newFound = [[str(i), str(x)]]
    while(len(newFound) != 0):
        temp.clear()
        for new in newFound:
            new0 = int(new[0])
            new1 = int(new[1])
            if((heatMap[new0][new1] < heatMap[new0-1][new1]) and heatMap[new0-1][new1] != "9"):
                checkIfAdded(new0-1, new1)
            if((heatMap[new0][new1] < heatMap[new0+1][new1]) and heatMap[new0+1][new1] != "9"):
                checkIfAdded(new0+1, new1)
            if((heatMap[new0][new1] < heatMap[new0][new1-1]) and heatMap[new0][new1-1] != "9"):
                checkIfAdded(new0, new1-1)
            if((heatMap[new0][new1] < heatMap[new0][new1+1]) and heatMap[new0][new1+1] != "9"):
                checkIfAdded(new0, new1+1)
        newFound.clear()
        newFound += temp
    return len(area)


file = open("input.txt")
heatMap = []
result = []
area = []
temp = []
newFound = []
for line in file:
    heatMap.append(list("9"+line.strip("\n") + "9"))
heatMap.insert(0, list("9" * len(heatMap[1])))
heatMap.insert(len(heatMap), list("9" * len(heatMap[1])))
for i in range(1, len(heatMap)-1):
    for x in range(1, len(heatMap[1])-1):
        if(heatMap[i][x] < heatMap[i-1][x] and heatMap[i][x] < heatMap[i+1][x] and heatMap[i][x] < heatMap[i][x-1] and heatMap[i][x] < heatMap[i][x+1]):
            amount = lowArea(i, x)
            if(len(result) < 3):
                result.append(amount)
            else:
                result = sorted(result)
                if (result[0] < amount):
                    result[0] = amount
val = 1
for i in result:
    val *= i
print(val)