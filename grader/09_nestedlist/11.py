n = int(input())

for i in range(n):
    p = input()
    if p.startswith('.'):
        cnt = 0
        for i in p:
            if i.isalnum():
                break
            cnt += 1
        print(p[cnt//2:])
    else:
        print(p)