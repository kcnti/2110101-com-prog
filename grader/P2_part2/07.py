balls = {
    "R": 6,
    "Y": 1,
    "G": 1,
    "W": 1,
    "B": 1,
    "P": 1,
    "K": 1
}

color_score = ["X", "R", "Y", "G", "W", "B", "P", "K"]

players = [0, 0]

while(sum(list(balls.values())) > 0):
    n = input().strip()
    player, ball1 = n[0], n[1]
    if ball1 == "X":
        continue
    if ball1 == "R":
        players[int(player)-1] += 1 + color_score.index(n[2])
        balls["R"] -= 1
    else:
        players[int(player)-1] += color_score.index(ball1)
        balls[ball1] -= 1

print(" ".join([str(i) for i in players]))
if players[0] > players[1]:
    print("Player 1 wins")
elif players[0] == players[1]:
    print('Tie')
else:
    print("Player 2 wins")