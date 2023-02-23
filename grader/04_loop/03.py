c = input()
s = input()
score = 0

if len(c) != len(s):
    print('Incomplete answer')
else:
    for i in range(len(c)):
        if c[i] == s[i]:
            score+=1
    print(score)
