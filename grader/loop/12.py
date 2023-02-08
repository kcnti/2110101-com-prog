def zigazig(x, y):
    red = []
    blue = []
    for i in range(len(x)):
        if (i+1)%2:
            red.append(x[i])
            blue.append(y[i])
        else:
            red.append(y[i])
            blue.append(x[i])
    return red, blue

x = []
y = []

n = int(input())
for i in range(n):
    p = input().split()
    x.append(int(p[0]))
    y.append(int(p[1]))

q = input()

if q == "Zig-Zag":
    red, blue = zigazig(x, y)
    print(min(red), max(blue))
else:
    red, blue = zigazig(y, x)
    print(min(red), max(blue))