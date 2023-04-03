typos = []
names = []

while(1):
    n = input().strip()
    if n == 'q':
        break
    n = n.split(', ')
    name, typo = n[0], n[1]
    if typo in typos:
        p = typos.index(typo)
        names[p].append(name)
    else:
        typos.append(typo)
        names.append([name])

for i in range(len(typos)):
    print(typos[i] + ":", ', '.join(names[i]))

# result = {}

# while(1):
#     n = input().strip()
#     if n == 'q':
#         break
#     n = n.split(', ')
#     name = n[0]
#     typo = n[1]
#     if not typo in result:
#         result[typo] = [name]
#     else:
#         result[typo].append(name)

# for i in result:
#     print(i + ':', ', '.join(result[i]))