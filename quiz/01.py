def rotate_left(s, n):
    return s[n:] + s[:n]

def rotate_right(s, n):
    return s[len(s)-1:] + s[:len(s)-1]

def str_mod(s, n):
    output = ""
    for i in s:
        output += str(int(i)%n)
    return output

def main():
    s = input()
    tmp = int(s[-2])
    if tmp == 1:
        print(rotate_left(s, tmp))
    elif tmp == 2:
        print(rotate_right(s, tmp))
    elif tmp == 3:
        print(len(s))
    else:
        print(s)