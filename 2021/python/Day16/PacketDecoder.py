def packet():
    global binary_row
    if len(binary_row) < 6:
        return 0

    version = int(binary_row[:3], 2)
    binary_row = binary_row[3:]
    id = int(binary_row[:3], 2)
    binary_row = binary_row[3:]

    match id:
        case 4:
            id4()
            pass
        case _:
            bit = binary_row[:1]
            binary_row = binary_row[1:]
            if bit == "1":
                version += other1()
            else:
                version += other0()
            pass
    return version


def id4():
    global binary_row
    while True:
        packet = binary_row[:5]
        binary_row = binary_row[5:]
        if packet[0] == "0":
            break


def other0():
    global binary_row
    lenght = int(binary_row[:15], 2)
    binary_row = binary_row[15:]

    sub_packets = binary_row[:lenght]
    binary_row = binary_row[lenght:]

    version_sum = 0
    temp_binary = binary_row
    binary_row = sub_packets
    while len(binary_row) >= 6 and not all(b == "0" for b in binary_row):
        version_sum += packet()
    binary_row = temp_binary
    return version_sum


def other1():
    global binary_row
    number_packet = int(binary_row[:11], 2)
    binary_row = binary_row[11:]
    version_sum = 0
    for _ in range(number_packet):
        version_sum += packet()
    return version_sum


file = open("input.txt")
binary_row = ""
result = 0
for line in file:
    for char in line.strip():
        binary_row += format(int(char, 16), "04b")

result = packet()

print(result)
