def missing_digits(t):
    a = set([int(j) for j in t if j.isdigit()])
    out = [i for i in range(10) if not i in a]
    return out

exec(input())