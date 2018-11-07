guests = ['wangyan','wangkexin','yoona','jessica']

for i in range(4):
	print("I want to invite "+guests[i] +" to come to my party")


absent_guest ='yoona'
print("this is a pity"+absent_guest+" can't come to my party")
guests.remove(absent_guest)


guests.append("chenle")

for j in range(4):
	print("I want to invite "+guests[j] +" to come to my party")


print("i find a bigger dinner table")

guests.insert(0,"renjun")
guests.insert(2,'jaemin')
guests.append('mark')
for k in range(len(guests)):
	print("I want to invite "+guests[k] +" to come to my party")


print("it's so sorry,i am only invite two guests")

s_guest1 = guests.pop()
print("i'm very sorry"+s_guest1+" can't come to my party")
s_guest1 = guests.pop()
print("i'm very sorry"+s_guest1+" can't come to my party")
s_guest1 = guests.pop()
print("i'm very sorry"+s_guest1+" can't come to my party")
s_guest1 = guests.pop()
print("i'm very sorry"+s_guest1+" can't come to my party")
s_guest1 = guests.pop()
print("i'm very sorry"+s_guest1+" can't come to my party")

for i  in range(len(guests)):
	print("I want to invite "+guests[i] +" to come to my party")

del guests[0]
del guests[0]

print(guests)