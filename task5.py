#! /usr/bin/env python3

L = ['Bart','Lisa','Adam']
i = 0
for name in L:
    print('Hello,%s'%name)

print('--------------')
while( i < 3):
    print('hello,%s'%L[i])
    i = i + 1
print('--------------')
n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n + 1
print('END')
print('--------------')
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)
