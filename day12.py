from copy import deepcopy
field = []
conditions = []
found_values = {}

with open("day12.txt") as file:
    for line in file:
        line = line.replace("\n","")
        pair = line.split(" ")
        field.append(pair[0])
        conditions.append([int(x) for x in pair[1].split(",")])


def test_str(s, conds, in_block=False):
    key = s + " " + str(conds) + " " + str(in_block)
    if key in found_values:
        return found_values[key]
    
    if conds == [0]:
        if s == "" or s.find("#") < 0:
            out = 1
        else:
            out = 0
    elif s == "":
        out = 0
    elif sum(conds) > len(s):
        out = 0
    elif s[0] == "#":
        if conds[0] == 0:
            out = 0
        else:
            new_conds = deepcopy(conds)
            new_conds[0] -= 1
            out = test_str(s[1:], new_conds, True)
    elif s[0] == ".":
        if conds[0] == 0:
            out = test_str(s[1:], conds[1:])
        elif in_block:
            out = 0
        else:
            out = test_str(s[1:], conds)
    else:  
        out = test_str("." + s[1:], conds, in_block) + test_str("#" + s[1:], conds, in_block)

    found_values[key] = out
    return out

def find_all_combinations(field, conds):
    total = 0
    for i in range(len(field)):
        value = test_str(field[i], conds[i])
        total += value
    return total

def part_one():
    return find_all_combinations(field, conditions)

def part_two():
    new_field = []
    new_conds = []
    for i in range(len(field)):
        new_field.append((field[i] + "?") * 4 + field[i])
        conds = ",".join([str(x) for x in conditions[i]])
        conds = (conds + ",") * 4 + conds
        new_conds.append([int(x) for x in conds.split(",")])
    return find_all_combinations(new_field, new_conds)

print("Answer to part 1:", part_one())
print("Answer to part 2:", part_two())
    