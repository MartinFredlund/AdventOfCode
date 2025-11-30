file = open("input.txt", "r")
sum = 0
for line in file:
    input = line.rstrip().replace(":", "|").split("|")
    correct = input[1].split()
    numbers = input[2].split()
    matches = len(correct) + len(numbers) - len(set(correct).union(set(numbers)))
    sum += int(2 ** (matches - 1))
print(sum)
