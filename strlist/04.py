m = input()
n = int(input())

if len(m) > n: n = len(m)

print("{}".format(("0"*n+m)[-n:]))