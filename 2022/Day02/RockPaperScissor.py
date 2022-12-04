file = open('input.txt', 'r')
score = 0
for line in file:
    nextLine = line.split()
    yPick = nextLine[1]
    if(yPick == "X"):
        score += 1
        print("X")
        if(nextLine[0]== "C"):
            score += 6
        elif(nextLine[0] == "A"):
            score += 3
    elif(yPick == "Y"):
        score += 2
        if(nextLine[0]== "A"):
            score += 6
        elif(nextLine[0] == "B"):
            score += 3
    elif(yPick == "Z"):
        score += 3
        if(nextLine[0]== "B"):
            score += 6
        elif(nextLine[0] == "C"):
            score += 3
        
print(score)