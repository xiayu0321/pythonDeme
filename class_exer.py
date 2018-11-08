from random import randint

class Restaurant():
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print("restaurant_name:" + self.restaurant_name + " cuisine_type:"+self.cuisine_type)

	def open_restaurant(self):
		print(self.restaurant_name +" is openning")

	def set_number_served(self,number_served):
		self.number_served = number_served

	def increment_number_served(self,increment_num):
		self.number_served += increment_num


restaurant = Restaurant('yuge','barbecue')
restaurant.describe_restaurant()
restaurant.open_restaurant()

print(restaurant.number_served)
restaurant.set_number_served(10)
print(restaurant.number_served)
restaurant.increment_number_served(20)
print(restaurant.number_served)

class IceCreamStand(Restaurant):
	def __init__(self,*flavors):
		self.flavors = flavors

	def showIceCreamSauce(self):
		print(self.flavors)

IceCream = IceCreamStand('vanilla','chocolates')
IceCream.showIceCreamSauce()


class User():
	def __init__(self,first_name,last_name,login_attempts = 0,*other_quality):
		self.first_name = first_name
		self.last_name = last_name
		self.login_attempts = 0
		self.other_quality = other_quality

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0

	def describe_user(self):
		constract = self.first_name + " " + self.last_name

		for v in self.other_quality:
			constract += str(v)

		print(constract)

	def greet_user(self):
		print("Hello,"+ str(self.first_name) + str(self.last_name))

yonna = User("Lim","yonna",0,"Singer","Kroean")
yonna.describe_user()
yonna.greet_user()
yonna.increment_login_attempts()
yonna.increment_login_attempts()
print(yonna.login_attempts)
yonna.reset_login_attempts()
print(yonna.login_attempts)

class Admin(User):
	def __init__(self,first_name,last_name,privileges):
		self.first_name = first_name
		self.last_name = last_name
		self.privileges = privileges

	def showPrivileges(self):
		print(self.privileges)
admin = Admin("lim","yonna","can add post")
admin.showPrivileges()


class Die():
	def __init__(self,sides = 6):
		self.sides = sides

	def roll_die(self):
		print(randint(1,self.sides))

One = Die(10)
One.roll_die()





