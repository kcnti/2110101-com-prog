# HW02_Selection_Loop (ไม่ลบหรือแก้ไขบรรทัดนี้ หรือเพิ่มอะไรก่อนบรรทัดนี้ โดยเด็ดขาด)

#-----------------------------
# Riemann sum functions
#-----------------------------
def riemann_left(f, a, b, n):
    # คืนค่าเป็นจำนวนจริงของ Riemann sum โดยใช้ Left rule
    dx = (b - a)/n
    _sum = 0
    for i in range(1, n):
        _sum += f(a + (dx*(i-1)))
    _sum += f(b-dx)
    return dx * _sum

def riemann_right(f, a, b, n):
    # คืนค่าเป็นจำนวนจริงของ Riemann sum โดยใช้ Right rule
    dx = (b - a)/n
    _sum = 0
    for i in range(1, n):
        _sum += f(a + (dx*i))
    _sum += f(b)
    return dx * _sum

def riemann_mid(f, a, b, n):
    # คืนค่าเป็นจำนวนจริงของ Riemann sum โดยใช้ Midpoint rule
    dx = (b - a)/n
    _sum = 0
    for i in range(1, n):
        _sum += f(a + (dx*((i+(i-1))/2)))
    _sum += f(b - (dx/2))
    return dx * _sum

def riemann_trap(f, a, b, n):
    # คืนค่าเป็นจำนวนจริงของ Riemann sum โดยใช้ Trapezoid rule
    return (riemann_left(f, a, b, n) + riemann_right(f, a, b, n))/2

#-----------------------------
def estimate(riemann_sum_function, f, a, b, precision):
    # คืนค่าเป็นลิสต์ที่ประกอบด้วย
    #  - ค่าที่ประมาณ (เป็นจำนวนจริง) ของ Riemann sum ที่ใช้วิธีตาม riemann_sum_function ที่ส่งมา (ที่มีความแม่นยำตามที่ต้องการ)
    #  - จำนวนช่วงน้อยที่สุด (เป็นจำนวนเต็ม) ที่ใช้แบ่งเพื่อให้ได้ความแม่นยำตามที่ต้องการ (คืนค่า k เมื่อค่าทีประมาณได้จากการแบ่งเป็น k ช่วงและแบ่งเป็น k+1 ช่วง มีค่าไม่แตกต่างกันตามความแม่นยำที่ต้องการ)

    # ในฟังก์ชันนี้ จะเรียก riemann_sum_function(f, a, b, n) หลาย ๆ รอบ จนกว่าจะได้คำตอบตามที่กำหนด
    n = 1
    k = 0
    while(1):
        riemann_sum1 = riemann_sum_function(f, a, b, n)
        riemann_sum2 = riemann_sum_function(f, a, b, n+1)
        check1 = round(riemann_sum1, precision)
        check2 = round(riemann_sum2, precision)
        if check1 == check2:
            k = n
            break
        n+=1

    return [round(riemann_sum1, precision), k] # ห้ามลบหรือแก้ไขบรรทัดนี้


import math

def f1(x):
    return 0.5*(x**2)

def test_riemann_left_1():
    print('---riemann_left of math.sin---')
    x = riemann_left(math.sin, 0, 0.5*math.pi, 10)
    print(x, round(x, 10))
    x = riemann_left(math.sin, 0, 0.5*math.pi, 100)
    print(x, round(x, 10))
    x = riemann_left(math.sin, 0, 2*math.pi, 10)
    print(x, round(x, 10))
    x = riemann_left(math.sin, 0, 2*math.pi, 100)
    print(x, round(x, 10))

def test_riemann_left_2():
    print('---riemann_left of f1---')
    x = riemann_left(f1, 0, 4, 50)
    print(x, round(x, 10))
    x = riemann_left(f1, 0, 4, 500)
    print(x, round(x, 10))
    x = riemann_left(f1, 3, 10, 50)
    print(x, round(x, 10))
    x = riemann_left(f1, 3, 10, 500)
    print(x, round(x, 10))
#-----------------------------------------------------
def test_riemann_right_1():
    print('---riemann_right of math.sin---')
    x = riemann_right(math.sin, 0, 0.5*math.pi, 10)
    print(x, round(x, 10))
    x = riemann_right(math.sin, 0, 0.5*math.pi, 100)
    print(x, round(x, 10))
    x = riemann_right(math.sin, 0, 2*math.pi, 10)
    print(x, round(x, 10))
    x = riemann_right(math.sin, 0, 2*math.pi, 100)
    print(x, round(x, 10))

def test_riemann_right_2():
    print('---riemann_right of f1---')
    x = riemann_right(f1, 0, 4, 50)
    print(x, round(x, 10))
    x = riemann_right(f1, 0, 4, 500)
    print(x, round(x, 10))
    x = riemann_right(f1, 3, 10, 50)
    print(x, round(x, 10))
    x = riemann_right(f1, 3, 10, 500)
    print(x, round(x, 10))
#-----------------------------------------------------
def test_riemann_mid_1():
    print('---riemann_mid of math.sin---')
    x = riemann_mid(math.sin, 0, 0.5*math.pi, 10)
    print(x, round(x, 10))
    x = riemann_mid(math.sin, 0, 0.5*math.pi, 100)
    print(x, round(x, 10))
    x = riemann_mid(math.sin, 0, 2*math.pi, 10)
    print(x, round(x, 10))
    x = riemann_mid(math.sin, 0, 2*math.pi, 100)
    print(x, round(x, 10))

def test_riemann_mid_2():
    print('---riemann_mid of f1---')
    x = riemann_mid(f1, 0, 4, 50)
    print(x, round(x, 10))
    x = riemann_mid(f1, 0, 4, 500)
    print(x, round(x, 10))
    x = riemann_mid(f1, 3, 10, 50)
    print(x, round(x, 10))
    x = riemann_mid(f1, 3, 10, 500)
    print(x, round(x, 10))
#-----------------------------------------------------
def test_riemann_trap_1():
    print('---riemann_trap of math.sin---')
    x = riemann_trap(math.sin, 0, 0.5*math.pi, 10)
    print(x, round(x, 10))
    x = riemann_trap(math.sin, 0, 0.5*math.pi, 100)
    print(x, round(x, 10))
    x = riemann_trap(math.sin, 0, 2*math.pi, 10)
    print(x, round(x, 10))
    x = riemann_trap(math.sin, 0, 2*math.pi, 100)
    print(x, round(x, 10))

def test_riemann_trap_2():
    print('---riemann_trap of f1---')
    x = riemann_trap(f1, 0, 4, 50)
    print(x, round(x, 10))
    x = riemann_trap(f1, 0, 4, 500)
    print(x, round(x, 10))
    x = riemann_trap(f1, 3, 10, 50)
    print(x, round(x, 10))
    x = riemann_trap(f1, 3, 10, 500)
    print(x, round(x, 10))
#-----------------------------------------------------
def test_estimate_1():
    print('### test estimate of math.sin ###')
    print('---riemann_left---')
    for precision in [1, 3, 5, 7]:
        print(estimate(riemann_left, math.sin, 0, 0.5*math.pi, precision))
    print('---riemann_right---')
    for precision in [1, 3, 5, 7]:
        print(estimate(riemann_right, math.sin, 0, 0.5*math.pi, precision))
    print('---riemann_mid---')
    for precision in [1, 3, 5, 7]:
        print(estimate(riemann_mid, math.sin, 0, 0.5*math.pi, precision))
    print('---riemann_trap---')
    for precision in [1, 3, 5, 7]:
        print(estimate(riemann_trap, math.sin, 0, 0.5*math.pi, precision))
#-----------------------------------------------------
def test_estimate_2():
    print('### test estimate of f1 ###')
    print('---riemann_left---')
    for precision in [2, 4, 6]:
        print(estimate(riemann_left, f1, 2, 5, precision))
    print('---riemann_right---')
    for precision in [2, 4, 6]:
        print(estimate(riemann_right, f1, 2, 5, precision))
    print('---riemann_mid---')
    for precision in [2, 4, 6]:
        print(estimate(riemann_mid, f1, 2, 5, precision))
    print('---riemann_trap---')
    for precision in [2, 4, 6]:
        print(estimate(riemann_trap, f1, 2, 5, precision))
#-----------------------------------------------------
# ให้ uncomment testcase เพื่อทดสอบทีละอัน
# ถ้า run testcase ทั้งหมดจะใช้เวลานาน
# test_riemann_left_1()
# test_riemann_left_2()
# test_riemann_right_1()
# test_riemann_right_2()
# test_riemann_mid_1()
# test_riemann_mid_2()
test_riemann_trap_1()
# test_riemann_trap_2()
# test_estimate_1()
# test_estimate_2()

# print(riemann_left(math.sin, 0, 0.5*math.pi, 4))