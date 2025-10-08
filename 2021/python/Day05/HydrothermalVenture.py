file = open("input.txt", "r")
grid = [[0 for _ in range(1000)] for _ in range(1000)]
for line in file:
    parts = line.replace(" -> ", ",").split(",")
    x1, y1, x2, y2 = map(int, parts)
    if (x1==x2):
        for y in range(min(y1,y2), max(y1,y2)+1):
            grid[x1][y] += 1
    elif(y1==y2):
        for x in range(min(x1,x2), max(x1,x2)+1):
            grid[x][y1] += 1
result = sum(cell > 1 for row in grid for cell in row)
print(result)