import timeit

start = timeit.default_timer()
file = open('input.txt', 'r')
setUpArray = [[] for y in range(9)]
setUp = True
for line in file:

    if(setUp):
        if(line != " 1   2   3   4   5   6   7   8   9 \n"):
            pos = 0
            for i in [line[i+1] for i in range(0, len(line), 4)]:
                if(i != " "):
                    setUpArray[pos].insert(0, i)
                pos += 1
        else:
            setUp = False
    if(line[0] == "m"):
        line = line.rstrip().split(" ")
        for x in range(0, int(line[1])):
            setUpArray[int(line[5])-1].insert(len(setUpArray[int(line[5])-1]),setUpArray[int(line[3])-1].pop())
print([setUpArray[x].pop() for x in range(0, len(setUpArray))])

stop = timeit.default_timer()

print('Time in ms: ', (stop - start)/1000)  