import os
import json


class User():
    def __init__(self, id, login, password):
        self.id = id
        self.login = login
        self.password = password


class Main(User):
    def getUsersList():
        file = open("user.json", "r")
        result = json.load(file)
        print(result)

    def saveUsers(self):
        file = open("user.json", 'a')
        dict = {
            'id ': self.id,
            'login': self.login,
            'password': self.password,
        }
        json.dump(dict, file)

    while True:
        choice = int(input("PRESS [1] TO ADD User\nPRESS [2] TO LIST User\nPRESS [0] TO EXIT\n"))
        if choice == 1:
            file = open("user.json", 'a')
            p = User(input("Введите Id"), input("введите login"),
                     (input("введите password")))
            saveUsers(p)
        elif choice == 2:
            file = open("user.json", "r")
            getUsersList()
        elif choice == 0:
            break
