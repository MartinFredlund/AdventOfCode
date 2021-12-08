def checkValue(seq):
    for i in range(0,10):
        if(seq == input[i]):
            return i
    print("fail")        
    return 0

def sort(input):
    temp = ["","","","","","","","","",""]
    for seq in input:
        seq = "".join(sorted(seq))
        #insrt nbr1
        if(len(seq) == 2):
            #input.remove(seq)
            temp[1] = seq
        #insert nbr7
        elif(len(seq) == 3):
            #input.remove(seq)
            temp[7] = seq
        #insert nbr4
        elif(len(seq) == 4):
            #input.remove(seq)
            temp[4] = seq
        #insert nbr8
        elif(len(seq) == 7):
            #input.remove(seq)
            temp[8] = seq
    for seq in input:
        seq = "".join(sorted(seq))
        if(len(seq) == 5): #235 
            #insert nbr3        
            if(all(i in seq for i in temp[7])):
                temp[3] = seq
            #insert nbr5
            elif(sum(i in seq for i in temp[4]) == 3):
                temp[5] = seq
            #insert nbr2
            else:
                temp[2] = seq
        elif(len(seq) == 6): #069
            #insert nbr9
            if(all(i in seq for i in temp[4])):
                temp[9] = seq
            #insert nbr0
            elif(all(i in seq for i in temp[1])):
                temp[0] = seq
            #insert nbr6
            else:
                temp[6] = seq
    return temp
        
file = open("input.txt", "r")
result = 0
amount = ""
for line in file:
    amount = ""
    nextLine = line.split(" | ")
    input = nextLine[0].split()
    #sort input list after value
    input = sort(input)
    results = nextLine[1].split()
    for seq in results:
        seq = "".join(sorted(seq))
        amount += str(checkValue(seq))
    result += int( amount)

print(result)