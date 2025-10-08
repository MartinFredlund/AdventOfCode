file = open('input.txt', 'r')
input = [0,0,0,0,0,0,0,0,0,0,0,0]
for line in file:
    for x in range(12):
        if(line[x] == "1"):
            input[x] += 1
        else:
            input[x] -= 1
binaryPos = 1
gamma = 0
epsilon = 0

for x in reversed(input):
    if(x >= 0):
        gamma += binaryPos
    else:
        epsilon += binaryPos
    binaryPos *= 2
print(gamma * epsilon)