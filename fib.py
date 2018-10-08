def fib(max):
    n,a,b = 0, 0, 1

    while n < max:
        yield b
        t = b
        b = a + b
        a = t
        n = n + 1
    return 'done'

