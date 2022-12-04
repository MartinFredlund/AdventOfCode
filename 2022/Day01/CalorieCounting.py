file = open('input.txt', 'r')
amountCal = 0
tempAmountCal = 0
for line in file:
    line = line.rstrip()
    if(line):
        tempAmountCal += int(line)
    else:
        if(tempAmountCal > amountCal):
            amountCal = tempAmountCal
        tempAmountCal = 0
        
print(amountCal)