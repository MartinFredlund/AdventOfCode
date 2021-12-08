file = open("input.txt", "r")
amount = 0
for line in file:
    nextLine = line.split(" | ")
    seqs = nextLine[1].split()
    for seq in seqs:
        if(len(seq) in {2,3,4,7}):
            amount += 1
print(amount)