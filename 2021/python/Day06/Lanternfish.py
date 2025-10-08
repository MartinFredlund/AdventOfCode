def runSim(runs, fishes):
    for _ in range(runs):
        updatedFishes = [0]*9
        for i, amount in enumerate(fishes):
            if (i == 0):
                updatedFishes[6] += amount
                updatedFishes[8] += amount
            else:
                updatedFishes[i - 1] += amount
        fishes = updatedFishes
    return fishes

file = open("input.txt", "r")
fishes = [0]*9
for fish in file.readline().split(","):
    fishes[int(fish)] += 1
fishes = runSim(80, fishes)
print(sum(fishes))