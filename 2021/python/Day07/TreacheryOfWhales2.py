from statistics import median
import math

file = open("input.txt", "r")
input = file.readline().split(",")
height = [int(i) for i in input]
maxPos = max(height)
fuelUse = [0] * (maxPos + 1)


for i in range(maxPos + 1):
    fuelUse[i] = sum((abs(h - i) * (abs(h - i) + 1)) // 2 for h in height)

print(min(fuelUse))
