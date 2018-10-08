def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 2
    print('step 3')
    yield 3
o = odd()
next(o)
print('123')
next(o)
print('456')
next(o)
print('789')
