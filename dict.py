acquaintances = {
	"first_name" : "lee",
	"last_name" : "Mark",
	"age" : 19,
	"city" : "vencouver",
	}

print("my acquaintances's first_name is:"+acquaintances['first_name']+
	" last_name:" + acquaintances["last_name"] + " age:"+str(acquaintances["age"])+
	" city: "+acquaintances["city"])


rivers = {
	"nile":"egypt",
	"Amazon River":"Brazil",
	"changjiang":"China"
	}

for k,v in rivers.items():
	print("the "+ k +" runs throught "+ v.title())


favorite_languages = {
	'jen':'python',
	'sarah':'c',
	'edwaid':'ruby',
	'phil':'python'
	}

Participants = ['jisung','phil','jessica','yoona','sarah']

for k in favorite_languages.keys():
	if k in Participants:
		print("Thank you participate the activity")
	else:
		print("please join the activity") 

