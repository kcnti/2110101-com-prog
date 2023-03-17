n = int(input())
v = list()

for i in range(n):
    v.append([i.strip() for i in input().split()])

cmd = input().split()

if cmd[0] == "show":
    for i in v:
        print(' '.join(i))
if cmd[0] == "get":
    tmp = ""
    for i in v:
        if i[0] == cmd[1]:
            tmp = ' '.join(i)
            break
    print(cmd[1] + " not found") if not tmp else print(tmp)
if cmd[0] == "avg":
    tmp = 0
    for i in v:
        tmp += float(i[int(cmd[1])])
    print(round(tmp/len(v), 4))
if cmd[0] == "max":
    v.sort()
    for i in v:
        i[int(cmd[1])] = float(i[int(cmd[1])])
    m = max(v, key=lambda x:x[int(cmd[1])])
    print(m[0], m[int(cmd[1])])
if cmd[0] == "sort":
    v.sort()
    fruities = sorted(v, key=lambda x: x[int(cmd[1])])
    print(' '.join([i[0] for i in fruities]))