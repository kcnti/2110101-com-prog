def convex_polygon_area(p):
    l, r = 0, 0
    p = p + [p[0]]
    for i in range(len(p)-1):
        l += p[i][0] * p[i+1][1]
        r += p[i][1] * p[i+1][0]

    return (1/2) * abs(l-r)

def is_heterogram(s):
    return all(s.lower().count(i.lower()) == 1 for i in s.replace(' ', '') if i.isalpha())

def replace_ignorecase(s, a, b):
    output = s
    c = 0
    while c < len(s):
        if output[c:c+len(a)].lower() == a.lower():
            output = output[:c] + b + output[c+len(a):]
            c += len(b)
        else:
            c += 1
    return output

def top3(votes):
    votes = sorted(sorted(votes.items()), key=lambda i:i[1], reverse=True)
    return [k[0] for k in votes][:3]


for k in range(2):
    exec(input().strip())
