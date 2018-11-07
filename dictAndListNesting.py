acquaintances1 = {
	"first_name" : "lee",
	"last_name" : "Mark",
	"age" : 19,
	"city" : "vencouver",
	}

acquaintances2 = {
	"first_name" : "zhong",
	"last_name" : "chenle",
	"age" : 17,
	"city" : "shanghai",
	}

acquaintances3 = {
	"first_name" : "huang",
	"last_name" : "renjun",
	"age" : 18,
	"city" : "jilin",
	}

people = [acquaintances1,acquaintances2,acquaintances3]

for h in people:
	print(h)


favorite_places = {
	'leeMark':['vencouver','seoul'],
	'zhongchenle':['shanghai','Vienna'],
	'huangrenjun':['jilin','seoul','beijing']
	}

for name in favorite_places:
	print("name:"+name)
	for f_p in favorite_places[name]:
		print('favorite_places:'+f_p)


cities = {
	'BeiJing':{'country':'China','population':21700000,'fact':'capital city of China'},
	'ShangHai':{'country':'China','population':24600000,'fact':'economy center of China'},
	'Seoul':{'country':'Korea','population':25000000,'fact':'capital city of Korea'},
	}

for city_name in cities:
	print("city_name:"+city_name)
	for k,v in cities[city_name].items():
		print(k + " "+ str(v))


