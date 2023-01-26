n = input()

f = n[3] + n[10] + n[17] + n[24] + n[31]

s = n[7] + n[12] + n[17] + n[22] + n[27]

t = int(f) + int(s) + 10000

ft = str((t//1000)%10) + str((t//100)%10) + str((t//10)%10)

fv = (sum([int(i) for i in str(ft)])%10) + 1

alpha = 'ABCDEFGHIJ'

print(ft + alpha[fv-1])