f = [int(input()) for i in range(int(input()))] + [int(i) for i in input().split()]
while(1):
    a = int(input())
    if a == -1: break
    f.append(a)

out = []
for i in range(len(f)):
    out.insert(0, f[i]) if i%2 else out.append(f[i])

print(out)