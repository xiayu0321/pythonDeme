L1 = ['Hello','World',18,'Apple',None]
L2 = []

for w in L1:
    if isinstance(w,str):
        L2.append(w)

print([w.lower() for w in L2])
