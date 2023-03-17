filename = input()
pattern = input().lower()
changeTo = input()
# filename = "data.txt"
# pattern = "T?m?".lower()
# changeTo = "Python"

match_idx = [i for i in range(len(pattern)) if pattern[i] != "?"]

data = [i.replace('\n', '') for i in open(filename, 'r').readlines()]
lst = []
for d in data:
    tmp = []
    text = ""
    for c in d:
        if c != '/':
            text += c
        elif text:
            tmp.append(text.strip())
            tmp.append('/')
            text = ""
        else:
            tmp.append('/')
    if text:
        tmp.append(text.strip())
    lst.append(tmp)

for i in range(len(lst)):
    for j in range(len(lst[i])-1):
        if len(lst[i][j]) == len(pattern):
            checker = all(lst[i][j][k].lower() == pattern[k] for k in match_idx)
            if checker and lst[i][j+1] == "/":
                lst[i][j] = changeTo

for i in lst:
    out = ""
    for j in range(len(i)):
        out += i[j]
    print(out)




# Bruh

# output = i
# for j in range(0, len(i)-len(pattern)):
#     tmp = i[j:j+len(pattern)]
#     checker = all(k for k in match_idx if tmp[k].lower() == pattern[k])
#     if not checker and i[j+len(pattern)] == '/':
#         output = output.replace(tmp, changeTo)
# print(output)