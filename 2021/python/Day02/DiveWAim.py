file = open('input.txt', 'r')
horizson = 0
depth = 0
aim = 0
for line in file:
    nextLine = line.split()
    if(nextLine[0] == "forward"):
        horizson += int(nextLine[1])
        depth += int(nextLine[1]) * aim
    elif(nextLine[0] == "down"):
        aim += int(nextLine[1])
    elif(nextLine[0] == "up"):
        aim -= int(nextLine[1])
print(horizson*depth)