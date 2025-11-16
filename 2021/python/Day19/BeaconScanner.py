file = open("input.txt")
scanners = []
current_scanner = []

for line in file:
    line = line.strip()
    if line.startswith("--- scanner"):
        current_scanner = []
    elif line == "":
        if current_scanner:
            scanners.append(current_scanner)
    else:
        x, y, z = map(int, line.split(","))
        current_scanner.append((x, y, z))
if current_scanner:
    scanners.append(current_scanner)

# input done, gave up on rest for now
