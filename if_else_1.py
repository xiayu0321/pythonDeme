users = []

if users:
	for user in users:
		if user == 'admin':
			print("Hello admin,would you like to see a status report?")
		else:
			print("Hello "+user+",thank you for logging in again")
else:
	print("We need to find some users!")


current_users = ['admin','wendy','nancy','jessica','yoona']
new_users = ['wendy','irene','yuri','yoona','chenle']

for user in new_users:
	if user in current_users:
		print("please change the name")
	else:
		print("this name can be used")


