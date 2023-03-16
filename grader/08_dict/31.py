def total(pocket):
    out = 0
    for i in pocket:
        out += i*pocket[i]
    return out

def take(pocket, money_in):
    for i in money_in:
        if i in pocket:
            pocket[i] += money_in[i]
        else:
            pocket[i] = money_in[i]
    return pocket

def pay(pocket, amt):
    if amt > total(pocket):
        return {}
    out = {}
    for i in sorted(pocket, reverse=True):
        if (amt // i) * i >= pocket[i] * i:
            sale = pocket[i] * i
            amt -= sale
            out[i] = sale//i
        elif (amt // i) * i > 0:
            sale = (amt // i) * i
            amt -= sale
            out[i] = sale//i
    if amt > 0:
        return {}
    else:
        for i in out:
            pocket[i] -= out[i]
    return out

exec(input().strip())