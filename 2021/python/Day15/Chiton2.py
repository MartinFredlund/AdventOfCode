import sys
import numpy as np
import heapq


file = open("input.txt")
setUp = []
pathBest = []
posBest = dict()
for line in file:
    setUp.append(list(map(int, line.strip("\n"))))
grid = np.array(setUp)
original_grid = grid.copy()


full_grid = []
for tile_row in range(5):
    row_tiles = []
    for tile_col in range(5):
        # Calculate increment for this tile position
        increment = tile_row + tile_col
        # Create tile with wrapped values
        tile = np.where(
            original_grid + increment <= 9,
            original_grid + increment,
            (original_grid + increment) - 9,
        )
        row_tiles.append(tile)
    # Concatenate tiles horizontally
    full_grid.append(np.concatenate(row_tiles, axis=1))

# Concatenate all rows vertically
grid = np.concatenate(full_grid, axis=0)

# Dijkstras algorithm
rows, cols = grid.shape
costs = np.full(grid.shape, np.inf)
costs[0, 0] = 0
heap = [(0, 0, 0)]
while heap:
    cost, row, col = heapq.heappop(heap)
    if (row, col) == (rows - 1, cols - 1):
        print(cost)
        break
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < rows and 0 <= new_col < cols:
            new_cost = cost + grid[new_row, new_col]
            if new_cost < costs[new_row, new_col]:
                costs[new_row, new_col] = new_cost
                heapq.heappush(heap, (new_cost, new_row, new_col))
