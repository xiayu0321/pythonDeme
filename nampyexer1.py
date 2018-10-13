import numpy as np

a = np.array([1,2,3])
print(type(a),a.shape,a[0])
a[0] = 5
print(a)

c = np.ones((1,2))
print(c)

d = np.eye(2)
print(d)
