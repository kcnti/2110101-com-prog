method = input().strip()
n = int(input())
length = 0
strings = []
for i in range(n):
    s = input().strip()
    strings.append(s)

output = ""

if not all(len(i) == len(strings[0]) for i in strings):
    output = "Invalid size"
elif method == '90':
    for i in range(len(strings[0])):
        for j in range(n-1, -1, -1):
            output += strings[j][i]
        if i != len(strings[0])-1: output += '\n'
elif method == 'flip':
    for i in range(len(strings)):
        output += strings[i][::-1]
        if i != len(strings[0])-1: output += '\n'
elif method == '180':
    for i in range(len(strings)-1, -1, -1):
        output += strings[i][::-1]
        if i: output += '\n'
else:
    output = "Invalid size"

print(output)