import re
p = input()
r = [sub[1] + sub[0] for sub in re.findall(r"(.)(\1*)", p)]
ans = ""
for i in r:
    ans += '{} {} '.format(i[0], len(i))
print(ans.strip())