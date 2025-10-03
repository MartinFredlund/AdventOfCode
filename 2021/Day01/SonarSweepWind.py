def nextValue(value, line):    
    for x in range(3):
        value[x] = value[x+1]
    value[3] = int (line)
    return value
    
file = open('input.txt', 'r')
value = [0,0,0,0]
amount = 0

for x in range(1, 4):
    value[x] = int (file.readline())

for line in file:
    value = nextValue(value, line)
    if(value[0] + value[1] + value[2] < value[1] + value[2] + value[3]):
        amount += 1
print(amount)
file.close()