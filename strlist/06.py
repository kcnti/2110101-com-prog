u = list(map(float, input().strip('][').split(', ')))
v = list(map(float, input().strip('][').split(', ')))

n = [u[i]+v[i] for i in range(len(u))]

print("{} + {} = {}".format(u, v, n))