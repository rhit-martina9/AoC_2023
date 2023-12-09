sequences = []

with open("day9.txt") as file:
    for line in file:
        line = line.replace("\n","")
        pair = [int(x) for x in line.split(" ")]
        sequences.append(pair)

def next_line(line):
    out = []
    for i in range(len(line)-1):
        out.append(line[i+1] - line[i])
    return out

def get_all_endings():
    endings = []
    for seq in sequences:
        current = [seq]
        while sum(map(lambda v: 1 if v == 0 else 0, current[-1])) != len(current[-1]):
            current.append(next_line(current[-1]))
        endings.append(current)
    return endings

def part_one():
    return sum(sum(x[-1] for x in grid) for grid in get_all_endings())

def part_two():
    new_values = []
    for seq in get_all_endings():
        total = 0
        for i in range(len(seq)):
            if i % 2 == 0:
                total += seq[i][0]
            else:
                total -= seq[i][0]
        new_values.append(total)
    return sum(new_values)

print("Answer to part 1:", part_one())
print("Answer to part 2:", part_two())