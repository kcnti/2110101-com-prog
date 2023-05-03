class Card:
 def __init__(self, value, suit):
    self.fl0wer = ['club', 'diamond', 'heart', 'spade']
    self.order = [str(i) for i in range(3, 11)] + ['J', 'Q', 'K', 'A', '2']

    self.value = value
    self.suit = suit

 def __str__(self):
    return '({} {})'.format(self.value, self.suit)

 def next1(self):
    flower = self.fl0wer.index(self.suit)
    num = self.order.index(self.value)

    if flower == 3:
        flower = flower%3 - 1
        num += 1
        if num == len(self.order):
            num = 0

    return '({} {})'.format(self.order[num], self.fl0wer[flower + 1])

 def next2(self):
    num = self.order.index(self.value)
    flower = self.fl0wer.index(self.suit)

    if flower == 3:
        flower = flower%3 - 1
        num += 1
        if num == len(self.order):
            num = 0

    self.value = self.order[num]
    self.suit = self.fl0wer[flower + 1]

    return self
    
n = int(input())
cards = []
for i in range(n):
 value, suit = input().split()
 cards.append(Card(value, suit))
for i in range(n):
 print(cards[i].next1())
print("----------")
for i in range(n):
 print(cards[i])
print("----------")
for i in range(n):
 cards[i].next2()
 cards[i].next2()
 print(cards[i])