grades = ['F', 'D', 'D+', 'C', 'C+', 'B', 'B+', 'A']
ids = []
student_grades = []
while(1):
    n = input().strip()
    if n == 'q':
        break
    student, grade = n.split()
    ids.append(student)
    student_grades.append(grade)

uids = input().split()
out = []
for i in ids:
    grade = student_grades[ids.index(i)]
    if i in uids and grade != 'A':
        grade = grades[grades.index(grade) + 1]
    print(i, grade)