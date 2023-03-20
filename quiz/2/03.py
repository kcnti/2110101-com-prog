def complex_replace(s, k_strs, r_strs):
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if s[i:j] in k_strs:
                return s[:i] + "<" + r_strs[k_strs.index(s[i:j])] + ">" + s[j:]
    return s
    
exec(input())











    # this is what I did on the quiz day
    # new_s = s.split()
    # p = 0
    # out = ""
    # for no, i in enumerate(new_s):
    #     if p:
    #         out += " " + ' '.join(new_s[no:])
    #         break
    #     for n, j in enumerate(k_strs):
    #         if j in i:
    #             if len(i) > 1:
    #                 for a in range(len(i)):    
    #                     if i[a:len(j)+a] == j:
    #                         out += i[:a] + "<" + r_strs[n] + ">" + i[len(j)+a:]
    #                         p = 1
    #             else:
    #                 for k in range(len(i)):
                        
    #                     if j == i[k]:
    #                         out += i[:k] + '<' + r_strs[n] + '>' + i[k+1:]
    #                         p = 1
    #                         break
    #             if p:
    #                 break
    #     if not p:
    #         out += i + ' '
        
    # return out.strip() if out else s