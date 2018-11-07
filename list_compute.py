import datetime

for v in range(1,21):
	print(v)

#for i in range(1,1000001):
#	print(i)

#Sstarttime = datetime.datetime.now()
#num = list(range(1,1000001))
#print(min(num))
#print(max(num))
#print(sum(num))
#endtime = datetime.datetime.now()
#print("time:"+str((endtime-starttime).seconds()))

even = list(range(1,21,2))
for j in even:
	print("even："+str(j))

num_by_3 = [x for x in range(3,31) if x % 3 == 0]
print("num_by_3:"+str(num_by_3))

cube = [x ** 3 for x in range(1,11)]
print(cube)

my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods
print(my_foods)
print(friend_foods)

my_foods.append('hotpot')
print(my_foods)
print(friend_foods)

friend_foods = my_foods[:]
my_foods.append('ice cream')
friend_foods.append('beef')
print(my_foods)
print(friend_foods)





