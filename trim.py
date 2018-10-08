def trim(s):
    if s == '':
        pass
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]

    return s
