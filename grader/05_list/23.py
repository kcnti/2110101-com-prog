n = int(input())
dist = []
for i in range(n):
    x, y = [float(i) for i in input().split()]
    dist.append([((x**2+y**2))**(1/2), i+1, (x, y)])
dist.sort()
print("#{}: {}".format(dist[2][1], dist[2][-1]))