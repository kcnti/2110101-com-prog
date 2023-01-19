n = input()
tmp = 0
ntmp = 13
for i in n:
    tmp += int(i) * ntmp
    ntmp-=1
n12 = (11-(tmp)%11)%10
print("{} {} {} {} {}".format(n[0], n[1:5], n[5:10], n[10:], n12))