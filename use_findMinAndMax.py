from findMinAndMax import findMinAndMax

if findMinAndMax([]) != (None,None):
    print('测试失败',findMinAndMax([]))
elif findMinAndMax([7]) != (7,7):
    print('测试失败',findMinAndMax([7]))
elif findMinAndMax([7,1]) != (1,7):
    print('测试失败',findMinAndMax([7,1]))
elif findMinAndMax([7,1,3,9,5]) != (1,9):
    print('测试失败',findMinAndMax(7,1,3,9,5))
else:
    print('测试成功')
