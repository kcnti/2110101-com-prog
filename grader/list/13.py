f = [int(input()) for i in range(int(input()))]
s = f + [int(i) for i in input().split()]
t = []
while(1):
    a = int(input())
    if a == -1: break
    s.append(a)
s.sort(reverse=True)
out = [s[i] for i in range(len(s)) if not i%2] + [s[-i] for i in range(len(s)) if i%2]

print(out) 

