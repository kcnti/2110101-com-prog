n = int(input().strip())

def convert(t):
    t = t.split(':')
    return int(t[0]) * 60 + int(t[1])

def rev_convert(t):
    minutes = t//60
    seconds = "0" + str(t%60)
    return '{}:{}'.format(minutes, seconds[-2::])

result = {}

for i in range(n):
    p = input().strip().split(', ')
    music_type = p[-2]
    time = p[-1]

    if not music_type in result:
        result[music_type] = convert(time)
    else:
        result[music_type] += convert(time)

result = sorted(result.items(), key=lambda x: x[1], reverse=True)

c = 0

for i in result:
    if c == 3:
        break
    time = rev_convert(i[1])
    print(i[0] + ' --> ' + time)
    c += 1