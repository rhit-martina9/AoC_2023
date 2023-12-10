input = []
start = []

with open("day10.txt") as file:
    for line in file:
        line = line.replace("\n","")
        input.append([*line])
        if "S" in input[-1]:
            start = [len(input)-1, line.rfind("S")]
# print(input)

def move(last, now):
    if input[now[0]][now[1]] == "|":
        if last == [now[0]-1, now[1]]:
            return now, [now[0]+1,now[1]]
        else:
            return now, [now[0]-1,now[1]]
    elif input[now[0]][now[1]] == "-":
        if last == [now[0], now[1]-1]:
            return now, [now[0],now[1]+1]
        else:
            return now, [now[0],now[1]-1]
    elif input[now[0]][now[1]] == "L":
        if last == [now[0]-1,now[1]]:
            return now, [now[0],now[1]+1]
        else:
            return now, [now[0]-1,now[1]]
    elif input[now[0]][now[1]] == "J":
        if last == [now[0]-1,now[1]]:
            return now, [now[0],now[1]-1]
        else:
            return now, [now[0]-1,now[1]]
    elif input[now[0]][now[1]] == "7":
        if last == [now[0]+1,now[1]]:
            return now, [now[0],now[1]-1]
        else:
            return now, [now[0]+1,now[1]]
    elif input[now[0]][now[1]] == "F":
        if last == [now[0]+1,now[1]]:
            return now, [now[0],now[1]+1]
        else:
            return now, [now[0]+1,now[1]]
    elif input[now[0]][now[1]] == "S":
        if now[0] > 0 and input[now[0]-1][now[1]] in ["|", "7", "F"]:
            if now[1] > 0 and input[now[0]][now[1]-1] in ["-", "L", "F"]:
                input[now[0]][now[1]] = "J"
            elif now[1] < len(input[0])-1 and input[now[0]][now[1]+1] in ["-", "J", "7"]:
                input[now[0]][now[1]] = "L"
            else:
                input[now[0]][now[1]] = "|"
            return now, [now[0]-1,now[1]]
        elif now[0] < len(input)-1 and input[now[0]+1][now[1]] in ["|", "J", "L"]:
            if now[1] > 0 and input[now[0]][now[1]-1] in ["-", "L", "F"]:
                input[now[0]][now[1]] = "7"
            else:
                input[now[0]][now[1]] = "F"
            return now, [now[0]+1,now[1]]
        else:
            input[now[0]][now[1]] = "-"
            return now, [now[0],now[1]-1]
    else:
        print("ERROR!!!!")

def part_one():
    loop = [["." for _ in range(len(input[0]))] for _ in range(len(input))]
    now = start
    last = [start[0], start[1]-1]
    counter = 1

    loop[now[0]][now[1]] = input[now[0]][now[1]]
    last, now = move(last, now)
    loop[now[0]][now[1]] = input[now[0]][now[1]]
    while [now[0],now[1]] != start:
        last, now = move(last, now)
        counter += 1
        loop[now[0]][now[1]] = input[now[0]][now[1]]
    return loop, counter // 2

def part_two(loop):
    counter = 0
    for line in loop:
        in_loop = 0
        flip_start = 0
        for cell in line:
            if cell == "." and in_loop % 2 == 1:
                counter += 1
            if cell == "7":
                if flip_start != "L":
                    in_loop += 1
            elif cell == "J":
                if flip_start != "F":
                    in_loop += 1
            elif cell != "." and cell != "-":
                in_loop += 1

            if cell == "L" or cell == "F":
                flip_start = cell
    return counter

loop, ans = part_one()
print("Answer to part 1:", ans)
print("Answer to part 2:", part_two(loop))