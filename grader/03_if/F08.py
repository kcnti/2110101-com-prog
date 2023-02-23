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

exec(input())