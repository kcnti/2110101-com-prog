def to_Thai(N):
    tuaThai = {
        0: "soon",
        1: "neung",
        2: "song",
        3: "sam",
        4: "si",
        5: "ha",
        6: "hok",
        7: "chet",
        8: "paet",
        9: "kao",
        10: "sip",
        100: "roi",
        1000: "pun"
    }
    out = ""
    ised = "et" if N%10 == 1 and len(str(N)) > 1 else ""
    while(N >= 0):
        if N//1000 > 0:
            out += tuaThai[N//1000] + " " + tuaThai[1000] + " "
            N %= 1000
        elif N//100 > 0:
            out += tuaThai[N//100] + " " + tuaThai[100] + " "
            N %= 100
        elif N//10 > 0:
            if N//10 == 2:
                out += "yi" + " "
            elif N//10 == 1:
                pass
            else:
                out += tuaThai[N//10] + " "
            out += "sip" + " "
            N %= 10
        else:
            if ised:
                break
            if N == 0 and len(out) > 1:
                break
            out += tuaThai[N]
            break

    return out + ised


exec(input().strip())