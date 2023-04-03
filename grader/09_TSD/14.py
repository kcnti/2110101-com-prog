courses = open(input().strip(), 'r').readlines()
teachers = open(input().strip(), 'r').readlines()
database = open(input().strip(), 'r').readlines()

new_courses = {}

for course in courses:
    p = course.replace('\n', '').split(',')
    new_courses[p[0]] = p[1]

for i in database:
    t = 0
    p = i.replace('\n', '').split(',')
    if not p[0] in new_courses:
        print('record error')
        continue
    for j in teachers:
        q = j.replace('\n', '').split(',')
        if q[0] == p[1]:
            t = 1
            print(new_courses[p[0]] + ',' + q[1])
    if not t:
        print('record error')