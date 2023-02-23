init = 0
step = 0
next = 0
n = int(input())

w = []

queue = {}

pcomm = ''

for i in range(n):
    command = input().split()
    if command[0] == 'reset':
        init = int(command[1])
        step = init
        next = init
    elif command[0] == 'new':
        queue[step] = int(command[1])
        print('ticket', step)
        step += 1
    elif command[0] == 'next':
        print('call', next)
        next += 1
        if pcomm == 'next':
            init += 1
    elif command[0] == 'order':
        time = int(command[1]) - queue[next-1]
        print('qtime', next-1, time)
        init += 1
        w.append(time)
    elif command[0] == 'avg_qtime':
        print('avg_qtime', sum(w)/len(w))
    # print(queue)
    pcomm = command[0]