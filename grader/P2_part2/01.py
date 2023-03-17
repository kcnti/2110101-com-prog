def is_odd(n):
    return n % 2 == 1


def has_odds(x):
    return any(i%2 for i in x)


def all_odds(x):
    return all(i%2 for i in x)


def no_odds(x):
    return all(i%2==0 for i in x)


def get_odds(x):
    return [i for i in x if i%2]


def zip_odds(a, b):
    out = []
    cnt = 0
    select = 0 # 0 = a 1 = b
    a_idx = 0
    b_idx = 0
    while(cnt != len(a) + len(b)):
        if select == 0:
            if a_idx < len(a):
                if a[a_idx]%2:
                    out.append(a[a_idx])
                    select = 1
                a_idx += 1
                cnt += 1
            else:
                select = 1
        elif select == 1:
            if b_idx < len(b):
                if b[b_idx]%2:
                    out.append(b[b_idx])
                    select = 0
                b_idx += 1
                cnt += 1
            else:
                select = 0
    return out

exec(input().strip())
