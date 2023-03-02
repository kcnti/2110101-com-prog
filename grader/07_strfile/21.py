out = ''
while(1):
    n = input()
    if n == 'end':
        break
    for i in n:
        if not i.isalpha():
            out += i
        elif ord(i) > ord('M') and i.isupper():
            out += chr(ord(i) - 13)
        elif ord(i) > ord('m') and i.islower():
            out += chr(ord(i) - 13)
        else:
            out += chr(ord(i) + 13)
    out += '\n'

print(out)
