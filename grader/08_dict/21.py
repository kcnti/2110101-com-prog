s = input().lower().strip()
f = sorted([[-s.count(i), i] for i in set(s) if i.isalpha()])

for cnt, c in f:
    print(c, '->', -cnt)