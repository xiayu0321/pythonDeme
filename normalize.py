

def normalize(name):
    first = name[0].upper()
    name = name[1:]
    second = name.lower()

    return first + second


L1 = ['adam','LISA','barT']
L2 = list(map(normalize,L1))
print(L2)
