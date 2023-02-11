def peaks(x):
    n = [int(i) for i in x]
    ans = []
    for i in range(1, len(n)-1):
        if n[i] > n[i-1] and n[i] > n[i+1]:
            ans.append(i)
    return ans

exec(input())