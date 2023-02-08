import math
sum_p, sum_s, sum_fs = 0, 0, 0

for i in range(9):
    p, s, c = [int(i) for i in input().split()]
    fs = 0
    if c:
        fs = p + 2 if p+2 < s else s
    sum_p += p
    sum_s += s
    sum_fs += fs



additional_s = math.floor(0.8 * (1.5*sum_fs - sum_p))
total_s = sum_s - additional_s

print(sum_s)
print(additional_s)
print(total_s)