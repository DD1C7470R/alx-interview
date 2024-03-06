#!/usr/bin/python3
'''Island perimeter'''


def island_perimeter(grid):
    ''''Calculates the perimerter of a grid'''
    perimeter = 0
    grid_length = len(grid)
    rows, cols = grid_length + 1, grid_length + 1
    for row in grid:
        if 1 in row:
            perimeter += 4
    return perimeter
