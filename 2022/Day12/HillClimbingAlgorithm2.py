import timeit
import sys

startTime = timeit.default_timer()
file = open('input.txt', 'r')
grid =[]
coord = (0,0)
start = (20,0)
end = (20,145)
dist = []
dNodes = []

def Solve():
    while True:
        min = sys.maxsize
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if(dist[y][x] < min and not dNodes[y][x]):
                    min = dist[y][x]
                    coord = (x, y)

        dNodes[coord[1]][coord[0]] = True
        if(coord[0] == end[1] and coord[1] == end[0]):
            print(dist[end[0]][end[1]])
            return
        rowLimit = len(grid)
        columnLimit = len(grid[0])
        if(coord[0] - 1 >= 0): 
            if(dist[coord[1]][coord[0]-1] > dist[coord[1]][coord[0]] + 1 and ord(grid[coord[1]][coord[0]]) + 1 >= ord(grid[coord[1]][coord[0]-1])):
                dist[coord[1]][coord[0]-1] = dist[coord[1]][coord[0]] + 1
        if(coord[0] + 1 < columnLimit):
            if(dist[coord[1]][coord[0]+1] > dist[coord[1]][coord[0]] + 1 and ord(grid[coord[1]][coord[0]]) + 1 >= ord(grid[coord[1]][coord[0]+1])):
                dist[coord[1]][coord[0]+1] = dist[coord[1]][coord[0]] + 1
        if(coord[1] - 1 >= 0):
            if(dist[coord[1]-1][coord[0]] > dist[coord[1]][coord[0]] + 1 and ord(grid[coord[1]][coord[0]]) + 1 >= ord(grid[coord[1]-1][coord[0]])):
                dist[coord[1]-1][coord[0]] = dist[coord[1]][coord[0]] + 1
        if(coord[1] + 1 < rowLimit): 
            if(dist[coord[1]+1][coord[0]] > dist[coord[1]][coord[0]] + 1 and ord(grid[coord[1]][coord[0]]) + 1 >= ord(grid[coord[1]+1][coord[0]])):
                dist[coord[1]+1][coord[0]] = dist[coord[1]][coord[0]] + 1

def setUp():
    for line in file:
        grid.append(line.replace("S", "a").replace("E", "z").rstrip())
    for i in range(len(grid)):
        dist.append([sys.maxsize]*len(grid[0]))
        dNodes.append([False]*len(grid[0]))
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if(grid[y][x] == "a"):
                dist[y][x] = 0

setUp()
Solve()
stop = timeit.default_timer()
print('Time: ', stop - startTime)  
