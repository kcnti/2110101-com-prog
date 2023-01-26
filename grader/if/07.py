n = int(input())

abbrev = {
    'K': range(4, 7),
    'M': range(7, 10),
    'B': range(10, 20)
}

length = len(str(n))
output = ""

for i in abbrev:
    if length in abbrev[i]:
        tmp = length - abbrev[i][0]
        if tmp >= 1:
            output = int(round(n/(10**(abbrev[i][0]-1)), 0))
        else:
            output = round(n/(10**(abbrev[i][0]-1)), 1)
        break

print("{}{}".format(output, i)) if output else print(n)