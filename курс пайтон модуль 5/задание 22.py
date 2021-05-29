log = input("Введите логин")
passw = input("введите пароль")
users = {
    "user": "qwerty", "user2": "qwerty2", "user3": "qwerty3"
}
for key,value in users.items():
    if key==log and value==passw:
        flag=True
        break
if flag:
    print("Authentication completed")
else:
    print("Invalid login or password")


