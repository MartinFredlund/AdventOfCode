import sys
import numpy as np
def move(pos, way, value):
    global endFound, best, grid, bestWay
    way.append(pos)
    value += int(grid[pos[1]][pos[0]])
    if(pos == [len(grid)-1, len(grid[0])-1]):
        if(not endFound):
            endFound = True
            best = value
            bestWay = way
        elif(value < best):
            best = value
            bestWay = way
    elif(value < best or not endFound):
        #print(not([pos[0]-1,pos[1]] in way))
        if(pos[0]-1 > 0 and not([pos[0]-1,pos[1]] in way)):
            move([pos[0]-1,pos[1]], way.copy(),value)
        if(pos[0]+1 < len(grid) and not([pos[0]+1,pos[1]] in way)):
            move([pos[0]+1,pos[1]], way.copy(),value)

        if(pos[1]-1 > 0 and not([pos[0],pos[1]-1] in way)):
            move([pos[0],pos[1]-1], way.copy(),value)
            
        if(pos[1]+1 < len(grid[0]) and not([pos[0],pos[1]+1] in way)):
            move([pos[0],pos[1]+1], way.copy(),value)
sys.setrecursionlimit(50000)
file = open("input.txt")
grid = []
bestAtPos = dict()
endFound = False
best = 0
bestWay = []    
for line in file:
    grid.append(list(line.strip("\n")))

move([0,0], [], 0)
print(best-int(grid[0][0]))