def is_odd(n):
    if(n % 2 != 0):
        return True

L = list(filter(is_odd,[1,2,3,4,5,6,7,8,9,10,11]))
for x in L:
    print(x)
