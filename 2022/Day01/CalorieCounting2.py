file = open('input.txt', 'r')
amountCal = [0,0,0]
tempAmountCal = 0

for line in file:
    line = line.rstrip()
    if(line):
        tempAmountCal += int(line)
    else:
        for k in range(3):
            if(tempAmountCal > amountCal[k]):
                amountCal[k] = tempAmountCal
                amountCal.sort()
                break
        tempAmountCal = 0   
print(sum(amountCal))