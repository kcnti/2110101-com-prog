a = input().strip()
al = a.lower()
a_d = {c:al.count(c) for c in sorted(set(al)) if c.isalpha()}
b = input().strip()
bl = b.lower()
b_d = {c:bl.count(c) for c in sorted(set(bl)) if c.isalpha()}

acheck = 0
print(a)
for i in a_d:
    if i in b_d and a_d[i] > b_d[i]:
        dif = abs(a_d[i] - b_d[i])
        if dif > 1: i += "'s"
        print(' - remove {} {}'.format(dif, i))
        acheck = 1
    if not i in b_d:
        dif = a_d[i]
        if dif > 1: i += "'s"
        print(' - remove {} {}'.format(dif, i))
        acheck = 1

if not acheck:
    print(' - None')

bcheck = 0
print(b)
for i in b_d:
    if i in a_d and b_d[i] > a_d[i]:
        dif = abs(a_d[i] - b_d[i])
        if dif > 1: i += "'s"
        print(' - remove {} {}'.format(dif, i))
        bcheck = 1
    if not i in a_d:
        dif = b_d[i]
        if dif > 1: i += "'s"
        print(' - remove {} {}'.format(dif, i))
        bcheck = 1
if not bcheck:
    print(' - None')

