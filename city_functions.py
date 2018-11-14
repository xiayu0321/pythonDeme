def city_country(city,country,population):
	city_country = {
			"Santiago":["Chile",200],
			"ShangHai":["China",2000],
			"Seuol":["Kroea",1000],
			"Tokyo":["Japan",500]
		}
	return str(city)+","+str(city_country[city][0])+" - "+str(city_country[city][1])