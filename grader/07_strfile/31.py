dna = {
    'A': 'T',
    'G': 'C'
}

n = ''.join([i.upper() for i in input().strip()])
oper = input().strip()

for i in n:
    if not i.upper() in 'ATGC':
        oper = 0
        break

if oper == 'R':
    out = ''
    n = n[::-1]
    for i in n:
        for f, s in dna.items():
            if f == i:
                out += s
            elif s == i:
                out += f
    print(out)
elif oper == 'F':
    _dna = 'ATGC'
    print(', '.join([i+'='+str(n.count(i)) for i in _dna]))

elif oper == 'D':
    find = input().strip()
    c = 0
    for i in range(len(n)-1):
        if n[i] + n[i+1] == find:
            c += 1
    print(c)
else:
    print("Invalid DNA")