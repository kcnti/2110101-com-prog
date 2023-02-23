cards = input().split()
method = input()
c = 0
for i in method:
    if i == 'C':
        cards[len(cards)//2:], cards[:len(cards)//2] = cards[:len(cards)//2], cards[len(cards)//2:]
    elif i == 'S':
        for i in range(len(cards) - 1):
            if i%2:
                t = cards[(len(cards))//2 + c]
                del cards[(len(cards))//2 + c]
                cards.insert(i, t)
                c += 1
    c = 0

print(' '.join(cards))