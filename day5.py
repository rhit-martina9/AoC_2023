import re
maps = []
seeds = []

with open("day5.txt") as file:
    for line in file:
        if line != "\n":
            line = line.replace("\n", "")
            if line.find("seeds") > -1:
                seeds = [int(x) for x in line.split(" ")[1:]]
            elif line.find(":") > -1:
                maps.append([])
            else:
                lst = [int(x) for x in line.split(" ")]
                maps[-1].append([[lst[1], lst[1]+lst[2]], [lst[0], lst[0]+lst[2]]])
                
    for i in range(len(maps)):
        maps[i] = sorted(maps[i], key=lambda v : v[-1][0])

def range_intersect(r1, r2):
    value = [max(r1[0],r2[0]), min(r1[1], r2[1])]
    if value[0] > value[1]:
        return []
    return value

def convert(mapNum, num):
    for m in maps[mapNum]:
        if range_intersect(m[0], [num, num]) != []:
            return num - m[0][0] + m[1][0]
    return num

def part_one():
    new_seeds = [seed for seed in seeds]
    for i in range(len(maps)):
        for j in range(len(new_seeds)):
            new_seeds[j] = convert(i, new_seeds[j])
    return min(new_seeds)

def intersectingRanges(mapRan, ran, outInIfEmpty = True):
    out = []
    for m in mapRan:
        ir = range_intersect(m[1], ran)
        if ir != []:
            out.append([m[0][0] - m[1][0] + ir[0], m[0][1] - m[1][1] + ir[1]])
    if outInIfEmpty:
        if ran[0] < mapRan[0][1][0]:
            out.append([ran[0], min(mapRan[0][1][0],ran[1])])
        if ran[1] > mapRan[-1][1][1]:
            out.append([max(mapRan[-1][1][1],ran[0]), ran[1]])
        if out == []:
            return [ran]
    return out

def seed_ranges():
    out = []
    for i in range(0,len(seeds),2):
        out.append([[seeds[i],seeds[i]+seeds[i+1]],[seeds[i],seeds[i]+seeds[i+1]]])
    return out

def find_seeds(ran):
    print(ran)
    for i in range(len(maps)-2, -1, -1):
        newRan = []
        for r in ran:
            newRan += intersectingRanges(maps[i], r)
        ran = newRan
        print(ran)

    seedRanges = seed_ranges()
    newRan = []
    for r in ran:
        newRan += [x[0] for x in intersectingRanges(seedRanges, r, False)]
    ran = list(set(newRan))
    return ran
    
def part_two():
    ran = [[0, maps[-1][0][1][0]]]
    if ran == [[0,0]]:
        ran = [maps[-1][0][0]]
    i = 0
    while i < len(maps[-1]):
        ran = find_seeds(ran)
        i += 1
        if ran != []:
            return ran
        ran += [maps[-1][i][0]]
        
    return find_seeds([maps[-1][-1][1][1], maps[-1][-1][1][1] + 10])

best = part_two()
print("Best Seed:", best)
seeds = best
print(part_one())