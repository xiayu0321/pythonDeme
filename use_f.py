from f import f1
from f import f2

f1(1,2)
f1(1,2,c = 3)
f1(1,2,3,'a','b')
f2(1,2,d = 99,ext=None)

args = (1,2,3,4)
kw = {'d':99,'x':'#'}
f1(*args,**kw)

args = (1,2,3)
kw ={'d':88,'x':'#'}
f2(*args,**kw)
