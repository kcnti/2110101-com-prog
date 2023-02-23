student1, student2 = [[i for i in input().split()] for j in range(2)]

if (student1[2] > 'A' or student1[3] > 'C' or student1[4] > 'C') and (student2[2] > 'A' or student2[3] > 'C' or student2[4] > 'C'):
    print('None')
elif student1[2] > 'A' or student1[3] > 'C' or student1[4] > 'C':
    print(student2[0])
elif student2[2] > 'A' or student2[3] > 'C' or student2[4] > 'C':
    print(student1[0])

elif student1[1:] == student2[1:]:
    print('Both')

elif student1[1] == student2[1] and student1[3] < student2[3]:
    print(student1[0])
elif student1[1] == student2[1] and student1[3] > student2[3]:
    print(student2[0])

elif student1[1:3] == student2[1:3] and student1[-1] < student2[-1]:
    print(student1[0])
elif student1[1:3] == student2[1:3] and student1[-1] > student2[-1]:
    print(student2[0])

elif student1[1] > student2[1]:
    print(student1[0])
elif student1[1] < student2[1]:
    print(student2[0])
