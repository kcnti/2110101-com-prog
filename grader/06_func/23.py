def make_int_list(x):
    return list(map(int, x.split()))

def is_odd(e):
    return True if e%2 else False

def odd_list(alist):
    return [i for i in alist if i%2]

def sum_square(alist):
    return sum([i*i for i in alist])

exec(input().strip()) 