problem_list = []
with open("input.txt", "r") as file:
    for row in file:
        line = row.strip().split()
        if len(problem_list) < 1:
            problem_list = [[] for _ in range(len(line))]
        for i, val in enumerate(line):
            problem_list[i].append(line[i])
total_score = 0
for problem in problem_list:
    operatior = problem[-1]
    match operatior:
        case "*":
            temp = 1
            for num in problem[:-1]:
                temp *= int(num)
            total_score += temp
        case "+":
            temp = 0
            for num in problem[:-1]:
                temp += int(num)
            total_score += temp
print(total_score)
