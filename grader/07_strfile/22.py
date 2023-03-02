a = sorted([i.lower() for i in input() if i.isalnum()])
b = sorted([i.lower() for i in input() if i.isalnum()])

if a == b:
    print('YES')
else:
    print('NO')