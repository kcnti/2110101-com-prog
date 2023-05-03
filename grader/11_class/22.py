class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return '({} {})'.format(self.value, self.suit)

    def getScore(self):
        value = self.value
        if self.value == 'A':
            value = 1
        elif self.value in ['J', 'Q', 'K']:
            value = 10
        return int(value)

    def sum(self, other):
        return (self.getScore() + other.getScore()) % 10

    def __lt__(self, rhs):

        fl0wer = ['club', 'diamond', 'heart', 'spade']

        out_of_number = ['', 'J', 'Q', 'K', 'A', '2']

        sscore = self.getScore() if not self.value in out_of_number else 10 + out_of_number.index(self.value)
        rscore = rhs.getScore() if not rhs.value in out_of_number else 10 + out_of_number.index(rhs.value)

        if sscore < rscore:
            return True
        elif sscore > rscore:
            return False

        if sscore == rscore:
            point1 = fl0wer.index(self.suit)
            point2 = fl0wer.index(rhs.suit)
            if point1 < point2:
                return True
                # return '({} {})'.format(sscore, self.suit)
            else:
                return False
                # return '({} {})'.format(rscore, rhs.suit)


n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))

for i in range(n):
    print(cards[i].getScore())
print('----------')
for i in range(n-1):
    print(Card.sum(cards[i], cards[i+1]))
print('----------')
cards.sort()
for i in range(n):
    print(cards[i])
