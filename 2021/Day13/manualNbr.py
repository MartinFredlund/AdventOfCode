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
            paper[int(temp[1])][int(temp[0])] = "#"
        elif(line[0] == "f"):
            temp = line.strip("fold along ").strip("\n").split("=")
            fold.append(temp)

def foldPaper(newFold, paper):
    if(newFold[0] == "y"):
        for i in range(0, len(paper[0])):
            paper[int(newFold[1])][i] = "X"
        for x in range(0, len(paper[0])):
            for y in range(int(newFold[1])+1, len(paper)):
                if(paper[y][x] == "#"):
                    diff = y - int(newFold[1])
                    paper[y - 2 * diff][x] = "#"
        del paper[int(newFold[1]):len(paper)]
        return paper
    
    elif(newFold[0] == "x"):
        for i in range(0, len(paper)):
            paper[i][int(newFold[1])] = "X"
        for x in range(int(newFold[1])+1, len(paper[0])):
            for y in range(0, len(paper)):
                if(paper[y][x] == "#"):
                    diff = x - int(newFold[1])
                    paper[y][x - 2 * diff] = "#"
        for y in range(0, len(paper)):
            del paper[y][int(newFold[1]):len(paper[y])]
        return paper
            
file = open("input.txt")
paper = arraySize(file)
fold = []
fillWithInput(paper, fold)
for i in fold:
    paper = foldPaper(i, paper)
for x in paper:
    print(' '.join(x))