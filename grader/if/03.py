a = [float(i) for i in input().split()]
a.sort()
print(round(sum(a[1:-1])/2, 2))


# if solution

# a = [float(i) for i in input().split()]
# MAX = a[0]
# MIN = a[0]

# for i in range(1, len(a)):
#     if a[i] > MAX:
#         MAX = a[i]
#     if a[i] < MIN:
#         MIN = a[i]

# a.remove(MAX)
# a.remove(MIN)
# print(round(sum(a)/2, 2))