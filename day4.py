import re

cards = []
scores = []
with open("day4.txt") as input:
    for line in input:
        line = re.sub("\n", "", line)
        data = line.split(": ")
        data[0] = re.sub("Card","", data[0])
        data[0] = int(re.sub(" ","", data[0]))
        data[1] = re.sub("  "," ",data[1])
        nums = data[1].split(" | ")
        cards.append([nums[0].split(" "), nums[1].split(" ")])

def part_one():
    total = 0
    for card in cards:
        score = 0
        for num in card[1]:
            if num in card[0]:
                score = score + 1
        scores.append(score)
        total = total + (0 if score == 0 else pow(2, score - 1))
    return total

def part_two():
    tickets = [1 for _ in range(len(cards))]
    for i in range(len(cards)):
        for j in range(i+1, i+scores[i]+1):
            tickets[j] += tickets[i]
    return sum(tickets)

print(part_one())
print(part_two())