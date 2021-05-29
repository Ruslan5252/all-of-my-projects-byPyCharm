import json
import os
users = {

    "user1": {"id": 1, "name": "Emily", "login": "emily@gmail.com", "password": "qwerty"},

    "user2": {"id": 2, "name": "Jack", "login": "jack@gmail.com", "password": "qwerty2"},

    "user3": {"id": 3, "name": "Tom", "login": "tom@gmail.com", "password": "qwerty3"}

}

log=input("Введите логин ")
password=input("Введите пароль ")
flag=False
a=''
for i in users.values():
    if log==i['login'] and password==i['password']:
        flag=True
        a=i['name']
        print("hello ",a)
        break
if flag==False:
    print("Try again")





