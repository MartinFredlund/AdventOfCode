import timeit

start = timeit.default_timer()
import sys
file = open('input.txt', 'r')
def time():
    stop = timeit.default_timer()
    print('Time: ', (stop - start)/1000)  

for line in file:
    for i in range(0, len(line)-3):
        strForCheck = line[i:i+14]
        foundDub = False
        for char in strForCheck:
            if(strForCheck.count(char) > 1):
                foundDub = True
        if(not foundDub):
            print(i+14)
            time()
            sys.exit()