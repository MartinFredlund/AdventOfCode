import sys
import numpy as np
def next(pos, path, value):
    if(pos[0]-1 > 0 and not([pos[0]-1,pos[1]] in path)):
        move([pos[0]-1,pos[1]], path.copy(),value)
    if(pos[0]+1 < len(grid) and not([pos[0]+1,pos[1]] in path)):
        move([pos[0]+1,pos[1]], path.copy(),value)
    if(pos[1]-1 > 0 and not([pos[0],pos[1]-1] in path)):
        move([pos[0],pos[1]-1], path.copy(),value)        
    if(pos[1]+1 < len(grid[0]) and not([pos[0],pos[1]+1] in path)):
        move([pos[0],pos[1]+1], path.copy(),value)
        
def move(pos, path, value):
    global grid, best, pathBest, posBest
    path.append(pos)
    value += grid[pos[1],pos[0]]
    posAsString = ''.join([str(elem) for elem in pos])
    if(pos == [len(grid)-1, len(grid[0])-1]):
        if(value < best):
            best = value
            pathBest = path
            print(value)
    elif(posAsString in posBest):      
        if(posBest.get(posAsString) > value):
            posBest[posAsString] = value
            next(pos, path, value)
    elif(not posAsString in posBest):
        posBest[posAsString] = value
        next(pos,path,value)  

sys.setrecursionlimit(50000)
file = open("input.txt")
setUp = []
pathBest = []
posBest = dict()
for line in file:
    setUp.append(list(map(int, line.strip("\n"))))
grid = np.array(setUp)
print(grid)
best = grid[:,0].sum() + grid[-1,1:].sum()
print(best)
move([0,0], [], 0)
print(best- grid[-1,-1])