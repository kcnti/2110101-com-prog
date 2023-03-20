def factor(N):
    ans = []
    k = 2
    c = 0
    while(N > 1):
        if N%k != 0:
            if c != 0:
                ans.append([k, c])
            k += 1
            c = 0
            continue
        else:
            c += 1
        N /= k
        
    ans.append([k, c])
    return ans

exec(input().strip())