fresh_id = []
amount_fresh = 0
with open("input.txt","r") as file:
    for row in file:
        value_row = row.strip().split("-")
        if value_row[0] == "":
            pass
        elif len(value_row) == 1:
            for pair in fresh_id:
                if int(value_row[0]) >= pair[0] and int(value_row[0])<=pair[1]:
                    amount_fresh += 1
                    break
        elif len(value_row) == 2:
            fresh_id.append((int(value_row[0]), int(value_row[1])))
print(amount_fresh)
