def update_dict(newStart, newEnd, fresh_id):
    added = False
    for start_Value, length in fresh_id.items():
        # inside
        if start_Value <= newStart and newEnd <= start_Value + length:
            # Do nothing range does not change
            added = True
            break
        # outside
        elif start_Value > newStart and newEnd > start_Value + length:

            added = True
            fresh_id.pop(start_Value)
            fresh_id[newStart] = newEnd - newStart
            break
        # Before
        elif start_Value >= newStart and newEnd >= start_Value:

            fresh_id.pop(start_Value)
            fresh_id[newStart] = max(newEnd, start_Value + length) - newStart
            added = True
            break
        # After
        elif start_Value <= newStart and newStart <= start_Value + length:

            fresh_id[start_Value] = max(newEnd, start_Value + length) - start_Value
            added = True
            break
    if not added:
        fresh_id[newStart] = newEnd - newStart
    return added


fresh_id = dict()
amount_fresh = 0
with open("input.txt", "r") as file:
    for row in file:
        value_row = row.strip().split("-")

        if len(value_row) == 2:
            newStart, newEnd = map(int, value_row)
            update_dict(newStart, newEnd, fresh_id)

overlap = True
while overlap:
    overlap = False
    new_dict = dict()
    for start_value, length in fresh_id.items():
        result = update_dict(start_value, start_value + length, new_dict)
        if result:
            overlap = True
    fresh_id = new_dict.copy()
full_range = 0
for value, length in fresh_id.items():
    full_range += length + 1
print(full_range)
