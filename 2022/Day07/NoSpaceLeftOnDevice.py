file = open('input.txt', 'r')  
dir = {}
dirArray = []
index = 0
for line in file:
    line = line.split()
    if(line[1] == "cd"):
        if(line[2] == ".."):
            dirArray.pop()
        else:
            if not (line[2] in dir):
                dirArray.append(line[2])
                dir[line[2]] = 0
            else:
                dirArray.append(line[2]+str(index))
                dir[line[2]+str(index)] = 0
                index += 1
    elif(line[0].isnumeric()):
        for i in dirArray:
            dir[i] = (int(dir.get(i)) + int(line[0]))
x = 0
for i in dir.keys():
    print(i, x, dir.get(i), int(dir.get(i)) <= 100000)
    if(int(dir.get(i)) <= 100000):
        x += int(dir.get(i))
        print()
print(x)