import numpy as np

def read_data():
    w = [float(e) for e in input().split()]
    weight = np.array(w)
    n = int(input())
    data = np.ndarray((n, 4), int)
    for i in range(n):
        data[i] = [int(e) for e in input().split()]
    return weight, data

def report_lower_than_mean(weight, data):
    students = []
    total_avg_score = np.sum(data[:, 1:] * weight) / (data[:, 1:].shape[0] * data[:, 1:].shape[1])
    for i in data:
        avg_score = sum(i[1:] * weight / weight.shape[0])
        if avg_score < total_avg_score:
            students.append(str(i[0]))
    print(', '.join(students)) if students else print(None)

# print(read_data())
exec(input().strip())
