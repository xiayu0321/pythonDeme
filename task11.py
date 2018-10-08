#! usr/bin/env python3
import math

def quadratic(a,b,c):
    if b * b - 4 * a * c < 0:
        return False;
    else:
        r1 = (-b + math.sqrt(b * b - 4 * a * c))/(2 * a)
        r2 = (-b - math.sqrt(b * b - 4 * a * c))/(2 * a)
        return r1,r2
