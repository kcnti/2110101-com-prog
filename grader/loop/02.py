a = float(input())
L = 0
U = a
answer = L+U
x = answer/2

while(abs(a-(10**x)) > ((10**(-10))*max(a, (10**x)))):
    if 10**x > a:
        U = x
    if 10**x < a:
        L = x
    x = (L+U)/2

print(round(x, 6))
