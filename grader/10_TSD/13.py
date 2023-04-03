n = int(input())

teams = {}

for i in range(n):
    p = input().split()
    teams[p[0] + '*' * i] = p[1]
    
win = list(teams.keys())
lose = list(teams.values())

result = []

for w in win:
    w = ''.join([i for i in w if i != '*'])
    
    if not w in lose and not w in result:
        result.append(w)

print(sorted(result))