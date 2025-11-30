file = open("input.txt", "r")
time = "".join(next(file).split()[1:])
dist = "".join(next(file).split()[1:])
startTime = 0
for t in range(int(time)):
    if t * (int(time) - t) > int(dist):
        startTime = t
        break
print(int(time) - 2 * startTime)
