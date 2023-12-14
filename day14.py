import numpy as np
input = []
memo_data = []

with open("day14.txt") as file:
    for line in file:
        line = line.replace("\n","")
        input.append([*line])

def calc_load(input):
    total = 0
    for i in range(len(input)):
        rocks = sum(map(lambda v: 1 if v == "O" else 0, input[i]))
        total += rocks * (len(input)-i)
    return total

def calc_load_str(input):
    input = input.replace("\"", "").replace("\'", "")
    input = input[2:-2].split("], [")
    for i in range(len(input)):
        input[i] = input[i].split(", ")
    return calc_load(input)

def roll_row_west(row):
    row = "".join(row)
    for j in range(len(row)):
        if row[j] != "O":
            round_x = row[j:].find("O")+j
            still_x = row[j:].find("#")+j
            if round_x != j-1 and (still_x == j-1 or (j < still_x and round_x < still_x)):
                row = row[:j] + "O" + row[j+1:round_x] + "." + row[round_x+1:]
    return [*row]

def roll(input, direction):
    if direction == "N":
        input = np.transpose(input).tolist()
        for i in range(len(input)):
            input[i] = roll_row_west(input[i])
        input =  np.transpose(input).tolist()
    elif direction == "W":
        for i in range(len(input)):
            input[i] = roll_row_west(input[i])
    elif direction == "S":
        input = np.transpose(input).tolist()
        for i in range(len(input)):
            input[i].reverse()
            input[i] = roll_row_west(input[i])
            input[i].reverse()
        input =  np.transpose(input).tolist()
    elif direction == "E":
        for i in range(len(input)):
            input[i].reverse()
            input[i] = roll_row_west(input[i])
            input[i].reverse()
    return input

def cycle(input):
    input = roll(input, "N")
    input = roll(input, "W")
    input = roll(input, "S")
    input = roll(input, "E")
    return input

def part_one():
    new_input = roll(input, "N")
    return calc_load(new_input)

def part_two(cycles):
    new_input = input
    for _ in range(cycles):
        if str(new_input) in memo_data:
            break
        memo_data.append(str(new_input))
        new_input = cycle(new_input)

    loc = memo_data.index(str(new_input))
    period = len(memo_data) - loc
    index = (cycles - loc) % period + loc
    return calc_load_str(memo_data[index])

print("Answer to part 1:", part_one())
print("Answer to part 2:", part_two(1000000000))
    