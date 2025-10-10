def decode_segments(segInput):
    decodeList = [""]*10
    for seg in sorted(segInput, key=lambda x: (len(x), sorted(x))):
        match len(seg):
            case 2:
                decodeList[1] = seg
            case 3:
                decodeList[7] = seg
            case 4:
                decodeList[4] = seg
            case 7:
                decodeList[8] = seg
            case 5:
                if set(decodeList[7]).issubset(set(seg)):
                    decodeList[3] = seg
                elif len(set(seg).intersection(set(decodeList[4]))) == 3:
                    decodeList[5] = seg
                else:
                    decodeList[2] = seg
            case 6:
                if set(decodeList[4]).issubset(set(seg)):
                    decodeList[9] = seg
                elif set(decodeList[7]).issubset(set(seg)):
                    decodeList[0] = seg
                else:
                    decodeList[6] = seg
    return decodeList


file = open("input.txt","r")
result = 0
for l in file:
    parts = l.split("|")
    signal_patterns = parts[0].split()
    nmbDecoded = decode_segments(signal_patterns)
    digits = parts[1].split()
    value = ""
    for dig in digits:
        for index, decoded_digit in enumerate(nmbDecoded):
            if(set(dig) == set(decoded_digit)):
                value += str(index)
                break

    result += int(value)
print(result)
