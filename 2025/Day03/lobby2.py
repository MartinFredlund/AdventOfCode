file = open("input.txt", "r")
score = 0
for battery in file:
    battery = battery.strip()
    larg_list = [0 for _ in range(12)]
    for i in range(len(battery)):
        val = int(battery[i])
        for x in range(len(larg_list)):
            if i <= len(battery)-(len(larg_list)-x) and val > larg_list[x]:
                larg_list[x] = val
                for r in range(x+1, len(larg_list)):
                    larg_list[r] = 0
                break
    s=[str(i) for i in larg_list]
    jn = int("".join(s))
    score += jn
print(score)