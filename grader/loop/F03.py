def grade_mcq(c, s):
    score = 0
    if len(c) != len(s):
        score = -1
    else:
        for i in range(len(c)):
            if c[i] == s[i]:
                score+=1
    return score

exec(input())

