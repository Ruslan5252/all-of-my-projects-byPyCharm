a=int(input("Введите первое число "))
b=int(input("Введите второе число "))
if a>b:
    print("yes")
else:
    a,b=b,a #переприсваивание переменных
    print(a,b)