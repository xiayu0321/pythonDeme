def make_shirt(size,style ="I love Python"):
	print("size:"+size +" "+"style:"+style)


make_shirt("big")
make_shirt("middle")
make_shirt("big","Python is so fun")


def city_country(city,country):
	return str(city) + ","+str(country)

print(city_country("ShangHai",'China'))
print(city_country("Seoul","Korea"))
print(city_country("Tokyo","Japan"))

def make_album(singer,album_name,song_num = ''):
	if song_num:
		return {"singer":singer,"album_name":album_name,"song_num":song_num}
	else:
		return {"singer":singer,"album_name":album_name}

print(make_album("nct-dream","we go up",6))
print(make_album("nct127","regular"))
print(make_album("nct2018","go",11))



def show_magicians(magicians):
	for magician in magicians:
		print(magician)

def make_great(magicians,great_magicians):
	for magician in magicians:
		great_magicians.append(str(magician) + " the Great")

def make_great_1(magicians,great_magicians):
	for magician in magicians:
		great_magicians.append(str(magician) + " the Great")
	return great_magicians


magicians = ["Mark","Jisung","Chenle"]
show_magicians(magicians)

great_magicians = []
make_great(magicians,great_magicians)
show_magicians(great_magicians)

show_magicians(make_great_1(magicians[:],great_magicians))


def build_profile(first,last,**user_info):
	profile = {}
	profile['first'] = first
	profile['last'] = last

	for k,v in user_info.items():
		profile[k] = v

	return profile

user_profile = build_profile('xia','yu',location = 'xi an',field = 'computer' )
print(user_profile)

def car_profile(factory,model,**car_other_info):
	car_info = {}
	car_info['factory'] = factory
	car_info['model'] = model

	for k,v in car_other_info.items():
		car_info[k] = v

	return car_info

car = car_profile('subaru','outback',color = 'blue',tow_package = True)
print(car)