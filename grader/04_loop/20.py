redzig, bluezig = int(), int()
redzag, bluezag = int(), int()

c = 1

while(1):
    try:
        n = input().split()
        p = int(n[0])
        q = int(n[1])
        if c == 1:
            redzig, bluezig = p, q
            redzag, bluezag = q, p
        if c%2:
            redzig = min(p, redzig)
            bluezig = max(q, bluezig)
            redzag = min(q, redzag)
            bluezag = max(p, bluezag)
        else:
            redzig = min(q, redzig)
            bluezig = max(p, bluezig)
            redzag = min(p, redzag)
            bluezag = max(q, bluezag)
        c+=1
    except:
        if n[0] == 'Zig-Zag':
            print(redzig, bluezig)
        else:
            print(redzag, bluezag)
        break

