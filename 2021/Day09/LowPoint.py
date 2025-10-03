file = open("input.txt")
heatMap = []
amount = 0
for line in file:
    heatMap.append(list("9"+line.strip("\n") + "9"))
heatMap.insert(0, list("9" * len(heatMap[1])))
heatMap.insert(len(heatMap), list("9" * len(heatMap[1])))
for i in range(1, len(heatMap)-1):
    for x in range(1, len(heatMap[1])-1):
        if(heatMap[i][x] < heatMap[i-1][x] and heatMap[i][x] < heatMap[i+1][x] and heatMap[i][x] < heatMap[i][x-1] and heatMap[i][x] < heatMap[i][x+1]):
            amount += int(heatMap[i][x])+1
print(amount)