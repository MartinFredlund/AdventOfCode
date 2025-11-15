file = open("input.txt")
line = file.readline()
parts = line.replace("target area: x=", "").replace(" y=", "").strip()
x_part, y_part = parts.split(",")
x_min, x_max = map(int, x_part.split(".."))
y_min, y_max = map(int, y_part.split(".."))

vy = -y_min - 1
height_max = vy * (vy + 1) / 2

print(height_max)
