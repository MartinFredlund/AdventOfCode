import sys
import numpy as np
def next(pos, value):
    if(pos[0]-1 > 0):
        move([pos[0]-1, pos[1]], value)
    if(pos[0]+1 < len(grid[0])):
        move([pos[0]+1, pos[1]], value)
    if(pos[1]-1 > 0):
        move([pos[0], pos[1]-1], value)        
    if(pos[1]+1 < len(grid)):
        move([pos[0], pos[1]+1], value)
        
def move(pos, value):
    global grid, best, pathBest, posBest
    value += grid[pos[1],pos[0]]
    posAsString = ''.join([str(elem) for elem in pos])
    if(pos == [len(grid)-1, len(grid[0])-1]):
        if(value < best):
            best = value
            print(value)
    elif(posAsString in posBest and value < best):      
        if(posBest.get(posAsString) > value):
            posBest[posAsString] = value
            next(pos, value)
    elif(not posAsString in posBest and value < best):
        posBest[posAsString] = value
        next(pos, value)  

sys.setrecursionlimit(50000)
file = open("input.txt")
setUp = []
pathBest = []
posBest = dict()
for line in file:
    setUp.append(list(map(int, line.strip("\n"))))
grid = np.array(setUp)
amount = len(grid[0])
#print(grid)
for i in range(1,5):
    for x in range(0, amount):
        #print([y+i if y < 10-i else [(y + i) - 9] for y in grid[:,[x]]])
        grid = np.append(grid, [y+i if y < 10-i else (y + i) - 9 for y in grid[:,[x]]], 1)
        #print(grid)

best = grid[:,0].sum() + grid[-1,1:].sum()
#print(len(grid[0]))
print(len(grid[0]), len(grid[-1]), len(grid[10]))
print(len(grid), len(grid))
print(best)
move([0,0], 0)
print(best - grid[0,0])