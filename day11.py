grid = []

with open("day11.txt") as file:
    for line in file:
        line = line.replace("\n","")
        grid.append([*line])

def find_dists(length):
    dist = [[1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for i in range(len(grid)):
        if sum(map(lambda v: 1 if v == "." else 0, grid[i])) == len(grid[i]):
            dist[i] = list(map(lambda v: v + length - 1,dist[i]))
        for j in range(len(grid[0])):
            if sum(map(lambda v: 1 if v == "." else 0, [x[j] for x in grid])) == len(grid):
                dist[i][j] += length - 1
    return dist

def get_dist(i, j, dist):
    total = 0
    for k in range(min(i[1],j[1])+1,max(i[1],j[1])+1):
        total += dist[i[0]][k]
    for k in range(min(i[0],j[0])+1,max(i[0],j[0])+1):
        total += dist[k][j[1]]
    return total

def get_total_dist(dist):
    locs = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "#":
                locs.append((i,j))

    total = 0
    for i in range(len(locs)):
        for j in range(i+1,len(locs)):
            total += get_dist(locs[i],locs[j], dist)
    return total

def part_one():
    return get_total_dist(find_dists(2))

def part_two():
    return get_total_dist(find_dists(1000000))

print("Answer to part 1:", part_one())
print("Answer to part 2:", part_two())