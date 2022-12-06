file = open('input.txt', 'r')  

for line in file:
    for i in range(0, len(line)-3):
        if(len(set(line[i:i+14])) == 14):
            print(i+14)
            break