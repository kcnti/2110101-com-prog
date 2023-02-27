a, b, c, d = [int(i) for i in input().split()]

if d > a:
    n = 0
    while a < d:
        n = n + 1
        a = a + abs(b)
        d = d - abs(c)
    print(n, a, d)
    
else:
    a, d = d, a
    if a > b:
        a, b = b, a
    if c > d:
        c, d = d, c
    if b == c:
        print(a, b, d)
    elif b > c:
        print((b+c)/2)
    else:
        print(a,b,c,d)