def RLE(t):
    import re
    r = [[sub[0], len(sub[1] + sub[0])] for sub in re.findall(r"(.)(\1*)", t)]
    return r

exec(input())