def increaseAdj(x,y):
    input[x][y] = "x"
    for i in range(x-1, x+2):
        for z in range(y-1, y+2):
            if(i >= 0 and i < 10 and z >= 0 and z < 10):
                if(input[i][z] != "x"):
                    input[i][z] = str( int(input[i][z]) + 1)
                    if(input[i][z] != "x" and int(input[i][z]) > 9):
                        increaseAdj(i,z)
                        
file = open("input.txt")
RUN = 100
input = []
flash = 0
newFlash = False
for row in file:
    input.append(list(row.strip("\n")))
for i in range(0, RUN):
    print("--------------------", i, "-----------------------------")
    for i in input:
        print(i)
    for row in input:
        for i in range(0, len(row)):
            row[i] = str( int(row[i]) + 1)
            if(int(row[i]) > 9):
                newFlash = True
    if(newFlash):
        for x in range(0,10):
            for y in range(0,10):
                if(input[x][y] != "x" and int(input[x][y]) > 9):
                    increaseAdj(x,y)
    for row in input:
        for i in range(0, 10):
            if(row[i] == "x"):
                row[i] = 0
                flash += 1

print(flash)