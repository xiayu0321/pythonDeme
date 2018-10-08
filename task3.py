#! /usr/bin/env python3

age = int(input('your age:'))

if age > 18:
    print('your age is:',age)
    print('adult')
elif age > 6:
    print('your age is:%s'%age)
    print('teen')
else:
    print('kid')
