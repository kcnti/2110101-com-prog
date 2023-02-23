p = float(input())
k, t = 1, 1
while(1):
    t = (t*(365-(k-1)))/365
    if 1-t >= p:
        break
    k+=1

print(k)