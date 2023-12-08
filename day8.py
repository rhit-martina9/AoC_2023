import re
import math
steps = []
nodes = {}

with open("day8.txt") as file:
    for line in file:
        line = line.replace("\n","")
        if "=" in line:
            line = re.sub("[()]", "", line)
            pair = line.split(" = ")
            nodes[pair[0]] = pair[1].split(", ")
        elif line != "":
            steps = [0 if x=='L' else 1 for x in [*line]]

def part_one():
    cur_node = "AAA"
    counter = 0
    while cur_node != "ZZZ":
        cur_node = nodes[cur_node][steps[counter % len(steps)]]
        counter += 1
    return counter

def part_two():
    cur_nodes = list(filter(lambda v:  v[-1] == "A", nodes.keys()))
    stops = [[] for _ in range(len(cur_nodes))]
    counter = 0
    for i in range(len(cur_nodes)):
        while True:
            cur_nodes[i] = nodes[cur_nodes[i]][steps[counter % len(steps)]]
            counter += 1
            if cur_nodes[i][-1] == "Z":
                stops[i].append(counter)
                if len(stops[i]) > 1 and (counter % len(steps)) in map(lambda v: v % len(steps), stops[i]):
                    break
        stops[i] = list(filter(lambda v : (v % len(steps) == stops[i][-1]  % len(steps)), stops[i]))
        stops[i] = stops[i][1] - stops[i][0] # period of cycle
    return math.lcm(*stops)

print("Answer to part 1:", part_one())
print("Answer to part 2:", part_two())