special_char = ['"', '(', ')', ',', '.', '\'']

p = input().strip()
q = input().strip()
for i in special_char:
    q = q.replace(i, ' ')
q = q.split()
print(len([i for i in q if i == p]))