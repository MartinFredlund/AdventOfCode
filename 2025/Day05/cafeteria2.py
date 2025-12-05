fresh_id = dict()
amount_fresh = 0
with open("input.txt","r") as file:
    for row in file:
        value_row = row.strip().split("-")
        if len(value_row) == 2:
            for start_Value, length in fresh_id.items():
                if start_Value < value_row[0] and value_row[0] < start_Value + length:
                    

            fresh_id.append([int(value_row[0]), int(value_row[1])])
print(fresh_id)
