import math

def mosteller(w, h):
    return math.sqrt(w*h)/60

def du_bois(w, h):
    return 0.007184 * (w**0.425) * (h**0.725)

def fujimoto(w, h):
    return 0.008883 * (w**0.444) * (h**0.663)

def main():
    w = float(input())
    h = float(input())

    a = mosteller(w, h)
    b = du_bois(w, h)
    c = fujimoto(w, h)

    print("Mosteller =", round(a, 5))
    print("Du Bois =", round(b, 5))
    print("Fujimoto =", round(c, 5))

exec(input())