n = int(input())
ppl = []
tmp = []
while(1):
    p = input().strip()
    if p == "Q":
        break
    p = p.split()
    ppl.append([p[0], int(p[1])])
    tmp.append([p[0], 0])

k = 0

while(n > 0):
    if tmp[k][1] == ppl[k][1]:
        k = (k+1) % len(ppl)
        continue
    if tmp[k][1] < ppl[k][1]:
        tmp[k][1] += 1
    n -= 1
    k = (k+1) % len(ppl)
    

for i in tmp:
    print(' '.join([str(j) for j in i]))