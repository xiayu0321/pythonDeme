import json


def get_stored_username():
    filename = './username.json'
    try:
        with open(filename, 'r') as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    username = input("please input your name:")
    filename = './username.json'

    try:
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def greet_user():
    username = get_stored_username()

    if username:
        print("good morning,"+str(username)+" !")
    else:
        username = get_new_username()
        print("We will remember you when you come back, "+str(username)+" !")


greet_user()


def store_lucky_number():
    lucky_num = input("please input you lucky number:")

    try:
        with open('./lucky_num.json', 'w') as ob:
            json.dump(lucky_num, ob)
    except FileNotFoundError:
        return None
    else:
        return True

def get_lucky_number():
    try:
        with open('./lucky_num.json','r') as ob:
            lucky_num = json.load(ob)
    except FileNotFoundError:
        return False
    else:
        print("lucky_num is "+str(lucky_num))

store_lucky_number()
get_lucky_number()

