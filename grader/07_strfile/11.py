changes = {
    'x': 'xes',
    's': 'ses',
    'ch': 'ches',
    'y': 'ies'
}

n = input()
flag = 0
for i in changes:
    if n.endswith(i):
        if i == 'ch':
            n = n[:-2] + changes[i]
        elif i == 'y' and not n[-2] in ['a', 'e', 'i', 'o', 'u']:
            n = n[:-1] + changes[i]
        elif i != 'y':
            n = n[:-1] + changes[i]
        else:
            continue
        flag = 1
        break

if not flag:
    print(n + 's')
else:
    print(n)