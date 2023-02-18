def distance1(x1, y1, x2, y2):
    return (((x2-x1)**2) + ((y2-y1)**2))**(1/2)

def distance2(p1, p2):
    return (((p1[0]-p2[0])**2) + ((p1[1]-p2[1])**2))**(1/2)

def distance3(c1, c2):
    distance = distance2(c1[:2], c2[:2])
    overlap = False
    if distance <= c1[-1] + c2[-1]:
        overlap = True
    return distance, overlap

def perimeter(points):
    total_d = 0
    for i in range(len(points)-1):
        total_d += distance2(points[i], points[i+1])
    total_d += distance2(points[0], points[-1])
    return total_d

exec(input().strip())