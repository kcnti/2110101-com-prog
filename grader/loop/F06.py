def print_triangle(n):
    output = ""
    for i in range(n-1, 0, -1):
        mid_dot = '.'*(n-i-1+n-i-2)
        if len(mid_dot) == 1 and n < 3:
            mid_dot = " "
        if i == n-1:
            output += '.'*i + '*' + '\n'
        else:
            output += '.'*i + '*' + mid_dot + '*' + '\n'
            
    output += '*' * (2*n-1)

    print(output)

exec(input())

