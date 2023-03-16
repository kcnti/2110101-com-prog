def reverse(d):
    return {v: k for k, v in d.items()}

def keys(d, v):
    return [k for k, vl in d.items() if vl == v]

exec(input().strip())