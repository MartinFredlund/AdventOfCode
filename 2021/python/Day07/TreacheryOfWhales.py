from statistics import median
import math

file = open("input.txt", "r")
input = file.readline().split(",")
height = [int(i) for i in input]
medianVal = median(height)
maxVal = math.ceil(medianVal)
minVal = math.floor(medianVal)
print(
    min(sum([abs(i - maxVal) for i in height]), sum([abs(i - minVal) for i in height]))
)
