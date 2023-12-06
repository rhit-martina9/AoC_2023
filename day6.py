# times = [54, 70, 82, 75]
# dsts = [239, 1142, 1295, 1253]
times = [54708275]
dsts = [239114212951253]

def solve():
    total = 1
    for i in range(len(times)):
        total *= len(list(filter(lambda v: v >= dsts[i], [x*(times[i]-x) for x in range(times[i])])))
    return total

print(solve())