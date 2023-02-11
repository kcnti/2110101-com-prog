n = int(input())
ans = [str(n)]

while n!=1:
    if not n%2:
        n = n // 2
    else:
        n = 3 * n + 1
    ans.append(str(n))

print('->'.join(ans[-15:]))