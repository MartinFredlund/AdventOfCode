def arraySize(file):
    maxX = 0
    maxY = 0
    for line in file:
        if(line[0].isnumeric()):
            temp = line.split(",")
            if(maxX < int(temp[0])):
                maxX = int(temp[0])
            if(maxY < int(temp[1])):
               maxY = int(temp[1])
    transPaper = [[]*(maxX+1)]*(maxY+1)    
    for i in range(0, maxY+1):
        transPaper[i] = ["."]*(maxX+1)
    file.seek(0)
    return transPaper

def fillWithInput(paper, fold):
    for line in file:
        if(line[0].isnumeric()):
            temp = line.strip("\n").split(",")
            print(temp)
            print(temp[0], len(paper), temp[1], len(paper[0]))
            paper[int(temp[1])][int(temp[0])] = "#"
        elif(line[0] == "f"):
            temp = line.strip("fold along ").strip("\n").split("=")
            fold.append(temp)
def foldPaper(dir, paper):
    if(dir == "y"):
        print("newY: ", int(len(paper[0])/2), "newX: ", len(paper))
        for i in range(0, len(paper[0])):
            paper[int(fold[0][1])][i] = "X"
        for x in range(0, len(paper[0])):
            for y in range(0, int((len(paper)+1)/2)):
                print("x:",  x, "y:", y, "count y:", len(paper)-1)
                if(paper[y][x] == "#" or paper[len(paper)-y-1][x] == "#"):
                    paper[y][x] = "#"
                #else:
                    #paper[y][x] = "."
        
        index = int((len(paper))/2)
        for y in range(0, int((len(paper)+1)/2)):
            print("y:", y, "Y:", len(paper))
            print(paper[int((len(paper)+1)/2)])
            print(index)
            del paper[index]
        return paper
    
    elif(dir == "x"):
        for i in range(0, len(paper)):
            paper[i][int(fold[0][1])] = "X"
        for x in range(0, int((len(paper[0]))/2)):
            for y in range(0, len(paper)):
                print("x", x, "y:", y, "calc X:", len(paper[0])-x-1)
                if(paper[y][x] == "#" or paper[y][len(paper[0])-x-1] == "#"):
                    paper[y][x] = "#"
        for i in paper:
            print(i)
        index = int((len(paper[0]))/2)
        for x in range(0, int((len(paper[0])+1)/2)):
            for y in range(0, len(paper)):
                del paper[y][index]
        return paper
            
file = open("input.txt")
paper = arraySize(file)
fold = []
fillWithInput(paper, fold)
paper = foldPaper(fold[0][0], paper)
amount = 0
for y in range(0, len(paper)):
    for x in range(0, len(paper[0])):
        if(paper[y][x] == "#"):
            amount += 1
            
for i in paper:
    print(i)
print(amount)