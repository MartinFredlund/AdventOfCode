import json
import math

# With assistance from llms


def explode(snailfish, depth=0):
    """Returns (modified, exploded, left_value, right_value)"""
    if isinstance(snailfish, int):
        return snailfish, False, None, None

    left, right = snailfish

    # Check if this pair should explode
    if depth >= 4 and isinstance(left, int) and isinstance(right, int):
        return 0, True, left, right

    # Try to explode left side
    new_left, exploded, left_val, right_val = explode(left, depth + 1)
    if exploded:
        # Add right_val to leftmost number in right side if it exists
        if right_val is not None:
            right = add_to_leftmost(right, right_val)
            right_val = None
        return [new_left, right], True, left_val, right_val

    # Try to explode right side
    new_right, exploded, left_val, right_val = explode(right, depth + 1)
    if exploded:
        # Add left_val to rightmost number in left side if it exists
        if left_val is not None:
            new_left = add_to_rightmost(new_left, left_val)
            left_val = None
        return [new_left, new_right], True, left_val, right_val

    return snailfish, False, None, None


def add_to_leftmost(snailfish, value):
    """Add value to the leftmost regular number"""
    if isinstance(snailfish, int):
        return snailfish + value
    left, right = snailfish
    return [add_to_leftmost(left, value), right]


def add_to_rightmost(snailfish, value):
    """Add value to the rightmost regular number"""
    if isinstance(snailfish, int):
        return snailfish + value
    left, right = snailfish
    return [left, add_to_rightmost(right, value)]


def split(snailfish):
    """Returns (modified, split_occurred)"""
    if isinstance(snailfish, int):
        if snailfish >= 10:
            return [math.floor(snailfish / 2), math.ceil(snailfish / 2)], True
        return snailfish, False

    left, right = snailfish

    # Try to split left side
    new_left, split_occurred = split(left)
    if split_occurred:
        return [new_left, right], True

    # Try to split right side
    new_right, split_occurred = split(right)
    if split_occurred:
        return [new_left, new_right], True

    return snailfish, False


def reduce(snailfish):
    """Reduce a snailfish number until no more reductions possible"""
    while True:
        # Try explode
        new_snailfish, exploded, _, _ = explode(snailfish)
        if exploded:
            snailfish = new_snailfish
            continue

        # Try split
        new_snailfish, split_occurred = split(snailfish)
        if split_occurred:
            snailfish = new_snailfish
            continue

        # No more reductions
        break

    return snailfish


def add(left, right):
    """Add two snailfish numbers"""
    result = [left, right]
    return reduce(result)


def magnitude(snailfish):
    if isinstance(snailfish, int):
        return snailfish
    total_mag = 0
    left, right = snailfish
    total_mag += 3 * magnitude(left)
    total_mag += 2 * magnitude(right)
    return total_mag


# Read input
file = open("input.txt")
lines = [line.strip() for line in file]

# Parse first number
result = json.loads(lines[0])

# Add remaining numbers
for line in lines[1:]:
    right_nmb = json.loads(line)
    result = add(result, right_nmb)
mag_value = magnitude(result)
print(mag_value)
print(str(result).replace(" ", ""))
