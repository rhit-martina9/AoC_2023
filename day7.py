card_bets = {}

with open("day7.txt") as file:
    for line in file:
        line = line.replace("\n","")
        pair = line.split(" ")
        card_bets[pair[0]] = pair[1]

def convert_jokers(hand):
    if "J" not in hand.keys():
        return hand
    
    other_cards = list(filter(lambda v: v != "J", hand))
    if len(hand) == 1:
        return hand  # five jokers
    elif len(hand) == 2: # five of a kind
        return {other_cards[0]: 5}
    elif len(hand) == 3:
        if hand["J"] == 3: # four of a kind
            out = {card : 1 for card in other_cards}
            out[other_cards[0]] += hand["J"]
            return out
        elif hand["J"] == 2: # four of a kind
            return {card : (1 if hand[card] == 1 else 4) for card in other_cards}
        elif hand[other_cards[0]] == 2: # full house
            out = {card : 2 for card in other_cards}
            out[other_cards[0]] += hand["J"]
            return out
        else: # four of a kind
            return {card : (1 if hand[card] == 1 else 4) for card in other_cards}
    elif len(hand) == 4:
        if hand["J"] == 2: # three of a kind
            out = {card : 1 for card in other_cards}
            out[other_cards[0]] += hand["J"]
            return out
        else: # three of a kind
            return {card : (1 if hand[card] == 1 else 3) for card in other_cards}
    elif len(hand) == 5: # one pair
        out = {card : 1 for card in other_cards}
        out[other_cards[0]] += hand["J"]
        return out

def hand_ranking(hand):
    hand = [*hand]
    hand = {i: hand.count(i) for i in set(hand)}
    hand = convert_jokers(hand)
    if len(hand) == 1:
        return 6 # five of a kind
    elif len(hand) == 2:
        counts = [hand[i] for i in list(hand.keys())]
        if max(counts) == 4:
            return 5 # four of a kind
        else:
            return 4 # full house
    elif len(hand) == 3:
        counts = [hand[i] for i in list(hand.keys())]
        if max(counts) == 3:
            return 3 # three of a kind
        else:
            return 2 # two pair
    elif len(hand) == 4:
        return 1 # one pair
    else:
        return 0 # high card

def hand_value(hand):
    hand = [*hand]
    total = 0
    for i in range(len(hand)):
        if hand[i] == "A":
            total += 14 * pow(10, 8-2*i)
        elif hand[i] == "K":
            total += 13 * pow(10, 8-2*i)
        elif hand[i] == "Q":
            total += 12 * pow(10, 8-2*i)
        elif hand[i] == "J":
            total += 1 * pow(10, 8-2*i)
        elif hand[i] == "T":
            total += 10 * pow(10, 8-2*i)
        else:
            total += int(hand[i]) * pow(10, 8-2*i)
        
    return total

def solve():
    sets = {i:[] for i in range(7)}
    for bet in card_bets:
        ranking = hand_ranking(bet)
        sets[ranking].append({bet: card_bets[bet]})

    ranking = 1
    total = 0
    for s in sets:
        sets[s] = sorted(sets[s], key = lambda v: hand_value(list(v.keys())[0]))
        for bet in sets[s]:
            total += ranking * int(bet[list(bet.keys())[0]])
            ranking += 1
    
    return total

print(solve())