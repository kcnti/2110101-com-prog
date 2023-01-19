def check_digit(n):
    ntmp = 13
    tmp = sum([int(n[13-i])*i for i in range(ntmp, ntmp-len(n), -1)])
    n12 = (11-(tmp)%11)%10
    return n12

exec(input())