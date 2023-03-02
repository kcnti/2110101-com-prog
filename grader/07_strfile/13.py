n = input()
for i in n:
    if not i.isalnum() and n != ' ':
        n = n.replace(i, ' ')

n = n.split()

converted = "".join(i[0].upper() + i[1:].lower() for i in n[1:])
print(n[0].lower() + converted)