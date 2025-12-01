file = open("input.txt", "r")
zeros = 0
current_value = 50

for turn in file:
    direction = turn[0]
    amount = int(turn[1:])
    if direction == "L":
        current_value -= amount
    else:
        current_value += amount
    
    #Check if 0
    if current_value%100 == 0:
        zeros += 1
print(zeros)