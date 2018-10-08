def fact(n):
    if n == 1:
        res = 1
    else:
        res = fact(n-1)*n
    return res
