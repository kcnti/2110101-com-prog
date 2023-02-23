def is_prime(n):
    if n <= 1: return False
    for i in range(2, int(n**0.5)+1):
        if not n%i:
            return False
    return True

def next_prime(N):
    N = N + 1
    while(not is_prime(N)):
        N+=1
    return N

def next_twin_prime(N):
    out = ()
    c = 0
    N = N + 1
    while(len(out) <= 2):
        if is_prime(N) and N-c == 2:
            out = (c, N)
            break
        if is_prime(N):
            c = N
        N+=1
    return out

exec(input().strip())