def knows(R, x, y):
    return y in R[x]

def is_celeb(R, x):
    for i in R:
        if knows(R, x, i):
            if x in R[i] and len(R[i]) == 1:
                continue
            return False
        elif not x in R[i] and R[i]:
            return False
    return True
        
def find_celeb(R):
    for i in R:
        if is_celeb(R, i):
            return i
    return None

def read_relations():
    R = dict()
    names = set()
    while(1):
        d = input().split()
        if len(d) == 1:
            for i in names:
                if not i in R:
                    R[i] = set()
            break
        if not d[0] in R:
            R[d[0]] = {d[1]}
        else:
            R[d[0]].add(d[1])
        names.add(d[1])
    return R

def main():
    R = read_relations()
    c = find_celeb(R)
    if c == None:
        print("Not Found")
    else:
        print(c)


exec(input().strip())