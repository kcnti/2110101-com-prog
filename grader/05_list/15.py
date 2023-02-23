def withSet():
    n = list(set(sorted([int(i) for i in input().split()])))
    print(len(n))
    print(n[:10]) if len(n) > 10 else print(n)

from collections import OrderedDict

result = sorted(list(OrderedDict.fromkeys([int(i) for i in input().split()])) )
print(len(result))
print(result[:10])