sports_data = {}

while(1):
    p = input().strip().split()
    if len(p) == 1:
        break
    sports_data[p[0]] = int(p[1])

data = {}

while(1):
    p = input().strip().split()
    if len(p) == 1:
        break
    if p[1] in data:
        if p[0] in data[p[1]]:
            [data[p[1]][p[0]].append(i) for i in p[2].split(',')]
        else:
            data[p[1]][p[0]] = [i for i in p[2].split(',')]
    else:
        data[p[1]] = {p[0]: [i for i in p[2].split(',')]}

result = {}

for i in sports_data:
    for j in data: # faculty
        for k in data[j]: # name
            if i in data[j][k]:
                if not i in result:
                    result[i] = {}
                    result[i][j] = 1
                else:
                    if not j in result[i]:
                        result[i][j] = 1
                    else:
                        result[i][j] += 1

for i in sorted(sports_data):
    max_per_team = sports_data[i]
    out = i + ":"
    if i in result:
        for j in sorted(result[i]):
            if result[i][j]//max_per_team == 0:
                continue
            out += "{}({},{})".format(j, result[i][j]//max_per_team, result[i][j]%max_per_team)
    print(out)