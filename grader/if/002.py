d, m, y = [int(i) for i in input().split()]

y = y - 543
n = 31

yon = [4, 6, 9, 11]

if m in yon:
    n = 30
else:
    if m == 2:
        n = 28
        if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
            n = 29

d = d + 15

if d > n:
    d = d - n
    m = m + 1
if m > 12:
    m = m - 12
    y = y + 1

y = y + 543

print("{}/{}/{}".format(d, m, y))
