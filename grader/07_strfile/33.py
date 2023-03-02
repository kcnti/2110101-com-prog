def sortFaculty(f):
    return int(f.split()[0][-2:])

f1, f2 = input().split()

f1 = open(f1, 'r').readlines()
f1[-1] += '\n'
f2 = open(f2, 'r').readlines()
f2[-1] += '\n'
file = f1 + f2

for i in range(len(file)):
    file[i] = file[i].strip()

print('\n'.join(sorted(sorted(file), key=sortFaculty)))