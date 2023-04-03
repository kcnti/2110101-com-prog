n = int(input())

keyID = []
cityName = []

for i in range(n):
    p = input().strip().split(': ')
    keyID.append(p[0])
    cityName.append(p[1].split(', '))

target = input().strip()
t_target = cityName[keyID.index(target)]

output = []

for i in range(len(keyID)):
    for j in cityName[i]:
        if j in t_target and i != keyID.index(target) and not keyID[i] in output:
            output.append(keyID[i])
            print(keyID[i])

if not output:
    print('Not Found')

# data = {}

# for i in range(n):
#     p = input().strip().split(': ')
#     data[p[0]] = p[1].split(', ')

# target = input().strip()
# t_target = data[target]

# for i in t_target:
#     for j in data:
#         if i in data[j] and j != target:
#             print(j)