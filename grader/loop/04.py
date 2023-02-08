parentheses = {
    "(": "[",
    "[": "(",
    ")": "]",
    "]": ")"
}

n = input()
c = 0

for i in range(len(n)):
    if n[i] in parentheses:
        n = n[:i] + parentheses[n[i]] + n[i+1:]
        c+=1

print(n)