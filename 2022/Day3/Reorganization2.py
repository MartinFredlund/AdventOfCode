import timeit
start = timeit.default_timer()

score = 0
lineCounter = 0
row = ["","",""]

def calc():
    global score 
    c = ' '.join(set(row[0]).intersection(row[1]).intersection(row[2]))
    if(c.islower()):
        score += ord(c) - 96
    else:
        score += ord(c) - 38
        
file = open('input.txt', 'r')
for line in file:
    row[lineCounter%3] = line[:-1]
    if((lineCounter+1) % 3 == 0):
        calc()
    lineCounter += 1
print(score)

stop = timeit.default_timer()
print('Time: ', stop - start)  

