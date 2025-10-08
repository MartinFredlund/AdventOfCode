file = open('input.txt', 'r')
horizson = 0
depth = 0
for line in file:
    nextLine = line.split()
    if(nextLine[0] == "forward"):
        horizson += int(nextLine[1])
    elif(nextLine[0] == "down"):
        depth += int(nextLine[1])
    else:
        depth -= int(nextLine[1])
print(horizson*depth)
