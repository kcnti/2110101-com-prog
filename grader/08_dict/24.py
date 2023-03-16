key_pad = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
    '0': ' '
}

def text2keys(text):
    out = ''
    for i in text.lower():
        for key, alpha in key_pad.items():
            if i in alpha:
                out += key * (alpha.index(i) + 1) + ' '
    return out.strip()

def keys2text(keys):
    out = ''
    keys = keys.split()
    for i in keys:
        out += key_pad[i[0]][len(i)-1]
    return out

exec(input().strip())