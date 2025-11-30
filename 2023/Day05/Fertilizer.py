file = open("input.txt", "r")
start_value = next(file).strip().split(":")
start_value = [eval(i) for i in start_value[1].split()]
next(file)
next(file)
temp = []
test_remove = []
for line in file:
    if line[0].isnumeric():
        this_line = line.split()
        index = 0
        for x in start_value:
            index += 1
            if int(this_line[1]) <= x and int(this_line[1]) + int(this_line[2]) >= x:
                temp.append(int(this_line[0]) + x - int(this_line[1]))
                test_remove.append(x)
        start_value = [i for i in start_value if i not in test_remove]
    else:
        start_value.extend(temp)
        temp = []
        next(file)
start_value.extend(temp)
print(min(start_value))
