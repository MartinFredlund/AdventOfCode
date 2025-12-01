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
    print("---------------------------------")
    print("New row: Current " + str(current_value) + " row: " + turn)
    
    #Count how many times we pass through 0
    if current_value < 0:
        zeros += abs(current_value) // 100 + 1
    elif current_value > 99:
        zeros += current_value // 100
    elif current_value == 0:
        zeros += 1
    
    #Wrap to range 0-99
    current_value = current_value % 100
    
    print("After wrap: New value : " + str(current_value) + " zeros " + str(zeros))


    

    