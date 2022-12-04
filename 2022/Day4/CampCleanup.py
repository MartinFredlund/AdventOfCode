file = open('input.txt', 'r')
score = 0
for line in file:
    row = line.replace("-", ",").replace("\n", "").split(",")
    row = [int(i) for i in row]
    if(row[0] <= row[2] and row[1] >= row[3]):
        score += 1
        print(row)
        print(score, " (1)")
       
    elif(row[2] <= row[0] and row[3] >= row[1]):
       
        score += 1
        print(row)
        print(score, " (2)")
        
print(score)
#['63', '65', '8', '64']
