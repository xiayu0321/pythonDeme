from trim import trim

if trim('hello  ') != 'hello':
    print('测试失败')
elif trim('   hello') != 'hello':
    print('测试失败')
elif trim('  hello  ') != 'hello':
    print('测试失败')
elif trim('  hello world  ') != 'hello world':
    print('测试失败')
elif trim('       ') != '':
    print('测试失败')
else:
    print('测试成功')

