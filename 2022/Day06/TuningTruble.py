import sys
file = open('input.txt', 'r')
for line in file:
    for i in range(0, len(line)-3):
        strForCheck = line[i:i+4]
        foundDub = False
        for char in strForCheck:
            if(strForCheck.count(char) > 1):
                foundDub = True
        if(not foundDub):
            print(i+4)
            sys.exit()