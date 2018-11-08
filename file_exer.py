#with在不再需要访问文件后将其关闭
with open('./pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents.rstrip())

#逐行读取
fileroute = './pi_digits.txt'

with open(fileroute) as file_o:
	lines = file_o.readlines()

for line in lines:
	print(line.rstrip())

#写入文件
with open(fileroute,'a') as file_oj:
	file_oj.write("\nThank you\n")


user_input = ''
with open(fileroute,'a') as file_obj:
	while(user_input !='q'):
		user_name = input("please input your name:")
		user_input = user_name
		file_obj.write("\n"+user_name+",greet you !\n")
	print('结束')

