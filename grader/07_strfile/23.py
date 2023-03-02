filename, year = input().split()
f = [float(i.split()[1].replace('\n', '')) for i in open(filename, 'r').readlines() if i.split()[0][:2] == year[-2:]]

print(min(f), max(f), sum(f)/len(f)) if f else print('No data')