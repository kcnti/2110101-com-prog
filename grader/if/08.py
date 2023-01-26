d, m, y = [''.join([i for i in input()]) for j in range(3)]

y = int(y) - 543

n = 28
if (int(y) % 400 == 0) or (int(y) % 4 == 0 and int(y) % 100 != 0):
    n = 29

out = 0

yon = [4, 6, 9, 11]

for i in range(1, int(m)):
    if i == 2:
        out += n
    elif i in yon:
        out += 30
    else:
        out += 31

out = out+int(d)
print(out)