def print_seats(assignments, n_rows, n_cols):
    d = ['--'] * (n_rows * n_cols)
    for i in assignments:
        d[i[1]-1] = i[0]
    cnt = n_cols
    for i in range(n_rows):
        print('|', ' | '.join(d[cnt-n_cols:cnt]), '|')
        cnt += n_cols
        
exec(input().strip())