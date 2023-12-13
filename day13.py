import numpy as np
input = [[]]

with open("day13.txt") as file:
    for line in file:
        line = line.replace("\n","")
        if line == "":
            input.append([])
        else:
            input[-1].append([*line])

def find_row_reflection(grid, diff):
    for i in range(len(grid)-1):
        count = 0
        for j in range(min(i+1, len(grid)-i-1)):
            count += sum(1 if grid[i-j][x] != grid[i+j+1][x] else 0 for x in range(len(grid[i-j])))
        if count == diff:
            return i+1
    return 0

def get_total(diff):
    row_total = 0
    col_total = 0
    for grid in input:
        row_total += find_row_reflection(grid, diff)
        col_total += find_row_reflection(np.transpose(grid).tolist(), diff)
    return row_total * 100 + col_total

def part_one():
    return get_total(0)

def part_two():
    return get_total(1)

print("Answer to part 1:", part_one())
print("Answer to part 2:", part_two())
    