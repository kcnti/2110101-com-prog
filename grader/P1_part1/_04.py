result = [x for x in input().strip()]
target = int(input())
total_score = 0
f = 0
newFrame = True

for i in range(len(result)):
    if result[i] == 'X':
        result[i] = 10
    elif result[i] == '/':
        result[i] = 10-result[i-1]
    else:
        result[i] = int(result[i])

for n, r in enumerate(result):
    tmp = 0
    if f == 10:
        print(total_score)
        break
    if r == 10:
        tmp += result[n+1] + result[n+2]
        f += 1
    elif not newFrame:
        if result[n-1] + r == 10:
            tmp += result[n+1]
        f += 1
        newFrame = True
    else:
        newFrame = False
    if f == target:
        print(r + tmp)
        break
    total_score += tmp + r

