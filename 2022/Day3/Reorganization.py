file = open('input.txt', 'r')
score = 0
for line in file:
    firstPart, secPart = line[:len(line)//2], line[len(line)//2:]
    c = ' '.join(set(firstPart).intersection(secPart))
    print(c)
    if(c.islower()):
        score += ord(c) - 96
        print(ord(c) -96)
    else:
        score += ord(c) - 38
        print(ord(c) -38)

print(score)