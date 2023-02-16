x = [int(i) for i in input().split()]
k = int(input())
out = []
c = 0
for i in range(c, len(x)):
    tmp = []
    for j in range(c, len(x)):
        if x[j] != x[c]:
            out.append(tmp)
            c = j
            break
        tmp.append(x[j])
    if i == len(x)-1:
        out.append(tmp)

print(sum([sum(i) for i in out if len(i) < k]))