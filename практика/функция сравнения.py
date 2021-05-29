def sravnenie(*args):
    a=int(input("Введите первое число "))
    b=int(input("Введите второе число "))
    if a>b:
        return "a>b"
    elif a<b:
        return "a<b"
    elif a==b:
        return "a==b"
print(sravnenie())

