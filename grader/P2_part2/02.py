cards_value = {
    "A": 1,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13
}

cards_type = {
    "C": 1,
    "D": 2,
    "H": 3,
    "S": 4
}

cards = input()

output = ""
for i in range(0, len(cards)-3, 2):
    card = cards[i:i+2]
    next_card = cards[i+2:i+4]
    value, _ = card[0], card[1]
    next_value, next_ = next_card[0], next_card[1]
    if value in cards_value:
        value = cards_value[value]
    if next_value in cards_value:
        next_value = cards_value[next_value]
    if value == next_value:
        diff = cards_type[_] - cards_type[next_]
    else:
        diff = int(value) - int(next_value)
    if diff > 0:
        output += "+" + str(diff)
    elif diff == 0:
        output += "0"
    else:
        output += str(diff)
print(output)
    