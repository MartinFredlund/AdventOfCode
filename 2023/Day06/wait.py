file = open("input.txt", "r")
time = next(file).split()[1:]
dist = next(file).split()[1:]
res = 1

for i in range(len(time)):
    poss = 0
    for t in range(int(time[i])):
        if t * (int(time[i]) - t) > int(dist[i]):
            poss += 1
    res = res * poss
print(res)
