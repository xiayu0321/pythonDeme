import timeit

sum_by_for = """
for d in data:
    s += d
"""

sum_by_sum = """
sum(data)
"""

sum_by_numpy_sum ="""
import numpy
numpy.sun(data)
"""

def timeit_using_list(n,loops):
    array_setup = """
data = [1] * {}
s = 0
""".format(n)
    print('array result:')
    print(timeit.timeit(sum_by_for,array_setup,number = loops))
    print(timeit.timeit(sum_by_sum,array_setup,numner = loops))
    print(timeit.timeit(sum_by_numpy_sum,arraysetup,number=loops))
