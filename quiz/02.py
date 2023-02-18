AQI = [int(i) for i in input().split()]

output = "AQI|1 2 3 4 5\n-------------\n"

for n, i in enumerate(AQI):
    tmp = ""
    if i <= 25:
        tmp += "+" + "." * 8
    elif i > 25 and i <= 50:
        tmp += ".." + "+" + "." * 6
    elif i > 50 and i <= 100:
        tmp += "...." + "+" + "." * 4
    elif i > 100 and i < 200:
        tmp += "." * 6 + "+" + ".."
    elif i >= 200:
        tmp += "." * 8 + "+"
    output += "{}..|{}\n".format(n+1, tmp)

output += "-------------"

print(output)