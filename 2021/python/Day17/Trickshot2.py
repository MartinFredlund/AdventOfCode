import math


def move(start_v):
    global x_min, x_max, y_min, y_max
    velocity = start_v
    current_pos = [0, 0]
    while True:
        current_pos[0] += velocity[0]
        current_pos[1] += velocity[1]
        if velocity[0] > 0:
            velocity[0] -= 1
        velocity[1] -= 1
        if x_min <= current_pos[0] <= x_max and y_min <= current_pos[1] <= y_max:
            return True
        if x_max < current_pos[0] or y_min > current_pos[1]:
            return False


file = open("input.txt")
line = file.readline()
parts = line.replace("target area: x=", "").replace(" y=", "").strip()
x_part, y_part = parts.split(",")
x_min, x_max = map(int, x_part.split(".."))
y_min, y_max = map(int, y_part.split(".."))
# Find smallest positive vx
vx_min = math.ceil(-1 / 2 + math.sqrt((1 / 4) + (2 * x_min)))
# Same as part 1
vy_max = -y_min - 1

amount_hit = 0
for x in range(vx_min, x_max + 1):
    for y in range(y_min, vy_max + 1):
        if move([x, y]):
            amount_hit += 1
print(amount_hit)
