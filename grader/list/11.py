a = set([int(j) for j in input() if j.isdigit()])
out = [str(i) for i in range(10) if not i in a]
print(','.join(out)) if out else print('None')