def triangles():

    n = 0
    L = [1]

    while True:
        yield(L)
        L = [L[x] + L[x+1] for x in range(n)]

        L.append(1)
        L.insert(0,1)
        n = n + 1
