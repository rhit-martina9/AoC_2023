input = []
paint = []

with open("day18.txt") as file:
    for line in file:
        line = line.replace("\n","")
        line = line.split(" ")
        input.append([line[0], int(line[1])])
        paint.append(line[2][2:-1])

# print(input)
# print(paint)
        
def find_points(steps):
    points = [(0,0)]
    perimeter = 0
    for step in steps:
        match step[0]:
            case 'L':
                x = points[-1][0]-step[1]
                y = points[-1][1]
            case 'R':
                x = points[-1][0]+step[1]
                y = points[-1][1]
            case 'U':
                x = points[-1][0]
                y = points[-1][1]+step[1]
            case 'D':
                x = points[-1][0]
                y = points[-1][1]-step[1]
        points.append((x,y))
        perimeter += step[1]
    return points, perimeter

def shoelace(points):
    total = 0
    for i in range(len(points)-1):
        total += points[i][1]*points[i+1][0] - points[i][0]*points[i+1][1]
        
    total += points[-1][1]*points[0][0] - points[-1][0]*points[0][1]
    return total/2

def part_one(input):
    points, perimeter = find_points(input)
    interior = shoelace(points) - perimeter/2 + 1
    return int(interior+perimeter)

def color_convert(i):
    match i:
        case "0":
            return "R"
        case "1":
            return "D"
        case "2":
            return "L"
        case "3":
            return "U"

def part_two():
    new_input = [[color_convert(x[-1]), int(x[:-1], 16)] for x in paint]
    return part_one(new_input)

print("Answer to part 1:", part_one(input))
print("Answer to part 2:", part_two())
    