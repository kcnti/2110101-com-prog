a = input().strip()
al = a.lower()
a_d = [[c, al.count(c)] for c in sorted(set(al)) if c.isalpha()]
b = input().strip()
bl = b.lower()
b_d = [[c, bl.count(c)] for c in sorted(set(bl)) if c.isalpha()]

acheck = 0
print(a)
for i in a_d:
    b_c = ""
    for c in b_d:
        if i[0] == c[0]:
            b_c = c
            break

    p = i[0]
    if b_c and i[1] > b_c[1]:
        dif = abs(i[1] - b_c[1])
        if dif > 1:
            p = i[0] + "'s"
        print(' - remove {} {}'.format(dif, p))
        acheck = 1
    elif not b_c:
        dif = i[1]
        if dif > 1:
            p = i[0] + "'s"
        print(' - remove {} {}'.format(dif, p))
        acheck = 1

if not acheck:
    print(' - None')

bcheck = 0
print(b)
for i in b_d:
    a_c = ""
    for c in a_d:
        if i[0].lower() == c[0].lower():
            a_c = c
            break

    if a_c and i[1] > a_c[1]:
        dif = abs(i[1] - a_c[1])
        if dif > 1: i[0] += "'s"
        print(' - remove {} {}'.format(dif, i[0]))
        bcheck = 1
    elif not a_c:
        dif = i[1]
        if dif > 1: i[0] += "'s"
        print(' - remove {} {}'.format(dif, i[0]))
        bcheck = 1
if not bcheck:
    print(' - None')

