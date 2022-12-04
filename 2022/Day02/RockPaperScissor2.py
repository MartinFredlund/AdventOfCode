import timeit

start = timeit.default_timer()
file = open('input.txt', 'r')
score = 0
for line in file:
    nextLine = line.split()
    yPick = nextLine[1]
    if(yPick == "X"):
        if(nextLine[0]== "A"):
            score += 3
        elif(nextLine[0] == "B"):
            score += 1
        elif(nextLine[0] == "C"):
            score += 2
    elif(yPick == "Y"):
        score += 3
        if(nextLine[0]== "A"):
            score += 1
        elif(nextLine[0] == "B"):
            score += 2
        elif(nextLine[0] == "C"):
            score += 3
    elif(yPick == "Z"):
        score += 6
        
        if(nextLine[0]== "A"):
            score += 2
        elif(nextLine[0] == "B"):
            score += 3
        elif(nextLine[0] == "C"):
            score += 1
        
print(score)
stop = timeit.default_timer()

print('Time: ', stop - start)  