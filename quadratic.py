import math

def quadratic(a,b,c):
    if b*b-4*a*c < 0:
        raise TypeError('number is not matched')
    elif b*b-4*a*c == 0:
        res1 = (-b + math.sqrt(b*b-4*a*c))/(2*a)
        res2 = res1
        return res1,res2
    else:
        res1 = (-b + math.sqrt(b*b-4*a*c))/(2*a)
        res2 = (-b - math.sqrt(b*b-4*a*c))/(2*a)
        return res1,res2
        

