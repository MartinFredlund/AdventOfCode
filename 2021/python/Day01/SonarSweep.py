lines = open('input.txt', 'r')
lastLine = int (lines.readline())
amount = 0
for line in lines:
    if int (line) > lastLine:
        amount += 1
    lastLine = int (line)
print(amount)
lines.close()