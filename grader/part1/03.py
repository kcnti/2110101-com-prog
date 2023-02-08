rsp_rule = {
    "P": "R",
    "R": "S",
    "S": "P"
}

class RSP():
    def __init__(self):
        self.p1 = 0
        self.p2 = 0
    def fight(self, p1, p2):
        if rsp_rule[p1] == p2:
            self.p1 += 1
        elif rsp_rule[p2] == p1:
            self.p2 += 1
    def getScore(self):
        return self.p1, self.p2

m = int(input())
rsp = RSP()


for i in range(0, m*3):
    p1, p2 = input().split()
    rsp.fight(p1, p2)
    p1, p2 = rsp.getScore()
    if i == m*3-1 and (p1 != m and p2 != m):
        print(p1, p2)
        print("Tie")
        break
    if p1 == m:
        print(p1, p2)
        print("Player 1 wins")
        break
    if p2 == m:
        print(p1, p2)
        print("Player 2 wins")
        break
