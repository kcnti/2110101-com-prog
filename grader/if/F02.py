def choose(student1, student2):
    if (student1[2] > 'A' or student1[3] > 'C' or student1[4] > 'C') and (student2[2] > 'A' or student2[3] > 'C' or student2[4] > 'C'):
        return []
    elif student1[2] > 'A' or student1[3] > 'C' or student1[4] > 'C':
        return [student2[0]]
    elif student2[2] > 'A' or student2[3] > 'C' or student2[4] > 'C':
        return [student1[0]]

    elif student1[1:] == student2[1:]:
        return [student1[0], student2[0]]

    elif student1[1] == student2[1] and student1[3] < student2[3]:
        return [student1[0]]
    elif student1[1] == student2[1] and student1[3] > student2[3]:
        return [student2[0]]

    elif student1[1:3] == student2[1:3] and student1[-1] < student2[-1]:
        return [student1[0]]
    elif student1[1:3] == student2[1:3] and student1[-1] > student2[-1]:
        return [student2[0]]

    elif student1[1] > student2[1]:
        return [student1[0]]
    elif student1[1] < student2[1]:
        return [student2[0]]

exec(input())