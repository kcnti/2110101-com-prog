def match(s, cs):
    new_cs = []
    previous_open = 0
    skip = 0
    for i in range(len(cs)):
        if cs[i] == '[':
            previous_open = i
            skip = 1
        elif cs[i] == ']':
            new_cs.append(''.join(cs[previous_open: i]))
            skip = 0
        elif cs[i] == '(':
            previous_open = i
            skip = 1
        elif cs[i] == ')':
            new_cs.append(''.join(cs[previous_open: i]))
            skip = 0
        elif not skip:
            new_cs.append(cs[i])

    if len(s) != len(new_cs):
        return False
    if s == ''.join(cs):
        return True
    
    for i in range(len(s)):
        if not s[i].isalnum():
            return False
        elif new_cs[i] == "?":
            continue
        elif new_cs[i][0] == '[':
            if not s[i] in new_cs[i][1:]:
                return False
        elif new_cs[i][0] == '(':
            if s[i] in new_cs[i][1:]:
                return False
        elif new_cs[i] != s[i]:
            return False
    return True

exec(input())












# wrong
    # for i in range(len(s)):
    #     if not s[i].isalnum():
    #         return False
    #     elif new_cs[i] == "?" and not s[i].isalnum():
    #         return False
    #     elif new_cs[i][0] == '[':
    #         if not s[i] in new_cs[i][1:] and not s[i].isalnum():
    #             return False
    #     elif new_cs[i][0] == '(':
    #         if s[i] in new_cs[i][1:] and not s[i].isalnum():
    #             return False
    # return True