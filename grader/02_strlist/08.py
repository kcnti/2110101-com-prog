# https://youtu.be/Ihws0d-WLzU

import math

n = input().split(',')

x = int(n[0] + n[1] + n[2]) - int(n[0] + n[1])
d = (10**(len(n[1])+len(n[2]))) - (10**len(n[1]))

gcd = math.gcd(x, d)

print(int(x//gcd), '/', int(d//gcd))