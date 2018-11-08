print('user can input some sauce:')
en = ''

while en != 'quit':
	en = input('please input some sauce:')
	print(en)

print('quit')


message = ''
active = True

while active:
	message = input("input some message:")

	if message == 'quit':
		active = False