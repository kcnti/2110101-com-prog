def index_of(grades, ID):
    for i in grades:
        if i[0] == ID:
            return grades.index(i)
    return -1

def upgrade(grades, IDs):
    grade_letters = ['F', 'D', 'D+', 'C', 'C+', 'B', 'B+', 'A']
    grades.sort()
    for i in range(len(grades)):
        grade = grades[i][1]
        if str(grades[i][0]) in IDs and grade != 'A':
            grades[i][1] = grade_letters[grade_letters.index(grade) + 1]

exec(input())
exec(input())
exec(input())