#!/usr/bin/python3
'''Island perimeter'''


def island_perimeter(grid):
    ''''Calculates the perimerter of a grid'''
    perimeter = 0
    grid_length = len(grid)
    rows, cols = grid_length, len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter
