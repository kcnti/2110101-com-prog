filename = input().strip()
f = [i.replace('\n', '').strip() for i in open(filename, 'r').readlines()]
code = f[0]
pattern = f[1]

prevclose = 0
prevchar = ""
char_dict = {}
morse_dict = {}
for i in range(1, len(pattern)):
    if pattern[i] == ']':
        prevchar = pattern[i-1]
        prevc = i
    if pattern[i] == '[':
        char_dict[prevchar] = pattern[prevc+1: i]
        morse_dict[pattern[prevc+1: i]] = prevchar

if code == "T2M":
    string = ''.join(i for i in pattern if i.isalpha())
    for i in f[2:]:
        checker = all(j in char_dict for j in i)
        if checker:
            tmp = ""
            for j in i:
                tmp += char_dict[j] + ' '
            print(tmp[:-1])
        else:
            print("Invalid : {}".format(i))
elif code == "M2T":
    for i in f[2:]:
        checker = all(j in morse_dict for j in i.split())
        if checker:
            print(''.join(morse_dict[j] for j in i.split()))
        else:
            print("Invalid : {}".format(i))

else:
    print("Invalid code")