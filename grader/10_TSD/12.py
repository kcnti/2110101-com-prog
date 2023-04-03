n = int(input())
if n == 0:
    print(0)
    print(0)
else:
    u = set(input().split())
    t = u
    for i in range(1, n):
        s = set(input().split())
        u = u.union(s)
        t.intersection_update(s)
        
    print(len(u))
    print(len(t))