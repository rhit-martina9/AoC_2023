input = {}

with open("day19.txt") as file:
    for line in file:
        line = line.replace("\n","")
        pair = line.split(" ")
        input[pair[0]] = pair[1]

def part_one():
    return "Unknown"

def part_two():
    return "Unknown"

print("Answer to part 1:", part_one())
print("Answer to part 2:", part_two())
    