def log_and_passw(*args):
    log=input("Введите логин ")
    passw=input("Введите пароль")
    if log=="admin" and passw=="qwerty":
        return "Authentication completed"
    else:
        return 'Invalid login or password'
print(log_and_passw())

