n = input()
ntmp = 13
tmp = sum([int(n[13-i])*i for i in range(ntmp, ntmp-len(n), -1)])
n12 = (11-(tmp)%11)%10
print("{} {} {} {} {}".format(n[0], n[1:5], n[5:10], n[10:], n12))