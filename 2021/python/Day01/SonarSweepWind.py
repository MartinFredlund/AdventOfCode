def nextValue(value, line):    
    return value[1:] + [line]
    
file = open('input.txt', 'r')
value = []
amount = 0

for _ in range(3):
    value.append(int (file.readline()))

for line in file:
    new_value = nextValue(value, int(line))
    if(sum(new_value) > sum(value)):
        amount += 1
    value = new_value
print(amount)
file.close()