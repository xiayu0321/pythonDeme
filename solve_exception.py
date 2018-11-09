Flag = True
while(Flag):
	FirstNum = input("please input first number:")
	SecondNum = input("please input second number:")
	try:
		answer = int(FirstNum) + int(SecondNum)
	except ValueError:
		print('your value is not integer')
	else:
		print(answer)
		Flag = False


try:
	with open('./cats.txt') as cat:
		cats = cat.readlines()
	with open('./dogs.txt') as dog:
		dogs = dog.readlines()
except Exception as FileNotFound:
	print('file not found')
else:
	for l in cats:
		print(l)
	for v in dogs:
		print(v)

