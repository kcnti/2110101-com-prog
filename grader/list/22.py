grades = ['F', 'D', 'D+', 'C', 'C+', 'B', 'B+', 'A']
ids = []
while(1):
    n = input().strip()
    if n == 'q':
        break
    student, grade = n.split()
    ids.append([int(student), grade])

uids = input().split()
ids.sort()
for i in ids:
    grade = i[1]
    if str(i[0]) in uids and grade != 'A':
        grade = grades[grades.index(grade) + 1]
    print(i[0], grade)