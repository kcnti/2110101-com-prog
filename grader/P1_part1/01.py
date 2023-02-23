from datetime import datetime

def cnvert(n):
    return datetime.strptime(' '.join(n.split()[1:]), "%B %d, %Y")

p1 = input()
p2 = input()
if p1.split()[1:] == p2.split()[1:]:
    print(p1.split()[0], p2.split()[0])
else:
    ans = {
        p1.split()[0]: cnvert(p1),
        p2.split()[0]: cnvert(p2)
    }

    print(min(ans, key=ans.get))