def row_number(t, e):
    return [i for i in range(len(t)) if e in t[i]][0]

def flatten(t):
    out = []
    for i in t:
        for j in i:
            if j != 0:
                out.append(j)
    return out

def inversions(x):
    c = 0
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            if x[i] > x[j]:
                c += 1
    return c

def solvable(t):
    f = flatten(t)
    iv = inversions(f)
    if len(t)%2 and iv%2 == 0:
        return True
    elif len(t)%2 == 0:
        if iv%2 and row_number(t, 0)%2 == 0:
            return True
        elif iv%2 == 0 and row_number(t, 0)%2:
            return True
    return False

exec(input().strip())