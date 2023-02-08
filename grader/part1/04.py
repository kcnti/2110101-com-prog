result = [x for x in input().strip()]
target = int(input())
total_score = 0
f = 0
newFrame = True
frames = []

for i in range(len(result)):
    if result[i] == 'X':
        result[i] = 10
    elif result[i] == '/':
        result[i] = 10-result[i-1]
    else:
        result[i] = int(result[i])

bprev = 0

for n, r in enumerate(result):
    tmp = 0
    if f == 10:
        break
    if r == 10:
        try:
            tmp += result[n+1] + result[n+2]
        except:
            tmp += result[n+1]
        f += 1
        frames.append(tmp + r)
    elif not newFrame:
        if result[n-1] + r == 10:
            tmp += result[n+1]
        f += 1
        newFrame = True
        bprev += tmp + r
        frames.append(bprev)
        bprev = 0
    else:
        bprev += tmp + r
        newFrame = False
    total_score += tmp + r

if not target in range(1, 10):
    print(total_score)
else:
    print(frames[target-1])