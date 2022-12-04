import timeit
start = timeit.default_timer()

file = open('input.txt', 'r')
score = 0
for line in file:
    row = line.replace("-", ",").replace("\n", "").split(",")
    row = [int(i) for i in row]
    if(not(row[1] < row[2] or row[3] < row[0])):
        score += 1        
print(score) 

stop = timeit.default_timer()
print('Time: ', stop - start)  
