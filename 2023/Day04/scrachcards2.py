file = open("input.txt", "r")
result = [1] * 220
round = 0
for line in file:
    input = line.rstrip().replace(":", "|").split("|")
    correct = input[1].split()
    numbers = input[2].split()
    matches = len(correct) + len(numbers) - len(set(correct).union(set(numbers)))
    for i in range(round + 1, round + 1 + matches):
        result[i] += result[round]
    round += 1
print(sum(result))
