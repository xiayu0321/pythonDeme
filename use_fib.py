from fib import fib
g = fib(6)

while True:
    try:
        x = next(g)
        print('g',x)
    except StopIteraction as e:
        print('StopInteration',e.value)
        break
