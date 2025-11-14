from math import prod


def packet():
    global binary_row
    if len(binary_row) < 6:
        return 0
    amount = 0
    version = int(binary_row[:3], 2)
    binary_row = binary_row[3:]
    id = int(binary_row[:3], 2)
    binary_row = binary_row[3:]

    match id:
        case 4:
            amount += id4()
            pass
        case _:
            bit = binary_row[:1]
            binary_row = binary_row[1:]
            if bit == "1":
                amount += other1(id)
            else:
                amount += other0(id)
            pass
    return amount


def id4():
    global binary_row
    num = ""
    while True:
        lead = binary_row[:1]
        binary_row = binary_row[1:]
        num += binary_row[:4]
        binary_row = binary_row[4:]
        if lead == "0":
            return int(num, 2)


def other0(id):
    global binary_row
    lenght = int(binary_row[:15], 2)
    binary_row = binary_row[15:]

    sub_packets = binary_row[:lenght]
    binary_row = binary_row[lenght:]

    res = []
    temp_binary = binary_row
    binary_row = sub_packets
    while len(binary_row) >= 6:
        res.append(packet())
    binary_row = temp_binary
    return calcNumber(id, res)


def other1(id):
    global binary_row
    number_packet = int(binary_row[:11], 2)
    binary_row = binary_row[11:]
    res = []
    for _ in range(number_packet):
        res.append(packet())
    return calcNumber(id, res)


def calcNumber(id, res):
    match id:
        case 0:
            return sum(res)
        case 1:
            return prod(res)
        case 2:
            return min(res)
        case 3:
            return max(res)
        case 5:
            if res[0] > res[1]:
                return 1
            else:
                return 0
        case 6:
            if res[0] < res[1]:
                return 1
            else:
                return 0
        case 7:
            if res[0] == res[1]:
                return 1
            else:
                return 0


file = open("input.txt")
binary_row = ""
result = 0
for line in file:
    for char in line.strip():
        binary_row += format(int(char, 16), "04b")

result = packet()
print(result)
