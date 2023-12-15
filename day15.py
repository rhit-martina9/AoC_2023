input = []

with open("day15.txt") as file:
    for line in file:
        line = line.replace("\n","")
        pair = line.split(",")
        input = pair

def hash(char, cur_value):
    return ((ord(char) + cur_value) * 17) % 256

def hash_value(value):
    total = 0
    for c in value:
        total = hash(c, total)
    return total

def part_one():
    total = 0
    for line in input:
        total += hash_value(line)
    return total

def generate_boxes(input):
    boxes = {i:[] for i in range(256)}
    for line in input:
        if line[-1] == "-":
            label = line[:-1]
            box = hash_value(label)
            boxes[box] = list(filter(lambda v: v[0] != label, boxes[box]))
        else:
            label = line[:-2]
            box = hash_value(label)
            found = False
            for i in range(len(boxes[box])):
                if boxes[box][i][0] == label:
                    boxes[box][i][1] = line[-1]
                    found = True
            if not found:
                boxes[box].append([label, line[-1]])
    return boxes


def part_two():
    boxes = generate_boxes(input)
    total = 0
    for i in range(len(boxes)):
        for j in range(len(boxes[i])):
            total += (i+1) * (j+1) * int(boxes[i][j][1])
    return total

print("Answer to part 1:", part_one())
print("Answer to part 2:", part_two())
    