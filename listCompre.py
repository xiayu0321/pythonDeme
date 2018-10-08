L1 = ['Hello','World',18,'Apple',None]
L2 = [x.lower() for x in L1 if isinstance(x,str) == True]

print(L2)
if L2 == ['hello','world','apple']:
    print('successs')
else:
    print('false')
