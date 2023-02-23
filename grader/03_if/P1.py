import math

def leapyear(y):
    y = y - 543
    n = 365
    if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
        n = 366
    return n

def day_of_year(d, m, y):
    y = y - 543
    n = 28
    if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
        n = 29
    out = 0
    yon = [4, 6, 9, 11]

    for i in range(1, m):
        if i == 2:
            out += n
        elif i in yon:
            out += 30
        else:
            out += 31

    out = out+int(d)
    return out

bd, bm, by, d, m, y = [int(e) for e in input().split()]

dbd = leapyear(by) - day_of_year(bd, bm, by) + 1
dy = max(0, y-by-1)

dy = 365*dy

dd = day_of_year(d, m, y) - 1

t = dbd + dy + dd

p = lambda n: math.sin((2*math.pi*t)/n)

physical = p(23)
emotional = p(28)
intellectual = p(33)

print("{} {:.2f} {:.2f} {:.2f}".format(t, physical, emotional, intellectual))