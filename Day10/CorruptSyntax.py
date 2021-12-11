file = open("input.txt")
result = 0
times = 0
syntax = []
for line in file:
    input = list(line)
    for char in input:
        if(char in {"(", "<", "{", "["}):
            syntax += char
        elif(char == ")"):
            if(syntax[-1] == "("):
                syntax.pop()
            else:
                result += 3
                times += 1
                break
        elif(char == ">"):
            if(syntax[-1] == "<"):
                syntax.pop()
            else:
                result += 25137
                times += 1
                break
        elif(char == "]"):
            if(syntax[-1] == "["):
                syntax.pop()
            else:
                result += 57
                times += 1
                break
        elif(char == "}"):
            if(syntax[-1] == "{"):
                syntax.pop()
            else:
                result += 1197
                times += 1
                break
    print(syntax)
print(result)
print(times)
           