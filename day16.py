input = []

with open("day16.txt") as file:
    for line in file:
        line = line.replace("\n","")
        input.append([*line])

def expand_dir(visited, loc, dir):
    while True:
        if loc[0] == -1 or loc[1] == -1 or loc[0] == len(input) or loc[1] == len(input[0]):
            return visited
        if str(loc) + " " + str(dir) in visited:
            return visited
        visited.append(str(loc) + " " + str(dir))
        match input[loc[0]][loc[1]]:
            case "|":
                if dir[0] == 0:
                    visited = expand_dir(visited, [loc[0]-1, loc[1]], [-1, 0])
                    dir = [1, 0]
            case "-":
                if dir[1] == 0:
                    visited = expand_dir(visited, [loc[0], loc[1]-1], [0, -1])
                    dir = [0, 1]
            case "/":
                dir = [-1*dir[1], -1*dir[0]]
            case "\\":
                dir = [dir[1], dir[0]]
            case _:
                pass

        loc[0] += dir[0]
        loc[1] += dir[1]

def part_one(loc, dir):
    return len(set([x[:x.find("]")+1] for x in expand_dir([], loc, dir)]))

def part_two():
    max = -1
    for i in range(len(input)):
        left = part_one([i, 0], [0, 1])
        if max < left:
            max = left

        right = part_one([i, len(input[0])-1], [0, -1])
        if max < right:
            max = right

    for i in range(len(input)):
        left = part_one([0, i], [1, 0])
        if max < left:
            max = left

        right = part_one([len(input)-1, i], [-1, 0])
        if max < right:
            max = right
    return max

print("Answer to part 1:", part_one([0,0], [0, 1]))
print("Answer to part 2:", part_two())
    