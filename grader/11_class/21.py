class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        a = self.a
        b = self.b

        if a == 0:
            a = ''
            if abs(b) == 1:
                mark = ['', '', '-']
                b = mark[b] + 'i'
            elif b > 0:
                b = str(b) + 'i'
            elif b < 0:
                b = '-' + str(abs(b)) + 'i'
        if b == 0:
            b = ''
        elif type(b) != str:
            if abs(b) == 1:
                mark = ['', '+', '-']
                b = mark[b] + 'i'
            elif b > 0:
                b = '+' + str(b) + 'i'
            elif b < 0:
                b = '-' + str(abs(b)) + 'i'

        
        out = "{}{}".format(a, b)
        if not out:
            out = '0'
        return out

    def __add__(self, rhs):
        self.a += rhs.a
        self.b += rhs.b
        return self

    def __mul__(self, rhs):
        # (ac-bd) + (ad+bc)
        a = (self.a*rhs.a) - (self.b*rhs.b)
        b = (self.a*rhs.b) + (self.b*rhs.a)
        self.a = a
        self.b = b
        return self

    def __truediv__(self, rhs):
        a = ((self.a*rhs.a+self.b*rhs.b)/(rhs.a**2 + rhs.b**2))
        b = ((-self.a*rhs.b+self.b*rhs.a)/(rhs.a**2 + rhs.b**2))
        self.a = a
        self.b = b
        return self

t, a, b, c, d = [int(i) for i in input().split()]

c1 = Complex(a, b)
c2 = Complex(c, d)

if t == 1: print(c1)
elif t == 2: print(c2)
elif t == 3: print(c1+c2)
elif t == 4: print(c1*c2)
else: print(c1/c2)

