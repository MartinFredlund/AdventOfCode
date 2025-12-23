from collections import deque

def find_shortest_path(lights, buttons):
   
    initial_state = tuple(lights)
    target_state = tuple([0] * len(lights))
    
    queue = deque([(initial_state, 0)])  # (state, steps)
    visited = set([initial_state])
    
    while queue:
        current_state, steps = queue.popleft()
        
        # Try pressing each button
        for button in buttons:
            new_state = list(current_state)
            for i in button:
                new_state[i] = 1-new_state[i]
            new_state_tuple = tuple(new_state)

            # Check if end state is found
            if new_state_tuple == target_state:
                return steps + 1
            # Add to queue if not visited before
            if new_state_tuple not in visited:
                visited.add(new_state_tuple)
                queue.append((new_state_tuple, steps +1))

    return -1

total = 0
with open("input.txt", "r") as file:
    for line in file:
        parts = line.split()
        lights = []
        buttons = []
        for part in parts:
            if part.startswith("["):
                for c in part[1:-1]:
                    if c == "#":
                        lights.append(1)
                    elif c == ".":
                        lights.append(0)
                        
            elif part.startswith("("):
                vals = part.strip("()").split(",")
                button_positions = tuple(int(v) for v in vals)
                buttons.append(button_positions)
        
        result = find_shortest_path(lights, buttons)
        total += result

print(total)
            