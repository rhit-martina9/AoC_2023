import re
import math

grid = []
gears = {}
with open("day3.txt") as input:
    for line in input:
        line = re.sub("\n","",line)
        line = re.sub("[^0-9\.]","*",line)
        grid.append([*line])

def nextToAsterisk(lon,num):
    out = False
    for i in range(max(0,lon[0][0]-1),min(len(grid[0])-1,lon[-1][0]+1)+1):
        for j in range(max(0,lon[0][1]-1),min(len(grid[1])-1,lon[-1][1]+1)+1):
            if grid[i][j] == "*":
                if (140*i+j) not in gears:
                    gears[i*140+j] = []
                gears[i*140+j].append(num)
                out = True
    return out

def findNumber(x, y):
    num = -1
    if grid[x][y].isdigit():
        num = int(grid[x][y])
        if y < len(line)-1 and grid[x][y+1].isdigit():
            num = num*10 + int(grid[x][y+1])
            if y < len(line)-2 and grid[x][y+2].isdigit():
                num = num*10 + int(grid[x][y+2])
    return findNumber

def part_one():
    total = 0
    for j in range(len(grid)):
        line = grid[j]
        i = 0
        while i < len(line):
            num = findNumber(j,i)
            if num < 0:
                i += 1
            else:
                if nextToAsterisk([[j,i+k] for k in range(numLength(num))], num):
                    total += num
                i += numLength(num)
    return total

def numLength(x):
    return math.floor(math.log(x,10)) + 1

def part_two():
    total = 0
    for gear in gears:
        if len(gears[gear]) == 2:
            total += gears[gear][0] * gears[gear][1]
    return total

print(part_one())
print(part_two())
