a=int(input("Введите первое число "))
b=int(input("Введите второе число "))
if a!=b:
    a=a+b
    b=a
    print(a,b)
elif a==b:
    a=0
    b=0
    print(a,b)