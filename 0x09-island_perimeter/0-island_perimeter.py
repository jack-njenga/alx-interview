#!/usr/bin/python3
"""
Create a function def island_perimeter(grid): that returns the perimeter of the island described in grid
"""


def island_perimeter(grid):
    """
    returns the perimeter of the island described in grid
    """
    if not grid:
        return 0

    pm, rows, cols = 0, len(grid), len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                pm = pm + 4

                if row > 0 and grid[row - 1][col] == 1:
                    pm = pm - 2
                if col > 0 and grid[row][col - 1] == 1:
                    pm = pm - 2
    return pm
