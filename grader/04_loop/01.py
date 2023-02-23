data = []

while(1):
    n = input()
    if n == 'q':
        break
    data.append(float(n))

if data:
    print(round(sum(data)/len(data), 2))
else:
    print('No Data')