#! usr/bin/env python3

def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('error operand type')
    if x >= 0:
        return x
    else:
        return -x


