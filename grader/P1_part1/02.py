def str2RLE(n):
    import re
    r = [sub[1] + sub[0] for sub in re.findall(r"(.)(\1*)", n)]
    ans = ""
    for i in r:
        ans += '{} {} '.format(i[0], len(i))
    return ans.strip()

def RLE2str(n):
    n = n.split()
    ans = ''
    for i in range(0, len(n), 2):
        ans += n[i] * int(n[i+1])
    return ans


try:
    func = input()
    if not func in ['RLE2str', 'str2RLE']:
        raise
    string = input()
    exec("print({}('{}'))".format(func, string))
except:
    print("Error")
